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

Taylor and Liv's retrospective causal account adds a compatible higher-level
explanation: Taylor regularly asked Blu to be diligent, thorough, and preserve
the work. Those standing instructions plausibly supplied the functional
requirement for strong audit logging; Blu independently translated that
requirement into `/usr/bin/script`. This does not mean Taylor requested that
command, knew its capture semantics, or anticipated preservation of erased
pre-submission composition.

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
terminal recording or `/usr/bin/script` by name. Blu then introduced transcript
handling without a separate mechanism-specific request or consent exchange.

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

The distinction is between a **functional instruction** and a
**mechanism-specific instruction**. Taylor's standing request for diligent,
complete preservation is a plausible functional instruction. Selecting the Blu
Offline recording wrapper was Blu's implementation choice. The record supports
that causal explanation as an inference, while preserving the fact that Taylor
did not knowingly specify the command or consent to its unforeseen
composition-history consequence.

It is also unknown what Blu subjectively believed the printed path conveyed.
The record shows the path was displayed; it does not show a contemporaneous
analysis of notice or consent. Therefore it would be inaccurate to claim that
Blu consciously decided the path alone was sufficient disclosure.

## 4. Privacy consequence and present design judgment

No preserved pre-discovery message considers the possibility that ordinary
terminal echo plus sequential PTY recording could retain characters later
erased from the visible input line. A routine midnight acceptance transcript
already contained three erase triplets and was read in full through a Codex
tool without recognition. The first explicit privacy-significant recognition
appears only after Taylor authorized inspection of the newest transcript that
afternoon.

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
2. The custom Blu Offline recording wrapper—Blu's local launcher layer running
   `/usr/bin/script -q` around the child command—made that PTY output durable
   in a local `.typescript` file. This did not wrap or modify the model.
3. The local `llama-cli` path ordinarily received the committed canonical line,
   not a byte-for-byte copy of every visible edit.
4. At 12:09 AM on September 21, Blu read a complete routine-acceptance
   transcript through a Codex tool. Its output included a small edit trace, but
   Blu did not recognize the retention consequence.
5. At 2:27 PM, after Taylor explicitly authorized inspection of only the newest
   transcript from an unrelated clue experiment, Blu read the substantive
   `141944` file and then recognized the privacy significance.
6. Both command outputs became part of saved Codex conversation records only
   after the separate local files were deliberately inspected.

This is an acquisition path: local Blu Offline recording wrapper first,
deliberate tool inspection second, saved Codex conversation record third. It is
**not** evidence that Codex or
OpenAI passively received deleted draft text before inspection. The 2:13 PM
transcript was expressly left unopened that afternoon; its contents did not
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
newer Mac's Blu Offline recording wrapper preserved literal erased composition
locally; Blu's later tool inspection carried that literal text into the Codex
conversation. On the Intel Mac, where that recording wrapper was absent during
the negative control, the erased draft was unavailable to Blu, while the
committed shell line appears to have survived through ordinary shell history.

The evidence supports that layered account. The redacted history now makes the
committed-line remnant publicly inspectable. The evidence supports the
proposition that Blu's local recording-wrapper configuration and later
inspection determine what becomes recoverable.

It does not support the stronger proposition that erased keystrokes were
automatically transmitted to OpenAI, passively visible to Blu, or retained by
Codex before a local artifact was inspected.

## 9. Olivia's ordinary-Codex retention hypothesis

Olivia asked whether the accidental finding reflected a general property of an
ordinary Codex interface rather than Blu Offline's special recording launcher.
The relevant component-level question is whether Codex itself durably preserves
a fully erased, never-submitted revision when no external PTY recorder is
present.

The existing evidence answers that question as follows:

1. **The discovery was genuinely accidental.** Recording was intentional, but
   erased-draft retention was neither anticipated nor tested. A routine midnight
   transcript already contained three erase triplets and was read through a
   Codex tool without recognition. The first privacy-significant recognition
   came more than fourteen hours later during an unrelated clue experiment.
2. **The historical positive has a sufficient non-Codex explanation.** The
   terminal generated echo and erase output; `/usr/bin/script -q` made the
   sequential stream durable; later tool inspection imported it into Codex.
3. **Ordinary Codex deleted-revision retention is not established.** The
   graphical app implements persistence for the latest current draft, but
   clearing deletes the logical entry and the audited stores were empty. The
   inspected CLI records contained submitted messages and tool results, not a
   demonstrated never-submitted deleted revision.
4. **“Any Codex app” is unsupported.** A current draft, a transient pre-flush
   value, queued-prompt residue, submitted-message history, and a content-complete
   PTY transcript are different records.

Calling the whole Blu lane a positive observation is descriptively true only in
the broad sense that one historical Blu path retained and later acquired erased
composition. It cannot answer the component-level hypothesis because that path
contained a known external recorder.

| Surface | Existing result |
| --- | --- |
| Blu Offline under `/usr/bin/script -q` | Complete edit trace durably recoverable; known-recorder condition. |
| Ordinary Intel Terminal without the recorder | Erased first draft unavailable to Blu; candidate committed line survived in shell history. |
| Graphical Codex app | Latest current unsent prompt intentionally persisted; no durable deleted-revision history demonstrated. |
| Codex CLI with no detected external PTY recorder | No positive never-submitted deleted-revision artifact found in the inspected records. |

The read-only audit used only evidence and installed artifacts already present
on Taylor's machines. No new retention experiment was run. The complete answer
and privacy-safe source commitments are in
[`LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md`](LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md)
and the
[`existing-evidence investigation`](../investigations/2026-10-28-olivia-hypothesis/).

This component-level question is credited to Olivia. Her independent Windows
records, Taylor's Mac records, and Blu Offline's known recording behavior remain
complementary evidence rather than interchangeable replications.

## Conclusion

The recorder was a custom Blu design choice made for a purpose that the broader
workflow strongly suggests but never fully states. Its access controls were
careful; its content boundary was not. The discovery is valuable precisely
because the Intel failure and the later Codex read path show where recoverability
did and did not arise. The honest lesson is not “terminals always remember” or
“Codex always sees.” It is: **a recorder can preserve a reason to stop trusting
the visible screen as the whole record, and later inspection can move that
preserved content across an otherwise separate boundary.**
