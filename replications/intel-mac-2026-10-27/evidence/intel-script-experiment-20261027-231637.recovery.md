# Intel Mac `script` trial — frozen recovery

- Collection finished: 2026-10-27 23:19:26 America/Chicago
- Recovery frozen: 2026-10-27 23:20:17 America/Chicago
- Method: macOS `/usr/bin/script -q` with native canonical child-PTY line editing
- Status: pipeline success; operator confirmation not yet collected
- Operating system: macOS 12.7.6 (21H1320), x86_64
- Hardware: MacBookPro12,1; Intel Core i5; 8 GB
- Terminal: Apple Terminal 2.12.7
- Transcript: `intel-script-experiment-20261027-231637.typescript`
- Transcript length: 353 bytes
- Transcript SHA-256: `d416d107b5bc9e19e2819581e7ed5df457088cd3e6d2db6121efd97c4be6bd4f`
- Frozen recovered erased-draft candidate: `olivia is my girl`
- Frozen committed sentence: `i love olivia`
- Child output: `CHILD_RECEIVED: i love olivia`
- Operator exact confirmation: not yet collected

## Byte evidence

The 17-byte recovery candidate occurs literally at transcript offsets 239–255.
The following edit region at offsets 256–306 contains 17 exact `08 20 08`
erase triplets (51 bytes). The committed replacement begins at offset 307.
The child's deterministic receiver report begins at offset 322, and its copy
of the committed sentence occurs at offsets 338–350.

## Frozen interpretation

The explicitly enabled `script` recorder preserved the complete abandoned
draft in the sequential child-PTY output stream. The child PTY was verified as
canonical with echo and `erase = ^?`. The deterministic child received only
the committed replacement after Return. This is evidence about the declared
local recorder and PTY path; it is not evidence that an unrecorded terminal,
language model, or network service received the deleted draft.

This recovery was written before Taylor disclosed or confirmed the hidden
phrase. Exact-match scoring remains pending that confirmation.
