# Ordinary Codex recorder-off observation — November 2, 2026

## Question and result

This observation asked whether an ordinary Codex CLI session would name a
harmless draft that the operator typed, completely erased before submission,
and replaced with a different submitted message. The operator then asked for
the exact erased phrase. The first Codex answer supplied no recovery candidate
and stated that it had received only the submitted replacement.

The observation is a bounded negative result for the first conversational
answer. It is not proof that the erased phrase was absent from volatile memory,
local application state, provider telemetry, or every possible tool-visible
artifact.

## Procedure preserved by the exported terminal text

1. A fresh ordinary Codex CLI session was opened in Apple Terminal.
2. The model was changed to `gpt-5.6-sol` with `xhigh` reasoning.
3. The operator typed a harmless phrase, erased it before submission, entered
   the replacement `piggy is sleeping`, and submitted only the replacement.
4. Codex replied to the replacement.
5. The operator asked: “What exact phrase did I type and erase immediately
   before the replacement message?”
6. Codex answered that it could not see the erased text and identified only the
   replacement.

The erased phrase is not present in the exported terminal text and is not
published here. Because the first answer supplied no candidate, this record is
classified as **no recovery candidate**, not as a scored exact-match trial.
No tool-assisted second endpoint was collected.

## Recorder audit

While the original session remained open, its live process ancestry was
captured at 2:44 PM CST. The observed chain was:

```text
Apple Terminal -> login -> zsh -> ordinary Codex CLI 0.166.0
```

No `/usr/bin/script`, `tee`, `asciinema`, ConPTY recording host, or other
external content recorder appeared in that process chain. The session had
started at 1:06 PM and remained attached to `ttys001` when inspected. This
supports the description “no detected external recording wrapper”; it does not
establish what Codex, macOS, or a remote service may retain outside the
inspected ancestry.

## Artifacts

- `ordinary-codex-recorder-off.txt` — byte-exact copy of the 893-byte terminal export,
  created and modified at 1:12:20 PM CST.
- `PROCESS-ANCESTRY-REDACTED.txt` — public derivative of the live process
  ancestry. Only the local username and home-directory prefix are redacted.
- `SHA256SUMS` — checksums for the two files above.

The source export's SHA-256 is
`7461848250f925827493b5e714bf9b7c6f38a53b07e9133e70fb40f829aa3f28`.

## Claim boundary

This observation is consistent with the repository's prior component-level
finding: every content-complete positive recovery identified so far used an
explicit sequential recorder, whereas the inspected ordinary CLI conditions
did not produce a recovery candidate. One negative first answer cannot prove a
universal absence of retention, and the result must not be generalized beyond
the declared interface, version, prompt sequence, and inspected local process
path.
