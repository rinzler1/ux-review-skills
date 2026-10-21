---
name: interaction-flow
description: >-
  Map, review and redesign how a person moves through a product to get their work done — the journeys, not the
  pixels. Starts from the product's intent and object hierarchy, walks the real app to measure each typical
  use case (clicks, page changes, waits, repeated or missing information, steps whose order the user must
  remember), tags every step by the person's mode (doing, waiting, understanding, configuring) since each mode
  needs different design, can fan out one agent per use case and merge their findings into a ranked priority
  list, checks that every object says why it exists and that context inherits from level to level and stays
  connected to what the product is today, judges how each screen groups, separates and orders its content for
  the way people read and whether each tab, pane, drawer, modal or fold fits how its content is used, rates
  what each screen shows against what the person needs at that moment (now, soon, on demand, elsewhere,
  never), finds flow defects, and proposes an interaction model with one place per decision, one vocabulary
  for state, and layers from beginner to expert. Use when a workflow "feels clunky", when the user asks how
  people actually use a feature, to plan where features and decisions should live, before redesigning
  navigation, when a user did steps in an order that could not work, or to turn UX feedback into small,
  sequenced stories. Complements screen-level design skills (impeccable, design-critique), which judge a page;
  this one judges the path between pages.
user-invocable: true
argument-hint: "[map | review <journey> | screen <url> | fan-out | model | layers | stories] [product or area]"
---

# Interaction flow

A screen can be well designed and the journey through it still fail: the right button exists but on another tab, the state reads differently in three places, the user must remember to do B before C because nothing stops C. This skill looks at the **path**: what a person wants, what they must know, where they decide, and what the product does for them in between.

Work from evidence. Read the product's own statement of intent and walk the real application before proposing anything. Every claim in your output names where it was observed.

## When the request is narrow

- **"Review this journey"** → steps 1, 3, 4 for that journey only, then a short fix list.
- **"Where should X live?"** → steps 1, 2, then the placement rules in step 5.
- **"Is our model of the work coherent?"** (why per level, context, plan vs product description, diagrams, creation options) → steps 1, 2 with the meaning lens, then the creation journeys.
- **"Is this screen doing its job?"** → step 1, the mode of the step it serves, then the screen pertinence pass on that screen.
- **"Make it easier for beginners / faster for experts"** → step 6.
- **"Turn this feedback into work"** → steps 3–4 on the journeys the feedback touches, then step 7.
- **"What should we fix first?"** across many use cases → steps 1–2, then fan out step 3 (one agent per journey), merge and rank.
- **Full review** → all steps, in order.

## 1. Restate the product intent

Before looking at screens, write in three to five sentences, from the product's own docs (README, brief, product thesis, roadmap) and the user's words:

- **Who** uses it and in what situation (one person or a team; daily or occasional; desktop or phone; expert or newcomer).
- **The job**: what they come to get done, in their words, not the product's.
- **The authority line**: what the person must decide themselves, and what the system may do on its own. A flow that makes the person do what the system could do, or lets the system do what only the person may decide, is wrong by definition.
- **What "good" feels like** for this product (quiet and fast; guided; dense and powerful).

If the intent is unclear, say what is missing and state the assumption you proceed under. Everything later is judged against this paragraph.

## 2. Map the objects and their hierarchy

List the things the person works with (the nouns they would use), how they nest, and the **states** each goes through. For each object note:

- **Its home**: the one place it is shown in full and changed. Elsewhere it may be referenced, linked or summarised, never edited a second way.
- **Its lifecycle**: states in order, which transitions the person triggers and which the system triggers, and which are irreversible.
- **Derived vs recorded**: what the product stores versus what it computes. Status words should be computed from records by one function, not re-phrased per screen.

Then run the **meaning and context** lens in `references/meaning-and-context.md` on the map: does each level say its why, what and how at its own level; does context inherit downwards instead of repeating; does the plan connect to the description of what the product is today; do living artifacts (diagrams, summaries) show their freshness; is creation staged with options explained by consequence. These findings are often the root of flow problems further down.

