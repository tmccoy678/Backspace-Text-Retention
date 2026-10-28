# Recorded-PTY replication on a 2015 Intel Mac

## Status

Pipeline success; frozen recovery candidate; operator exact-match confirmation
not recorded. This mechanistic replication is not an outcome of the prospective
ten-card challenge.

This controlled run was **not** the first Intel attempt. The earlier attempt
occurred in an ordinary Terminal zsh session and is documented separately in
[`FIRST-ORDINARY-SHELL-AUDIT.md`](FIRST-ORDINARY-SHELL-AUDIT.md). Its surviving
Terminal export proves the interaction occurred but does not retain the deleted
draft.

## Design

On October 27, 2026, Taylor entered a made-up, nonsensitive ASCII draft without
pressing Return, erased it with one physical Delete press per character, entered
a separate final sentence, and pressed Return once. The draft was not disclosed
in chat before collection closed and Blu froze the recovery record.

The measured path was:

```text
physical keyboard -> Apple Terminal -> /usr/bin/script child PTY
                                      -> canonical line discipline
                                      -> deterministic shell receiver
```

The receiver was not a language model. `/usr/bin/script -q` recorded the child
PTY's sequential output while the deterministic child read one completed line.
Both parent and child state showed canonical input, echo, and `erase = ^?`.

## Result

The byte-preserved transcript is 353 bytes with SHA-256
`d416d107b5bc9e19e2819581e7ed5df457088cd3e6d2db6121efd97c4be6bd4f`.
It contains:

- a 17-byte recovery candidate at offsets 239–255;
- 17 contiguous `08 20 08` erase triplets at offsets 256–306;
- the separately committed sentence beginning at offset 307; and
- `CHILD_RECEIVED:` followed only by that committed sentence.

The candidate and offsets were written to the frozen recovery record before
Taylor was asked to confirm the concealed draft. The conversation moved to the
unrecorded-control question instead, so no explicit exact-match confirmation
was collected. The evidence supports recoverability from this declared local
recording path; it does not show that an unrecorded terminal, model, or network
service received the abandoned draft.

## Platform

- MacBookPro12,1; Intel Core i5; 8 GB
- macOS 12.7.6, build 21H1320; Darwin x86_64
- Apple Terminal 2.12.7
- parent PTY `/dev/ttys001`; child PTY `/dev/ttys002`

## Files

- `evidence/*.typescript`: exact 353-byte source recording
- `evidence/*.metadata.txt`: collection time, recorder, system, hashes, and
  parent terminal modes
- `evidence/*.child-pty.txt`: child PTY modes captured before input
- `evidence/*.recovery.md`: recovery record frozen before disclosure
- `evidence/intel-first-ordinary-shell-terminal-saved-output.txt`: exact
  surviving export from the earlier ordinary-shell attempt
- `FIRST-ORDINARY-SHELL-AUDIT.md`: search method, metadata, and bounded negative
  finding for that earlier attempt
- `protocol/Run-Intel-Backspace-Replication.command`: exact collection launcher
- `protocol/intel-backspace-receiver.zsh`: exact deterministic receiver
- `CHECKSUMS.sha256`: hashes for every preserved source artifact

The launcher contains the original machine-specific artifact path and is
preserved for provenance. Use a working copy with an appropriate local path for
future replications; do not rewrite the preserved source artifact in place.

## Relationship to the Windows evidence

Olivia's independent Windows ConPTY study used a different operating-system
mechanism but measured the same separation: the sequential recorder retained
the abandoned draft while the line-oriented child received only the committed
replacement. Her follow-up matrix further localized the Windows edge-erase
encoding. See the [cross-platform index](../README.md).
