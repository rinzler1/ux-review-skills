"""List what is visible on a screen, top to bottom, with the share of the viewport each element covers.

    uv run --no-project --with playwright python screen_inventory.py URL [--width 1920 --height 1080] [--wait 1500]
        [--chromium PATH] [--full] [--json]

Reads only: it opens the page, waits, and inspects the DOM. Run it against a throwaway instance, never against a page that
changes data on load. Output: the regions (boxed or filled containers, with their heading and viewport share), then one row per
visible element a person reads or acts on (kind, share, position, text) in reading order, then a summary. Headings are found
by visual weight and primaries by background contrast, so the result does not depend on the app's tag or class names. --full includes elements below the first viewport (marked "below"). The rows are a starting point
for the pertinence pass in references/screen-pertinence.md, not a verdict."""

from __future__ import annotations

import argparse
import json
import sys

from playwright.sync_api import sync_playwright

JS = r"""
(full) => {
  const W = innerWidth, H = innerHeight;
  const lum = c => { const m = c.match(/[\d.]+/g); if (!m) return null; const [r, g, b, a = 1] = m.map(Number); if (a < 0.2) return null;
    const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const pageBg = lum(getComputedStyle(document.body).backgroundColor) ?? lum(getComputedStyle(document.documentElement).backgroundColor) ?? 1;
  const bodySize = parseFloat(getComputedStyle(document.body).fontSize) || 14;
  const box = (el) => { const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity === 0) return null;
    const r = el.getBoundingClientRect(); if (r.width < 4 || r.height < 4) return null;
    if (!full && (r.bottom <= 0 || r.top >= H || r.right <= 0 || r.left >= W)) return null;
    for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {   // clipped by a scrolling or overflow-hidden ancestor
      const o = getComputedStyle(a); if (o.overflowX === 'visible' && o.overflowY === 'visible') continue;
      const c = a.getBoundingClientRect(); if (r.bottom <= c.top || r.top >= c.bottom || r.right <= c.left || r.left >= c.right) return null; }
    return r; };
  const share = r => { const x0 = Math.max(0, r.left), y0 = Math.max(0, r.top), x1 = Math.min(W, r.right), y1 = Math.min(H, r.bottom);
    return x1 > x0 && y1 > y0 ? +(((x1 - x0) * (y1 - y0)) / (W * H) * 100).toFixed(2) : 0; };
  const isIcon = el => /material|icon|phosphor|symbols/i.test(getComputedStyle(el).fontFamily) || /(^|\s)(q-icon|material-icons|ph-|fa-)/.test(el.className && el.className.baseVal === undefined ? el.className : '');
  const ownText = el => isIcon(el) ? '' : [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join(' ').replace(/\s+/g, ' ').trim();
  const visibleText = el => { let t = ''; const walk = n => { for (const c of n.childNodes) { if (c.nodeType === 3) t += ' ' + c.textContent; else if (c.nodeType === 1 && !isIcon(c) && getComputedStyle(c).display !== 'none') walk(c); } }; walk(el); return t; };
  const label = el => (el.getAttribute('aria-label') || visibleText(el) || el.value || el.getAttribute('alt') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim();
  const contrast = el => { const l = lum(getComputedStyle(el).backgroundColor); if (l === null) return 0;
    const [a, b] = l > pageBg ? [l, pageBg] : [pageBg, l]; return (a + 0.05) / (b + 0.05); };

  // regions: boxed or filled containers covering at least 2% of the viewport, outermost first
  const regions = [];
  for (const el of document.querySelectorAll('body *')) {
    const s = getComputedStyle(el); const r = box(el); if (!r) continue;
    const framed = (parseFloat(s.borderTopWidth) > 0 && s.borderTopStyle !== 'none') || s.boxShadow !== 'none' || contrast(el) > 1.08 || /^(main|aside|nav|header|footer|section|dialog)$/i.test(el.tagName) || el.getAttribute('role') === 'dialog';
    const sh = share(r);
    if (!framed || (sh < 2 && !(full && r.top >= H)) || (r.width >= W * 0.98 && r.height >= H * 0.95)) continue;
    if (regions.some(o => o.el.contains(el) && o.share - sh < 1)) continue;
    const head = [...el.querySelectorAll('*')].slice(0, 60).map(c => ({c, t: ownText(c), f: parseFloat(getComputedStyle(c).fontSize), w: +getComputedStyle(c).fontWeight}))
      .filter(x => x.t.length > 1 && (x.f >= bodySize * 1.1 || x.w >= 700))[0];
    const words = (el.innerText || '').split(/\s+/).filter(Boolean).length;
    const style = (parseFloat(s.borderTopWidth) > 0 && s.borderTopStyle !== 'none') ? 'bordered' : s.boxShadow !== 'none' ? 'shadowed' : contrast(el) > 1.08 ? 'filled' : 'bare';
    regions.push({el, words, style, share: sh, top: Math.round(r.top + scrollY), left: Math.round(r.left), w: Math.round(r.width), h: Math.round(r.height),
                  below: r.top >= H, title: head ? head.t.slice(0, 70) : label(el).slice(0, 70)});
  }
  const outer = regions.filter(r => !regions.some(o => o !== r && o.el.contains(r.el) && o.share > r.share + 1 && o.share < 60));

  // elements: what a person reads or acts on
  const KIND = [['action', 'button,[role=button],input[type=submit],input[type=button],a[href],[role=tab],[role=link]'],
                ['field', 'input:not([type=hidden]):not([type=submit]):not([type=button]),select,textarea,[contenteditable=true]'],
                ['table', 'table,[role=table],[role=grid]'], ['media', 'img,svg[role=img],canvas,video,[role=img]']];
  const seen = new Set(), rows = [];
  const push = (el, kind, r, text) => { seen.add(el);
    rows.push({kind, text: text.slice(0, 90), share: share(r), top: Math.round(r.top + scrollY), left: Math.round(r.left), below: r.top >= H,
               primary: kind === 'action' && contrast(el) >= 3}); };
  for (const [kind, sel] of KIND) for (const el of document.querySelectorAll(sel)) {
    if (seen.has(el) || [...seen].some(o => o.contains(el))) continue;
    const r = box(el); if (r) push(el, kind, r, label(el));
  }
  for (const el of document.querySelectorAll('body *')) {   // text with its own words: headings by visual weight, status-like short words, prose
    if (seen.has(el) || [...seen].some(o => o.contains(el))) continue;
    const t = ownText(el); if (t.length < 2) continue;
    const r = box(el); if (!r) continue;
    const s = getComputedStyle(el), f = parseFloat(s.fontSize), w = +s.fontWeight;
    const kind = (f >= bodySize * 1.25 || (w >= 700 && t.length < 80 && s.textTransform === 'uppercase')) ? 'heading'
               : (t.length <= 24 && (s.textTransform === 'uppercase' || contrast(el) > 1.08 || parseFloat(s.borderTopWidth) > 0)) ? 'status' : 'text';
    push(el, kind, r, t);
  }
  // disclosure patterns: what is tabbed, folded, overlaid or docked, and whether it is open
  const patterns = [];
  const pat = (kind, el, open, label) => { const r = el.getBoundingClientRect(); if (r.width < 4 || r.height < 4) return;
    patterns.push({kind, open, label: (label || '').replace(/\s+/g, ' ').trim().slice(0, 60), top: Math.round(r.top + scrollY), left: Math.round(r.left)}); };
  for (const el of document.querySelectorAll('[role=tab]')) pat('tab', el, el.getAttribute('aria-selected') === 'true' || /active|is-active/.test(el.className), label(el));
  for (const el of document.querySelectorAll('details')) pat('fold', el, el.open, label(el.querySelector('summary') || el));
  for (const el of document.querySelectorAll('[aria-expanded]')) if (!el.closest('details') && el.getAttribute('role') !== 'tab') pat('fold', el, el.getAttribute('aria-expanded') === 'true', label(el));
  for (const el of document.querySelectorAll('[role=dialog],dialog[open],[aria-modal=true]')) { const s = getComputedStyle(el); if (s.display !== 'none' && s.visibility !== 'hidden') pat(el.getAttribute('aria-modal') === 'true' || /modal|dialog/i.test(el.className) ? 'modal-or-drawer' : 'dialog', el, true, label(el).slice(0, 60)); }
  for (const el of document.querySelectorAll('aside,[class*=drawer],[class*=pane],[class*=sidebar]')) { const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
    if (r.width > 120 && r.height > H * 0.4 && s.display !== 'none' && s.visibility !== 'hidden') pat(s.position === 'fixed' && r.left > W * 0.3 ? 'overlay-pane' : 'docked-pane', el, true, el.getAttribute('aria-label') || visibleText(el)); }
  rows.sort((a, b) => (a.top - b.top) || (a.left - b.left));
  outer.sort((a, b) => (a.top - b.top) || (a.left - b.left));
  return {viewport: [W, H], page_height: document.documentElement.scrollHeight,
          patterns, regions: outer.map(({el, ...r}) => ({...r, leaf: !outer.some(o => o.el !== el && el.contains(o.el)), depth: regions.filter(o => o.el !== el && o.el.contains(el)).length})), rows};
}
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--wait", type=int, default=1500, help="milliseconds to wait after load")
    ap.add_argument("--chromium", help="path to a Chromium executable, if Playwright has none installed")
    ap.add_argument("--full", action="store_true", help="include elements below the first viewport")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=a.chromium) if a.chromium else p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": a.width, "height": a.height})
        page.goto(a.url, wait_until="load")
        page.wait_for_timeout(a.wait)
        out = page.evaluate(JS, a.full)
        browser.close()
    if a.json:
        json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
        return 0
    rows, regions = out["rows"], out["regions"]
    print(f"viewport {out['viewport'][0]}x{out['viewport'][1]} · page height {out['page_height']} · {len(regions)} regions · {len(rows)} elements")
    print("REGIONS (d = nesting depth, then container style; words are a measure, not a verdict: judge them against what the person came to do)")
    for r in regions:
        where = "below" if r["below"] else f"{r['share']:5.1f}%"
        print(f"  {r['top']:5d} {r['left']:5d} {r['w']:4d}x{r['h']:<4d} {where:>6} {r['words']:5d}w  d{r['depth']} {r['style']:<8} {'  ' * r['depth']}{r['title']}")
    print("ELEMENTS (* = filled, high-contrast action: reads as a primary)")
    for r in rows:
        where = "below" if r["below"] else f"{r['share']:5.2f}%"
        print(f"  {r['top']:5d} {r['left']:5d}  {where:>6}  {r['kind']:<8}{' *' if r['primary'] else '  '} {r['text']}")
    first = [r for r in rows if not r["below"]]
    by_kind: dict[str, int] = {}
    for r in first:
        by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + 1
    print("first viewport:", ", ".join(f"{k} {n}" for k, n in sorted(by_kind.items())),
          f"· reads-as-primary actions {sum(1 for r in first if r['primary'])}",
          f"· innermost regions cover {sum(r['share'] for r in regions if not r['below'] and r['leaf']):.0f}% of the first viewport")
    vis = [r for r in regions if not r["below"]]
    edges = sorted({r["left"] // 4 * 4 for r in vis} | {r["left"] // 4 * 4 for r in first if r["kind"] == "heading"})
    styles: dict[str, int] = {}
    for r in vis:
        styles[r["style"]] = styles.get(r["style"], 0) + 1
    print(f"structure: max container depth {max((r['depth'] for r in vis), default=0)}",
          "· container styles " + ", ".join(f"{k} {n}" for k, n in sorted(styles.items())),
          f"· distinct left edges (regions and headings) {len(edges)}: {edges[:12]}")
    order = [r["title"][:40] for r in sorted(vis, key=lambda r: (r["top"] // 40, r["left"])) if r["leaf"]][:5]
    print("reading order (first five innermost regions, top-left first):", " → ".join(order))
    pats = out.get("patterns", [])
    if pats:
        print("DISCLOSURE PATTERNS (judge each: does its promise fit how the person uses it?)")
        seen = set()
        for p_ in sorted(pats, key=lambda p_: (p_["top"], p_["left"])):
            key = (p_["kind"], p_["label"], p_["top"] // 8)
            if key in seen:
                continue
            seen.add(key)
            print(f"  {p_['top']:5d} {p_['left']:5d}  {p_['kind']:<15} {'open  ' if p_['open'] else 'closed'}  {p_['label']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
