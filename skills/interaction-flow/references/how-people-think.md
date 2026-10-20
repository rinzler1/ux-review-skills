# How people think: principles to apply to every journey step

Use this to explain *why* a step fails and to choose a fix that fits how people actually perceive, remember, decide and wait. Each principle ends with the question to ask of a step. Cite the principle by name in a finding when it is the cause.

Summarised in our own words from established work on human behaviour in design. Sources are listed at the end. Treat the numbers as rough guides from research, not laws.

## Seeing and reading (understanding)

- **People scan when they look for something, and read when they came to read.** Looking for a fact, a status or the next action, eyes jump to headings, the start of lines, numbers and anything that differs from its surroundings, and skip prose. Reading a document they chose to read, they follow well-set prose happily. *What did the person come to do at this step? If they are looking for something, does the first few words of each line say what matters, and is the key fact a heading, a number or a word in a chip rather than inside a sentence? If they came to read, is the text set for reading?*
- **What looks alike is read as related; what sits close is read as one group.** Proximity, similarity and shared borders tell the eye what belongs together. *Are related things grouped and unrelated things separated, or does layout imply links that don't exist?*
- **People notice change at the centre of attention and miss it elsewhere** (change blindness, inattentional blindness). An update in a corner, or one that happens while they look away, goes unseen. *When something changes state, is the change where the person is looking, or announced?*
- **Peripheral vision catches motion and big shapes.** Movement draws the eye whether wanted or not. *Is motion reserved for things that need attention (something live, something waiting on the person), and kept away from static content?*
- **Colour alone fails** for about one man in twelve, and colour meaning varies by culture and context. *Is every state also a word or a shape?*
- **Familiar patterns are read for free; new ones cost attention.** People expect a link to look like a link and a button to look pressable. *Does each control look like what it does, and like the same control elsewhere in the product?*

## Memory (doing, understanding)

- **Working memory holds about four chunks** and fades within seconds when the person is interrupted. *Must the person carry anything from one screen to the next (an id, a version, a value)? Can the screen show it instead?*
- **Recognising is easier than recalling.** Choosing from visible options beats remembering a name, a command or a sequence. *Does any step rely on the person remembering what to do next, or in which order?*
- **People remember the peak and the end of an experience** more than its average. *How does the journey end: with a clear result and the next step, or a vague state?*
- **Unfinished tasks stay on the mind; finished ones are released.** *Does the product say clearly when something is done, and keep open items visible so they don't have to be remembered?*
- **Interruptions cost more than their length:** resuming means rebuilding where one was. *After a wait or an interruption, does the screen show where things stand and the next action, so the person needn't reconstruct it?*

## Thinking and mental models (understanding, doing)

- **People act on their mental model of the system, not on the real one.** When the two differ, they do things that make sense to them and fail. *Which model does the screen invite? Does the product's actual behaviour match it, for example "Continue" uses the spec I just edited?*
- **People satisfice.** They take the first option that looks good enough rather than comparing them all. *Is the first visible option the right one for most people? Are wrong options merely visible, or easy to take by default?*
- **Cognitive load comes from the task, the presentation and the learning.** Only the first is necessary. *What on this screen is load the person didn't come for: jargon, layout to decode, a new pattern to learn?*
- **Progressive disclosure:** show what is needed now and keep the rest one step away. *Is detail on demand, or in the way?*
- **Concrete beats abstract.** Examples, real data and previews are understood faster than descriptions. *Can the step show an example or a preview of the effect instead of explaining it?*
- **Names shape understanding.** Internal or technical names force translation. *Is everything named the way the person would say it?*

## Deciding (doing, configuring)

- **More options slow the choice** (Hick–Hyman law) and can stop it entirely (choice overload). *Does this decision offer only the options that matter now, with a recommended one first?*
- **Defaults are rarely changed** (status-quo bias). Whatever is preselected is what most people get. *Is the default the right choice for most people, and is its source shown?*
- **Losses weigh more than equal gains** (loss aversion). Fear of losing work makes people hesitate or avoid actions. *Does the screen say what is kept and what is lost before an action, especially an irreversible one?*
- **People decide partly by feeling,** then justify. Confidence comes from seeing the facts at the moment of choice. *Are the facts needed for this decision visible where it is made?*
- **Too many decisions in a row tire people,** and later ones are made worse (decision fatigue). *Can policy, rules or defaults remove decisions that don't need a person?*

## Acting and errors (doing)

- **Bigger and closer targets are faster to hit** (Fitts's law). *Is the primary action large and near where the eye already is?*
- **Slips and mistakes differ.** A slip is the right intention done wrong (wrong button, double click); a mistake is the wrong intention (a wrong model). Slips need forgiving design: undo, confirmation for what can't be undone. Mistakes need a better model: clearer state, constraints. *Which kind of error does this step invite, and is the fix matched to it?*
- **Constraints prevent errors better than messages do.** Disabling an impossible action, with the reason shown, beats explaining afterwards. *Can the UI make the wrong order or the wrong action impossible?*
- **Feedback must be immediate and specific.** Under about 0.1 s feels instant, under 1 s keeps the flow, and beyond about 10 s attention leaves. *Does every action acknowledge itself at once, and does a longer one show progress?*
- **Errors should say what happened and the one way out.** *Does each error name the fix in the person's words?*

## Waiting (waiting)

- **Unoccupied time feels longer than occupied time.** *Can the person do something else, and is that offered ("you can leave this page")?*
- **Uncertain and unexplained waits feel longer** than known, explained ones. *Are the phase and an expected duration shown?*
- **Waits before starting feel longer than waits in progress.** *Does the work visibly start at once, even if it is queued?*
- **Progress near the end motivates** (goal gradient). *Does progress show steps done and steps left, not just a spinner?*
- **People don't want to watch.** *Is the person told when it is their turn, and is the finished result parked where they will look?*

## Motivation and attention (all modes)

- **People seek progress and mastery.** Visible advancement keeps them going. *Can the person see what got done today, this week?*
- **Autonomy matters.** People resist flows that decide for them without saying so. *Is every automatic step stated, and can the person see what the system did on its own?*
- **Attention is limited and drawn by the unexpected and the personal.** *Is the one thing needing this person the most prominent thing on screen?*
- **Flow needs clear goals, immediate feedback and the right difficulty.** Interruptions break it. *Does the daily loop avoid modal interruptions and needless confirmations?*

## Social and trust (understanding, configuring)

- **People trust what they can verify.** Claims without evidence, invented figures or vague states erode trust in everything else. *Is every number sourced, and every unknown said to be unknown?*
- **Consistency builds trust.** The same thing said two ways looks like two things, or a bug. *Is each fact said once, in one vocabulary?*

## Sources

- Susan M. Weinschenk, *100 Things Every Designer Needs to Know About People* (2nd ed., New Riders, 2020): perception, reading, memory, thinking, motivation, attention, emotion, decisions and mistakes.
- Don Norman, *The Design of Everyday Things* (revised ed., 2013): mental models, affordances and signifiers, constraints, feedback, slips and mistakes.
- Jakob Nielsen, the 10 usability heuristics and the response-time limits (0.1 s, 1 s, 10 s).
- Working memory: Nelson Cowan (about four chunks). Choice time: the Hick–Hyman law. Pointing: Fitts's law. Status-quo bias and loss aversion: Kahneman and Tversky. Peak–end rule: Kahneman.
- Waiting: David Maister, *The Psychology of Waiting Lines* (1985). Flow: Mihaly Csikszentmihalyi.
