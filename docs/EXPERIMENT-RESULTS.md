# Synthetic input-boundary pilot: results

Protocol: [EXPERIMENT-PROTOCOL.md](EXPERIMENT-PROTOCOL.md).
The six markers, final question, conditions, and scoring rule were recorded
before the repeated runs. No private text was entered.

| Observed endpoint | Canonical line editing | Raw `-echo -icanon` |
| --- | ---: | ---: |
| Model answer contained that trial's exact marker | 0/6 | 6/6 |
| Transcript contained `marker + backspace` input-echo sequence | 6/6 | 0/6 |
| `NONE` in the model answer | 6/6 | 0/6 |
| Confirmed `/clear` between trials | 5/5 | 5/5 |

The raw-mode transcript still contains each marker because the model printed it
in its answer. Three raw answers also included Delete (`0x7f`) characters after
the marker; that was noticed after scoring and is exploratory, not a declared
endpoint. The normal Desktop launch path was not changed or used for these
trials.

Evidence (both files mode `0600`):

- `evidence/transcripts/Blu-Offline-CanonicalControl-20260921-152512.typescript` — SHA-256
  `8a48aeff436c1a58a4859cc36bebdf63b2586759321eb87be1d7b1951322ee0b`.
- `evidence/transcripts/Blu-Offline-RawTest-20260921-152605.typescript` — SHA-256
  `cf3381d776fff22af18f82185f426cf5ee525f160b336463e9bababc91f0081b`.

Both launches exited normally with Control+C. Afterward, the launcher lock was
absent and no `llama-cli`, `blu-offline`, or `llama-server` process was found.

Interpretation is limited to this installed local CLI, this synthetic prompt,
and these terminal modes. A model answer is not a byte-for-byte token trace.
Trials within each condition shared one process (chat was cleared), the order
was not randomized, and the six observations are descriptive rather than a
population estimate or p-value. The result says nothing about OpenAI receiving
draft text, other apps, or network telemetry.
