# Manual tests

These skills are judged by how an agent behaves with them, so they are tested by using them and watching. Run each test in a **fresh session** (skills load at session start) and tick what you observe. Report what you saw in an issue: what passed, what didn't, the agent and its version.

## 1. Fan-out over journeys

```text
/interaction-flow fan-out <your app's URL or name>
```

Give it nothing else, and watch whether it:

- [ ] reads the product's own docs and states the intent (who, job, authority line) before anything else
- [ ] maps the objects and proposes five to eight journeys, saying why each was picked (frequency × consequence)
- [ ] asks where the agents may walk (a disposable instance or a read-only URL) and doesn't guess how to start the app
- [ ] announces the number of agents, a rough cost and where they'll walk, then waits for your go-ahead
- [ ] launches one subagent per journey in parallel (Claude Code), or says it will walk them one after another
- [ ] gives every agent the same brief: intent, objects, modes, checklist, human principles
- [ ] never writes in a read-only walk (no saves, sends, payments, deletions), and marks such steps "not observed"
- [ ] returns per journey: the measured steps with modes, screen passes (pertinence, structure, disclosure), and findings with severity, mode and human cause
- [ ] merges duplicates across journeys, ranks by frequency × consequence × reach, and reports time per mode
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
