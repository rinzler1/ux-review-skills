# Structure and reading: are things grouped and ordered the way a person reads them?

The pertinence pass asks whether the right content is on the screen. This pass asks whether it is **grouped, separated and ordered** so a person reads it as intended. Run it on every screen a journey stops at, using the regions, depths, styles and order the inventory script reports, then check against the screenshot.

People don't read a screen from code; they read shapes. Containers (borders, fills, cards, panels, columns), space and alignment tell them what belongs together, what is separate, what comes first and how deep they are. When the structure says something the content doesn't mean, people misread the screen however good each element is.

## 1. One container, one thing

- *Does each container hold one topic or one object, with a heading that names it in the person's words?*
- *Is any one thing split across several containers (the same story's state in three boxes)?*
- *Does any container hold two unrelated things (a decision and a history in one card)?*
- *Is there a container with no heading whose purpose is only guessable from its contents?*

Human cause: grouping by common region; a box is read as one unit.

## 2. Separation matches relationship

How strongly two things are separated should match how unrelated they are. The scale, weakest to strongest: space → a hairline → a change of surface (fill) → a bordered card → a separate panel or column → a separate page.

- *Are closely related things separated by space alone, and only unrelated things by a card or panel?*
- *Is everything boxed?* When every block has a border, borders stop meaning anything, and the person loses the signal of what belongs together.
- *Are containers nested more than two levels deep (a card in a card in a panel)?* Each level costs attention and makes "where am I" harder. Prefer space and headings inside one container.
- *Does the gap between groups exceed the gap within a group?* If not, proximity groups the wrong things.

Human cause: proximity and common region; working memory for nesting.

## 3. The same kind of content, the same kind of container

- *Is a status always drawn the same way (a chip), a decision always the same way (a panel with one primary action), a history always the same way (a log list)?*
- *Does the same container style mean the same thing across screens?* When a bordered card is sometimes a decision and sometimes a note, the reader relearns it on each screen.
- *Do containers follow the product's design system* (its panel, card, chip and divider pieces), rather than one-off boxes?

Human cause: familiar patterns are read for free; consistency builds trust.

## 4. The reading path follows importance

On a dense screen, people start top-left and move across and down, skimming left edges and headings (an F-shaped scan); on a sparse screen, the eye goes to the largest, highest-contrast shape first.

- *Is the first thing the eye lands on the most important thing for this step's mode?* (doing: the action and its facts; waiting: the phase; understanding: what this is and where it stands; configuring: the current value.)
- *Does the reading order (the inventory's order) match the order the person needs things in?* The question before its answer, the state before the action, the summary before the detail.
- *Is anything important placed where the scan skips:* the far right of a wide screen, below a tall block, or inside a fold?
- *On a wide screen, do columns have a reading order (left feeds right), or are they read in parallel?* Say which, and check that it's obvious.

Human cause: scanning patterns; attention drawn by size and contrast.

## 5. Alignment and rhythm

- *Do containers and their contents share a small number of left edges?* Many slightly different edges make a screen look busy and break grouping. The inventory reports the distinct left edges in the first viewport.
- *Is spacing on a consistent scale,* with larger gaps between groups than within them?
- *Do the columns mean something* (a list beside its detail, a decision beside its evidence), or are they a grid filled for its own sake?

Human cause: similarity and good continuation; cognitive load from presentation.

## Measures to report per screen

- **Containers:** the count in the first viewport, and how many hold more than one thing or have no heading.
- **Maximum nesting depth** of containers. More than 2 is a finding.
- **Container styles in use:** bordered, filled, shadowed, bare. Note any style used for two different kinds of content.
- **First fixation:** the largest, highest-contrast region or element in the first viewport. Say whether it's this step's answer.
- **Reading order:** the first five regions in order, judged against the order the person needs.
- **Distinct left edges:** among top-level regions and headings in the first viewport. Compare with the layout's intended columns.

Turn each mismatch into a finding with its severity, mode and human cause, like any other.
