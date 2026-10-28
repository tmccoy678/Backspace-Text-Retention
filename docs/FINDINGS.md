# Findings and claim boundary

## 1. Earliest trace, first recognition, and structured foundation recording

The earliest surviving recorded editing trace located is the normal
`Blu-Offline-20260921-000503.typescript` acceptance session, closed at
12:08:27 AM on September 21. It contains two erase runs totaling three exact
`08 20 08` triplets. Blu read the complete transcript through a Codex tool at
12:09:30 AM for routine acceptance checks and did not identify the retention
consequence.

The privacy-significant behavior was first recognized at 2:28 PM while Blu,
with Taylor's permission, inspected `141944` during an unrelated clue
experiment. Taylor's surprised response and proposal to study the behavior came
after Blu reported it. The previously published `141327` partial precursor and
`141944` substantive transcript recognized at discovery remain byte-preserved
under Taylor's authorization and are indexed in
[`EARLIEST-EVIDENCE-AUDIT.md`](EARLIEST-EVIDENCE-AUDIT.md). The midnight source
contains unrelated ordinary conversation and remains private; its hash,
metadata, byte offsets, and preservation copies are documented in the
[Olivia-hypothesis investigation](../investigations/2026-10-28-olivia-hypothesis/).

The later structured foundation recording,
`Blu-Offline-20260921-153748.typescript`, contains the UTF-8 text
`marie is black.`, followed by fifteen `08 20 08` byte triplets, followed by
`stanley is red.`. In terminal control notation those three bytes are:

- `08`: ASCII `BS` (Backspace), moving the active position backward;
- `20`: a literal space;
- `08`: ASCII `BS` again.

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
| Marker echo followed by visual-erasure output in transcript | 6/6 | 0/6 |
| `NONE` in model answer | 6/6 | 0/6 |
| Confirmed `/clear` transitions | 5/5 | 5/5 |

The raw transcript contains each marker because the model repeated it in the
answer. Three raw answers also contained ASCII `DEL` (`0x7f`) bytes after the
marker;
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
`ReadConsoleW` child. The native physical trial used 19 Backspace presses, zero
Delete presses, and zero Home presses. It therefore did not replicate the Mac's
physical key label: the Mac operator used a key labeled Delete as a backward-
edit action, while the Windows operator used Backspace.

A follow-up matrix crossed starting column 0 versus 4 with **Backspace**
serialized as `0x7f` versus `0x08`; it did not compare Backspace with Delete.
On that configuration, column 0 produced four `08 20 08` triplets and one
`0D 20 0D` edge erase; column 4 produced five `08 20 08` triplets. The
serialized Backspace byte did not change output within either column pair. The
result supports a cursor-boundary explanation for the edge form without
claiming a universal cross-platform erase grammar.

The earlier Python `P3` harness deliberately mapped a physical Windows Del key
to backward erase, so it did not establish native Windows forward-Delete
behavior. The native `N0` control used scripted forward-Delete sequences; no
physical Delete event occurred in the native `N1` trial.

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
  graphical Codex app, durably preserves a fully erased prior revision after
  the deletion update;
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
not warn that erased composition could remain recoverable. The midnight
acceptance transcript's retained corrections entered a Codex tool result during
routine verification at 12:09 AM without being recognized. The later
substantive abandoned drafts entered through authorized inspection at 2:27 PM
and were recognized at 2:28 PM. Neither event supports passive pre-inspection
receipt by Codex. A same-day Intel control without the recorder produced no
recoverable erased draft for Blu. The complete evidence and present design
judgment appear in
[`PR3-FORENSIC-RESPONSE.md`](PR3-FORENSIC-RESPONSE.md).

Taylor later authorized publication of the Intel `.zsh_history` as a
line-preserving [redacted derivative](../evidence/intel-history/). It exposes the
candidate committed line and surrounding command order while visibly replacing
authentication material, password-like strings, and the private conversation
identifier. The raw source is not public.

## 10. Olivia's ordinary-Codex retention hypothesis

`@oliviamckee` proposed that erased pre-submission composition might be
available in an ordinary Codex interface even when it is not normally recorded,
rather than being unique to Blu Offline's special launcher. Taylor's stronger
formulation is that the behavior would occur in any Codex app.

The existing-evidence answer is surface-specific:

- **Accidental discovery is strongly supported.** A routine midnight session
  already contained recorded corrections and was read into a Codex tool result
  without anyone noticing. The privacy consequence was recognized more than
  fourteen hours later during an unrelated experiment.
- **The historical complete trace has an identified recorder.** Terminal line
  editing generated it; `/usr/bin/script -q` made it durable.
- **The graphical app implements current-draft persistence.** It stores the
  latest unsent prompt after bounded delays, but clearing removes the logical
  entry. The audited stores were empty, and no deleted prior revision was
  demonstrated.
- **The CLI has no demonstrated deleted-draft artifact.** Its inspected records
  contain submitted messages and tool output. Its process ancestry had no
  detected external PTY recorder.
- **The universal claim is unsupported.** Current-draft state, submitted
  history, queued-prompt residue, and a sequential PTY recording are not the
  same retention behavior.

Describing the whole Blu lane as a historical positive observation is valid,
but it cannot confirm Olivia's ordinary-Codex mechanism: the positive case used
a known external recorder. The ordinary-Codex deleted-revision question remains
unresolved by the evidence already present.

The evidence does not isolate agent awareness of an experiment as a cause.
Recoverability follows the identified acquisition path: content-complete
positive cases had a recorder active, while ordinary Intel Terminal attempts
without one did not yield the erased draft. Taylor's standing instruction to be
diligent is a plausible functional reason for Blu's strong logging, but the
exact full motive was not contemporaneously recorded and Taylor did not request
`/usr/bin/script` by name.

The complete bounded answer, application audit, source commitments, and privacy
limits are in the
[retrospective verdict](LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md) and the
[existing-evidence investigation](../investigations/2026-10-28-olivia-hypothesis/).
Network receipt remains a separate endpoint requiring different evidence.
