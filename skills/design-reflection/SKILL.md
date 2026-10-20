---
name: design-reflection
description: Bring a designer's reflection to a feature idea before it is specified or built. The product owner drives what to build; this skill asks the questions a good designer would — what need is behind it, which existing concept it belongs to, the simplest shape that delivers it, what to leave out, its states and edge cases, what can be derived instead of asked, where it lives in each mode and layer, how it scales (more items, parallel work, teams), what it removes, and how we will know it worked — then recommends a shape with alternatives and a few decisive questions. Use when someone proposes a feature or a change ("epics should have dependencies", "add a diagram section"), when shaping an epic or story before its spec, when reviewing a spec for design soundness, or when an idea feels right but its form is unclear. Pairs with interaction-flow, which reviews flows that already exist.
user-invocable: true
argument-hint: "[feature idea or spec to reflect on]"
---

# Design reflection

The person proposing a feature knows the need and the product. This skill does not override their decision; it makes sure the decision is taken with a designer's questions answered. Its output is a short brief: the need, where the feature belongs, a recommended shape, two alternatives, the few questions only the owner can answer, and how success will show.

Read the product's own definition first (README, brief, current state, design system, open feedback and issues) and, when the product runs, look at the places the feature would touch. Reflection grounded in the real product beats generic advice.

## The reflections

Go through them in order. Write one or two sentences each; skip one only by saying why it doesn't apply.

1. **The need behind the request.** Restate it as a job, not a solution: who, in what situation, how often, in which mode (doing, waiting, understanding, configuring; see the interaction-flow skill), and the evidence (feedback, incidents, measurements). A request is often a solution to an unstated problem; name the problem.

2. **Where it belongs in the concept model.** Is this a new concept, or a property, state or view of one that exists? Prefer extending an existing concept to adding a new one. Name it the way the person would. If it overlaps an existing feature, say which one gives way. *Example: "tasks should depend on other tasks" is a property of tasks, and can turn a separate per-run setting ("run these in sequence") into a consequence of the plan instead of a choice to remember.*

3. **Derive, judge, or ask.** For every piece of information the feature needs, decide its source:
   - **derived** by a rule from records;
   - **judged** by a model as a proposal;
   - **asked** of the person.

   Asking is the most expensive. Ask only what the authority line reserves for the person, or what can't be derived. Show derived values with their source, so a person can correct them.

4. **The simplest shape that delivers the outcome.** Describe the smallest version a person would actually use, and what it leaves out on purpose. Name the fuller version as a later step, not as scope now. Subtract before adding: what can this feature remove or replace in the product?

5. **States and edge cases.** Empty, first use, one, many, very many; error, conflict, concurrency; undo and reversal; what happens to existing data (migration, defaults for old records); permissions and the authority line. Name the state most likely to be forgotten.

6. **Where it lives and how it shows.** For each mode it serves:
   - its place (its one home, and where it is only referenced);
   - its layer: L0 glance, L1 next action, L2 on demand, L3 expert.

   Required decisions are never hidden in L2 or L3. Explain options by their consequence, not their mechanism.

7. **Scale and the future.** More items, more projects, parallel work, several people or machines, longer history. Which of today's choices would block that future? Prefer two-way doors (reversible) and say which parts are one-way (data model, public names, migrations).

8. **Consistency.** The same words, patterns and design-system pieces as the rest of the product. A new pattern must earn its cost of learning.

9. **Cost and attention.** What it costs to build, to run (tokens, time, compute), and in attention (a new thing to read, a new choice to make). A feature that adds a daily decision has to save more than it costs.

10. **How we'll know it worked.** One observable signal the product itself can show: fewer clicks on a journey, a count that drops, a wait that disappears, a feedback code that stops recurring.

## Designerly principles to apply

Use these to judge each reflection. Name the principle when it decides something.

- **Subtract first.** The best feature often removes one.
- **One concept per job; one home per concept.**
- **Name things in the person's words,** never the system's.
- **Defaults over options.** Policy over prompts. A good default with a visible source beats a choice.
- **Make the right thing the easy thing.** Make the wrong order impossible, not documented.
- **Show state; don't ask people to remember it.**
- **Reversible by default.** Say clearly when something isn't.
- **Design the second use, not only the first.** The tenth time matters more than the demo.
- **Design the empty, the error and the many,** not just the happy one.
- **Consistent beats clever.**
- **People scan, forget, satisfice and get interrupted.** See [references/how-people-think.md](references/how-people-think.md).
- **Every level says its why, and context inherits.** See [references/meaning-and-context.md](references/meaning-and-context.md).

## Output: the design brief

Keep it to about one page:

- **Need:** the job, who, when, mode, evidence.
- **Belongs to:** the concept it extends, or why it's new; what it replaces.
- **Recommended shape:** the simplest version. What is derived, judged and asked. Where it lives and its layer. States covered.
- **Alternatives:** two other shapes with their trade-offs, including "don't build it" when it's credible.
- **Left out on purpose:** and when it might come back.
- **One-way doors:** what will be hard to change later.
- **Questions for the owner:** at most three. Only decisions the brief can't take: priorities, authority, taste.
- **Signal of success:** the one thing to watch.
- **Next:** mock it (interaction-flow, design-critique), spec it, or file it.

## Don'ts

- Don't decide for the owner what the authority line reserves for them. Recommend, and say why.
- Don't produce a feature list. Produce one shape and its reasons.
- Don't add a concept when a property of an existing one will do.
- Don't skip the states and the future because the happy path looks good.
- Don't ask the owner questions the product or its records can answer.
