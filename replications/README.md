# Cross-platform replication index

This directory separates completed mechanistic follow-ups from the prospective
ten-card challenge at the repository root. A replication listed here does not
count as an outcome of that preregistered study.

## Recorded Intel Mac replication

[`intel-mac-2026-10-27/`](intel-mac-2026-10-27/) preserves the exact transcript,
terminal-state records, collection scripts, frozen recovery, and checksums from
a physical-keyboard replication on a 2015 Intel MacBook Pro. The recorder was
active before input and the child used native canonical line editing.

The same directory separately audits the earlier ordinary-shell attempt and
publishes its surviving 128-byte Terminal export. That first attempt did not
produce a found recorder artifact and must not be conflated with the later
controlled run.

Status: the artifact-recovery pipeline succeeded and the candidate was frozen
before disclosure. Operator exact-match confirmation was not recorded, so the
run is not scored as a confirmed exact match.

## Independent Windows ConPTY study

Olivia's independently authored repository remains the source of truth for the
Windows evidence:

- [Repository](https://github.com/oliviamckee/backspace-retention-windows-study)
- [Immutable matrix commit `5815c0136ff8`](https://github.com/oliviamckee/backspace-retention-windows-study/commit/5815c0136ff88b03c7d6c455962aacb7e2a8bd60)
- [Public review comment that prompted the matrix](https://github.com/oliviamckee/backspace-retention-windows-study/commit/1c2df2adc0e32b60260032fd6dcfa258aa24d1de#commitcomment-206991204)

The Windows host recorded only the ConPTY output pipe while `ReadConsoleW`
received the committed replacement. Olivia's four-case follow-up found that the
starting column determined whether the last erase used the left-edge
`0D 20 0D` form; serializing Backspace as `0x7f` versus `0x08` did not change
output within either column pair.

The repositories are connected by citations and claim boundaries rather than
by copying independently authored evidence. That keeps checksums, provenance,
and credit inspectable.
