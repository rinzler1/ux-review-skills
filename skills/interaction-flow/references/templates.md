# Templates

## Intent

> **Who:** … **Job:** … **Authority line:** the person decides …; the system may … on its own. **Good feels like:** …

## Object map

| Object | Contains / belongs to | States (person → / system →) | Authoritative model / editing surfaces | Irreversible steps |
|---|---|---|---|---|

## Journey (one per typical use case)

**Evidence:** browser-observed / shared-walker evidence / source-inferred / not observed. **Deployment/source parity:** confirmed <version> / differs / unknown.

**Journey:** <name> · **Trigger:** … · **End state:** … · **Frequency:** daily / weekly / rare · **Walked on:** <instance, date>

| # | Mode | Where | What the person does | What the system does | Clicks | Wait (shown?) | Carried in memory | Defect |
|---|---|---|---|---|---|---|---|---|

Mode is one of: doing, waiting, understanding, configuring.

Totals: observed clicks, page changes, waits (stated / unstated), repeated facts, order-dependent steps, and measured time or observed steps per mode. Leave unobserved write/recovery segments and unmeasured durations unknown; separate tool/reviewer elapsed time. Record walkthrough shortcuts and their effect on evidence.

## Screen pertinence (one per stop)

**<screen>** · journey <name> step <n> · mode <mode> · question: "<what the person wants to know or do>"

| Region / element | Share of first viewport | Rating (now · soon · on demand · elsewhere · never) | Verdict |
|---|---|---|---|

Structure: max depth <n> · container styles <list> · predicted visual prominence <element, does it serve the task?> · reading order <first five> · left edges <n> · containers holding two things <list>

Disclosure: <pattern → content → fits? (simultaneity, sequence, frequency, discoverability)> per pattern found

Pertinence ratio: <measured x% or unknown> of the first viewport is **now** · The answer is <where, how large> · Competing primaries: <n> · Repeats: <list> · Remove: <list> · Fold: <list> · Move: <list → place>

## Finding

- **[blocks|costs|confuses] · <mode> · <short title>.** Journey <name>, step <n>. What happens: … Human cause: <principle from how-people-think.md>. Evidence: <screenshot / file:line / record>. Next action: investigate / implement / existing work / owner decision. Fix and expected benefit: … Preserve: … Validation: … Closes: <feedback / issue>.

## Priorities (after fan-out)

| Rank | Case / finding | Kind / severity | Usage and basis | Reach | Evidence / confidence | Next action | Effort / dependency | Since last review |
|---|---|---|---|---|---|---|---|---|---|

Kind: observed defect / source concern / approved implementation gap / recommendation / owner decision. Next action: investigate / implement / existing story / decide. Frequency is measured, reported or estimated; missing values remain unknown. Reach counts distinct affected cases. Keep effort separate from user impact. Use the optional ordinal aid in recommendations.md only with labelled assumptions; don't rank a hypothesis as a proven blocker. Since last review: still present / resolved / new / unverified. Report only measured task time, separate from tool/reviewer time.

## Interaction model

**Places**

| Place | Its one job | Shows | Never shows |
|---|---|---|---|

**Decision placement**

| Decision | Made in | Information visible there | Parks the item in |
|---|---|---|---|

**Vocabulary**

| Gate / phase | Sub-words | Shape | Waits on |
|---|---|---|---|

**Layers**

| Journey | L0 | L1 | L2 | L3 |
|---|---|---|---|---|

## Story

**<title>** — fixes <journey · defect>; closes <codes>; touches <files found by search>; depends on <story>; needs the person's yes: yes/no.

## Review coverage and use-case contract

**Scope / exclusions:** … **Review depth:** full / bounded journeys / explicitly requested smoke. **Evidence environment and mutation authority:** … **Observed implementation / accepted target / delivery status:** …

| ID | Actor and job | Trigger / starting state | Successful end state | Frequency / consequence | Entry and regions crossed | Capability (working / partial / placeholder / absent) | Evidence (observed / source / intent / unknown) | Allowed validation / remaining gap |
|---|---|---|---|---|---|---|---|---|

For each case include current path → friction and human cause → proposed path using accepted primitives → normal, empty, busy, failure, retry, interruption and return states as applicable → beginner and expert access → concrete acceptance steps. Mark not applicable rather than inventing states. For placeholders, name the accepted intent and unresolved owner decision; never supply a fictional completed journey.

Before delivery, map every requested region and capability to its covered cases. Disclose every missing case and why. Link each recommendation to the case it improves, evidence, expected practical benefit, affected boundary, owner decision if needed, and a test/validation scenario. A collection of button observations does not satisfy this template.
