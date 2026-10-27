# Flow defect checklist

Select questions that fit the requested journey and perspective. Treat them as prompts, not automatic defects. A finding needs a concrete consequence with evidence; record an unobserved concern as a hypothesis. Measurements and action counts are diagnostic, including on spatial canvases and multiple intentional authoring views.

## Modes
- Which steps benefit from a doing, waiting, understanding or configuring lens? Other tasks may need a different description.
- Does each screen serve the mode the person is in at that step, rather than another one?
- Doing: is the one action there, with the facts it needs and nothing else in the way?
- Waiting: are the phase, the expected duration and "you may leave" shown, and is the person told when it's their turn?
- Understanding: does the screen say what this is and where it stands, in plain words, with the "why" one click away?
- Configuring: are the current value and its source shown, the effect previewed, and a way back offered? Is it out of the daily path but linked from where it matters?
- Is configuration ever required in the middle of doing? Make it a default, or move it before the journey.
- Is long waiting time handled by parking the work and notifying, not by asking the person to watch?

## Structure and reading
- Does each container hold one thing, with a heading that names it?
- Does the strength of separation (space, hairline, fill, card, panel) match how unrelated things are, and are containers nested at most two deep?
- Is the same kind of content always in the same kind of container, across screens?
- Is the predicted visual entry point this step's answer, and does the reading order match the order the person needs? Do not claim actual fixation without eye-tracking evidence.
- Do regions and headings share a few left edges, with larger gaps between groups than within them?

## Disclosure patterns
- Is everything the person needs at the same moment visible together (not split across tabs, or a drawer and the page behind it)?
- Is every sequence a stepper or a single flow, and every set of peers tabs or columns, not the other way round?
- Is any required decision or input hidden in a fold, a closed tab or a drawer?
- Does any pane, drawer or overlay cover the action it supports?
- Is a modal used only for blocking, short, consequential decisions?
- Can the person tell what a closed tab or fold holds, and whether it needs them, without opening it?
- Do opening, closing and switching keep their place and unsaved input, and do the back button and links work?
- Is one thing shown through one pattern, not several (a checkbox, a section and a fold for the same decision)?

## Meaning and context
- Does every level of work (project, group, unit, run) have a place for its why, shown where its children are decided?
- Does a child say only what is new and link to its parent's why, rather than repeating it?
- Does each group of work name the part of the product it changes, and does finished work propose an update to the product's description?
- Do diagrams and summaries say what they were built from and when, and offer a rebuild?
- Is creation staged one decision at a time, with every option defaulted by policy and explained by its consequence?
- Does the amount and form of text fit why the person is here: well-set prose where they came to read, the answer first in a few words where they came to decide, act, wait or find one fact?

## What's on the screen
- Does the visible area support this step's task and evidence needs? Viewport share is diagnostic, not a pass threshold.
- Is the answer findable at the point it is needed? Check placement and prominence in context.
- Within the active task or region, is the next action clear? Concurrent canvas tools and inspection controls need not reduce to one screen-wide primary.
- Is anything shown that belongs to another journey or place (rate it "elsewhere": link it instead)?
- Is anything shown that no step needs: internals, duplicates, decoration, unsourced figures (rate it "never": remove it)?
- Is detail needed only sometimes folded one click away rather than spread on the page?

## Order and prerequisites
- Can every step that depends on an earlier one only be taken after it? (If B needs A, is B disabled with a reason until A is done, or does B do A itself?)
- When the user starts an action, is it bound to the latest version of what they just edited, or can it silently use an older one?
- Are draft, approved and in-use versions visibly distinct at the point of action ("this will run with v1; v2 is a draft")?
- Can the user leave mid-journey and come back to the same step?

## Decisions
- Do intentional authoring surfaces share the same decision semantics and saved state, without forcing the person to reconcile conflicting copies?
- Is everything needed for the decision visible where it is made, or one click away (L2)?
- Is the decision reversible, and does the screen say so when it is not?
- Are defaults shown with their source, and changeable before they take effect?
- Does the product ever decide something reserved for the person?

## State and vocabulary
- Is each object's state said in the same word and shape everywhere?
- Is the state derived from records by one function rather than re-phrased per screen?
- Do the board, the list, the object's page and any counts agree at the same moment?
- Is "waiting on you" kept apart from "waiting on the system or someone else"?

## Next action
- Does every screen showing an object's state also show its next action?
- Is the primary action clear within each active task or region, without unrelated actions competing for attention?
- After an action, does the user land where the next step is?

## Questions and answers
- Is every question shown next to where it is answered (no drawer, tab or page between)?
- Are suggested answers prefilled and editable?

## Waiting
- Does every wait longer than a few seconds show its phase, its expected duration and whether the user may leave?
- Does the product notify or park the work when it is done, instead of requiring the user to watch?

## Findability
- Can every option be reached from the journey that needs it, without visiting settings?
- Is any capability only discoverable through documentation or a menu the journey never opens?
- Do multiple entry points reach the same object consistently and preserve context? Graph links, navigation trees and breadcrumbs may be useful complementary routes; remove only demonstrated confusion or divergent behavior.

## Errors and recovery
- Does every error say what happened, why, and the one action that fixes it?
- Does a failed or stopped run say what is kept and what the options are?
- Is there an in-product path for every recovery, so nobody has to fix things by hand outside the product?

## Load
- Count what the user must remember across screens. Can the screen carry it instead?
- Count repeated information. Can one copy be removed?
- Count clicks on the daily loop. Can a system step replace one?

## Layers
- Can a newcomer finish each typical journey with L0 and L1 only?
- Are expert tools (raw data, overrides, batch) present but out of the default path?
- Does anything required hide in L2 or L3?
