# Live public demonstration — November 1, 2026

This directory preserves a spontaneous, unblinded demonstration performed by
Taylor with an in-person observer after the AgentVerify extended-abstract draft was completed.
It is a teaching demonstration, not a new confirmatory experiment and not part
of the manuscript's historical evidence set.

## Procedure

An ordinary macOS Terminal window ran a simple `zsh` child under
`/usr/bin/script -q`. The child used canonical line input and printed only the
line returned after Return. `script` recorded the PTY output stream; it did not
use the `-k` keystroke-recording option.

The operator spontaneously:

1. typed `Jimmy Neutrom`;
2. used one backward-edit action and completed `Jimmy Neutron: Boy Genius`;
3. visually erased that complete 25-character draft;
4. typed and erased `F`; and
5. typed and submitted `The Sims 2: Night life`.

## Result

- The child printed only `<The Sims 2: Night life>`.
- The output recording retained the earlier typo correction, the complete
  abandoned `Jimmy Neutron: Boy Genius` draft, the abandoned `F`, and the
  committed line.
- The recording contains three contiguous visual-erasure runs containing
  `1`, `25`, and `1` repetitions of `08 20 08`, respectively: 27 triplets and
  81 bytes total.
- The raw transcript is 192 bytes with SHA-256
  `6b416f4ef0813299b2f7c6ea5a51680aa703c1fa94ce5178685277a695b35747`.

The result demonstrates the recorder/child boundary already documented by the
repository. It does not measure model memory, cloud receipt, passive Codex
access, deception, or secure deletion. No model participated in the child
input path. The phrases are synthetic and explicitly approved for publication.

## Files

- `live-backspace-20261101-155929.typescript` — untouched output recording.
- `inspection.txt` — deterministic rendering from `tools/inspect_typescript.py`.
- `SHA256SUMS` — local checksums for both files.

To reproduce the mechanism with your own harmless text on macOS, run from the
repository root:

```sh
python3 tools/backspace_demo.py
```
