# Retrospective answer to Olivia's ordinary-Codex retention hypothesis

## Question

Olivia's component-level question is whether an ordinary Codex interface can
durably preserve composition erased before submission without Blu Offline's
special `/usr/bin/script` recording layer. Taylor's stronger formulation is
that this behavior would occur in any Codex app.

This answer uses only evidence that already existed on the MacBook Pro, Mac
Studio, Seagate preservation volume, and accessible 2015 Intel Mac. No new
retention experiment was run.

The relevant unit is the persistence mechanism, not the identity label “Blu.”
Calling the whole Blu lane a positive n=1 observation is descriptively true,
because one historical Blu path retained erased composition. It cannot by
itself answer the ordinary-Codex question: that positive path contained a known
external PTY recorder.

## Verdict

1. **Accidental discovery: strongly supported.** Blu deliberately enabled
   owner-only transcript recording, but neither Taylor nor Blu anticipated or
   tested the consequence that visually erased composition would remain in the
   transcript. A routine midnight acceptance session already contained three
   recorded erase triplets. Blu imported that complete transcript into a Codex
   tool result at 12:09 AM and did not recognize the privacy consequence. The
   first explicit recognition came at 2:28 PM during an unrelated clue
   experiment, followed by Taylor's surprised response.
2. **Historical durability mechanism: identified.** Terminal line editing
   generated the echo-and-erasure stream. Blu Offline's external
   `/usr/bin/script -q` layer made that stream durable. This explains the
   historical recovery without requiring the local model, Codex composer, or a
   network service to have retained the erased draft independently.
3. **Graphical Codex current-draft persistence: implemented and locally
   instantiated, but not a deleted-history result.** The installed app contains
   code that persists the latest current unsent draft. Ordinary non-delete
   updates are generally published after 250 ms; clearing is published
   immediately by the helper, followed by a 500 ms native flush debounce.
   Clearing removes the logical draft entry. The audited draft objects were
   empty. No surviving erased prior revision was demonstrated.
4. **Codex CLI deleted-revision retention: not established.** Existing history,
   rollouts, thread projections, abort records, and logs show submitted messages
   and tool results, not a never-submitted deleted revision. The inspected
   current process ancestry had no detected external PTY recorder. This is an
   evidence limit rather than proof that no transient buffer could exist.
5. **“Any Codex app” is unsupported.** Current-draft autosave, queued-prompt
   residue, submitted-message history, terminal screen state, and a sequential
   PTY transcript are different records. Existing evidence does not justify
   treating them as interchangeable.

The concise answer is:

> The first Backspace Gate discovery was genuinely accidental. The September
> trace became durable because Blu had already placed `/usr/bin/script` around
> the terminal session. Codex-native current-draft persistence exists, but the
> evidence already present does not show that an ordinary or every Codex
> interface durably preserves a fully erased earlier revision.

## Pre-discovery chronology

The earlier midnight artifact strengthens the accidental-discovery conclusion:

| Time (CDT) | Evidence |
| --- | --- |
| Sep 20, 11:26–11:34 PM | Blu introduced transcript handling, tested `script`, and embedded it in the normal launcher. No message discussed erased composition. |
| Sep 21, 12:05–12:08 AM | Routine accepted Blu Offline run `000503` recorded two editing runs totaling three `08 20 08` triplets. |
| 12:09:30 AM | Blu read the complete 68-line transcript through a Codex tool for acceptance checks. The tool output contained pre-correction bytes and erase output; Blu did not identify retention. |
| 2:13–2:17 PM | Partial `141327` template-erasure precursor ended in Control-C. |
| 2:19–2:23 PM | `141944` preserved substantive abandoned Doberman drafts and a committed couch sentence. |
| 2:28:06 PM | Blu first reported that erased composition had survived in the transcript. |
| 2:32:32 PM | Taylor reacted with surprise and proposed studying the behavior. |
| 3:37 PM onward | Structured and matched controls deliberately tested the mechanism. |

The midnight source is 3,366 bytes, mode `0600`, SHA-256
`7b1d32f14cfdaf21c99666acab623e16bb15d8f3bee3dc6a3f9b0ad17ccf8e6b`.
Its raw ordinary conversation remains private; metadata, offsets, copies, and
the import chronology are documented in the
[existing-evidence investigation](../investigations/2026-10-28-olivia-hypothesis/).

This chronology distinguishes four milestones that earlier repository versions
conflated:

