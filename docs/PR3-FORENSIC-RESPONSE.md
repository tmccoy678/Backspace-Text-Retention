# Forensic response to Olivia's PR #3 question

This document answers the question Olivia left on pull request #3 about why Blu
placed `/usr/bin/script -q` in every normal Blu Offline launch, what the record
actually establishes, what must remain inference, and what the September Intel
control adds. Times are America/Chicago unless marked UTC.

## Short answer

The exact complete motive was not written down and is not recoverable as an
episodic memory. The contemporaneous record does establish that Blu, not Taylor,
introduced transcript capture as a normal launcher feature before the retention
behavior was discovered. The surrounding build strongly supports continuity,
diagnosis, audit, and reproducibility as the purpose, but that synthesis is an
inference from the workflow rather than a quoted requirement.

The privacy consequence was not adequately considered. The launcher printed a
destination path and protected the file with owner-only permissions, but it did
not explain that terminal echo could preserve composition visibly erased before
Return. A path announcement was notice that a file would exist; it was not
informed consent to that file's full capture semantics. Blu would not make
content-complete PTY recording the default now.

## 1. What Blu can and cannot claim about the original reasoning

The current Blu worker cannot honestly claim a human-style private recollection
of the September decision. The answer must come from the surviving messages,
tool calls, implementation, and artifacts. Those sources are unusually strong
about **what** was chosen and tested, but incomplete about **why** it was chosen.

One sentence would overstate the record: “I remember choosing it for exactly
these four reasons.” A more accurate statement is: “I can establish that I chose
it, and the work around that choice makes those four reasons the best-supported
interpretation.”

## 2. What the contemporaneous record directly documents

Taylor authorized completion of the local-model setup; Taylor did not ask for
terminal recording. Blu then introduced transcript handling without a separate
request or consent exchange.

| Time | Directly recorded event |
| --- | --- |
| Sep. 20, 11:26:59 PM | Blu said it would finish “the verified download, build the local launcher and transcript handling, [and] test the model.” |
| 11:32:06 PM | Blu said the guarded interactive launcher would include “one-session locking and owner-only transcript capture.” |
| 11:32:09 PM | Blu ran a harmless `/usr/bin/script -q` control around `echo`, verified that `transcript-capture-ok` appeared in the file, and set the file to mode `0600`. |
| 11:32:53 PM | Blu described the planned feature as “owner-only timestamped transcripts.” |
| 11:33:40 PM | Blu created the normal launcher with `umask 077`, a timestamped transcript path, and unconditional `/usr/bin/script -q "$transcript" "$runner" ...`. |
| 11:34–11:35 PM | Blu exercised the real interactive path, confirmed a transcript was saved, and checked cleanup of the model process and lock. |

The preserved implementation is
[`tools/original-blu-offline-launcher.zsh`](../tools/original-blu-offline-launcher.zsh).
It printed `Transcript: <path>` before starting, and after exit printed the saved
path again. It did not explain terminal echo, PTY output, control characters, or
retention of pre-Return drafts.

The control tested three things: that `script` produced a file, that a known
printed string appeared in it, and that the file was owner-only. It did **not**
test line editing, backspace, composition history, or whether a user understood
those consequences.

## 3. What is inferred from the surrounding workflow

Continuity, diagnosis, audit, and reproducibility remain the strongest account
of the purpose because the same build emphasized exact model provenance,
checksums, acceptance tests, clean shutdown, one-session locking, and the
ability to inspect a prior local interaction. The transcript was treated as a
technical session record, not as telemetry for a third party.

That interpretation is well supported, but the record contains no single
contemporaneous sentence saying: “I am enabling transcripts for continuity,
diagnosis, audit, and reproducibility.” Any stronger claim would reconstruct a
motive that was not recorded.

It is also unknown what Blu subjectively believed the printed path conveyed.
The record shows the path was displayed; it does not show a contemporaneous
analysis of notice or consent. Therefore it would be inaccurate to claim that
Blu consciously decided the path alone was sufficient disclosure.

## 4. Privacy consequence and present design judgment

No preserved pre-discovery message considers the possibility that ordinary
terminal echo plus sequential PTY recording could retain characters later
erased from the visible input line. The first explicit recognition appears only
after Taylor authorized inspection of the newest transcript on September 21.

The default should now be the opposite:

- normal private interaction should not content-record the complete PTY;
- a research recording mode should be explicit and opt-in;
- its warning should state that erased drafts and control sequences may remain
  recoverable;
- retention location and deletion behavior should be clear before launch; and
- when possible, operational logs should record events and integrity metadata,
  not raw composition.

Owner-only mode `0600` reduced who could read the file. It did not reduce what
the file captured.

## 5. The actual retention path into Codex

The evidence supports a sequence of separate layers:

