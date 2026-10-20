# ux-review-skills

Three agent skills that bring a designer's eye to software work. The product owner decides what to build; these skills bring the questions a good designer would ask: about how people move through the product, what each screen is for, and what a feature really means before anyone builds it.

| Skill | Use it to | Talks to you? |
|---|---|---|
| **interaction-flow** | Review what exists: walk the real app, measure each journey, judge every screen, rank what to fix | No. It works from evidence and reports priorities |
| **design-reflection** | Shape a feature before it is specified: the need, where it belongs, the simplest shape, states, scale | No. It writes a one-page brief with at most three questions for you |
| **clarify-intent** | Pin down meaning and intent with you, then review a spec or write one | Yes. It asks a few questions at a time, each with proposed answers |

## Install

With npm (Node 18 or later):

```sh
npx ux-review-skills install            # all three, for every project (~/.claude/skills)
npx ux-review-skills install --project  # for the current project only (./.claude/skills)
npx ux-review-skills install clarify-intent   # just one
npx ux-review-skills list               # what is installed
```

With the cross-agent `skills` CLI (Claude Code, Cursor, Codex and others):

```sh
npx skills add rinzler1/ux-review-skills
```

As a Claude Code plugin:

```text
/plugin marketplace add rinzler1/ux-review-skills
/plugin install ux-review@ux-review
```

Or copy `skills/*` into `~/.claude/skills/`. Skills load on the next session.

## Use

```text
/interaction-flow review the checkout journey
/interaction-flow fan-out our app at http://localhost:3000     (one agent per journey, then a ranked list)
/interaction-flow screen http://localhost:3000/orders/42
/design-reflection "users should be able to pin reports"
/clarify-intent review specs/pinned-reports.md
/clarify-intent spec "export the ledger as CSV"
```

Installed as a plugin, the commands are prefixed: `/ux-review:interaction-flow`.

## What each skill looks at

**interaction-flow** reviews the path between screens, not the pixels. It works through these passes:

- **Intent and objects:** who the product is for, the job they come to do, who decides what, and each object's one home.
- **Meaning and context:** does every level of work say why it exists, does context pass from parent to child, and is the plan connected to what the product is today?
- **Journeys:** each typical use case walked in the running app. It counts clicks, waits, what the person must remember, what is said twice, and steps whose order they must know.
- **Modes:** each step is tagged doing, waiting, understanding or configuring, because each mode needs a different design.
- **Screen pertinence:** each region and element rated against the moment it serves: now, soon, on demand, elsewhere or never.
- **Structure and reading:** one container per thing, separation that matches relationship, and a reading path that follows importance.
- **Disclosure:** why a tab, pane, drawer, modal, fold or page, and whether its promise fits how the content is used.
- **How people think:** every finding names its human cause, and the cause picks the fix.
- **Priorities:** findings merged and ranked by frequency × consequence × reach.

A Playwright script (`skills/interaction-flow/scripts/screen_inventory.py`) lists a screen's regions, elements, nesting, reading order and disclosure patterns, so the review starts from what is really on the screen. It needs Python with Playwright: `pip install playwright && playwright install chromium`, or `uv run --with playwright python …`.

**design-reflection** asks ten questions of a feature idea:
1. The need behind it.
2. Which existing concept it belongs to.
3. What can be derived, judged by a model, or must be asked.
4. The simplest shape, and what it removes.
5. Its states and edge cases.
6. Where it lives and at which layer.
7. How it scales.
8. Consistency with the rest of the product.
9. Its cost in effort and attention.
10. How you will know it worked.

It ends with a one-page brief: one recommended shape, two alternatives, the one-way doors, and at most three questions for you.

**clarify-intent** explores the product and code first, so it never asks what they already answer. Then it asks only what is yours to decide: the need, the outcome, the authority line, scope, trade-offs, names, the states that matter, and the success signal. It ends with a decisions log. `review` resolves the ambiguities in an existing spec; `spec` interviews you and then writes one.

## Credits

The principles in `how-people-think.md` are summarised in our own words from Susan M. Weinschenk, *100 Things Every Designer Needs to Know About People*; Don Norman, *The Design of Everyday Things*; Jakob Nielsen's usability heuristics and response-time limits; and research by Cowan, Hick and Hyman, Fitts, Kahneman and Tversky, Maister and Csikszentmihalyi. Full references are in the file.

## Contributing

The shared references live in `skills/interaction-flow/references/` and `skills/design-reflection/SKILL.md`; `npm run sync` copies them into the skills that read them. Edit the originals, never the copies.

## License

MIT
