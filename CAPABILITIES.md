# Capabilities and boundaries

Record each platform limit the day you find it, with the date, the endpoint, and how it was probed (call and verbatim response).

## Proven

None yet.

## Assumed (re-probe in our tenant)

- Spreadsheet cell edits are zero-based for rows and columns.
- Links do not update on their own; publish links after any source change.
- Presentation text boxes are read-only after creation.
- Number formats cannot be set on document table cells.
- Wdata-to-sheet connections cannot be created via API.
- Large uploads hit MCP payload limits; chunk (about 300 rows per chunk).
- Uploads and imports are async; poll the returned resource URL.
- Rapid anchor/link creation is throttled; batch and pace (about 6s per batch).
