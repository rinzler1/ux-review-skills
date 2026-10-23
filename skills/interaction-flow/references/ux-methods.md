# UX methods to apply to a journey

Use the method that addresses the task's uncertainty. These lenses explain judgments; they are not mandatory checklists, numerical laws or substitutes for watching users. The questions below are paraphrased, not copied source checklists.

## Discoverability and learning: cognitive walkthrough

For an unfamiliar task, state the assumed user's knowledge and goal. At each transition ask whether the next step is motivated, visible, understandable in relation to the goal, and followed by feedback that makes progress recognizable. A reviewer knowing an undocumented shortcut is not evidence that a novice can discover it. Distinguish first-use learning from repeat efficiency.

Source: Clayton Lewis and John Rieman, [Task-Centered User Interface Design, chapter 4](https://pages.cpsc.ucalgary.ca/~tam/2002/hci_topics/papers/LewisRiemanBook/chap-4.html), especially cognitive walkthroughs. Use for first useful item, setup, unfamiliar gestures and finding the next step. This is expert inspection, not a test with actual users.

## State, recovery and control: usability heuristics

Check whether actions expose their consequences, domain words match the user's understanding, repeated operations behave consistently, and a mistake has a comprehensible way out. Look for task-specific memory burdens and unnecessary choices. A rule of thumb becomes a finding only when tied to an affected step and practical consequence; not every surface needs one primary action or one access route.

Source: Jakob Nielsen, [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/). Use for navigation, async status, explicit versus automatic work and failure recovery.

For journeys with several steps, ask whether completion gives closure, cancellation/reversal is understandable and expert efficiency preserves control. Preserve existing safeguards when simplifying.

Source: Ben Shneiderman, [Eight Golden Rules](https://www.cs.umd.edu/~ben/goldenrules.html). Treat its domain-dependent guidance as a starting point, not a mandate to add undo/history or force a wizard.

## Keyboard, focus and perceivable status

Walk the scoped task by keyboard where practical. Check that necessary actions can be reached and used, focus remains visible and follows a meaningful path, overlays can be exited, and returning keeps a useful focus/context. Do not require a custom tree-widget keyboard model when native links/buttons already provide a usable path.

For relevant asynchronous changes, inspect programmatic status as well as visible feedback; a screen reader announcement and a visual dot do not automatically serve the same person or purpose. A markup attribute alone is not evidence that the whole task is accessible.

Primary guidance: W3C WCAG 2.2 [Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html), [Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html), [Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html), and [Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html). The Understanding pages are explanatory; the [WCAG 2.2 recommendation](https://www.w3.org/TR/WCAG22/) is the normative standard. Report the exact criterion and observed scope when useful; this focused UX pass cannot certify whole-product conformance.

## Choosing the lens

| Uncertainty | Useful lens | Evidence to retain |
|---|---|---|
| Can a newcomer finish? | Cognitive walkthrough | Assumed knowledge, visible cues, next action, feedback |
| Why is this slow/confusing? | Heuristics plus human principles | Specific steps, repeated decisions, memory carried, recovery |
| Can I resume or reverse safely? | Closure/control and recovery | Retained work, clear outcome, return route, cancellation meaning |
| Can keyboard/assistive users do the task? | Scoped WCAG guidance | Performed keys, focus/status evidence, gaps and untested assistive technology |

The existing how-people-think.md explains attention, memory, decisions and waiting; do not repeat every principle in every finding. Name the method/cause only when it helps explain the observed failure and choose a better fix.
