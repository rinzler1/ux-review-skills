<!-- Copied from design-reflection/SKILL.md by scripts/sync-shared.mjs. Edit the original, then run npm run sync. -->

# Design reflection

The person proposing a feature knows the need and the product. This skill does not override their decision; it makes sure the decision is taken with a designer's questions answered. Its output is a short brief scaled to the request: the need, where the feature belongs, a recommended shape, credible alternatives when useful, consequential questions only the owner can answer, and how success will show.

Read the product's own definition first (README, brief, current state, design system, open feedback and issues) and, when the product runs, look at the places the feature would touch. Reflection grounded in the real product beats generic advice.

Separate what was observed or supplied from your interpretation and remaining uncertainty. If the prompt asks you to simulate a perspective, label the exercise heuristic; it does not establish what real users think or do.

## The reflections

Use the reflections that could change this decision. A small request needs only the relevant ones; a broad feature may need most of them. Stop when further lenses would repeat evidence or leave the recommendation unchanged.

1. **The need behind the request.** Use the prompt's perspective: whose, in what situation, what they need to accomplish or decide, and what evidence they need. Reuse known frequency and feedback when available. Doing, waiting, understanding and configuring are useful lenses, not exhaustive categories. Distinguish observed need from inferred need and ask only about a gap that changes the shape.

2. **Where it belongs in the concept model.** Is this a new concept, or a property, state or view of one that exists? Prefer extending an existing concept to adding a new one. Name it the way the person would. If it overlaps an existing feature, say which one gives way. *Example: "tasks should depend on other tasks" is a property of tasks, and can turn a separate per-run setting ("run these in sequence") into a consequence of the plan instead of a choice to remember.*

3. **Derive, judge, or ask.** For every piece of information the feature needs, decide its source:
   - **derived** by a rule from records;
   - **judged** by a model as a proposal;
   - **asked** of the person.

   Asking is the most expensive. Ask only what the authority line reserves for the person, or what can't be derived. Show derived values with their source, so a person can correct them.

4. **The simplest shape that delivers the outcome.** Describe the smallest version a person would actually use, and what it leaves out on purpose. Name the fuller version as a later step, not as scope now. Subtract before adding: what can this feature remove or replace in the product?

5. **States and edge cases.** Empty, first use, one, many, very many; error, conflict, concurrency; undo and reversal; what happens to existing data (migration, defaults for old records); permissions and the authority line. Name the state most likely to be forgotten.

6. **Where it lives and how it shows.** For each relevant task or mode:
   - its place and intentional authoring surfaces, with one authoritative model for state, rules and permissions;
   - its layer: L0 glance, L1 next action, L2 on demand, L3 expert.

   Required decisions are never hidden in L2 or L3. Explain options by their consequence, not their mechanism.

7. **Scale and the future.** More items, more projects, parallel work, several people or machines, longer history. Which of today's choices would block that future? Prefer two-way doors (reversible) and say which parts are one-way (data model, public names, migrations).

8. **Consistency.** The same words, patterns and design-system pieces as the rest of the product. A new pattern must earn its cost of learning.

9. **Cost and attention.** What it costs to build, to run (tokens, time, compute), and in attention (a new thing to read, a new choice to make). A feature that adds a daily decision has to save more than it costs.

10. **How we'll know it worked.** Choose an observable signal relevant to the outcome. Click counts or other measurements are diagnostic evidence, not universal quality thresholds; say whether a baseline was measured or only proposed.

## Designerly principles to apply

Use these to judge each reflection. Name the principle when it decides something.

- **Subtract first.** The best feature often removes one.
- **One authoritative model per concept.** Multiple editing surfaces can work when they share state, rules and permissions; flag divergence or unclear ownership.
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
- **Alternatives:** credible shapes and trade-offs when they would affect the decision, including "don't build it" when credible.
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
