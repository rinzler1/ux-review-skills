# Product
A report contains editable rows; parent reports summarize saved child reports. Values should be understandable at each level.

# Existing source
Header buttons are Refresh and Recalculate. Refresh fetches saved child snapshots and marks parent totals out of date. Recalculate saves current edits, reads descendants, writes result snapshots and reports completion through a bell. Local row previews react to input changes. No source excerpt starts cross-report recomputation after save.

# Decision archive
2025-01-10: Recalculation is explicit; no background parent mutation.
2025-03-02 accepted replacement: On unlocked current reports, each saved edit automatically propagates to parent summaries. Remove Recalculate on current reports. Retry appears only after a failed propagation. Status reads Saving, Propagating, Propagated or Out of date with a reason. The local preview alone is not propagation. This explicitly supersedes the January decision.

# Current work records
Implementation story R6 is open/planned and defines automatic propagation after save; result-state story R1 is open/planned. The trigger location and batching budget are implementation questions. The owner has already accepted automatic propagation and the removal of the normal Recalculate action. No delivery or deployed-runtime evidence is available.
