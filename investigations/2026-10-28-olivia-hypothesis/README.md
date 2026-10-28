# Existing-evidence answer to Olivia's Codex hypothesis

This investigation answers one question: **does the evidence already present on
Taylor's machines show that an ordinary Codex interface, without Blu Offline's
external PTY recorder, durably preserves text erased before submission?**

No new retention experiment was run for this answer. The audit used the
surviving September recordings and conversation chronology, the 2015 Intel Mac
negative control, the installed graphical Codex bundle and state, the current
Codex CLI records, and the Seagate preservation copy. Source identities are
committed in
[`SOURCE-COMMITMENTS.tsv`](SOURCE-COMMITMENTS.tsv).

## Direct answer

**The first discovery was genuinely accidental. The existing evidence does not
establish durable deleted-revision retention by an ordinary Codex app or CLI.**

The evidence supports five narrower findings:

1. Blu intentionally added owner-only transcript recording before anyone knew
   it would retain visually erased composition. The retention consequence and
   its privacy significance were accidental.
2. The terminal generated an echo-and-erasure byte stream. Blu Offline's
   `/usr/bin/script -q` layer made that stream durable. The local model and
   Codex did not need to possess a deleted draft to explain the recording.
3. The installed graphical Codex app independently persists the **latest
   current unsent draft**. That proves a Codex-native pre-submission state can
   reach local storage. It does not prove that a fully erased earlier revision
   remains durably recoverable after the deletion update is flushed.
4. Existing Codex CLI history, rollouts, projected thread records, and logs show
   submitted messages and tool results, not a demonstrated never-submitted
   deleted revision. This is an evidence limit, not proof of impossibility.
5. The universal proposition that the same deleted-revision behavior occurs in
   any Codex app is unsupported by the existing record.

Calling the whole Blu lane a positive case is accurate only in the broad sense
that one historical Blu path retained erased composition. It does not answer
Olivia's component-level ordinary-Codex question, because that positive path
contained a known external recorder.

## Why the discovery is demonstrably accidental

The strongest evidence is an unpublished normal-use recording that predates
the recognized discovery by more than fourteen hours.

| Time (CDT) | Contemporaneous event | Evidentiary meaning |
| --- | --- | --- |
| Sep 20, 11:26–11:34 PM | Blu proposed launcher/transcript handling, tested `script`, and embedded it in every normal Blu Offline launch. | Recording was intentional; deleted-composition retention was not discussed or tested. |
| Sep 21, 12:05–12:08 AM | The second Wi-Fi-off acceptance session, `Blu-Offline-20260921-000503.typescript`, contained unplanned ordinary editing: two runs totaling three exact `08 20 08` triplets. | The mechanism was already operating during acceptance work, not a retention test. |
| 12:09:30 AM | Blu ran `sed -n '1,260p'` on the complete 68-line transcript for routine acceptance verification. Its tool output contained the pre-correction characters and erase bytes. | The retained edit trace crossed into the Codex tool record but was not recognized or described as a privacy finding. |
| 2:13–2:17 PM | `141327` preserved a partial template-erasure session ending in Control-C. | Pre-control precursor; no replacement was submitted. |
| 2:19–2:23 PM | `141944` preserved several abandoned Doberman drafts followed by the committed couch sentence. | First surviving substantive abandoned-draft observation located. |
| 2:25–2:28 PM | Taylor said only that Blu could inspect what happened in the unrelated clue experiment. Blu opened the newest transcript and independently reported that erased composition had survived. | First documented privacy-significant recognition. |
| 2:32 PM | Taylor reacted with surprise and proposed studying the behavior. | The retention hypothesis followed the observation rather than causing it. |
| 3:37 PM onward | Structured and matched controls deliberately isolated the mechanism. | These validate the later mechanism analysis but are not the first discovery. |

