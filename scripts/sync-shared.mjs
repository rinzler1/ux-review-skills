#!/usr/bin/env node
// Copies the shared references into every skill that reads them, so each skill works on its own
// (the `skills` CLI and a plugin can install one skill without the others). The originals live in
// skills/interaction-flow/references/ and skills/design-reflection/SKILL.md; never edit the copies.
// Run: npm run sync   (also runs before npm publish)
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const skills = join(root, "skills");
// Every SKILL.md description must be a folded block (description: >-): a plain value containing ": " is invalid YAML
// and strict parsers (the skills CLI) silently skip the skill.
for (const name of readdirSync(join(root, "skills"))) {
  const file = join(root, "skills", name, "SKILL.md");
  const head = readFileSync(file, "utf8").split("---")[1] || "";
  if (!/^description: >-\s*$/m.test(head)) { console.error(`${name}/SKILL.md: write the description as a folded block (description: >-)`); process.exit(1); }
}
const banner = (src) => `<!-- Copied from ${src} by scripts/sync-shared.mjs. Edit the original, then run npm run sync. -->\n\n`;

const copies = [
  ["interaction-flow/references/how-people-think.md", ["design-reflection/references/how-people-think.md", "clarify-intent/references/how-people-think.md"]],
  ["interaction-flow/references/meaning-and-context.md", ["design-reflection/references/meaning-and-context.md", "clarify-intent/references/meaning-and-context.md"]],
];

const write = (target, text) => {
  const path = join(skills, target);
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, text);
  console.log("synced", target);
};

for (const [src, targets] of copies) {
  const text = readFileSync(join(skills, src), "utf8");
  for (const t of targets) write(t, banner(src) + text);
}

// clarify-intent reads design-reflection's ten reflections; copy them without the frontmatter.
const dr = readFileSync(join(skills, "design-reflection/SKILL.md"), "utf8").replace(/^---[\s\S]*?---\n/, "");
write("clarify-intent/references/design-reflections.md", banner("design-reflection/SKILL.md") + dr.trimStart());
