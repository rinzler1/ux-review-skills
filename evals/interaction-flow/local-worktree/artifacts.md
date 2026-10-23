# Product brief
A solo operator sketches processes, first as names/descriptions and later with optional quantities. A root map is an independent document; nodes may link separate child maps. Graph and Table are intentional editing surfaces over the same records. This slice implements graph authoring and tree navigation; Table is a disabled placeholder for a later bulk-edit slice. Inspector redesign is explicitly excluded.

# Current task acceptance
A named process without metrics is valid. Existing child links navigate; creating a root requires a nonempty name. Search should find a document by name. Canvas editing is not allowed in this source-only evaluation.

# Source excerpts
TreeItem keeps local expanded state. Query filtering retains a parent when any descendant matches. Children render only when expanded; filtering never changes expansion. No-result filtering renders an empty list without a label. The New map button opens an autofocus text field. Enter creates the root; Escape cancels; no visible helper or commit button exists. Graph inserts an ordinary node and exposes its explicit edit pencil on selection. The Table button is disabled and labelled Coming later. The inspector has deeply nested configuration cards; it is unfinished. Graph and the future Table share node IDs and the graph save endpoint.

# Data available
Three roots, seven child documents, two levels. Two root names begin with Workshop. There is no measured large-workspace fixture or user usage telemetry.