Draw it as a small tree or table. Mismatches between the object model and the navigation (an object with two homes, a state with no visible home, a parent that cannot show its children's progress) are findings.

## The four modes

At any moment a person is mostly in one of four modes. Each wants different things from the screen, so tag every journey step with its mode. Many flow defects are a screen built for one mode while the person is in another.

| Mode | The person is… | They want | Design for it | Typical defects |
|---|---|---|---|---|
| **Doing** | acting on their task: creating, deciding, approving, answering | speed and certainty: the next action, the facts it needs, nothing else | one primary action; the information for the decision beside it; land on the next step afterwards; keyboard path for repeats | the action on another tab; explanation text crowding the action; a decision split across places; order they must remember |
| **Waiting** | idle while the system or someone else works | to know it's moving, how long, whether they may leave, and to be told when it's their turn | the phase and an expected duration; a quiet live indicator; "you can leave this page"; park the result and raise one decision row when done | a spinner with no phase or duration; the user must keep watching; a result arriving silently; waits counted as "needs you" |
| **Understanding** | reading what is in front of them, orienting, checking why | a clear hierarchy: what this is, where it stands, why, in plain words | one state per object said once; headings that name the thing; the "why" one click away, not inline; real data, never invented | the same state in different words; jargon or internal names; dense blocks; numbers without units or source |
| **Configuring** | setting something up once or changing how the product behaves | to see the current value and where it came from, the effect before committing, and a safe way back | defaults with their source; a preview of the effect; undo or reset; kept out of the daily path but linked from where it matters | settings needed in the daily path; a setting with no visible effect; options hidden where the journey never goes; changes with no way back |

Each mode has its own section of human principles in `references/how-people-think.md` (perception and memory for understanding, decisions and errors for doing, the psychology of waiting for waiting, defaults and trust for configuring). Read the relevant ones before judging a step.

Rules that follow:

- A step's mode decides its layer (step 6). Doing lives in L1, understanding in L0 and L2, configuring in L3 and in settings, linked from the doing step it affects.
- When a step mixes modes (configure in the middle of doing), either decide the configuration by policy and show it as a default, or move it to its own moment before the journey starts.
- Count the time per mode across a journey. Long waiting time is a case for automation or notification, not a faster spinner. Long understanding time means the screen doesn't say what it is.
- Recovery after a failure is doing, preceded by understanding what failed. The screen must serve both, in that order.

## 3. Inventory the typical journeys

Pick the journeys by **frequency × consequence**: the daily loop first, then the rare-but-costly ones (recovery from failure, first use, undo). Usually five to eight. For each, write the trigger, the intended end state, and then **walk it in the real app** (a throwaway instance with sample data, never production writes) and record per step:

| Measure | Why it matters |
|---|---|
| Clicks and keystrokes | effort |
| Page or tab changes, drawers, dialogs | context lost |
| Waits on the system, and whether the screen says how long | idle time, uncertainty |
| Information the user must carry from one screen to another | memory load |
| Information shown twice, in different words | doubt |
| Steps whose **order** the user must know, unenforced by the UI | silent failure |
| Decisions the user makes, and where | decision placement |
| Options that exist but are hard to find | hidden capability |

Tag each step with its mode (doing, waiting, understanding, configuring). At every stop, also run the **screen pertinence pass** in `references/screen-pertinence.md`: inventory what is visible (`python ${CLAUDE_SKILL_DIR}/scripts/screen_inventory.py <url>` (needs Playwright: `pip install playwright && playwright install chromium`, or `uv run --with playwright python …`) lists regions and elements with their share of the viewport), rate each against this step's mode and question (now · soon · on demand · elsewhere · never), and report the pertinence ratio, where the answer sits, competing primaries and repeats. Then run the **structure and reading pass** in `references/structure-and-reading.md` on the same screen: one container per thing, separation matching relationship, the same container for the same kind of content, a reading path that follows importance, alignment and nesting depth (the script reports depth, container styles, reading order and left edges). Finally the **disclosure pass** in `references/disclosure-patterns.md`: for every tab, pane, drawer, modal, fold, stepper and popover (the script lists those it finds, open or closed), does the promise the pattern makes fit how the person uses the content — simultaneity, sequence, frequency, context kept, addressability, discoverability, mode and width? Use the template in `references/templates.md`. Screenshot each stop. Count, don't estimate. Where you could not observe something (a model call you cannot make, a state you cannot reach), say so and say where the claim comes from instead.

### Fanning out over use cases

With four or more journeys, walk them in parallel: one agent per journey, then merge. Walk them yourself when there are fewer, or when the app can't run several instances at once.

1. **Prepare one brief, shared by every agent.** It holds the intent paragraph and the object map (steps 1–2), the four modes table, the path to `references/flow-checklist.md` and the journey template.
2. **Add per journey:** its trigger, its end state, its frequency, and how to reach its starting state (sample data or a seed script).
   Also include the paths to `references/how-people-think.md`, `references/screen-pertinence.md`, `references/structure-and-reading.md`, `references/disclosure-patterns.md` and `references/meaning-and-context.md` (and the inventory script), so each agent names the human cause of its findings.
   If the product has a stand-in for slow or paid outside calls (a fake model, a sandbox payment provider), name it so agents can walk those steps, and have them label what it produced as simulated.
   If an earlier review exists, give each agent its findings for that journey, so it reports which are still there, which are gone and which are new.
3. **Isolate each agent.** Before launching, ask the person where the agents may walk:
   - a disposable instance they start for you (a local dev server with seed data, a preview deploy), with how to start it if each agent needs its own;
   - or a staging or production URL to walk **read-only**.

   Never guess how to start or reset their app. Read-only means page loads, tabs, folds, menus, hovering and reading only; any step that would save, send, pay, delete or publish is described from the code and the records instead, and marked "not observed". No agent edits the product's code. The agent's only output is its report.

   Agents reach their starting state through the product's own screens or its documented seed script. An agent that steps around a check to get there, or skips its instance, says so and why, and marks what followed as reached by a shortcut.
4. **Fix the return format.** The measured journey table, then findings with the template's fields, each tagged with mode and severity. Where the agent could not observe something, it says so.
5. **Launch them together,** one subagent per journey in a single message (the Agent tool in Claude Code). First tell the person the number of agents, roughly the cost (about 200,000 tokens and up to 20 minutes per journey: eight journeys on one real product used 1.7 million tokens), and where they will walk, and wait for their go-ahead. This can share the question that picks the journeys, as long as the count, cost and walk target are stated before the answer that serves as the go-ahead. Where the agent has no subagents, walk the journeys one after another yourself with the same brief, and say so.

**Merging:**
- **Group duplicates.** Two journeys hitting the same defect make one finding with a higher reach.
- **Keep a finding seen on one journey only** with reach 1. Don't drop it.
- **Rank** by `priority = frequency × consequence × reach`:
  - frequency: daily 3, weekly 2, rare 1;
  - consequence: blocks 3, costs 2, confuses 1;
  - reach: the number of journeys affected.
- **Break ties,** which are common once several groups reach every daily journey:
  - a group containing a blocker first;
  - then the group with more findings;
  - then doing and waiting steps over configuring ones, since they are on the daily path.
- **Compare with the earlier review** when there is one: mark each group still there, new or gone.
- **Report back** a ranked table first, then the per-journey details. Report the time spent per mode across all journeys. Say which journeys could not be fully walked.

## 4. Find the flow defects

Run each journey through `references/flow-checklist.md`. The most common and most costly defects, in order:

1. **Order-dependent steps the UI allows out of order.** The user must do A before B, both buttons are live, doing B first silently does the wrong thing. Fix by disabling B with a reason, by making B do A first, or by merging them into one action.
2. **One decision in several places, or one place with several unrelated decisions.**
3. **State said differently on different screens.** One vocabulary, derived once.
4. **The next action is not on the screen where the state is.**
5. **The question is separated from where it is answered** (drawer, other tab, other page).
6. **A system wait with no progress, no expected duration, and no way to leave.**
7. **A capability hidden behind a setting, a menu or a panel the journey never passes.**
8. **An error that says what failed but not what to do.**

For each finding, name the human cause from `references/how-people-think.md` (for example: relies on recall, not recognition; uncertain wait; mental model differs from the system's behaviour; choice overload; change outside the focus of attention). The cause chooses the fix: a slip needs undo or a constraint, a mistake needs a clearer model, a recall burden needs the screen to carry the fact.

Rate each finding: **blocks** (the journey fails or produces a wrong result), **costs** (extra steps, waits, memory), **confuses** (inconsistent words or places). Fix blocks first.

## 5. Propose the interaction model

Few places, each with one job. A useful default for work-tracking products, to adapt rather than copy:

- **Status** — where everything stands (a board, a list). Read-only. Shows each item's state in the shared vocabulary.
- **Decisions** — what waits on *this person*, and nothing else (an inbox). Each row opens the exact place the decision is made. Things waiting on the system or on others are listed apart and never counted.
- **Record** — what happened, as a filterable log. Prefer a log to a record screen for anything that is history.
- **The object's own page** — the one home where it is read in full and changed, its next action in the header.

Placement rules:

- Put a decision where the information needed for it is visible.
- A system-owned step should not need a click. Park the work and raise one decision row when a person is required.
- Say the expected wait and the current phase for anything slower than a few seconds.
- Write the vocabulary as a table: object state → word → visual shape → who it waits on. Words need a shape or a label, not colour alone.

Show the model as a short list of places with their jobs, a decision-placement table, and the vocabulary table. Mock up only the screens that change, at the product's real scale and in its design system. The user reviews mock-ups before anything is built.

## 6. Layer from beginner to expert

Design four layers, each complete on its own:

| Layer | The person sees | Example |
|---|---|---|
| **L0 glance** | where things stand, in one word and shape | a status chip, a count |
| **L1 next action** | the one thing to do now, as a primary button | "Approve and queue" |
| **L2 on demand** | the details behind the decision, one click away | the spec, the diff, the criteria with evidence |
| **L3 expert** | raw data, overrides and batch tools, out of the default path | the prompt sent, take over the session, edit the policy |

Rules:

- A beginner can finish every typical journey using only L0 and L1, with defaults chosen by policy.
- Never hide a *required* decision in L2 or L3. Hide options, not obligations.
- Experts get speed, not different rules: keyboard paths, batch actions, saved choices, deep links.
- When an expert option changes a default, show the default and its source next to it ("defaulted from the template: required").
- Name things by what the person recognises, not by how the system is built.

## 7. Turn it into work

Sequence the changes as stories small enough for one implementation pass each:

- **Shared foundations first.** A vocabulary module, say, comes before the screens that use it.
- **Then the most-used screen,** then the rest.
- **Each story names** the journey and defect it fixes, the feedback or issue it closes, and the files it will touch, found by search.
- **Stories that touch the same files** either run in sequence, each on the previous one's result, or are split so they don't overlap.
- **Mark which stories need the person's yes** before they are written (removing a place, changing an authority line).

## Output

Deliver, in this order, with the templates in `references/templates.md`:

1. The intent paragraph and the object map.
2. **The priorities:** findings ranked by frequency × consequence × reach, each tied to a journey step, its mode and evidence.
3. The journeys as they are, measured, with time per mode.
4. The proposed model: places, decision placement, vocabulary, layers.
5. Mock-ups of the screens that change.
6. The sequenced stories.

State what was verified, where and when, and what was not.

## How people think

Judge a flow against how people really behave, not how a careful user should. `references/how-people-think.md` turns principles from Weinschenk's *100 Things Every Designer Needs to Know About People*, Norman, Nielsen and research on memory, decisions and waiting into one question per principle, grouped by mode. Fan-out agents get it in their brief.

## Don'ts

- Don't judge a flow from code or screenshots alone when the app can be walked.
- Don't propose a new place before checking an existing one can't hold the job.
- Don't solve a flow defect with documentation or a tooltip when the UI can prevent it.
- Don't let a model decide what the authority line reserves for the person.
- Don't design for the ideal careful user. Design for people who scan, forget, satisfice and get interrupted.
- Don't invent data in mock-ups. Use real records or label examples as examples.
