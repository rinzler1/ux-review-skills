# What's on the screen, and how pertinent it is

At a relevant stop, use the prompt's perspective and task to ask what the person needs to accomplish or decide and what evidence they need. Doing, waiting, understanding and configuring are useful lenses, not an exhaustive classification. This pass judges whether visible content serves that moment.

## 1. Inventory the screen

For important stops, list what is visible. The optional `scripts/screen_inventory.py` lists elements and viewport shares at a chosen size. Check it against the screen: merge pieces that read as one thing and add anything missed. Use the viewport relevant to the request; a number from the script is diagnostic evidence, not a quality threshold.

Name each element by what the person sees ("the five-step progress track", "Approve and queue button"), not by its code name.

## 2. Rate each element against this step

| Rating | Meaning | Default verdict |
|---|---|---|
| **Now** | serves this step's mode and question | keep, and make it prominent if it is the answer |
| **Soon** | needed later in this same journey | keep, but quieter; or show it when its step comes |
| **On demand** | needed sometimes, to check or understand (the why, the detail, the history) | fold to one click (layer L2) |
| **Elsewhere** | belongs to another journey or another place | link to its home; don't repeat it here |
| **Never** | internals, duplicates of something shown above, decoration, invented or unsourced figures | remove |

Rate in context: the same element can be **Now** at one stop and **Elsewhere** at another. Use the mode rules: a doing step wants the action and its facts; a waiting step wants phase, duration and "you can leave"; an understanding step wants what this is and where it stands; a configuring step wants current value, source, preview and way back.

## 3. Measure

Per screen, report:

- **Pertinence ratio** — share of the first viewport covered by **Now** elements. Use this as a contextual heuristic, not a pass/fail threshold. Count a working canvas as task content even when sparse; report the viewport and non-overlapping area denominator, and never sum overlapping containers or assign an unmeasured percentage.
- **The answer's place** — where the element that answers the person's question sits. Below the fold or smaller than neighbours may matter when it impedes this task; explain the consequence before calling it a finding.
- **Competing primaries** — count of elements styled as the main action or the main status. Judge competition within the active task or region; several legitimate actions on a spatial workspace are not automatically a defect.
- **Repeats** — facts shown more than once on the screen or already shown on the previous stop.
- **Text against purpose** — the words per region (from the inventory) judged against the step: plenty is right where the person came to read, a few words where they came to decide, act, wait or find one fact.
- **Never count** — elements rated Never; each is a removal candidate.

## 4. Verdict

Summarize only the measurements that help explain this task. Mark unmeasured percentages as unknown. Add irrelevant content, misplaced answers or competing actions as findings only with a practical consequence and supporting evidence.

Rules:

- Removing beats folding beats shrinking. Don't shrink an element that should not be there.
- Don't fold what the step requires. A required decision is always **Now**.
- When one screen serves several journeys, rate it per journey and keep what is **Now** for the most frequent; give the others a link or an L2 fold.
- Real content only. Rate the screen with realistic data, including long titles and empty states.
