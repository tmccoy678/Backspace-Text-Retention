# Read-only search coverage and limitations

The search was performed on October 28, 2026 and was intended to be read-only
on the MacBook Pro, Mac Studio, and 2015 Intel Mac evidence sources. One
auxiliary SQLite coordination-file timestamp side effect is disclosed below.
Exact-content copies of the two pre-control recordings were compared with the
canonical files published concurrently under `evidence/transcripts`. One Intel
screenshot was copied into the temporary publication workspace and added to
this investigation folder.

## 2026 MacBook Pro and Mac Studio

The following were checked:

- the complete local Codex JSONL exchange covering the first observation and
  the September Intel attempt;
- the MacBook's Desktop, Documents, Downloads, Movies, Pictures,
  `Blu-Workbench`, `Agent-Work`, screenshot inbox, and shell history;
- September 21 screenshots and three surviving videos, all of which predate the
  5:35 PM Intel signal;
- the migrated Studio transcript bundle under
  `Blu-Workbench/offline/transcripts`;
- exact filenames, likely transcript names, and `script` invocations;
- the mounted Seagate preservation volume for matching transcript and media
  names; and
- Git history, current repository content, releases, and public discussion.

The two pre-control recordings were found in the migrated Studio bundle. The
MacBook's migration record states that the complete bundle was compared
byte-for-byte before the MacBook copy was removed. The current Studio files
retain the September birth and modification times and have an October 26 change
time corresponding to that migration.

The MacBook shell history has no September 21 Intel `script` invocation. Its
only relevant later line belongs to the separate October 27 replication. No
MacBook screenshot or video from the 5:18–5:38 PM Intel-attempt window was
found. The Photos library was not exhaustively queried, so this is not an
absolute statement about every app-managed media asset.

## 2015 Intel Mac

The accessible Intel host identifies as `x86_64`, macOS 12.7.6, build
21H1320. The following readable areas and records were checked:

- all visible `/Users` trees for `.typescript`, default `typescript`,
  `Blu-Offline`, Intel-control, backspace, and script-related names;
- Desktop, Documents, Downloads, Movies, Pictures, Workshop, Blu-History,
  Trash, `/private/tmp`, and `/var/tmp`;
- the complete retained `.zsh_history`, all `.zsh_sessions`, and the absence of
  `.bash_history`;
- command and shell launchers for `/usr/bin/script`, `script -q`, `llama-cli`,
  and `Blu-Offline`;
- Terminal saved state and preferences, recent-document metadata, Desktop
  `.DS_Store`, and Spotlight filename/phrase results;
- files created or modified during the 5:18–5:45 PM target window;
- local login records, unified logs, APFS snapshots, and mounted volumes; and
- screenshots and videos in and around the target window.

Only two `.typescript` files were visible anywhere under `/Users`: the copied
September 21 Apple-silicon transcript and the separately published October 27
Intel replication. No September Intel launcher, native transcript, default
`typescript`, saved process list, or experiment log was found. No screenshot or
video from the 5:18–5:38 PM attempt window was found; the included 4:29 PM
screenshot documents inspection of the earlier copied transcript. The
exact-window filesystem results were routine application metadata, not
experiment artifacts.

The retained shell history contains no September command that launched
`script` or `llama-cli`. It does contain one candidate committed line at line
52, between the command used to display the copied `153748` transcript and the
next later command. The history file was 78 lines and 3,239 bytes at inspection,
with SHA-256
`60903be6b747f8074e9a0a768a8c9478c7472f52a8603cc5913698dd36b90b5e`.
The candidate line including its newline has SHA-256
`d09c195d5113e39b8f93f60008caae6ded6d32ab472898a2d88f5e6cd605dfd0`.
Taylor later authorized publication of a line-preserving
[redacted derivative](../../evidence/intel-history/). It exposes the exact
candidate, `he could remarry and inheret her estate.`, while visibly replacing
credentials, password-like material, and the private conversation identifier;
the raw source remains private. Position makes its association with the
September control contextually strong, but the lack of per-entry timestamps and
the history file's October 27 modification time prevent proof. It is consistent
with preservation of the committed replacement line and does not recover the
erased first draft.

History evidence is corroborating rather than conclusive because
`HIST_IGNORE_SPACE` was enabled and commands can be omitted or later aged out.
Unified logs for the window have been pruned, no local APFS snapshot remains,
and no external volume was mounted on the Intel host.

## Access and forensic limits

- `/Users/Blu/Workshop/system-backups/20260919-194356-sharing-lockdown` returned
  permission denied during the contemporaneous 5:36 PM search. Its date
  predates the experiment, and the broader October search found no reference to
  a September recording in visible metadata.
- Root-only `/var/audit` and `.fseventsd` were not accessible.
- The search did not attempt deleted-file recovery or change machine security
  settings.
- A transcript could theoretically have existed and later been deleted. No
  surviving artifact or metadata found in this search supports that scenario.

## Read-only-method transparency

One `sqlite3 -readonly` query on the Intel Mac opened
`/Users/Blu/.codex/logs_2.sqlite`. The database file and its WAL remained
unchanged, but SQLite updated the modification time of the auxiliary
`logs_2.sqlite-shm` coordination file. Non-immutable SQLite access stopped
immediately. No database content, transcript, shell history, screenshot, or
other evidentiary artifact was changed.

Subject to those limits, the positive and negative evidence converge: the
September Intel attempt occurred in Terminal, but it preceded activation of a
recorder and left no surviving native transcript.
