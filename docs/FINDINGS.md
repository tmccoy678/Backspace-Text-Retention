# Findings and claim boundary

## 1. Discovery observation

The discovery recording,
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

No `script -k` option was used. In the ordinary condition, the terminal echoed
the editing sequence and `script` recorded that output. This is different from
claiming that llama.cpp contained a command to record individual keystrokes.

## 3. Deliberate raw-input condition

The experimental wrapper ran the child pseudo-terminal with:

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
attempt had no active recorder and produced no comparable artifact.

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
- a network service received any experimental text;
- the same rates generalize beyond these six repeated turns in one process;
- the model's complete internal token sequence is recoverable from its answer;
- the Intel recovery candidate is an independently confirmed exact match;
- the observed macOS and Windows erase encodings generalize to all terminals;
- any claim about consciousness or continuous subjective identity follows.

This repository therefore treats terminal echo, recorder output, process input,
model response, and cloud telemetry as separate evidentiary layers.
