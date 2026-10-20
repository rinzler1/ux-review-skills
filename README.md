# UX Review Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-3-blue)
![Agents](https://img.shields.io/badge/agents-Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex%20%C2%B7%20more-lightgrey)

**Agent skills that bring a designer's eye to software work.**

Your agent can build any screen you ask for. These skills make it ask the questions a good designer would: what the person is trying to do, where a decision belongs, what this screen is for at this moment, and what a feature really means before anyone builds it.

They don't generate styles or colour palettes. They review **how people move through a product**, **what each screen should show**, and **what the work actually means**, and they turn what they find into ranked, small pieces of work.

---

## Quick start

### 1. Install

```sh
npx ux-review-skills install
```

That installs all three skills into `~/.claude/skills` for every project. Add `--project` for the current project only, or name the skills you want.

<details>
<summary><b>Other agents and install methods</b></summary>

**Any agent supported by the `skills` CLI** (Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot and others):

```sh
npx skills add rinzler1/ux-review-skills
```

**Claude Code plugin** (updates with the marketplace):

```text
/plugin marketplace add rinzler1/ux-review-skills
/plugin install ux-review@ux-review
```

Commands are then prefixed: `/ux-review:interaction-flow`.

**By hand:** copy `skills/*` into your agent's skills folder.

Pick one method per agent; installing twice gives you every skill twice.

</details>

### 2. Use

```text
/interaction-flow fan-out http://localhost:3000
/design-reflection "users should be able to pin reports to their home page"
/clarify-intent spec "export the ledger as CSV"
```

Skills load in the next session.

---

## The three skills

| Skill | Use it when | You get | Talks to you? |
|---|---|---|---|
| [**interaction-flow**](skills/interaction-flow/SKILL.md) | a workflow feels clunky, before a redesign, or to rank UX work | journeys measured in the running app, every screen judged, findings ranked by priority, small stories to fix them | No. It works from evidence |
| [**design-reflection**](skills/design-reflection/SKILL.md) | someone proposes a feature, before its spec | a one-page design brief: the need, where it belongs, the simplest shape, two alternatives, at most three questions | Rarely. At most three questions |
| [**clarify-intent**](skills/clarify-intent/SKILL.md) | an intent is vague, or a spec reads well but could mean two things | a few questions at a time with proposed answers, a decisions log, then a reviewed or written spec | Yes. That's its job |

---

## Why these skills exist

### 1. Every screen looks fine, and the journey still fails

**The problem.** Each page passes a design review. But the action the person needs is on another tab, the same state is worded three ways, and two buttons work only if pressed in an order nobody wrote down. Screen-level tools never see it, because the defect sits between the screens.

**The fix.** Walk the real app, journey by journey, and measure it: clicks, page changes, waits, what the person must remember, what's said twice, which steps depend on an order the screen doesn't enforce. Then give each decision one place, and each state one word.

→ [`interaction-flow`](skills/interaction-flow/SKILL.md)

### 2. The screen shows everything, so it shows nothing

**The problem.** A person arrives with one question: what do I do now, is it done yet, what is this. The screen answers ten other questions first. Tabs hide what's needed together. A drawer holds the question while the answer box sits behind it. A decision gets buried in prose.

**The fix.** Rate every region against the moment it serves: *now*, *soon*, *on demand*, *elsewhere* or *never*. Judge every container for whether it holds one thing, every tab, pane or modal for whether its promise fits the use, and every block of text for whether its length fits why the person is there. Reading wants prose; deciding wants the answer first.

→ [`interaction-flow`](skills/interaction-flow/SKILL.md): pertinence, structure and disclosure passes

### 3. The feature gets built before its shape is questioned

**The problem.** "Tasks should depend on other tasks" becomes a new screen, a new concept and a new setting, when it could have been one property of something that already exists, and could have removed a setting instead of adding one.

**The fix.** Ten reflections before the spec:
1. the need behind the request;
2. the concept it belongs to;
3. what can be derived by a rule, judged by a model, or must be asked;
4. the simplest shape, and what it removes;
5. its states;
6. where it lives;
7. how it scales;
8. consistency with the rest of the product;
9. its cost in effort and attention;
10. how you'll know it worked.

→ [`design-reflection`](skills/design-reflection/SKILL.md)

### 4. The spec reads well and means two things

**The problem.** Two careful readers build two different products from the same paragraph. The agent fills each gap with a guess, and you find out in review.

**The fix.** Explore the code and records first, so nothing is asked that they already answer. Then ask the owner only what is theirs to decide, a few questions at a time, each with proposed answers and their consequences. Write every decision down.

→ [`clarify-intent`](skills/clarify-intent/SKILL.md)

---

## What a review looks like

An excerpt from `interaction-flow` on a fictional shop. The example is illustrative, not a benchmark.

```text
┌─ Priorities ──────────────────────────────────────────────────────────────────────────┐
│ #  Finding                                            Mode       Severity  Reach  Pri │
│ 1  "Pay" stays enabled while the address is invalid;  doing      blocks    3      27  │
│    the error appears only after the card is charged                                   │
│ 2  Order status reads "processing", "pending" and     understand confuses  3       9  │
│    "in progress" on three screens                                                     │
│ 3  Shipping options open in a drawer that covers the  doing      costs     1       6  │
│    total they change                                                                  │
└───────────────────────────────────────────────────────────────────────────────────────┘
  Finding 1 · blocks · doing · Journey "checkout", step 4
  Human cause: constraints prevent errors better than messages (the UI allows a wrong order)
  Fix: disable "Pay" with the reason shown until the address validates
```

Each screen gets a pertinence and structure report, starting from what's actually rendered:

```text
$ python scripts/screen_inventory.py http://localhost:3000/checkout
REGIONS (d = nesting depth, then container style)
     64   240  980x620  31.0%   212w  d1 bordered   Your order
     64  1240  440x900  19.2%    48w  d1 filled     Shipping
structure: max container depth 3 · container styles bordered 4, filled 2 · distinct left edges 9
reading order: Your order → Shipping → Promo code → Payment
DISCLOSURE PATTERNS
    120  1240  overlay-pane    open    Shipping options
    610   240  fold            closed  Expand "Order details"
```

And `clarify-intent` ends with a decisions log the next reader can trust:

```text
Q: "Export the ledger" — all entries, or the filtered view?   A: the filtered view
   By: owner · Changes: export reads the current filters; criterion 2 rewritten
Q: Include a totals row?                                     A: assumed yes (finance asked for it in #41)
   By: assumed · Changes: criterion 4 added
```

---

## How `interaction-flow` works

```text
 intent ─▶ objects ─▶ journeys ───────────────────▶ findings ─▶ priorities ─▶ model ─▶ stories
 who,      one home    walked in the running app,    each with   frequency ×   places,    small,
 job,      per object, measured step by step         its human   consequence   decisions, sequenced,
 authority meaning     (one agent per journey with   cause       × reach       vocabulary, each with
           and context  fan-out)                                               layers      its files
                              │
                              ▼  at every screen
            pertinence · structure & reading · disclosure · text vs purpose
```

Every step is tagged with the person's **mode**, because each mode needs a different design:

| Mode | The person wants | Typical defect |
|---|---|---|
| Doing | the one next action and the facts it needs | the action on another tab; an order to remember |
| Waiting | the phase, how long, whether to leave, a nudge when it's their turn | a spinner with no phase; having to keep watching |
| Understanding | what this is and where it stands, in plain words | the same state in different words |
| Configuring | the current value, its source, a preview, a way back | settings needed in the middle of doing |

Every finding names its **human cause**: limited working memory, recognition over recall, choice overload, scanning, change outside the focus of attention, the psychology of waiting. The cause chooses the fix: a slip needs undo or a constraint, a mistake needs a clearer model.

---

## Example prompts

```text
/interaction-flow review the onboarding journey
/interaction-flow screen http://localhost:3000/settings
/interaction-flow fan-out our admin app — what should we fix first?
/design-reflection "add a diagram section that updates from the codebase"
/design-reflection review docs/specs/bulk-edit.md
/clarify-intent review docs/specs/bulk-edit.md
/clarify-intent spec "let users schedule reports"
```

They also trigger on plain requests like *"this workflow feels clunky"*, *"where should this setting live?"* or *"grill me on this spec"*.

---

## FAQ

<details>
<summary><b>Does it change my app or my data?</b></summary>

No. `interaction-flow` walks the app read-only. For anything that writes, it uses a throwaway instance you can point it at, never production. `design-reflection` and `clarify-intent` write a brief, a log or a spec, and saving them where your work is tracked is a separate step you approve.
</details>

<details>
<summary><b>The screen inventory script fails</b></summary>

It needs Python 3 and Playwright: `pip install playwright && playwright install chromium`, or `uv run --with playwright python scripts/screen_inventory.py <url>`. Pass `--chromium <path>` to use an installed browser. It only reads the page.
</details>

<details>
<summary><b>How expensive is a fan-out review?</b></summary>

One agent per journey, each walking the app and reading code. On a medium web app, six journeys took about a million tokens. The skill tells you how many agents it will launch before it starts. For one journey or one screen, use `review` or `screen` instead.
</details>

<details>
<summary><b>A skill doesn't show up after installing</b></summary>

Skills load when a session starts: open a new one. If you installed with more than one method, remove the duplicates. `npx ux-review-skills list` shows what is installed where.
</details>

<details>
<summary><b>How does this compare to design-system or UI-generation skills?</b></summary>

They complement each other. Those skills decide how a screen looks and generate it. These decide what the screen is for, where things live and what the work means, then hand the screens that change to whichever design skill you use.
</details>

---

## Contributing

Issues and pull requests are welcome.

The shared references have one source each:
- `skills/interaction-flow/references/` for the shared reference files;
- `skills/design-reflection/SKILL.md` for the design reflections.

`npm run sync` copies them into the skills that read them. Edit the originals, never the copies. Every `SKILL.md` description must be a folded YAML block (`description: >-`); the sync script checks it.

## Credits

The principles in [`how-people-think.md`](skills/interaction-flow/references/how-people-think.md) are summarised in our own words from Susan M. Weinschenk, *100 Things Every Designer Needs to Know About People*; Don Norman, *The Design of Everyday Things*; Jakob Nielsen's usability heuristics and response-time limits; and research by Cowan, Hick and Hyman, Fitts, Kahneman and Tversky, Maister and Csikszentmihalyi.

## License

[MIT](LICENSE) © Philip Oligny
