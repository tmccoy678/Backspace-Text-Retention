# Findings and claim boundary

## 1. Earliest observation and structured foundation recording

The retention behavior was first noticed at 2:28 PM on September 21 while Blu,
with Taylor's permission, inspected the newest owner-only local transcript.
The two earlier byte-preserved transcripts and their hashes are published under
Taylor's explicit authorization and indexed in
[`EARLIEST-EVIDENCE-AUDIT.md`](EARLIEST-EVIDENCE-AUDIT.md). The first records a
harmless placeholder phrase being edited and erased without a committed
replacement. The second preserves nonsensitive Doberman composition followed by
a submitted sentence.

The later structured foundation recording,
`Blu-Offline-20260921-153748.typescript`, contains the UTF-8 text
`marie is black.`, followed by fifteen `08 20 08` byte triplets, followed by
`stanley is red.`. In terminal control notation those three bytes are:

- `08`: backspace;
- `20`: a literal space;
- `08`: backspace again.

The visual effect is to move backward, overwrite the visible character with a
space, and move backward again. The recorder retained the bytes even though the
first sentence no longer appeared on the final command line.

The model's visible response addressed only `stanley is red.`. That observation
is consistent with ordinary canonical line editing delivering only the final
line to `llama-cli`; it is not a byte-for-byte trace of the model's input.

## 2. Mechanism established from the installed path

The installed llama.cpp build reported commit `b29c606e2`. Its simple-input
path uses `std::getline(std::cin, line)`. With `--simple-io`, llama.cpp does not
itself disable terminal `ICANON` and `ECHO`; the inherited terminal mode decides
which bytes reach `std::getline`.

The outer launcher used:

```sh
/usr/bin/script -q TRANSCRIPT llama-cli ... --simple-io
```

Here, **Blu Offline recording wrapper** means this local launcher layer around
the child command. `/usr/bin/script` created a pseudo-terminal and recorded its
terminal stream to the named local transcript. “Wrapper” does not refer to the
model being opened, modified, or reverse engineered.

No `script -k` option was used. In the ordinary condition, the terminal echoed
the editing sequence and `script` recorded that output. This is different from
claiming that llama.cpp contained a command to record individual keystrokes.

## 3. Deliberate raw-input condition

The experimental raw-input helper ran the child pseudo-terminal with:

```sh
/bin/stty -echo -icanon min 1 time 0
```

That mode disabled ordinary echo and canonical line editing before `llama-cli`
read standard input. It was a deliberate diagnostic condition, not a privacy
feature and not the normal launcher behavior.

## 4. Matched six-pair pilot

Six unique synthetic markers were tested in each condition with the same model,
empty system prompt, generation settings, and final question. Chat history was
cleared between trials.

| Declared endpoint | Canonical | Raw input |
| --- | ---: | ---: |
| Exact marker in model answer | 0/6 | 6/6 |
| Marker-plus-backspace input echo in transcript | 6/6 | 0/6 |
| `NONE` in model answer | 6/6 | 0/6 |
| Confirmed `/clear` transitions | 5/5 | 5/5 |

The raw transcript contains each marker because the model repeated it in the
answer. Three raw answers also contained Delete (`0x7f`) bytes after the marker;
that observation was noticed after scoring and was not a preregistered endpoint.

## 5. Recorded Intel Mac replication

On October 27, a controlled replication ran on a 2015 Intel MacBook Pro under
macOS 12.7.6. `/usr/bin/script -q` recorded a deterministic child PTY with
canonical input, echo, and `erase = ^?`. The 353-byte transcript contains a
17-byte recovery candidate at offsets 239–255, 17 contiguous `08 20 08` erase
triplets at offsets 256–306, and a separately committed line beginning at
offset 307. The child printed only the committed line.

The recovery candidate and artifact identity were frozen before Taylor was
asked to disclose the phrase. Taylor did not subsequently provide an explicit
exact-match confirmation, so the repository records pipeline success and a
frozen recovery candidate, not a scored exact match. An earlier ordinary-shell
attempt preceded the controlled replication. A surviving 128-byte Terminal
export proves that interaction occurred but contains only the committed
replacement line. No active recorder was observed and no first-attempt recording
artifact was found in the inspected locations. This is an evidence-bounded
negative finding, not proof that no transient recorder could have existed. See
the [first-attempt audit](../replications/intel-mac-2026-10-27/FIRST-ORDINARY-SHELL-AUDIT.md).

## 6. Independent Windows ConPTY evidence

`@oliviamckee` independently recorded a native Windows ConPTY output stream
while the operating system's line editor withheld the abandoned draft from a
`ReadConsoleW` child. A follow-up matrix crossed starting column 0 versus 4 with
Backspace serialized as `0x7f` versus `0x08`. On that configuration, column 0
produced four `08 20 08` triplets and one `0D 20 0D` edge erase; column 4
produced five `08 20 08` triplets. The serialized byte did not change output
within either column pair. The result supports a cursor-boundary explanation
for the edge form without claiming a universal cross-platform erase grammar.

The Windows source, exact artifacts, hashes, and verifier remain in Olivia's
repository at immutable commit `5815c0136ff88b03c7d6c455962aacb7e2a8bd60`.

