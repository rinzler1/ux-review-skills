# Prioritize and validate recommendations

## From observation to action

Every finding names a task/step, observed behaviour or source evidence, inferred consequence or explanation, and uncertainty. A principle can explain a possible cause, but does not prove a problem. Separate observed defects from source-backed concerns, already-approved implementation gaps, design recommendations and unresolved product meaning. Label a simulated-perspective review as a heuristic exercise, not user research. Route findings to implementation, investigation, existing work, or owner decision as appropriate.

Preserve current benefits. A proposal to remove duplicate access may harm orientation; automatic action may remove needed control; hiding configuration may hide a required decision. State what the proposed change makes easier, what it could worsen and which accepted behaviour must remain. For consequential structural changes compare the current path and one or two plausible alternatives. Prefer a small coherent change using existing concepts; keeping the current design is a valid conclusion.

## Rank without invented certainty

Rank confirmed blockers, wrong outcomes and other serious consequences ahead of lesser friction. Within comparable severity, use frequency and reach to order findings. State frequency as measured, owner-reported or estimated; do not treat a journey count as measured incidence. An owner's explicit complaint is evidence of concern, not a population rate. Reach counts distinct affected use cases, not agents or repeated observations. Confidence describes reproduced, source-supported or hypothetical evidence; implementation effort stays separate from user impact.

If an ordinal aid helps break ties within a severity band, use labelled frequency and reach assumptions. Do not multiply severity into a score that can bury a blocker, fill missing values, double-count overlapping cases, or rank a hypothesis as a confirmed obstruction. Explain meaningful dependency or evidence considerations.

| Rank | Case / finding | Consequence | Usage and basis | Reach | Evidence / confidence | Next action | Effort / dependency |
|---|---|---|---|---|---|---|---|

An unknown estimate stays unknown. Make the next action explicit: reproduce with a fixture, implement a bounded correction, deliver an existing approved story, or resolve a specific owner question. Do not re-sequence the product roadmap through a UX scoring formula.

## Validate the improved journey

For each proposed fix, write an executable acceptance scenario with starting data, actions, expected outcome and what must survive. Include relevant empty, interrupted or failed states; not every trivial control needs all states. Compare the actual task before/after when it can be walked. A new label or fewer clicks alone is not proof that the task improved.

Verify invariants such as preserved drafts, units, identity, authorizations, context and save ordering relevant to the change. Separate hypothetical benefit from observed improvement. Use representative disposable data for mutations; no production writes or fabricated timings. On a re-review, resolved means the affected journey was checked. A source-only correction is source-addressed, journey unverified; stating its limits does not make an unobserved fix resolved.

An expert review predicts likely usability problems. It does not establish actual user frequency, comprehension, satisfaction or an accessibility conformance level. For the most consequential uncertainty, suggest a short task-based user test rather than accumulating more heuristics.
