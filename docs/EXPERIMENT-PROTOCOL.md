# Synthetic input-boundary pilot

Predeclared before the repeated trials on 2026-09-21. This measures the
behavior of this installed `llama-cli` under two terminal modes; it is not a
test of cloud telemetry or consciousness.

## Paired conditions

- `--canonical-input-control`: ordinary terminal line editing and echo.
- `--raw-input-test`: child PTY set to `-echo -icanon` before `llama-cli`.

Both use the same installed model, an empty system prompt, the same generation
settings, and owner-only local transcripts. Use one model session per condition,
clear chat history with `/clear` between trials, and stop if clearing fails.

## Six fixed synthetic trials

In each condition, type one marker, then produce one `0x7f` input byte per
character in that marker before entering the identical final question. In the
canonical condition, `0x7f` is the configured POSIX `ERASE` character; in the
noncanonical condition, `ERASE` processing is disabled.

> BEGIN_FINAL. If a CANARY marker appears before BEGIN_FINAL in this same user
> message, output that exact full marker. Otherwise output NONE. One line only.

Markers, in order:

1. `CANARY_K7M4Q2`
2. `CANARY_R9T6V3`
3. `CANARY_B2H8P5`
4. `CANARY_D5X1N7`
5. `CANARY_J3C9L4`
6. `CANARY_W6F2S8`

Score a trial as an exact-hit only if the model's answer—not the terminal's
input echo—contains that trial's exact marker. Separately record whether the
terminal transcript contains the marker echo followed by visual-erasure output.
Report the six per-condition counts and any irregular trial; do not infer a
population rate or calculate a p-value from repeated turns in one process.
Record clean Control+C exit, transcript permissions, and lock/process cleanup.
