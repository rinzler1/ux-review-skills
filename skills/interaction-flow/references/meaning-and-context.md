# Meaning and context: does each object say why it exists, and does context flow?

Journeys and screens can be smooth while the product still confuses, because people don't know *why* a thing exists, what it inherits from its parent, or how it relates to what the product is today. Use this lens where origin, inherited context or meaning affects the requested task.

## 1. Every object answers three questions, at its own level

| Level | Why (purpose) | What (outcome, done when) | How (the work) |
|---|---|---|---|
| Product or project | the thesis, the people it serves | what good looks like | — |
| Group of work (initiative, epic, theme) | the problem and its evidence | the outcome and when it counts as done | which pieces, in what order |
| Unit of work (story, task, ticket) | only what is new beyond its parent's why | the observable result, testable | the spec, the plan |
| Run, job, execution | — (inherited) | the result and its evidence | what was done |

- *Does each level have a place for its why, and is it shown where decisions about its children are made?*
- *Does a child repeat its parent's context, or say only what is new and link up? Repetition drifts; inheritance stays true.*
- *Can a person reading one object reach the why above it in one click?*
- *Is the why written once, by a person, and read by every tool and model that acts on the children?*

## 2. Context is layered, not piled

Context for a person (or a model) acting on an object is assembled from the levels above it plus what is specific to it. Problems to look for:

- **Text that doesn't fit the purpose.** How much text is right depends on why the person is there. Reading a document, a spec, an article or a book, long prose is expected; judge it as reading: clear headings, comfortable line length (about 50–75 characters), one idea per paragraph, typography made for reading. Deciding, acting, waiting or looking for one fact, the person scans: the answer must come first in a few words, and the explanation belongs one click away. The defect is the mismatch — a decision buried in paragraphs, or a document chopped into chips — never length alone. Several unrelated blocks of prose shown at once is a mismatch in any mode.
- **Context with no home:** information that matters to several children but lives in one child (decisions taken, constraints) instead of on the parent.
- **Context with no reader:** sections nobody and nothing reads. Remove them or wire them to the thing that should read them.
- **Stale context:** a summary that no longer matches the records or the code, with no date or source.

## 3. The plan connects to what the product is

A plan (what we intend to change) and a description of the product (what it is today: capabilities, decisions, limits — call it current state, ontology, house, map) are two views of one thing. Check:

- *Does each group of work name which part of the product it changes (capability, area, module)?*
- *When work is done, does the description of the product get updated, by a proposal a person confirms, rather than silently or never?*
- *Can a person see, for a part of the product, the work that shaped it and the work still planned for it?*
- *Is the vocabulary the same in the plan and in the description of the product?*

## 4. Living artifacts show their freshness

Diagrams, maps and summaries help understanding only while they are true.

- *Is each diagram or summary generated from the source of truth (the code, the records), or hand-drawn? Generated is preferred; hand-drawn must say who and when.*
- *Does it show what it was built from ("from commit abc123, 4 days ago; main is 12 commits ahead") and offer to rebuild it?*
- *Is a model-drawn or model-written artifact a proposal the person confirms, not an overwrite?*
- *Is there one diagram per question it answers (structure, flow, data, ownership), rather than one that tries to show everything?*

## 5. Creation and choice architecture

Creating something (a project, an epic, a story, a spec) and choosing how it runs are where options pile up.

- *Is creation staged, one decision per stage (intent → spec → how it runs → approve), with the current stage clear and the others summarised in one line?*
- *Are options explained by their consequence for the person ("two reviewers: slower, catches more"), not by their mechanism ("pi-subagents team with orchestrating lead")?*
- *Is there a default chosen by policy for every option, shown as one sentence with "Change", so a beginner never has to decide it?*
- *Are expert options (orchestration, models, routes, budgets) in layer L3, reachable but not on the creation path?*
- *Does each alternative path (write by hand, ask the companion, run a protocol, import) appear as one choice at the start, not as stacked panels all visible at once?*

Name the human cause for each finding from `how-people-think.md` (choice overload, recall over recognition, mental model mismatch, scanning, attention).
