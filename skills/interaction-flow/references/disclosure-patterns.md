# Disclosure patterns: why is this a tab, a pane, a drawer, a modal, a fold or its own page?

Every way of showing or hiding content makes a promise to the person: tabs say "peers, one at a time", a modal says "decide this now", a fold says "detail if you want it". When the pattern's promise doesn't match how the person uses the content, they hunt, lose their place, or miss what was hidden. Use this pass where disclosure affects the scoped task, starting from observed tabs, folds, drawers, dialogs or panes.

## The patterns and their promises

| Pattern | What it tells the person | Fits when | Typical misuse |
|---|---|---|---|
| **Tabs** | these are peers; one at a time; switch freely | parallel views of one object, not needed at the same moment | sequential steps in tabs (no order); things needed together split across tabs; a hidden tab holding state or a decision with no badge; tabs inside tabs |
| **Side pane** (docked) | reference beside your work | the person needs both at once, often | a pane covering the action it serves; a pane for something used once |
| **Drawer / overlay** | a short side task, then back where you were | a brief task without losing context | long work in a drawer; content the main page needs (a question in the drawer, its answer box behind it) |
| **Modal** | stop: decide this now | blocking, short, consequential decisions | information, optional choices or long forms in a modal; a modal chain |
| **Own page** | this thing has its own home | its own object, a deep link, long or focused work | one object split across pages; a page for a single field |
| **Fold / accordion** | detail on demand, in reading order | sometimes-needed detail, history, internals | a required decision or the step's answer inside a fold; many folds all closed with no hint of contents |
| **Stepper / wizard** | do these in order | a real sequence with dependencies | free-form work forced into steps; a stepper that hides what later steps will ask |
| **Popover / tooltip** | glance at a detail | short facts that help but aren't required | anything to act on or read at length; hover-only information with no other route |
| **Inline expansion** | more of this, right here | growing a list or a row in place | expanding into content that belongs elsewhere |

## The questions

For each pattern on the screen, answer:

1. **Simultaneity:** does the person need this and the thing beside it at the same moment? If yes, not tabs, not a modal: side by side or inline.
2. **Sequence:** does the order matter? If yes, a stepper or a single flow, not tabs.
3. **Frequency:** how often do they open it? Daily means visible or one click; rare means fold or expert layer.
4. **Context:** do they keep their place, scroll position and unsaved input when they open and close it, or switch tabs?
5. **Addressability:** does the back button work, can it be linked, does a reload keep it?
6. **Discoverability:** without opening it, can they tell what it holds and whether it needs them (a label that says what's inside, a count or a status on a tab, a summary on a fold)?
7. **Mode fit:**
   - doing likes inline or a stepper;
   - waiting likes a quiet in-place indicator, or nothing at all, with a notification when done;
   - understanding likes tabs, folds and its own page;
   - configuring likes its own page or the expert layer, linked from where it matters.
8. **Width:** on a wide desktop, could two tabs become two columns? Panes and columns cost nothing there that tabs save.

## Common findings

- A decision or required input hidden in a fold, a tab or a drawer: severity **blocks** when the journey can't finish without finding it.
- The question in one container and its answer in another (drawer vs page, tab vs tab).
- A pane or overlay that covers the action it supports.
- Tabs used for a sequence, or a stepper used for peers.
- Several patterns for one thing, such as a checkbox, a section, an inline form and a fold all for grilling.
- A modal for something that isn't blocking.
- Hidden state with no signal: a tab with new content and no badge, a closed fold that holds an error.

For each, name the pattern, the promise it makes, what the person actually needs (from the questions), the human cause (from `how-people-think.md`: limited working memory, change outside focus, recognition over recall, attention), and the pattern that fits.
