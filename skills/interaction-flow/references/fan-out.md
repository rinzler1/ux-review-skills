# Fan out over complete use cases

Use for `fan-out`, or a broad review with authorized delegation. The default goal is a useful snapshot of this project, not an exhaustive product audit.

## Pick goals, not screen ownership

Identify a small set of relevant operator outcomes before dispatch. Usually four to eight is enough, but use the actual scope. Examples: resume yesterday's work; create a first useful item; edit several related items; accept an updated source; recover from a failed action; return from settings without losing place. “Left pane” and “period button” are regions/actions, not use cases.

Include first-use and repeated/expert paths where they differ. Sample representative data and relevant failure/return states; do not invent rare cases merely to fill a quota. Treat partial/unavailable capability paths as intended journeys, clearly distinguished from observable completion.

## Give every reviewer the same context

Share intent/authority, object relationships, review target/version, relevant accepted decisions, scope/exclusions, allowed actions, evidence vocabulary and prior findings. Add per case its trigger, starting state, successful outcome, likely frequency and how to reach it through real screens or documented fixtures, prepared before dispatch where it isn't in the data (see SKILL.md step 2). Add what the reviewer may change, which side effects were disabled, and its budget for actions that spend money. Include only the reference lenses relevant to the task. Within a reviewer's word budget, apply the full pertinence, structure and disclosure passes to the one or two screens where the case's decision or wait happens, and note only clear problems elsewhere.

Use available delegation tools, one reviewer per independent use case where practical; group adjacent cases when resources are limited and retain their individual outcomes. State count, target and a task-specific effort estimate; missing usage/cost is unknown. Honor session authorization and obtain any missing access or material additional cost approval. Do not use a historical token total as a per-journey minimum.

Independent browser walks need isolated state: disposable instances or independent read-only sessions. With one authenticated session, a shared walker can gather evidence for parallel analysis. Label this shared-walker review; screenshot/source reviewers have not independently completed the journey. If delegation is unavailable, walk sequentially and say so. Never give several agents conflicting edit ownership or credentials in public artifacts.

## Return format

Each reviewer returns, within a stated word budget: current path and mode per step; measurements with evidence boundaries; findings with consequence and human cause; what works; proposed path/trade-off; recovery/return states; acceptance scenario and coverage gaps. Explicitly label fixture shortcuts or simulated external calls. An unexecuted mutation is not a measured successful journey.

## Merge by cause and useful next action

- Group the same cause across cases and count distinct affected use cases, not reviewers or repeated sightings.
- Retain a finding with reach one. Do not multiply reach by how finely the review happened to split journeys.
- Separate demonstrated defects, concerns awaiting reproduction, approved delivery gaps and owner decisions.
- Prioritize consequence, usage frequency and reach; show confidence and separate effort/dependencies. Use the optional ordinal aid in recommendations.md only with labelled assumptions.
- Compare prior findings as still present, resolved, new or unverified. Missing access is not a pass.
- Keep contextual exceptions: a repeated route may be useful, a sparse workspace may be appropriate, and explicit operator control may justify a click.

Publish one coherent fix list and use-case coverage summary. Include per-case detail needed to act, not every agent transcript. Recommend the smallest useful investigation, implementation or owner decision; don't automatically invent one story per finding or dispatch code changes.
