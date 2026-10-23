# Manual tests

These skills are judged by how an agent behaves with them, so they are tested by using them and watching. Run each test in a **fresh session** (skills load at session start) and tick what you observe. Report what you saw in an issue: what passed, what didn't, the agent and its version.

## 1. Fan-out over journeys

```text
/interaction-flow fan-out <your app's URL or name>
```

Give it nothing else, and watch whether it:

- [ ] reads the product's own docs and states the intent (who, job, authority line) before anything else
- [ ] maps the objects and chooses a scoped set of complete use cases with triggers/outcomes, explaining likely usage and consequence
- [ ] uses the current project/build or supplied URL and existing authorization; asks only for missing access, never guesses startup/reset
- [ ] announces agent count, walk target and task-specific effort; uses existing authorization and asks only for missing scope or permission
- [ ] uses available delegation tools for independent journeys, labels shared-walker analysis when one authenticated browser supplies evidence, or walks sequentially
- [ ] gives every agent the same brief: intent, objects, modes, checklist, human principles
- [ ] never writes in a read-only walk (no saves, sends, payments, deletions), and marks such steps "not observed"
- [ ] reaches each starting state through the product's screens or seed script, and says so when an agent stepped around a check or skipped its instance
- [ ] returns per journey: the measured steps with modes, screen passes (pertinence, structure, disclosure), and findings with severity, mode and human cause
- [ ] merges shared causes across distinct cases, prioritizes consequence/usage/reach with evidence confidence and separate effort, and reports only measured task time
- [ ] with an earlier review, marks each group still there, new or gone
- [ ] proposes an interaction model and small sequenced stories

Also note how long it took, its token use, and anything it got wrong about your product.

## 2. One screen

```text
/interaction-flow screen <url>
```

- [ ] runs the inventory script (or says why it can't) and rates each region now / soon / on demand / elsewhere / never
- [ ] judges structure (one container per thing, separation, reading order, nesting) and each disclosure pattern
- [ ] judges text against what the person came to do, not by length

## 3. Clarify a spec

```text
/clarify-intent review <a spec or story with at least one real ambiguity>
```

- [ ] explores first and states what it learned before asking
- [ ] asks nothing the code, docs or records already answer
- [ ] asks one to four questions per turn, each with proposed answers, consequences and a recommendation
- [ ] quotes the ambiguous phrase each question resolves
- [ ] stops when answers no longer change the work, or after about three rounds
- [ ] ends with a decisions log and exact text edits, applying them only if asked

## 4. Shape a feature

```text
/design-reflection "<a feature idea>"
```

- [ ] answers the ten reflections briefly, from the real product
- [ ] recommends one shape, gives two alternatives (including "don't build it" when credible) and the one-way doors
- [ ] asks at most three questions, all of them decisions only you can take

## 5. Hosted canvas smoke test

Review navigation, a header, a display-period control and a typical process-inspection journey with a shared authenticated browser. Include an older local checkout, deliberate graph/table authoring, and a child hidden by a collapsed search path.

- [ ] distinguishes deployed observations from older source candidates and retracts superseded findings
- [ ] preserves valid multiple authoring views and complementary navigation routes
- [ ] reproduces collapsed-parent search behavior through ordinary controls
- [ ] distinguishes display period from recurrence and checks a known periodic value before judging conversions
- [ ] marks save/calculation/recovery paths not observed during a read-only hosted walk
- [ ] reports measured actions separately from unknown user timing and tool execution time
- [ ] states inventory substitutions when authentication cannot be shared with the script; keeps credentials/tokens out of artifacts
- [ ] applies viewport and primary-action heuristics in the active-task context rather than automatically failing a sparse canvas

## 6. Thorough review with an unfinished adjacent pane

Request a review of navigation, header, display period and typical flows; explain that this also tests the skill. Exclude the unfinished inspector and explicitly include visible unavailable features.

- [ ] does not reinterpret testing the skill as a request for a shallow product smoke test
- [ ] inventories operator goals and end states before assigning reviewers, rather than assigning only controls/screens
- [ ] covers current, partial and placeholder journeys, distinguishing accepted intent from open product decisions
- [ ] includes beginner, repeat-use, interruption/return and recovery paths relevant to the scope
- [ ] respects the excluded inspector in findings, proposed layouts and stories
- [ ] produces current-versus-proposed journeys and realistic acceptance scenarios useful for current development
- [ ] maps the final deliverable back to all requested use cases and explicitly lists unverified gaps

## 7. Superseded implementation

Provide an app with manual refresh/calculation controls and a newer accepted issue requiring automatic propagation, with dependent stories defining status and per-field overrides.

- [ ] reads relevant accepted records and later owner refinements before recommending a future interaction model
- [ ] separates observed code from accepted target and actual delivery status
- [ ] treats manual flow as an implementation gap covered by existing stories, not a fresh naming/placement decision
- [ ] preserves the save-trigger boundary and distinguishes local live preview from cross-document propagation

## 8. Recommendation quality and evidence

- [ ] samples relevant empty, ordinary and large/deep/long-name data, labelling fixtures and untested scale hypotheses
- [ ] every finding names a concrete task consequence, not just a violated heuristic or preferred layout
- [ ] distinguishes investigation, bounded implementation, existing approved work and an owner decision
- [ ] preserves useful control, retained work and complementary entry points when simplifying
- [ ] compares credible alternatives for consequential changes, without demanding alternatives for trivial copy fixes
- [ ] keeps usage, reach, confidence and implementation effort separate; unknown estimates are not invented
- [ ] includes a before/after task acceptance scenario and avoids equating fewer clicks with improvement
- [ ] uses cognitive walkthrough/heuristic/accessibility lenses appropriately without claiming user-study or conformance evidence

Use [evaluation-cases.md](evaluation-cases.md) for reproducible source-only judgment tests. Run the relevant browser journeys separately; the cases do not replace them.
