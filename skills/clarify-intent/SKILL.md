---
name: clarify-intent
description: Interview the person to pin down meaning and intent before (or while) work is specified — the conversational counterpart of design-reflection and interaction-flow. First explores the product, code and records so it never asks what they can answer, then asks only what the person alone can decide (the need, who and when, what done means, the authority line, scope, trade-offs, names, states that matter, the success signal), a few questions at a time, each with proposed answers and why, and records every decision. Two commands: `review <spec, story or feature>` finds where meaning or intent is ambiguous and resolves it with the person; `spec <idea or story>` interviews and then writes the spec. Use when the person says "ask me", "clarify", "interview me", "grill me on this", when an intent is vague, when a spec reads well but could mean two things, or before a costly run.
user-invocable: true
argument-hint: "review <spec | story | feature> · spec <idea | story>"
---

# Clarify intent

A spec fails most often not in its code but in its meaning: two readers, two products. This skill closes that gap by talking with the person who owns the intent. It explores first, asks second, and writes last.

## Before asking anything: explore

Read what can answer questions without the person: the product's own definition (README, brief, current state), the object's parents (the epic's why and decisions, the project's intent), the code the change would touch, related feedback, issues and earlier specs, and the lenses in this skill's references ([meaning-and-context.md](references/meaning-and-context.md), [how-people-think.md](references/how-people-think.md), [design-reflections.md](references/design-reflections.md)). Write down what you now know and what you assume. **Never ask a question the records, the code or the person's earlier words already answer**; state the answer as an assumption instead and let them correct it.

## What to ask about

Only what the person alone can decide. Draw candidates from these, then keep the ones that matter:

| Topic | The question behind it |
|---|---|
| Need | What problem, for whom, observed where? Is the request a solution to something else? |
| Who, when, mode | Who does this, how often, while doing, waiting, understanding or configuring? |
| Outcome | What does done look like, observably? What would make you reject the result? |
| Authority line | What must you decide yourself; what may the system or a model decide; what is never automatic? |
| Scope | What is explicitly out? What tempting extension must wait? |
| Trade-offs | Speed or safety, simple or complete, now or later: which wins here? |
| Names | What do you call it? Which word must never appear? |
| States that matter | Empty, many, failure, conflict, undo, old data: which must work on day one? |
| Order and dependencies | Does this need something else first, or block something? |
| Signal of success | What will you look at to know it worked? |

Rank candidates by **uncertainty × impact**: ask first where a wrong guess would change the most work. Skip topics whose answer is already clear; say so in the summary.

## How to ask

- **Few at a time.** One to four questions per turn, related ones together. In Claude Code use the AskUserQuestion tool: two to four options per question, the recommended one first with "(Recommended)" in its label, and a short description of each option's consequence. The person can always answer in their own words.
- **Propose, don't quiz.** Every question carries proposed answers and why you lean to one, drawn from what you explored. People recognise faster than they recall.
- **Name the consequence.** Each option says what it would change in the spec or the product ("Refuse from the queue: safer, but a line can stall").
- **Plain words.** The person's vocabulary, not the code's. Quote the ambiguous phrase you are resolving.
- **Follow the answers.** An answer can open a better question or close three others; re-rank after each turn.
- **Stop on time.** Stop when the remaining uncertainty would not change the work, or after about three rounds, whichever comes first. Say what you left as an assumption.

## Command: `review <target>`

1. Read the target (a spec, a story's intent, a feature description, a mock-up) and explore its context.
2. List its **ambiguities of meaning**: a phrase two careful readers would build differently, a done-when that can't be observed, an unstated authority line, a missing out-of-scope, a state left undefined, a name used two ways, a dependency left implicit. Quote each.
3. Resolve what exploration can; ask the person about the rest, ranked.
4. Deliver: the ambiguities found, each with its resolution (answered by the person, or assumed with reason), and the exact edits to the target's text that encode the answers. Apply the edits only if the person asks, or if the target is a draft you were asked to improve.

## Command: `spec <idea or story>`

1. Explore, then write a one-paragraph understanding of the intent and show it first ("Here is what I understand; correct me").
2. Interview, ranked, in rounds.
3. Write the spec in the project's own format (its card or template if it has one; otherwise: Outcome, Acceptance criteria, Scope, Out of scope, Files likely touched, Verification, Open questions). Every acceptance criterion is observable; every decision from the interview appears where it constrains the work; nothing the person left undecided is silently decided: it is either an assumption stated in Scope or an open question.
4. If the project limits spec size or has a spec check, respect it and run it.
5. Saving the spec where the work is tracked is a separate, explicit step the person approves (for example a draft in the tracker, never an approval).

## The decisions log

End every session with the log, short and reusable:

> **Q:** <question, quoting the phrase it resolved> · **A:** <answer> · **By:** person | assumed (why) · **Changes:** <what it changes in the spec or product>

Keep it with the work (in the spec's notes, the story, or the issue) so later readers and models see why the spec says what it says.

## Don'ts

- Don't ask what you could have looked up.
- Don't ask more than four questions in one turn, or keep going once answers stop changing the work.
- Don't ask leading questions that hide a decision in a default; show the trade-off.
- Don't decide for the person what the authority line reserves for them, and don't approve anything.
- Don't let the interview replace the spec: always end with written decisions.
