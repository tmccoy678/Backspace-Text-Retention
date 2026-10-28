# Byte-preserved terminal transcripts

Files in this directory are exact byte copies. ANSI control sequences, carriage
returns, terminal echo, and erasure bytes are source evidence rather than
formatting defects. Use [`../../tools/inspect_typescript.py`](../../tools/inspect_typescript.py)
to render a read-only representation.

## Earliest accidental sessions

- `Blu-Offline-20260921-141327.typescript` is the first surviving Backspace
  Gate session. Taylor did not ask anyone to record it; the pre-existing Blu
  Offline launcher invoked `/usr/bin/script` automatically. Taylor entered the
  harmless template `My harmless target sentence is: [WRITE YOUR SENTENCE
  HERE].`, edited and erased it, and exited without submitting a replacement.
- `Blu-Offline-20260921-141944.typescript` is the second early session. It
  preserves Taylor revising several nonsensitive Doberman phrases before
  submitting a final sentence about her favorite Doberman sleeping on the
  couch.

Taylor explicitly authorized public release of both raw transcripts on October
28, 2026. Neither file contains credentials or private identifiers. Their exact
hashes are recorded in the repository-wide [`MANIFEST.sha256`](../../MANIFEST.sha256).

## Structured and diagnostic sessions

- `Blu-Offline-20260921-153748.typescript` is the later structured foundation
  recording containing the `marie` / `stanley` sequence.
- `Blu-Offline-CanonicalControl-20260921-152512.typescript` and
  `Blu-Offline-RawTest-20260921-152605.typescript` preserve the matched
  canonical/raw diagnostic.

The earliest accidental observation must not be replaced in the chronology by
the later structured recording.
