# Earliest-evidence and launcher-origin audit

This audit separates the earliest accidental observation from later controlled
recordings and documents why `/usr/bin/script` was present in Blu Offline. It
also distinguishes the first ordinary-shell attempt on the 2015 Intel Mac from
the later recorded-PTY replication.

## What the contemporaneous launcher record establishes

On September 20, 2026, Taylor authorized Blu to finish configuring a newly
installed local model but did not request terminal recording. At 11:26:59 PM
CDT, Blu said it would build "the local launcher and transcript handling." At
11:32:53 PM, before the launcher existed, Blu described the planned feature as
"owner-only timestamped transcripts."

The implementation sequence then:

1. tested `/usr/bin/script -q` with a harmless `echo` command;
2. confirmed that the resulting transcript was mode `0600`; and
3. placed `/usr/bin/script -q "$transcript" ...` in the normal Blu Offline
   launcher path under `umask 077`.

The preserved launcher is
[`tools/original-blu-offline-launcher.zsh`](../tools/original-blu-offline-launcher.zsh).
It prints the transcript path before launch, records every normal session, and
sets the completed transcript to mode `0600`.

This establishes that transcript capture was a custom Blu Offline launcher
feature, selected by Blu before the Backspace Gate observation. It was not a
Codex default, a `llama.cpp` default, a macOS background recorder, or a feature
Taylor specifically requested. The surrounding acceptance workflow—complete
readback, permission checks, hashes, and preservation of technical sessions—
supports continuity, diagnosis, audit, and reproducibility as the design
purpose. The contemporaneous record does not contain a single sentence giving
that full rationale, so this purpose is the best-supported interpretation, not
a quoted design requirement.

The launcher announced that a transcript would be written. It did **not** warn
that terminal echo could preserve text visibly erased before Return. That
composition-history consequence was discovered later.

## Earliest September 21 evidence

Two owner-only local transcripts predate the later structured
`marie is black.` / `stanley is red.` recording:

| Artifact | Closed / filesystem time (CDT) | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| [`Blu-Offline-20260921-141327.typescript`](../evidence/transcripts/Blu-Offline-20260921-141327.typescript) | 2026-09-21 2:17:31 PM | 1,190 | `5cc08346d7de25988aa687d292eefc1bf994ba74d5031ff9b0cd7e3fc271cb5e` |
| [`Blu-Offline-20260921-141944.typescript`](../evidence/transcripts/Blu-Offline-20260921-141944.typescript) | 2026-09-21 2:23:20 PM | 1,816 | `7175aea528876898938e13eb98432f0b0e7bc8170e9c62fb3fadecf80126b375` |

At 2:27:03 PM, the contemporaneous conversation listed both files. After Taylor
gave permission to inspect only the newest transcript, Blu opened `141944`. At
2:28:06 PM, Blu reported the privacy-significant observation: "the transcript
records text you erased while composing, not just what you finally submitted."
Blu expressly left `141327` unopened at that time and asked whether it was the
earlier clue-making attempt.

The first file records the harmless template `My harmless target sentence is:
[WRITE YOUR SENTENCE HERE].`, cursor movement, erasure, and Control-C; no
replacement line was submitted. The second records Taylor revising several
nonsensitive Doberman phrases before submitting a final couch sentence.

Taylor explicitly authorized publication of both byte-preserved raw files on
October 28, 2026. They contain no credentials or private identifiers. Their
release does not retroactively convert the first session into a planned
recording experiment: Taylor did not request recording, and the pre-existing
Blu Offline wrapper had already embedded `/usr/bin/script` in every launch.

The 3:37 PM artifact `Blu-Offline-20260921-153748.typescript` is the later
structured foundation recording used for the byte-level case report. It remains
valid evidence, but it was not the first accidental observation.

## October 27 Intel sequence

The first 2015 Intel Mac attempt was conducted in an already-open ordinary zsh
shell. The surviving Terminal export and later read-only inspection establish:

- Terminal started at 10:48:19 PM and zsh at 10:48:20 PM on `ttys000`;
- `/dev/ttys000` was modified at 10:49:04 PM;
- `Terminal Saved Output.txt` was created at 10:49:15 PM;
- the saved output contains the committed replacement command and its shell
  error, not the abandoned draft; and
- the live process state contained Terminal and zsh, not `script`.

The exact saved Terminal export is published with the
[first-attempt audit](../replications/intel-mac-2026-10-27/FIRST-ORDINARY-SHELL-AUDIT.md).
Targeted searches found no first-attempt `.typescript` file or `script`
invocation in shell history. That evidence is consistent with Taylor's report
that the attempt occurred outside the recording wrapper. Absence of a found
artifact alone cannot prove that no transient recorder ever existed; the
bounded claim is that no active recorder was observed and no recording artifact
was found in the inspected locations.

The controlled `/usr/bin/script` replication began later, at 11:16 PM. It is a
separate experiment and must not be substituted for the first ordinary-shell
attempt.

## Same-day September Intel control and Codex acquisition boundary

An earlier negative control occurred on the Intel Mac on September 21. The
operator completed the two-sentence procedure in ordinary Terminal before the
proposed `script` control had started. After the signal, Blu found no new Intel
recording and could not recover either sentence. A later audit found a private
candidate committed line in untimestamped shell history, but not the erased
draft. See the full [PR #3 forensic response](PR3-FORENSIC-RESPONSE.md).

This result also sharpens the cloud boundary. On the newer Mac, the local
wrapper first preserved PTY output. Literal recovered text entered the Codex
conversation only when Blu later read the local transcript through a tool after
Taylor authorized that inspection. The Intel negative control does not support
passive pre-inspection receipt by Codex or OpenAI.

## Privacy boundary

This public audit excludes credentials, unrelated shell history, and the full
private conversation record. The two nonsensitive raw transcripts are included
under Taylor's explicit publication authorization.
