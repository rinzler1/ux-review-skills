---
name: interaction-flow
description: >-
  Evaluate a project's current UX through complete user journeys, then propose prioritized,
  actionable fixes. Use for clunky workflows, multi-screen or multi-pane reviews, discoverability,
  navigation, feedback, recovery, and beginner-to-expert paths. Can fan out by use case and merge
  findings. Complements visual design skills: this skill evaluates how people get work done.
user-invocable: true
argument-hint: "[map | review <journey> | screen <url> | fan-out | model | layers | stories] [project or area]"
---

# Interaction flow

Give the person a useful snapshot evaluation of their current project: which journeys are hard, why, and what to fix. Walk the product where possible; don't substitute a checklist of buttons for the work a person came to do. Start with what is available and deliver a scoped review without making the person configure a review process.

## Choose the depth

- No subcommand or `review`: evaluate the requested area's important journeys and return prioritized fixes.
- `screen`: evaluate the screen at the moments and tasks it serves, including entry and return.
- `fan-out`: choose complete use cases, review them in parallel where supported, and merge shared causes. Read [fan-out.md](references/fan-out.md).
- `map`: explain the current objects and journeys; `model` or `layers`: propose placement or progressive disclosure; `stories`: turn findings into bounded development work.

A multi-region request still needs complete journeys through those regions. Testing the *skill* does not make the product review a shallow smoke test. Match the requested scope; do not turn a single journey into a whole-product audit. Read [review-coverage.md](references/review-coverage.md) for multi-region reviews and use-case fan-out.

## 1. Understand enough to review the snapshot

Use session context and the product's brief, local instructions, task/spec and available records to state who uses it, the job, and the authority line: what the person decides versus what the system may do. Note the objects they work with and their relationships. Do not impose a methodology or completeness requirements on a permissive tool.

Identify the review target internally: current worktree/local build, deployed URL or supplied prototype. Record the version if known. A local project is a normal starting point; source access and GitHub are not prerequisites. Check relevant current decisions when available, especially explicit replacements of the observed workflow; don't demand a roadmap audit or a separate baseline exercise. Keep **observed behaviour**, **accepted target**, and **delivery status** distinct. Existing manual behaviour may be an already-planned implementation gap, not a fresh design decision. If intent is unavailable, state a narrow assumption rather than inventing it.

Use existing authorization and documented startup instructions. Ask only for missing access or decisions that materially change the review. Walk hosted sites read-only unless writes are expressly authorized; evaluate write paths from source and label them unobserved. Use disposable data for authorized creation, saving, sending or deletion tests. Never persist credentials/session tokens in reports or treat authenticated access as permission to mutate data.

## 2. Choose complete use cases

Pick goals by likely usage and consequence, including the ordinary daily loop and relevant first-use, interruption/return and recovery cases. Use representative available records: an empty state, ordinary data and a large/deep/long-name case where relevant. Label invented fixtures and frequency estimates. Don't claim a large-data problem from a tiny example alone.

For each case state actor, trigger/start, successful outcome, entry points, regions crossed and relevant capability availability: **working / partial / placeholder / absent**. Include unavailable controls when they promise an in-scope job, but distinguish their intended journey from a working one. Do not recommend building every placeholder. Explicit exclusions apply to findings, proposed layouts and stories as well as screenshots.

Map the objects to their authoritative records and intentional editing surfaces. Graph/table views or a tree/breadcrumb can be valid complementary routes. Look for divergent state or edit semantics, not merely multiple entry points. Adapt [meaning-and-context.md](references/meaning-and-context.md) to the product's own nouns rather than imposing project/epic/run structures.

## 3. Walk the task, not just the screen

For each case, follow the real interface to its outcome where allowed. Record observed actions, transitions, waits, recovery and return; screenshot meaningful stops. Count only performed steps. Keep unmeasured user time, unexecuted writes and unreachable states unknown; browser/tool execution time is not user task time. A source-derived path is useful evidence, not a completed browser journey.

Tag each step with its main mode:

