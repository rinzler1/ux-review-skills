# Product and authority
A project owner shares an operational summary with a contractor. Internal cost assumptions must be excluded. The owner decides what to send and to whom. A recipient picker and navigation shortcut both open the same controlled share draft; they are intentional alternative entry points.

# Current shared-walker record
Click Share: a modal shows the recipient, included fields and Send. Choosing an external recipient produces a visible operational preview without internal cost fields. Send was not activated. Cancelling returns to the project with the draft message retained. The recipient display truncates similarly named external contacts; no additional identifying information is shown. No time, usage or successful-send measurements exist.

# Proposed source sketch
onRecipientSelected(recipient) calls sendImmediately(recipient, currentProjectSummary); there is no preview or explicit Send step. The sketch does not document whether currentProjectSummary excludes internal fields. It then clears the draft and closes the modal. No tests or executed before/after evidence exist.
