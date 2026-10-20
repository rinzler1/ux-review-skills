#!/usr/bin/env node
// ux-review-skills: install the skills into Claude Code's skills folder. No dependencies.
//
//   npx ux-review-skills install            all skills, for every project   (~/.claude/skills)
//   npx ux-review-skills install --project  all skills, for this project     (./.claude/skills)
//   npx ux-review-skills install interaction-flow clarify-intent   only these
//   npx ux-review-skills list               what is available and what is installed
//   npx ux-review-skills uninstall [names]  remove installed copies
//   --force  replace an installed copy that differs from this version
//   --dir <path>  install into another skills folder (another agent's, for example)
import { cpSync, existsSync, readdirSync, readFileSync, rmSync, statSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const pkgRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const source = join(pkgRoot, "skills");
const version = JSON.parse(readFileSync(join(pkgRoot, "package.json"), "utf8")).version;
const available = readdirSync(source).filter((n) => existsSync(join(source, n, "SKILL.md"))).sort();

const args = process.argv.slice(2);
const flag = (name) => { const i = args.indexOf(name); if (i === -1) return false; args.splice(i, 1); return true; };
const option = (name) => { const i = args.indexOf(name); if (i === -1) return null; const v = args[i + 1]; args.splice(i, 2); return v; };
const project = flag("--project");
const force = flag("--force");
const dirOpt = option("--dir");
const command = args.shift() || "help";
const target = dirOpt ? dirOpt : project ? join(process.cwd(), ".claude", "skills") : join(homedir(), ".claude", "skills");

const files = (dir) => readdirSync(dir).flatMap((n) => {
  const p = join(dir, n);
  return statSync(p).isDirectory() ? (n === "__pycache__" ? [] : files(p)) : [p];
});
const same = (a, b) => {
  if (!existsSync(b)) return false;
  const fa = files(a).map((p) => relative(a, p)).sort(), fb = files(b).map((p) => relative(b, p)).sort();
  return fa.length === fb.length && fa.every((f, i) => f === fb[i] && readFileSync(join(a, f)).equals(readFileSync(join(b, f))));
};
const pick = () => {
  const names = args.length ? args : available;
  const unknown = names.filter((n) => !available.includes(n));
  if (unknown.length) { console.error(`Unknown skill: ${unknown.join(", ")}. Available: ${available.join(", ")}`); process.exit(1); }
  return names;
};

if (command === "install") {
  let failed = false;
  for (const name of pick()) {
    const from = join(source, name), to = join(target, name);
    if (existsSync(to) && !same(from, to) && !force) {
      console.log(`skip     ${name}: an installed copy differs from ${version} (use --force to replace it)`); failed = true; continue;
    }
    if (existsSync(to) && same(from, to)) { console.log(`ok       ${name}: already installed`); continue; }
    rmSync(to, { recursive: true, force: true });
    cpSync(from, to, { recursive: true, filter: (p) => !p.includes("__pycache__") });
    console.log(`install  ${name} -> ${to}`);
  }
  console.log(`\nIn Claude Code, type /interaction-flow, /design-reflection or /clarify-intent. Skills load on the next session.`);
  process.exit(failed ? 1 : 0);
} else if (command === "uninstall") {
  for (const name of pick()) {
    const to = join(target, name);
    if (!existsSync(to)) { console.log(`absent   ${name}`); continue; }
    rmSync(to, { recursive: true, force: true });
    console.log(`removed  ${name} from ${target}`);
  }
} else if (command === "list") {
  console.log(`ux-review-skills ${version} · target ${target}`);
  for (const name of available) {
    const to = join(target, name);
    const state = !existsSync(to) ? "not installed" : same(join(source, name), to) ? "installed" : "installed, differs";
    const desc = (readFileSync(join(source, name, "SKILL.md"), "utf8").match(/^description:\s*(.*)$/m) || [, ""])[1];
    console.log(`  ${name.padEnd(18)} ${state.padEnd(20)} ${desc.slice(0, 90)}…`);
  }
} else {
  console.log(`ux-review-skills ${version}
Usage:
  npx ux-review-skills install [names…] [--project] [--force] [--dir <path>]
  npx ux-review-skills uninstall [names…] [--project] [--dir <path>]
  npx ux-review-skills list [--project] [--dir <path>]
Skills: ${available.join(", ")}`);
}
