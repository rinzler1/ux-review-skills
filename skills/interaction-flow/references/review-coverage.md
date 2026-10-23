# Cover the requested jobs in the current snapshot

Use for multi-region reviews and fan-out. Do this context work internally; users should be able to ask for a review and receive useful fixes without running a setup command.

## Identify the review target

| Available target | Useful context | Boundary |
|---|---|---|
| Current worktree/local build | Local changes, task/spec, acceptance criteria and relevant repository decisions | Work in progress can intentionally omit later work; source is not proof of running behaviour |
| Deployed site | Observable journeys, supplied intent and deployed version if identifiable | Local source may differ; unavailable version/source remains unknown |
| Partial implementation/prototype | What should work in this slice, visible promises and accepted next behaviour | Distinguish partial completion from a defect; never claim a placeholder works |
| Site without repository access | Interface, representative tasks and the user's stated goals | Review still proceeds; don't invent code, issue status or approval |

Check enough authoritative intent to avoid recommending an obsolete workflow. Use session instructions, local specs and relevant accepted decisions when available; GitHub is one possible source, not a prerequisite. Follow explicit supersession links or later refinements for affected behaviour. Keep observed implementation, accepted target and delivery status separate. Don't widen a bounded review into a roadmap audit.

State requested regions/jobs, exclusions, depth and allowed actions. Keep exclusions in findings, layouts and stories; mention excluded areas only when needed to identify a transition. Reuse existing access/authorization and startup guidance. Ask only for missing information that changes the review, not a new coverage sign-off.

## Inventory goals before controls

A case needs an actor, trigger/start and recognizable successful outcome. “Click Monthly” is a step; “compare the same quantity at a monthly scale without changing the plan” is a goal. Choose relevant first-use, repeated, interruption/return and recovery cases by usage/consequence, without filling a quota.

Use available representative data: empty/new, ordinary, and large/deep/long-name where relevant. Record what was actually sampled and what remains a scale hypothesis. Label synthetic examples. Classify capability availability independently from evidence:

| Availability | What to review |
|---|---|
| Working | Actual path and outcome, relevant transitions and recovery |
| Partial | Working segment, missing completion and how that boundary is disclosed |
| Placeholder | Promised job, accepted intent if known, placement and unresolved meaning |
| Absent | Only where necessary to a requested job; flag new scope rather than approve it |

Observed, source-inferred, accepted intent and unknown describe evidence, not availability. Multiple intentional authoring views or navigation routes can share one authoritative model; divergent semantics or state are the concern.

## Return complete cases

For each case include current path and modes; decisions/memory carried; friction and consequence; coherent proposed path; useful beginner/expert differences; relevant normal/empty/busy/failed/interrupted/return states; and an executable acceptance scenario. Mark unobserved or not applicable states rather than invent them.

For unavailable capabilities, assess the promised journey without fabricating completion. Reference existing approved work; distinguish open owner decisions from settled ones. Proposed fixes should explain practical benefit, what works today, trade-offs and what must survive. A flaw needs consequence, not merely a violated numerical heuristic or personal preference.

Before delivery reconcile requested jobs/regions with covered, partial, unavailable and inaccessible cases. Unknown is a coverage gap, not a pass. The result should remain useful after removing screenshots: a short ranked fix list, enough journey evidence to act, and explicit next steps for investigation, implementation or an owner decision.