| Mode | What the person needs | Check |
|---|---|---|
| Doing | Act confidently with the necessary facts | Discoverable action, prerequisites, useful immediate feedback |
| Waiting | Understand progress and whether they can leave | Phase, completion/failure and safe return; no fabricated ETA |
| Understanding | Know what this is and what the numbers/state mean | Scope, units, freshness, plain vocabulary and hierarchy |
| Configuring | Understand the current setting and its effect | Scope, source/default, consequence and reset/recovery |

Use the relevant lenses, not every reference at every stop:

- [flow-checklist.md](references/flow-checklist.md): prerequisites, state, decision placement, navigation and recovery.
- [screen-pertinence.md](references/screen-pertinence.md): what serves this task now or on demand.
- [structure-and-reading.md](references/structure-and-reading.md) and [disclosure-patterns.md](references/disclosure-patterns.md): grouping, reading order and whether tabs/panes/dialogs preserve needed context.
- [ux-methods.md](references/ux-methods.md): cognitive walkthrough for discoverability, heuristic review for feedback/recovery, keyboard/focus/status checks.
- [how-people-think.md](references/how-people-think.md): explain a supported human cause rather than attaching a decorative principle name.

The optional inventory helper is `python3 "$SKILL_DIR/scripts/screen_inventory.py" <url>` with `SKILL_DIR` set to this skill's directory. It needs Python Playwright; use existing approved tooling rather than install dependencies without permission. For an authenticated app, reuse an authorized browser context or inspect DOM/screen evidence and report the substitution. Check inventory against screenshots: nested regions overlap, a blank canvas can be working space, and visual estimates cannot establish eye fixation or human understanding time.

## 4. Keep only consequential findings

A finding needs an affected case/step, concrete behaviour, a practical consequence and evidence. Distinguish:

- **Observed defect:** reproduced behaviour obstructs or misleads the task.
- **Source-backed concern:** plausible problem needing reproduction or failure injection.
- **Approved implementation gap:** existing work already defines the intended change; reference it instead of reopening it.
- **Design recommendation:** a reasoned improvement with an explicit trade-off.
- **Open product decision:** meaning or scope only the owner can choose.

Severity: **blocks** prevents completion or produces a wrong result; **costs** adds steps, memory, waiting or recovery; **confuses** obscures meaning/state. Do not upgrade a hypothesis to a proven blocker. No fixed viewport ratio, nesting count or one-primary-per-screen rule automatically creates a defect; judge the active task and demonstrated consequence.

Preserve what works. Identify useful complementary routes, explicit control, safe partial states and context that a proposed simplification could damage. Fewer clicks is not always a better journey. For consequential changes compare the current approach with one or two credible alternatives, including keeping it when warranted. A small wording correction needs no elaborate alternatives exercise.

## 5. Return fixes someone can use

Lead with the important findings and practical next steps. Use [templates.md](references/templates.md) proportionately; a narrow review need not fill every table. Read [recommendations.md](references/recommendations.md) for prioritization and validation.

1. Brief intent, review target/scope and use-case coverage, including explicit gaps.
2. A ranked fix table: affected case, consequence, estimated or measured usage, reach, evidence confidence, next action and relevant dependency/decision. Keep implementation effort separate from user impact; unknown estimates stay unknown.
3. Per case: current path → friction/cause → coherent proposed path → relevant failure/return behaviour → acceptance scenario. Distinguish beginner discoverability from expert efficiency.
4. The small interaction model needed to make the fixes coherent: places, decision ownership, shared state vocabulary and what belongs on demand. Reuse existing primitives; don't invent a dashboard to solve a misplaced action.
5. Bounded next steps: **investigate**, **implement**, or **owner decision**. Link existing approved work before proposing new stories. Include affected files when source is available, expected benefit, what must survive, and how to verify it. Mock up changed screens when structure needs review, not for every finding.

Before delivery reconcile requested regions/jobs against coverage. Mark cases observed, partially reviewed, unavailable or inaccessible. Group shared causes without dropping isolated findings. With a prior review, distinguish still present, resolved, new and unverified. Never mark an unobserved fix resolved. The review is an expert evaluation, not user research or accessibility conformance certification.

This skill evaluates and proposes work; it does not silently edit the product, publish, notify others or create a roadmap. A request to implement findings supplies a separate scope, subject to the project's existing permissions and instructions.
