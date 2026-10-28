# First ordinary-shell attempt audit

## Scope

This record concerns the **first** October 27, 2026 attempt on the 2015 Intel
Mac. It predates the controlled recorded-PTY replication in this directory.
Taylor typed and erased a nonsensitive hidden phrase in an already-open ordinary
Terminal zsh session, then committed a different line. The controlled
`/usr/bin/script` rerun was performed later.

## Surviving source artifact

The Intel Mac retained `/Users/Blu/Documents/Terminal Saved Output.txt`. An exact
byte-preserved copy is published as
[`evidence/intel-first-ordinary-shell-terminal-saved-output.txt`](evidence/intel-first-ordinary-shell-terminal-saved-output.txt).

- Creation and modification time: 2026-10-27 10:49:15 PM CDT
- Size: 128 bytes
- Original mode: `-rw-r--r--`
- SHA-256: `a90e2c11eb1e46f275f8dd5ab27ea7ae0aaa2265ef068f19b58004766b2492b8`
- Type: ASCII text
- Extended text encoding attribute: `utf-8;134217984`

The file contains the session login line, the committed replacement command,
the resulting zsh error, and the next prompt. It does not contain the deleted
phrase and cannot reconstruct it.

## Process and terminal state

A later read-only inspection found the original Terminal and zsh session still
open:

```text
16620 Tue Oct 27 22:48:19 2026  ??       S   Terminal.app
16622 Tue Oct 27 22:48:20 2026  ttys000  S+  -zsh
/dev/ttys000 modified 2026-10-27 22:49:04 CDT
```

No `script` process appeared in that surviving process state. This observation
was made after the input event; it is not a process snapshot taken at the exact
moment of typing.

## Search performed

The read-only audit checked:

- `/Users/Blu` for `*.typescript`, names containing `backspace`, names
  containing `intel*experiment`, and terminal-transcript names;
- the 10:40–11:00 PM filesystem modification window;
- `~/.zsh_history` and `~/.zsh_sessions` for `script`, `typescript`, and the
  committed command;
- the still-open Terminal/zsh process tree; and
- the canonical private conversation record for the contemporaneous inspection.

Results:

- no `.typescript` or other recorder output attributable to the first attempt
  was found;
- the active session's `.historynew` file was zero bytes and the committed
  command was not present in persisted zsh history;
- the only relevant human-created artifact in the event window was the saved
  Terminal output published here; and
- controlled replication artifacts begin later and are separately named.

The full filesystem window also contained unrelated operating-system databases
and caches. Those were inspected only to classify the search and are excluded
from publication.

## Claim boundary

The evidence does **not** justify the categorical inference that a recorder
could not have existed. It supports the narrower statement that the operator
reported using an ordinary shell outside the wrapper, no recorder was observed
in the surviving process state or history, and no first-attempt recording
artifact was found in the inspected locations. The saved output proves that the
ordinary-shell interaction occurred but does not preserve the abandoned draft.
