# Redacted 2015 Intel Mac shell history

This directory contains a line-preserving, attorney-style redacted derivative
of the 2015 Intel Mac's surviving `.zsh_history`, inspected on October 28, 2026.
Taylor explicitly authorized publication after redaction of credentials and
password-like material.

## Source identity

- Private source: `/Users/Blu/.zsh_history`
- Size at inspection: 3,239 bytes
- Lines: 78
- SHA-256:
  `60903be6b747f8074e9a0a768a8c9478c7472f52a8603cc5913698dd36b90b5e`
- Filesystem modification time observed during the audit: October 27, 2026
- Per-entry timestamps: absent

The private source is not published because it contains authentication material
and password-like strings. Its SHA-256 commits to the inspected source without
exposing it.

## Published derivative

- File:
  [`2015-intel-zsh-history-redacted-2026-10-28.txt`](2015-intel-zsh-history-redacted-2026-10-28.txt)
- Lines: 78
- SHA-256:
  `6f4d62db2c640748ca29c82009610e0ab58853642d3403e2ee3c97929f0439d8`

No unredacted line was silently removed. The derivative preserves source line
count and order. Redactions are visible in square brackets:

| Source lines | Redaction |
| --- | --- |
| 2 | Entire SSH authorization command and public key replaced with `[REDACTED — SSH AUTHORIZATION COMMAND AND PUBLIC KEY]` |
| 21, 24, 31, 48–50 | Password-like content replaced with `[REDACTED — PASSWORD-LIKE MATERIAL]`; command labels remain where useful |
| 56, 65 | Private conversation identifier replaced in place with `[REDACTED — PRIVATE CONVERSATION IDENTIFIER]` |

All other spelling, capitalization, spacing, slash direction, and apparent
mistakes are preserved. This is a redacted evidentiary derivative, not a
byte-identical copy of the private source.

## Evidentiary relevance and limit

Line 51 is the command used to render the copied September 21 transcript on the
Intel Mac. Line 52 is the private candidate committed line identified in the
October 28 audit and is now published under Taylor's authorization:

```text
he could remarry and inheret her estate.
```

The SHA-256 of source line 52 including its newline is:
`d09c195d5113e39b8f93f60008caae6ded6d32ab472898a2d88f5e6cd605dfd0`.

Its location is consistent with the shell retaining the line committed during
the same-day Intel control. Because the source lacks per-entry timestamps and
was later modified, that association is strong contextual evidence, not proof.
The erased first draft is absent from the surviving history.