1. earliest surviving recorded editing trace located: 12:05–12:08 AM;
2. earliest known ingestion of such a trace into a Codex tool record: 12:09 AM;
3. first privacy-significant recognition and substantive recovery: 2:28 PM; and
4. later structured foundation case: 3:37 PM.

## Evidence by surface

| Existing observation | What it establishes | What it does not establish |
| --- | --- | --- |
| Blu Offline `.typescript` files | A known external PTY recorder durably preserved sequential echo and erase output. | Codex-native composer retention. |
| Midnight routine acceptance and unnoticed Codex tool import | The behavior existed and entered a tool result before anyone recognized it. | Passive receipt by Codex before deliberate file inspection. |
| September ordinary Intel Terminal attempt | Blu could not recover the erased first sentence without the recorder; a candidate committed line survived in shell history. | Behavior of a Codex composer, because Intel had no Codex app or binary. |
| October Intel ordinary-shell export versus controlled `script` run | Ordinary export kept the committed command; active `script` recorded seventeen erase triplets. | A universal absence theorem for volatile terminal state. |
| Installed graphical Codex bundle | The app implements latest-current-draft persistence independent of Blu Offline. | Durable deleted-revision history after clearing and flush. |
| Graphical state snapshots | The draft keys existed and were empty; two content-withheld prompt-history entries were unmatched to completed-message projection. | The origin of those entries, or that they came from Backspace or September. |
| Codex CLI records | Submitted messages and tool results are durable; the historical experimental phrases entered after transcript inspection. | A demonstrated never-submitted deleted composer revision. |

## The installed graphical app

The inspected app identified itself as:

- bundle identifier `com.openai.codex`;
- version `26.1021.31345`, build `21828`;
- `app.asar` size 640,530,938 bytes; and
- SHA-256
  `130145706a912db74e4d260ad7538f10f1e05e88af955f9afba42cdf01e64606`.

The packaged renderer defines `composer-prompt-drafts-v2`, with
`composer-prompt-drafts-v1` as a legacy key. The draft helper generally
publishes ordinary non-delete changes after 250 milliseconds, while clearing
or supplying an expected value is published immediately. The Electron main
process stores persisted atoms in `~/.codex/.codex-global-state.json` after a
500-millisecond debounce and uses two sequential atomic temp-file renames to
replace the main file and then `.bak` with the newest state.

This supports a bounded transitional possibility: an older nonempty value may
remain on disk until a deletion update is published and flushed. It does not
create the content-complete revision sequence present in a PTY transcript.

At the Studio snapshot, both state files were byte-identical, 299,967 bytes,
had SHA-256
`19dee65be9f59ac5ab3e3bca071132d523bd2c5d40fe9ec7151929f037f396fb`,
and contained an empty `composer-prompt-drafts-v2` object. The separate MacBook
snapshot also contained an empty saved conversation draft. No private prompt
content is published.

The privacy-safe commands, identifiers, and offsets are preserved in the
[Codex-native audit](../investigations/2026-10-28-olivia-hypothesis/CODEX-NATIVE-AUDIT.md).

## Codex CLI with no detected external PTY recorder

The inspected Blu Private ancestry was:

```text
Terminal.app
  -> login
    -> zsh
      -> portable_blu.py
        -> codex
```

No `script`, `tee`, or `asciinema` content recorder appeared in that chain.
“No detected external PTY recorder” describes this observed local process path;
it makes no claim about model internals.

The September CLI record identifies source `cli`, originator `codex-tui`, and
historical version `0.154.0`. The current build differs. In the relevant
historical sequence, Codex stored the submitted signal first; the erased
experimental phrases first appeared when a command read the separate local
transcript. No existing record demonstrates a fully erased, never-submitted
composer revision being durably written by the CLI.

## Why the acquisition path is the supported explanation

Existing evidence does not isolate agent state or experimental context as a
cause. The content-complete positive cases had an explicit recorder active. The
ordinary Intel cases without one did not yield the erased draft. Recovery
tracks the acquisition path in the evidence presently available.

Taylor's standing requests for diligent, complete work are a plausible
functional reason Blu chose strong logging. The exact full motive was not
contemporaneously recorded, and Taylor did not ask for `/usr/bin/script` by
name or know its composition-history consequence.

## Claim boundary

This answer does not establish what a network service received, what volatile
process memory once contained, or what deleted/unallocated storage might have
held. Historical graphical logs do not cover September 21. The negative result
is therefore “no surviving positive ordinary-Codex deleted-revision artifact
was found in the inspected evidence,” not proof that such retention is
impossible.

No fresh marker trial was required or performed to state this verdict.