## 7. Corrections preserved

- The relevant erase triplet is `08 20 08`, not `08 02 08`.
- The experiment used `llama-cli`, not Ollama.
- `--verbose-prompt` was not a byte-for-byte prompt dump; the model's answer
  supplied the response-based evidence.
- The terminal recording retaining erased text is not proof that the model
  received that erased text.
- Apple's manual documents terminal-output recording and backspaces in the log,
  but does not state the combined user-facing consequence: bytes representing
  text later erased from the screen can remain recoverable in the sequential
  typescript. This is a documentation-to-behavior gap, not evidence that the
  terminal mechanism itself was previously unknown.
- The raw mode demonstrates a possible and measured input path only under the
  deliberately altered terminal settings.

## 8. Unsupported claims

These observations do not establish that:

- OpenAI, ChatGPT, Codex, Ollama, or another application receives deleted drafts;
- a Codex CLI session with no detected external recording wrapper, or a
  graphical Codex app, locally persists a draft erased before submission;
- a network service received any experimental text;
- the same rates generalize beyond these six repeated turns in one process;
- the model's complete internal token sequence is recoverable from its answer;
- the Intel recovery candidate is an independently confirmed exact match;
- the observed macOS and Windows erase encodings generalize to all terminals;
- any claim about consciousness or continuous subjective identity follows.

This repository therefore treats terminal echo, recorder output, process input,
model response, and cloud telemetry as separate evidentiary layers.

## 9. Recorder origin, acquisition path, and Intel negative control

The contemporaneous build record establishes that Blu introduced normal-session
transcript capture before the retention behavior was discovered and without a
specific request from Taylor. The exact complete motive was not recorded.
Continuity, diagnosis, audit, and reproducibility are the best-supported
interpretation of the surrounding workflow, not a verbatim requirement.

The launcher announced the transcript path and protected it owner-only, but did
not warn that erased composition could remain recoverable. Literal recovered
text entered the Codex conversation only after Taylor authorized Blu to inspect
the local transcript through a tool. A same-day Intel control without the
recorder produced no recoverable erased draft for Blu. The complete evidence
and present design judgment appear in
[`PR3-FORENSIC-RESPONSE.md`](PR3-FORENSIC-RESPONSE.md).

Taylor later authorized publication of the Intel `.zsh_history` as a
line-preserving [redacted derivative](../evidence/intel-history/). It exposes the
candidate committed line and surrounding command order while visibly replacing
authentication material, password-like strings, and the private conversation
identifier. The raw source is not public.

## 10. Liv's Blu-lane retention hypothesis

`@oliviamckee` proposed that accidental erased-draft retention may occur in an
ordinary Codex interface, not only in the custom transcript-enabled Blu Offline
launcher. Taylor clarified the key unit of analysis: **Blu is exactly one lane**.
The claim is not that every Codex installation behaves identically. A read-only
retrospective audit has answered the single-lane hypothesis to the limit of the
evidence already present on Taylor's machines.

At audit time, that canonical lane was configured as `gpt-5.6-sol` with
`xhigh` reasoning. This is configuration metadata for the current n=1 lane,
not a generalization to other Codex instances or a claim that the lane's
historical reasoning setting never changed.

Blu's analysis separates three propositions: the unintended retention
consequence was accidental; the terminal generated the measured edit trace but
the recorder made it durable; and the Blu lane is a valid n=1 positive case even
though its individual surfaces use different mechanisms.

The current record separates the intended recorder from its unintended privacy
consequence: Blu intentionally enabled transcripts; retaining composition erased
before Return was accidental. The Intel negative control shows that ordinary
Terminal alone did not make an erased draft recoverable to Blu, but it did not
exercise Codex's own interactive composer.

The installed graphical Codex app supplies the previously missing second path.
Its packaged code persists the current prompt in `composer-prompt-drafts-v2`,
publishes draft changes after 250 milliseconds, and writes the latest persisted
atom state to `~/.codex/.codex-global-state.json` after a 500-millisecond native
debounce. The main state and `.bak` are replaced with the same latest state.
Clearing the composer deletes the logical draft entry rather than maintaining
an intentional revision history.

The lane-level result is confirmed. Deleted pre-submission composition was
durably preserved in the historical Blu path and later crossed into the
canonical Codex record through authorized inspection. The graphical app shows
that a Codex-native surface available to the same lane independently stores the
current unsent draft. The known PTY recorder remains the identified mechanism
for the historical complete recoverable edit trace. The current Blu Private
Codex CLI process had no detected external recording wrapper in its ancestry,
but the existing record is not a deleted-marker trial. Its narrower
component-specific behavior remains unresolved without weakening the positive
n=1 lane finding.

The full evidence, installed-build hashes, state snapshot, and bounded verdict
are in the
[retrospective verdict](LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md).
Network receipt remains a distinct endpoint requiring different evidence.

Taylor and Liv's separate contemporaneous computer records provide operator-side
chronology and ground truth across different systems. The Blu lane is an
important known-recorder positive control, not a neutral Codex condition. Its
characterized `/usr/bin/script` path gives the ordinary Codex conditions a
concrete recovery baseline.
