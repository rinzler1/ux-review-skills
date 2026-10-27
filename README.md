# UX Review Skills

[![npm](https://img.shields.io/npm/v/ux-review-skills)](https://www.npmjs.com/package/ux-review-skills)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-3-blue)
![Status](https://img.shields.io/badge/status-early-orange)
![Agents](https://img.shields.io/badge/best%20in-Claude%20Code-lightgrey)

**Agent skills that bring a designer's eye to software work.**

Coding agents can now produce a polished screen in minutes. Polish is not the same as design. A product can look finished and still be hard to use: the action you need sits on another tab, the same state is worded three ways, and a decision only works if you remember to make another one first.

These skills give your agent the questions a thoughtful designer asks before anyone argues about colours: what the person is trying to get done, what they need to know at this moment, where each decision belongs, and what a feature really means. They review the product you already have, explain what they find, and turn it into small, ranked pieces of work.

> **Status: early (v0.3).** The method comes from real use on one product. The skills as packaged here are new: feedback and issues are very welcome.

**v0.3.2 patch:** Reviews now follow the perspective and scope in the prompt, distinguish observation from interpretation, and rank confirmed blockers before frequency or reach. Multiple synchronized editing surfaces remain valid. See [manual review checks](docs/manual-tests.md).

## Design is more than how it looks

Typography, colour, spacing and a consistent component library matter. They are also the part of design that is easiest to see, and the part most AI design tools now cover well. A great designer spends much of their time on what lies beneath:

| Concept | The question it asks |
|---|---|
| **User journeys** | What is the person trying to get done, and what path do they actually take across screens, waits and decisions? |
| **Mental models** | Does the product behave the way people expect it to, or must they learn its internals? |
| **Information architecture** | Do the places people use share a clear authoritative model, and are related things found together? |
| **Cognitive load** | What must the person remember from one screen to the next, and could the screen carry it for them? |
| **Progressive disclosure** | Is what matters now shown first, with the rest one step away and nothing required hidden? |
| **Feedback and waiting** | Does the person know what happened, what is in progress, how long it will take and whether they can leave? |
| **Errors and recovery** | Can mistakes be prevented, and when something fails, does the screen say what to do next? |
| **Meaning and vocabulary** | Is each state named one way everywhere, in the person's words rather than the system's? |

Most design skills for agents today work on the surface: they choose fonts, generate palettes, align grids and remove visual clutter. That work is valuable, and these skills don't replace it. What surface tools mostly can't fix is a journey that fails between two well-designed screens, a decision placed far from the facts it needs, or a feature whose shape was never questioned. That is the gap these skills address. Use them alongside a visual design skill, not instead of one.

### A first step, not a replacement for designers

These skills don't replace a designer, and certainly not a senior one. Experienced designers bring things no checklist can: research with real people, judgement about trade-offs that have no right answer, a sense of the business and its users, taste built over years, and the ability to bring a team to a shared decision. An agent walking an app is an expert inspection. It predicts likely problems; it doesn't observe real users.

What the skills can do is the methodical part, quickly and on every change: walk each journey, count the steps, notice the state worded three ways, the wait with no feedback, the error with no way out. For a team without a designer, that is a useful first step and a common vocabulary. For a team with one, it may clear the routine findings from the table, so that designers spend their time on the problems that need them: research, strategy, and the hard trade-offs.

### What the three skills do

They don't generate styles or colour palettes. They review **how people move through a product**, **what each screen should show**, and **what the work actually means**.

For broad reviews, agents can **fan out over journeys**. Each reviewer follows a use case through the running app where possible. Their findings merge into a list ranked by consequence, then usage and reach within comparable severity. A narrow screen or journey review stays narrow.

---

## Quick start

### 1. Install

```sh
npx skills add rinzler1/ux-review-skills
```

The [`skills` CLI](https://skills.sh) installs them for Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot and other agents. Add `--skill <name>` for just one.

<details>
<summary><b>Other install methods</b></summary>

**npm:**

```sh
npx ux-review-skills install            # all three into ~/.claude/skills
npx ux-review-skills install --project  # this project only
npx ux-review-skills list               # what is installed where
```

**Claude Code plugin** (updates with the marketplace):

```text
/plugin marketplace add rinzler1/ux-review-skills
/plugin install ux-review@ux-review
```

Commands are then prefixed: `/ux-review:interaction-flow`.

**By hand:** copy `skills/*` into your agent's skills folder.

Pick one method per agent; installing twice gives you every skill twice.

</details>

<details>
<summary><b>What works where</b></summary>

| Feature | Claude Code | Other agents |
|---|---|---|
| All three skills, all passes and references | yes | yes |
| Fan-out, one reviewer per complete use case | yes (subagents) | uses available delegation, shared-walker analysis, or sequential walks |
| `clarify-intent` multiple-choice questions | yes | asked in plain text, in the same format |
| Screen inventory script | needs Python and Playwright | same |

</details>

### 2. Use

```text
/interaction-flow fan-out http://localhost:3000
/design-reflection "users should be able to pin reports to their home page"
/clarify-intent spec "export the ledger as CSV"
```

Skills load in the next session.

---

## Fan out: one agent per user journey

Most UX reviews look at screens one at a time. People don't use screens one at a time: they come to get something done, and they cross five screens, two waits and a decision to do it. `interaction-flow fan-out` reviews your product the way people use it, **one typical journey per agent, in parallel**.

```text
 intent + object map                        one agent per journey, in parallel
          │                ┌─▶ "sign up and invite a teammate"   weekly ─┐
          ▼                ├─▶ "create an order"                 daily  ─┤
 journeys picked by  ──────┼─▶ "fix a failed payment"            rare   ─┼─▶ merge ─▶ ranked
 consequence and usage     ├─▶ "find what changed this week"     weekly ─┤           priorities
                           └─▶ "end-of-day review"               daily  ─┘           ─▶ stories

 each agent: its own throwaway instance · real clicks · screenshots · measured steps
             · relevant screen lenses at decision and wait points
```

**How the journeys are chosen.** The prompt establishes whose perspective matters, their situation, goal or decision, and evidence needs. The skill chooses the journeys needed for that scope, led by consequence and informed by usage. A broad review may cover several journeys; a screen request stays narrow.

**What each agent does.** Each agent gets the same brief: the intent, the object map, the four modes, the checklist and the human principles. Then it walks its one journey in the running app:
- it clicks, waits and reads as the person would;
- it screenshots every stop and measures each step: clicks, page changes, waits, what must be remembered, what's said twice, steps whose order isn't enforced;
- at consequential stops it applies the relevant pertinence, structure or disclosure lenses;
- it returns findings in one shared format, each with its mode, severity and human cause.

**Start with your current project.** Point the skill at the current worktree/local build, a prototype or a deployed URL. It uses available task/spec context internally; no separate baseline command, repository access or GitHub connection is required. Existing startup and access instructions are reused; missing access or mutation permission is requested only when needed. It never guesses how to reset your app. Read-only means loading pages, opening tabs and folds, and reading. A step that would save, send, pay or delete is described from the code instead, and marked "not observed". This is an instruction to the agents, not a sandbox, so point them at something you can afford.

**How the findings merge:**
- The same defect seen on several journeys becomes one finding, with a higher reach.
- A finding seen on only one journey keeps reach 1; it's never dropped.
- Measured incidence is labelled separately from owner reports and reviewer estimates; journey counts and complaints do not establish a population rate.
- Confirmed blockers and serious consequences lead. Frequency and reach order findings within comparable severity; the report labels measured, reported and assumed frequency. Evidence confidence and implementation effort stay separate.
- With an earlier review, each group is marked still there, new or gone.
- The report separates observed task time from tool execution time, leaves missing measurements unknown, and says which journeys could not be fully walked.
- Each finding names a practical consequence, what should change, what must survive, and an acceptance scenario. Source concerns go to investigation; already-approved delivery gaps link existing work rather than reopening decisions.

**Why it works.** A defect that one journey shows as a small irritation can be the same defect that blocks two others. Only walking them side by side shows that. The method's first real use was a six-journey review of a delivery-pipeline app, orchestrated by hand from this method. It independently found the main problems the team had run into that week:
- an action that could be taken in the wrong order;
- a state worded four ways;
- a decision screen stacking every option;
- a missing way to order the work.

Its top finding came from four of the six journeys.

The packaged `fan-out` command was then run end to end on the same app, given only the command, in a session that already knew the product. It stated the intent, proposed eight journeys with reasons, asked where to walk, launched eight agents in parallel, and merged 106 findings into 12 ranked groups. It confirmed which earlier problems were still there and found new ones the first run couldn't: a feature shipped the day before missing one of its four entry points, and a feedback loop nobody closed. Two agents strayed from the brief (one skipped its instance, one stepped around a check), and five groups tied for first place. The review brief and tie-break were revised after that run.

A third run walked seven journeys on local copies of the same app's real data. Because the agents traced what they saw to the source, it found real bugs: an approval that went through and then refused its next step, a "fixed" notice raised while linked work was still open, and a timeline warning about a finished item. It also showed where the method was thin. Version 0.3 fixes these:
- The copy held none of the short-lived states two journeys needed, so their agents spent about a third of their effort rebuilding them.
- The app's own background jobs would have acted on the developer's working copy if they had not been redirected by hand.
- Guessed frequency ranked the operator's most frequent real pain below cosmetic issues.
- Two agents called records duplicates from their titles alone.
- The screen inventory script failed on a client-rendered page.

Tell us how it does on your product.

**Copies of real data, side effects and starting states.** A local copy of your real data is often the best place to walk. Before any agent writes there, the skill lists what the app does beyond its own data (background jobs, webhooks, mail, payments, git or deploy hooks, outbound APIs) and disables or redirects each. Actions that cost money, such as model calls in an AI product, are described from the code or capped per journey. Real data rarely holds the moment a journey starts from (work in flight, a failed action, a result waiting for a decision), so the skill decides per journey how that state is reached and prepares shared states once.

**Before it starts,** the skill states how many reviewers it will use, where they will walk and the task-specific effort. It reuses existing authorization and asks only for missing access or material additional scope/cost. One authenticated browser may supply evidence to parallel reviewers; the report distinguishes this from independent walks. To review a single journey or screen without fanning out, use `review` or `screen`.

---

## The three skills

| Skill | Use it when | You get | Talks to you? |
|---|---|---|---|
| [**interaction-flow**](skills/interaction-flow/SKILL.md) | a workflow feels clunky, before a redesign, or to rank UX work | scoped journey or screen review, with optional fan-out; findings grounded in evidence and ranked by consequence | Only for consequential gaps |
| [**design-reflection**](skills/design-reflection/SKILL.md) | someone proposes a feature, before its spec | a one-page design brief: the need, where it belongs, the simplest shape, two alternatives, at most three questions | Rarely. At most three questions |
| [**clarify-intent**](skills/clarify-intent/SKILL.md) | an intent is vague, or a spec reads well but could mean two things | a few questions at a time with proposed answers, a decisions log, then a reviewed or written spec | Yes. That's its job |

---

## Why these skills exist

### 1. Every screen looks fine, and the journey still fails

**The problem.** Each page passes a design review. But the action the person needs is on another tab, the same state is worded three ways, and two buttons work only if pressed in an order nobody wrote down. Screen-level tools never see it, because the defect sits between the screens.

**The fix.** Walk the real app, journey by journey, with one agent per journey, all in parallel. Measure each one: clicks, page changes, waits, what the person must remember, what's said twice, which steps depend on an order the screen doesn't enforce. Merge what they find, rank it, then give each decision one place and each state one word.

→ [`interaction-flow fan-out`](#fan-out-one-agent-per-user-journey)

### 2. The screen shows everything, so it shows nothing

**The problem.** A person arrives with one question: what do I do now, is it done yet, what is this. The screen answers ten other questions first. Tabs hide what's needed together. A drawer holds the question while the answer box sits behind it. A decision gets buried in prose.

**The fix.** Rate every region against the moment it serves: *now*, *soon*, *on demand*, *elsewhere* or *never*. Judge every container for whether it holds one thing, every tab, pane or modal for whether its promise fits the use, and every block of text for whether its length fits why the person is there. Reading wants prose; deciding wants the answer first.

→ [`interaction-flow`](skills/interaction-flow/SKILL.md): pertinence, structure and disclosure passes

### 3. The feature gets built before its shape is questioned

**The problem.** "Tasks should depend on other tasks" becomes a new screen, a new concept and a new setting, when it could have been one property of something that already exists, and could have removed a setting instead of adding one.

**The fix.** Ten reflections before the spec:
1. the need behind the request;
2. the concept it belongs to;
3. what can be derived by a rule, judged by a model, or must be asked;
4. the simplest shape, and what it removes;
5. its states;
6. where it lives;
7. how it scales;
8. consistency with the rest of the product;
9. its cost in effort and attention;
10. how you'll know it worked.

→ [`design-reflection`](skills/design-reflection/SKILL.md)

### 4. The spec reads well and means two things

**The problem.** Two careful readers build two different products from the same paragraph. The agent fills each gap with a guess, and you find out in review.

**The fix.** Explore the code and records first, so nothing is asked that they already answer. Then ask the owner only what is theirs to decide, a few questions at a time, each with proposed answers and their consequences. Write every decision down.

→ [`clarify-intent`](skills/clarify-intent/SKILL.md)

---

## What a review looks like

An excerpt from `interaction-flow` on a fictional shop. The example is illustrative, not a benchmark.

```text
┌─ Priorities ──────────────────────────────────────────────────────────────────────────┐
│ #  Finding                                            Lens       Severity  Reach      │
│ 1  "Pay" stays enabled while the address is invalid;  doing      blocks    3          │
│    the error appears only after the card is charged                                   │
│ 2  Shipping options open in a drawer that covers the  doing      costs     1          │
│    total they change                                                                  │
│ 3  Order status reads "processing", "pending" and     understand confuses  3          │
│    "in progress" on three screens                                                     │
└───────────────────────────────────────────────────────────────────────────────────────┘
  Finding 1 · blocks · doing · Journey "checkout", step 4
  Human cause: constraints prevent errors better than messages (the UI allows a wrong order)
  Fix: disable "Pay" with the reason shown until the address validates
```

A consequential screen can get a pertinence and structure report, starting from what's actually rendered:

```text
$ python scripts/screen_inventory.py http://localhost:3000/checkout
REGIONS (d = nesting depth, then container style)
     64   240  980x620  31.0%   212w  d1 bordered   Your order
     64  1240  440x900  19.2%    48w  d1 filled     Shipping
structure: max container depth 3 · container styles bordered 4, filled 2 · distinct left edges 9
reading order: Your order → Shipping → Promo code → Payment
DISCLOSURE PATTERNS
    120  1240  overlay-pane    open    Shipping options
    610   240  fold            closed  Expand "Order details"
```

And `clarify-intent` ends with a decisions log the next reader can trust:

```text
Decision: export the filtered view · Source: owner answer
   Changes: export reads the current filters; criterion 2 rewritten
Assumption: include a totals row (requested in #41, not yet confirmed)
   Could change: criterion 4
```

---

## How `interaction-flow` works

```text
 intent ─▶ objects ─▶ journeys (fanned out) ───────▶ findings ─▶ priorities ─▶ model ─▶ stories
 who,      one model   walked in the running app,    each with   severity,     places,    small,
 job,      with views, measured step by step         its human   then usage    decisions, sequenced,
 authority meaning     (one agent per journey with   cause       and reach     vocabulary, each with
           and context  fan-out)                                               layers      its files
                              │
                              ▼  at relevant stops
            pertinence · structure & reading · disclosure · text vs purpose
```

The four **modes** are useful lenses for relevant steps, not a complete set of perspectives:

| Mode | The person wants | Typical defect |
|---|---|---|
| Doing | the one next action and the facts it needs | the action on another tab; an order to remember |
| Waiting | the phase, how long, whether to leave, a nudge when it's their turn | a spinner with no phase; having to keep watching |
| Understanding | what this is and where it stands, in plain words | the same state in different words |
| Configuring | the current value, its source, a preview, a way back | settings needed in the middle of doing |

Every finding names its **human cause**: limited working memory, recognition over recall, choice overload, scanning, change outside the focus of attention, the psychology of waiting. The cause chooses the fix: a slip needs undo or a constraint, a mistake needs a clearer model.

---

## Review depth and evidence

The default is a snapshot evaluation with actionable fixes, not a setup exercise. Broad reviews choose complete operator goals before dividing the work; working, partial and placeholder features are distinguished. Each case includes current versus proposed paths, relevant return/recovery states and concrete validation steps. Excluded areas stay excluded.

Code establishes what an implementation does; current accepted intent establishes what it should do. When an accepted change supersedes the build, the review identifies the delivery gap rather than improving an obsolete workflow. Without those records it proceeds from observable tasks and states its assumptions.

The review uses cognitive walkthroughs, usability heuristics and scoped keyboard/focus/status guidance as practical lenses. See [UX methods and primary references](skills/interaction-flow/references/ux-methods.md). This is expert inspection, not a user study or accessibility certification. Reproducible source-only evaluation cases are in [docs/evaluation-cases.md](docs/evaluation-cases.md).

## Example prompts

```text
/interaction-flow review the onboarding journey
/interaction-flow screen http://localhost:3000/settings
/interaction-flow fan-out our admin app — what should we fix first?
/design-reflection "add a diagram section that updates from the codebase"
/design-reflection review docs/specs/bulk-edit.md
/clarify-intent review docs/specs/bulk-edit.md
/clarify-intent spec "let users schedule reports"
```

They also trigger on plain requests like *"this workflow feels clunky"*, *"where should this setting live?"* or *"grill me on this spec"*.

---

## FAQ

<details>
<summary><b>Does it change my app or my data?</b></summary>

No. `interaction-flow` walks the app read-only. For anything that writes, it uses a throwaway instance you can point it at, never production. On a local copy of your real data, it lists the side effects it disabled (jobs, webhooks, mail, payments, git, outbound calls) before any write. `design-reflection` and `clarify-intent` may write a brief, log or spec within the request's established authorization; they ask only when an external destination or authority is unclear.
</details>

<details>
<summary><b>The screen inventory script fails</b></summary>

It needs Python 3 and Playwright: `pip install playwright && playwright install chromium`, or `uv run --with playwright python scripts/screen_inventory.py <url>`. Pass `--chromium <path>` to use an installed browser. It waits for client-rendered pages to settle and retries while the page mounts; raise `--wait` for slow apps. It only reads the page.
</details>

<details>
<summary><b>How expensive is a fan-out review?</b></summary>

Cost depends on requested scope, browser access, available context and delegation. Budget the relevant journeys, stops, references and output detail; stop when requested outcomes are covered and further inspection would repeat evidence. Mark unavailable cost/usage unknown. For one journey or screen, use `review` or `screen`.
</details>

<details>
<summary><b>A skill doesn't show up after installing</b></summary>

Skills load when a session starts: open a new one. If you installed with more than one method, remove the duplicates. `npx ux-review-skills list` shows what is installed where.
</details>

<details>
<summary><b>Will this replace our designer?</b></summary>

No. It is an expert inspection that runs quickly and repeatably, not research with real people, and it has no taste or business judgement of its own. See [A first step, not a replacement for designers](#a-first-step-not-a-replacement-for-designers). Teams with a designer can use it to clear routine findings before a design review, so that the review is spent on harder questions.
</details>

<details>
<summary><b>How does this compare to design-system or UI-generation skills?</b></summary>

They complement each other. Those skills decide how a screen looks and generate it. These decide what the screen is for, where things live and what the work means, then hand the screens that change to whichever design skill you use.
</details>

---

## Contributing

Issues and pull requests are welcome. The most useful contribution right now is a test report: run the checks in [docs/manual-tests.md](docs/manual-tests.md) on your own product and tell us what the agent did.

The shared references have one source each:
- `skills/interaction-flow/references/` for the shared reference files;
- `skills/design-reflection/SKILL.md` for the design reflections.

`npm run sync` copies them into the skills that read them. Edit the originals, never the copies. Every `SKILL.md` description must be a folded YAML block (`description: >-`); the sync script checks it.

## Credits

The principles in [`how-people-think.md`](skills/interaction-flow/references/how-people-think.md) are summarised in our own words from Susan M. Weinschenk, *100 Things Every Designer Needs to Know About People*; Don Norman, *The Design of Everyday Things*; Jakob Nielsen's usability heuristics and response-time limits; and research by Cowan, Hick and Hyman, Fitts, Kahneman and Tversky, Maister and Csikszentmihalyi.

## License

[MIT](LICENSE) © Philip Oligny