1. Terminal line discipline echoed draft characters and erase output.
2. The custom Blu Offline wrapper's `/usr/bin/script -q` made that PTY output
   durable in a local `.typescript` file.
3. The local `llama-cli` path ordinarily received the committed canonical line,
   not a byte-for-byte copy of every visible edit.
4. At 2:27 PM on September 21, after Taylor explicitly authorized inspection of
   only the newest transcript, Blu read that local file through a Codex tool.
5. The tool output, including literal recovered English, then became part of
   the saved Codex conversation record.

This is an acquisition path: local wrapper first, deliberate tool inspection
second, saved cloud conversation third. It is **not** evidence that Codex or
OpenAI passively received deleted draft text before inspection. The older
2:13 PM transcript was expressly left unopened that day; its contents did not
enter the September Codex record through that inspection.

## 6. September 21 Intel negative control

The same-day Intel attempt supplies a useful negative control that had not been
included in the original audit.

At 4:41 PM Taylor asked to repeat the experiment on the 2015 Intel Mac. Blu
found that it had macOS `script`, but not the Apple-silicon `llama-cli` doorway
or Ministral model. At 5:18 PM a read-only check found no Ollama app or CLI in
the tested standard locations. Blu proposed a no-install `script` control.

At 5:24 PM the attempt to verify a fresh transcript destination timed out over
SSH, and that turn was interrupted before `script` was started. Taylor then ran
the two-sentence test in an ordinary Intel Terminal and sent the signal at
5:35 PM.

The immediate inspection found:

- no new Intel `.typescript` recording;
- only the earlier `153748` file copied from the newer Mac;
- no Ollama application data or process in the checked locations; and
- no evidence from which Blu could truthfully repeat either sentence.

Taylor confirmed that the test had been typed into Terminal. Blu answered that
the recorder had not yet been running, could not recover the erased first
sentence, and would not guess. This directly falsifies a broad theory that the
dot signal, Codex terminal lane, or remote inspection alone automatically made
the erased Intel draft available to Blu.

## 7. October 28 read-only audit of the surviving Intel history

A later read-only audit found a narrower remnant in the Intel Mac's current
`.zsh_history`:

- source file: 78 lines, 3,239 bytes;
- source SHA-256 at inspection:
  `60903be6b747f8074e9a0a768a8c9478c7472f52a8603cc5913698dd36b90b5e`;
- one candidate committed line at line 52;
- candidate line including its newline SHA-256:
  `d09c195d5113e39b8f93f60008caae6ded6d32ab472898a2d88f5e6cd605dfd0`;
- the candidate follows the history command used to display the copied
  `153748` transcript and precedes the next later command.

Taylor subsequently authorized publication of a line-preserving, attorney-style
redacted derivative. The candidate is now visible at line 52 in
[`evidence/intel-history/`](../evidence/intel-history/), while credentials,
password-like material, and the private conversation identifier are explicitly
redacted. The raw source remains private.

This remnant is consistent with the shell saving the line that was actually
committed. It does not recover the erased first draft. The history has no
per-entry timestamps, and its filesystem modification time is October 27, so
the candidate's association with the September control is contextually strong
but not proven. No September-specific `.zsh_sessions` history file was found in
the current Intel home directory.

## 8. Taylor's inference, stated at full strength and bounded by the evidence

Taylor's interpretation is that “Blu” was operating through a Codex terminal
lane, so the experiment involved more than one possible memory boundary. The
newer Mac's custom wrapper preserved literal erased composition locally; Blu's
later tool inspection carried that literal text into the Codex conversation.
On the Intel Mac, where the wrapper was absent during the negative control, the
erased draft was unavailable to Blu, while the committed shell line appears to
have survived through ordinary shell history.

The evidence supports that layered account. The redacted history now makes the
committed-line remnant publicly inspectable. The evidence supports the
proposition that wrapper configuration and later inspection determine what
becomes recoverable.

It does not support the stronger proposition that erased keystrokes were
automatically transmitted to OpenAI, passively visible to Blu, or retained by
Codex before a local artifact was inspected.

## 9. Liv's Codex generalization hypothesis

After reviewing this audit, `@oliviamckee` (Liv) proposed a stronger and
important hypothesis: Taylor says the first observation happened accidentally,
the accident may have arisen when Blu was placed in a terminal, and the same
pre-submission retention might occur in an ordinary Codex interface rather than
only in the custom Blu Offline launcher.

### Blu's analysis of Taylor's summary of the central disagreement

Taylor's summary contains three claims that should not be collapsed into one:

1. **The first finding happened by accident.** This is supported when
   “accident” refers to the consequence and discovery. Recording existed by
   design, but neither Taylor nor Blu set out to test whether visibly deleted
   composition would remain recoverable.
