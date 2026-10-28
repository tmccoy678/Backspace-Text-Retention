# September 21 pre-control evidence and Intel-attempt audit

This folder analyzes the first two Backspace-specific recordings published under
[`evidence/transcripts/`](../../evidence/transcripts/) and documents the later,
unrecorded September 21 attempt on the 2015 Intel Mac. The source machines were
searched with read-only intent on October 28, 2026; one auxiliary SQLite
coordination-file timestamp side effect is disclosed in
[`SEARCH-COVERAGE.md`](SEARCH-COVERAGE.md). The three evidence artifacts covered
by this audit are identified by SHA-256 in
[`EVIDENCE.sha256`](EVIDENCE.sha256).

A subsequent expanded pass located an earlier private routine-acceptance
recording, `Blu-Offline-20260921-000503.typescript`. It is now the earliest
surviving recorded editing trace located, and it had already been read without
recognition through a Codex tool at 12:09 AM. Its unrelated natural conversation
remains private; its hash, metadata, erase-run offsets, and preservation copies
are committed in the
[existing-evidence answer to Olivia](../2026-10-28-olivia-hypothesis/).

This audit answers the artifact questions raised by
[`@oliviamckee` on PR #2](https://github.com/tmccoy678/Backspace-Text-Retention/pull/2#issuecomment-6461455009):
the command or launcher, shell history, any transcript, process evidence,
screenshots, timestamps, contemporaneous conversation, and the scope of the
search.

## Main findings

### The first published substantive Backspace-specific observation predates the controlled case

`Blu-Offline-20260921-141944.typescript` is the earliest published recording in
which meaningful erased drafts were noticed and then inspected. It is
1,816 bytes and contains seven runs totaling 69 exact `08 20 08` erase
triplets. The recoverable composition includes successive abandoned text such
as `the purple `, `the doberman bit `, and
`the doberman won best in show`, followed by edits that resolve to the submitted
sentence:

```text
marie is my favorite doberman and she is sleeping on the couch.
```

At 2:27:15 PM CDT, the contemporaneous assistant opened that exact transcript.
At 2:28:06 PM it reported the privacy-relevant observation: the transcript had
recorded text erased during composition. This is the first documented
privacy-significant recognition in the surviving records. It occurred more
than an hour before the 3:37 PM two-sentence case currently centered in the
foundation manuscript and more than fourteen hours after the unnoticed
midnight trace.

`Blu-Offline-20260921-141327.typescript` is an even earlier, partial session.
It is 1,190 bytes and contains two erase runs totaling 35 `08 20 08` triplets,
but the visible input is still the literal prompt template
`My harmless target sentence is: [WRITE YOUR SENTENCE HERE].` and the session
ends with Control-C. It is relevant pre-control evidence, but not the first
substantive discovery run.

Both files remained owner-readable source recordings (`0600`) and were later
migrated byte-for-byte from the 2026 MacBook Pro to the Mac Studio. Their
September filesystem birth and modification times survived the migration; the
October 26 change time records the migration, not a September rewrite. Exact
metadata is in [`ARTIFACT-METADATA.tsv`](ARTIFACT-METADATA.tsv).
Exact run offsets and counts are in [`BYTE-ANALYSIS.md`](BYTE-ANALYSIS.md).

### The September Intel attempt happened, but the recorder never started

The surviving evidence supports the following reconstruction:

1. At 4:17–4:29 PM, the already-published 1,344-byte Apple-silicon transcript
   was copied to and inspected on the Intel Mac. The included Intel screenshot
   shows that file, its `/Users/taylor/...` model path, and the command used to
   render its erased bytes. Its hash exactly matches the published source, so
   it is not an Intel-generated recording.
2. At 5:18 PM, Taylor proposed a fresh test on the 2015 Mac. The assistant said
   it was not ready, found no Ollama installation, and proposed a built-in
   `script` control instead.
3. At 5:24 PM, the assistant said it would confirm a fresh filename and then
   provide the exact sequence. The preflight SSH command referenced
   `~/Desktop/Blu-Intel-Control-20260921.typescript`, but the connection timed
   out. No recording command or launcher was then delivered or executed.
4. The Intel login database records a local `Blu` session on `ttys000` at
   5:28 PM. At 5:35 PM Taylor sent the inspection signal. At 5:37 PM Taylor
   confirmed that the sentences had been typed in Terminal on the 2015 Mac.
5. The immediate search found only the earlier copied Apple-silicon transcript.
   The assistant contemporaneously acknowledged that the recorder was not yet
   running and that plain Terminal had not produced a `.typescript` artifact.

The best-supported interpretation is therefore not that a recorded Intel
experiment failed. A real Intel Terminal attempt occurred, but it ran outside
`script`; no native Intel recording was created at the declared or searched
locations. The broad October 28 search again found no unpublished September
Intel transcript, launcher, saved process list, or shell-history entry that
launched `script`, and no screenshot or video from the attempt window. It did
find one untimestamped candidate committed line in the Intel
`.zsh_history`. Taylor later authorized a line-preserving
[redacted derivative](../../evidence/intel-history/), which publishes the
candidate at source line 52 as `he could remarry and inheret her estate.` while
keeping credential-bearing source content private. Its position makes
association with the control contextually strong but unproven; it preserves no
erased draft. The search cannot forensically disprove a file that was created
and later deleted, but no surviving evidence points to one.

The exact conversation and original command outputs are transcribed in
[`CONTEMPORANEOUS-RECORD.md`](CONTEMPORANEOUS-RECORD.md). Search locations and
limitations are in [`SEARCH-COVERAGE.md`](SEARCH-COVERAGE.md). The shell-history
source commitment, redaction log, and privacy rationale are recorded under
[`evidence/intel-history/`](../../evidence/intel-history/) and in
[`PR3-FORENSIC-RESPONSE.md`](../../docs/PR3-FORENSIC-RESPONSE.md).

## Historical correction

Commit [`c4b366945e23`](https://github.com/tmccoy678/Backspace-Text-Retention/commit/c4b366945e23e959aabfbb66f26c7443114903a8),
dated September 25, already stated that “a later attempt on a 2015 Intel Mac”
lacked an active `script` recorder. The statement therefore referred to the
September 21 episode described here. Commit
[`40dc0ff898dc`](https://github.com/tmccoy678/Backspace-Text-Retention/commit/40dc0ff898dc8606d4cb1890cc91a8cabc944ade)
later changed that sentence to “An initial October 27 attempt” while adding the
separate October 27 replication. That edit conflated two episodes. The
September attempt and the October replication are distinct.

## Included evidence

| File | Evidentiary role |
| --- | --- |
| [`Blu-Offline-20260921-141327.typescript`](../../evidence/transcripts/Blu-Offline-20260921-141327.typescript) | First published partial Backspace-specific precursor |
| [`Blu-Offline-20260921-141944.typescript`](../../evidence/transcripts/Blu-Offline-20260921-141944.typescript) | First published substantive retention observation and first privacy-significant recognition |
| [`evidence/intel-screen-20260921-162939.png`](evidence/intel-screen-20260921-162939.png) | Intel-side inspection of the copied 3:37 PM Apple-silicon transcript |

The screenshot is evidence of Intel access to the copied transcript, not of a
fresh Intel run. The raw recordings and screenshot are preserved evidence and
are not relicensed by the repository's top-level Apache license; see
[`LICENSE-SCOPE.md`](../../LICENSE-SCOPE.md).

## Reproduce the byte inspection

From the repository root:

```sh
shasum -a 256 -c investigations/2026-09-21-pre-control-and-intel/EVIDENCE.sha256
python3 tools/inspect_typescript.py \
  evidence/transcripts/Blu-Offline-20260921-141327.typescript
python3 tools/inspect_typescript.py \
  evidence/transcripts/Blu-Offline-20260921-141944.typescript
```