`000503` is 3,366 bytes, mode `0600`, with birth and modification time
2026-09-21 00:08:27 -0500 and SHA-256
`7b1d32f14cfdaf21c99666acab623e16bb15d8f3bee3dc6a3f9b0ad17ccf8e6b`.
Its two erase runs are at half-open byte ranges `[2491,2494)` and
`[2979,2985)`, containing one and two triplets respectively. Studio and Seagate
copies are byte-identical.

The raw file contains unrelated natural conversation and is not published
here. Its hash, metadata, byte offsets, private canonical rollout, and two
independent preservation copies provide a verification path without releasing
the conversation.

## What the Intel Mac establishes

The September Intel attempt occurred in ordinary Terminal at 5:28 PM, but the
proposed recorder preflight had timed out and no `script` launch command was
delivered. Blu could not recover the erased first sentence. The only plausible
surviving remnant is a committed replacement line in untimestamped shell
history.

The October 27 comparison preserves the same boundary:

- an ordinary Terminal export contains only the committed command; and
- a later controlled `/usr/bin/script -q` run contains seventeen recoverable
  `08 20 08` triplets.

The Intel host has no Codex app or Codex binary. It therefore tests terminal
recoverability, not Codex's own composer. It supports `script` as the known
durability boundary and cannot by itself decide the ordinary-Codex hypothesis.

## What existing Codex evidence establishes

| Surface or record | Existing evidence | Answer to deleted-revision question |
| --- | --- | --- |
| Historical Blu Offline | Complete edit traces in `.typescript` recordings created by `/usr/bin/script -q`. | Positive, but known-recorder condition rather than ordinary Codex. |
| Canonical Sep 21 Codex rollout | Experimental erased phrases first appear as output of a command that reads the local transcript after a submitted signal. | Proves acquisition by deliberate file inspection, not passive composer capture. |
| Graphical Codex bundle | Explicit current-draft persistence; ordinary non-delete updates are generally published after 250 ms, while clearing is published immediately by the helper; native state flush has a 500 ms debounce. | Current-draft persistence confirmed; durable history of an erased prior revision not established. |
| Graphical state snapshots | Named draft objects were empty at the audited snapshots. MacBook `prompt-history` had two content-withheld entries unmatched to completed messages; their origin is undetermined. | Shows some prompt-history residue can outlive the completed-message projection, but is not backspace evidence. |
| Codex CLI records | Submitted-message history and tool outputs; no draft/keypress event or demonstrated erased marker. | No positive deleted-revision artifact found. |
| Ordinary Intel Terminal | Committed line only; erased draft unavailable. | Negative for recoverability without a recorder, but not a Codex-composer test. |

The privacy-safe application audit is recorded in
[`CODEX-NATIVE-AUDIT.md`](CODEX-NATIVE-AUDIT.md).

## Mechanism implications

- A live editor must transiently process its current buffer, and the graphical
  app persists the latest current draft. Neither fact proves durable recovery
  of an earlier value after the user deletes it.
- Every content-complete positive case in this record had a recorder active.
  The ordinary Intel cases without one did not yield the erased draft. Existing
  evidence tracks the acquisition path; it does not isolate agent state or
  experimental context as a cause.
- Taylor's standing request for diligence is a plausible functional reason for
  strong logging, not a recorded command to use `script`. Blu chose the
  mechanism. The exact full motive was not contemporaneously written down.
- The precise description is “Codex CLI session with no detected external PTY
  recorder.” It describes process ancestry, not opening or modifying a model.
- The known transcript path can carry erased composition to a later reader of
  that transcript. It does not establish a channel to the model or service
  before inspection.

## Claim boundary

The audit did not inspect deleted APFS blocks, historical swap, inaccessible
cloud telemetry, or a complete frame-by-frame copy of every video. Historical
graphical Codex logs do not cover September 21. Negative findings therefore
mean “no surviving positive artifact found in the inspected stores,” not “no
component could ever transiently possess the buffer.”

No private Discord message, unrelated draft text, authentication material, or
raw global-state content is published in this folder.