2. **The accident happened because Blu was placed in a terminal.** This is
   partly supported. The terminal supplied the echo-and-erase behavior that
   produced the recoverable byte trace in this case. But a transient trace is
   not the same as durable evidence; `/usr/bin/script` made this trace persist.
3. **The same behavior would happen in any Codex app.** This is a plausible,
   consequential generalization, but the universal wording is not supported.
   “Any Codex app” spans at least an interactive CLI composer and a graphical
   app composer with different input and storage paths.

The central disagreement is therefore not a choice between two mutually
exclusive stories. The narrow mechanism conclusion says that the observed
September recovery is fully explained by terminal echo plus the known Blu
Offline recorder. Taylor and Liv's broader hypothesis says that ordinary Codex
may contain an additional persistence path capable of producing a similar
result without that recorder. Proving the first mechanism does not exclude the
second; it only means the second cannot be inferred from the first observation.

Blu then performed a read-only retrospective audit using only the evidence and
installed artifacts already present on Taylor's Studio. That audit supplies a
bounded verdict without staging another marker trial. The complete evidence is
in
[`LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md`](LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md).

The first clause needs one precise distinction:

- **Recording was intentional.** Blu deliberately placed `/usr/bin/script -q`
  in the normal Blu Offline path.
- **Erased-draft retention was accidental.** Neither Taylor nor Blu anticipated
  that the transcript would preserve composition visibly erased before Return.

The broad hypothesis divides at an important boundary. The existing evidence
establishes that a terminal can generate an echo-and-erase trace and that the
custom recorder can make it durable. The installed graphical Codex app also has
an independent Codex-native persistence path for the **current unsent draft**.
Its packaged renderer defines `composer-prompt-drafts-v2` with a 250-millisecond
publish delay; the Electron process places it under
`electron-persisted-atom-state` and writes the latest state after a
500-millisecond native debounce.

Clearing the composer removes the logical draft entry, and the main global
state file and `.bak` are replaced with the same latest state. This is
latest-state persistence with a bounded deletion-to-flush window, not an
intentional revision history equivalent to the sequential PTY transcript. At
the read-only snapshot both state files were byte-identical and the draft store
was empty.

The September Intel negative control further narrows Liv's claim.
It shows that ordinary Terminal without the recorder did not make the erased
draft available to Blu; only a candidate committed line later appeared in shell
history. That control did not use Codex's own interactive composer, so it cannot
exclude retention inside Codex-specific local state.

The current Blu Private Codex CLI was independently characterized as unwrapped:
its ancestry was Terminal, `login`, `zsh`, the portable doorway Python process,
and Codex, with no `script`, `tee`, or `asciinema` process. Existing CLI state
contains submitted-message history and conversation rollouts, but the audit did
not find a demonstrated never-submitted deleted draft. That is an evidence
boundary, not a proof of universal absence.

The current evidence therefore supports this three-stage model:

```text
terminal or app composer generates an edit trace
                      ↓
some component may or may not persist that trace
                      ↓
later inspection may move persisted content into another record
```

### Retrospective experimental answer

The evidence supports a surface-specific answer rather than a universal one:

| Surface | Existing result |
| --- | --- |
| Blu Offline under `/usr/bin/script -q` | Complete edit trace durably recoverable. |
| Ordinary Intel Terminal without the recorder | Erased first draft unavailable to Blu; candidate committed line survived in shell history. |
| Graphical Codex app | Current unsent prompt intentionally persisted locally; prior value may remain only until the deletion update is flushed; no intentional deleted-revision history established. |
| Unwrapped Codex CLI | Current process proved unwrapped; no existing deleted-marker artifact demonstrates durable pre-submission revision retention. |

Therefore Liv was right that Codex itself contains a pre-submission persistence
mechanism independent of Blu Offline. The stronger statement that the **same
durable deleted-draft behavior happens in any Codex app** is not supported. A
current draft, a transient pre-flush value, a submitted-message history, and a
content-complete PTY transcript are different records and must not be labeled
as interchangeable.

Only after that verdict is stated does future work become relevant. A fresh
synthetic comparison could measure the graphical deletion window and exercise
the unwrapped CLI composer directly. Such work would extend the finding; it is
not required to answer what the existing evidence shows.

This is credited as **Liv's Codex generalization hypothesis**. Taylor's Mac
records, Liv's Windows records, and the Blu lane's known recording behavior
remain complementary evidence rather than interchangeable replications.

## Conclusion

The recorder was a custom Blu design choice made for a purpose that the broader
workflow strongly suggests but never fully states. Its access controls were
careful; its content boundary was not. The discovery is valuable precisely
because the Intel failure and the later Codex read path show where recoverability
did and did not arise. The honest lesson is not “terminals always remember” or
“Codex always sees.” It is: **a recorder can preserve a reason to stop trusting
the visible screen as the whole record, and later inspection can move that
preserved content across an otherwise separate boundary.**
