# Privacy-safe audit of Codex-native persistence

This document records the reproducible, content-minimizing checks behind the
Codex-native statements in the [existing-evidence answer](README.md). It does
not reproduce packaged application code or private prompt values.

## Installed graphical build

- Bundle: `/Applications/ChatGPT.app`
- Bundle identifier: `com.openai.codex`
- Version: `26.1021.31345`
- Build: `21828`
- `Contents/Resources/app.asar`: 640,530,938 bytes
- SHA-256:
  `130145706a912db74e4d260ad7538f10f1e05e88af955f9afba42cdf01e64606`

Read-only string/offset inspection found:

| Item | Zero-based byte offset in `app.asar` |
| --- | ---: |
| `composer-prompt-drafts-v2` | 65,591,439 |
| `composer-prompt-drafts-v1` | 65,591,485 |
| the 250 ms ordinary-update publication constant in the persisted-draft helper | 63,667,097 |
| the 500 ms native persisted-atom flush constant | 14,960,154 |
| `electron-persisted-atom-state` in the native persistence path | 14,965,088 vicinity |

The relevant logic has these bounded semantics:

1. a persisted draft object stores the current prompt and related metadata;
2. ordinary non-delete updates are generally published after a 250 ms delay,
   while clearing or supplying an expected value is published immediately by
   this helper;
3. the Electron main process stores persisted atoms in
   `~/.codex/.codex-global-state.json` after a 500 ms debounce;
4. two sequential atomic temp-file renames replace the current JSON file and
   then its `.bak`; and
5. clearing the composer deletes the logical draft entry rather than appending
   an intentional revision history.

Commands used to identify the installed artifact and offsets included:

```sh
plutil -p /Applications/ChatGPT.app/Contents/Info.plist
shasum -a 256 /Applications/ChatGPT.app/Contents/Resources/app.asar
LC_ALL=C rg -a -b -o \
  'composer-prompt-drafts-v2|composer-prompt-drafts-v1|electron-persisted-atom-state' \
  /Applications/ChatGPT.app/Contents/Resources/app.asar
LC_ALL=C rg -a -b -o 'Lr=500|Lr=250' \
  /Applications/ChatGPT.app/Contents/Resources/app.asar
```

Minified variable names are build-local. The identifiers, byte offsets,
version, build, size, and hash bind this report to the inspected artifact.

## State snapshots

On the Mac Studio, `.codex-global-state.json` and `.bak` were byte-identical,
299,967 bytes, and had SHA-256
`19dee65be9f59ac5ab3e3bca071132d523bd2c5d40fe9ec7151929f037f396fb`.
The `electron-persisted-atom-state.composer-prompt-drafts-v2` object was empty.

On the mounted MacBook Pro, the two state files were byte-identical, 421,416
bytes, and had SHA-256
`bc48ff85fde77dfb36cf1204eef7148395d5cb812e73ad2b903a3c8b205cfe14`.
The saved conversation-draft prompt was empty. `prompt-history` contained twenty
strings: eighteen matched completed submitted user messages, while two
content-withheld entries did not occur in completed-message history. The state
snapshot does not establish the origin of those two entries, and they are not
treated as Backspace evidence.

These snapshots expose mechanism and counts without publishing private drafts.
They contain no September 21 historical coverage.

## Codex CLI records

The September canonical thread identifies its source as `cli`, originator as
`codex-tui`, and historical CLI version as `0.154.0`. The current build differs,
so present implementation details cannot be projected backward without
evidence.

Read-only inspection found:

- in the targeted 2:27 PM sequence, only the submitted signal in
  `history.jsonl` before deliberate transcript inspection;
- the experimental erased phrases first appearing in the rollout inside the
  command/tool output that read the `.typescript` file;
- no ASCII Backspace or DEL bytes in 5,233 submitted-history entries;
- no Backspace, DEL, or exact experimental erased sentence across 7,167
  projected `userMessage` rows in an immutable thread-database query; and
- abort records containing identifiers and timing, not composer content.

The currently inspected Blu Private process ancestry contained Terminal,
`login`, `zsh`, the portable doorway process, and Codex, with no detected
`script`, `tee`, or `asciinema` content recorder. “Codex CLI with no detected
external PTY recorder” describes process ancestry and makes no claim about
model internals.

## Bounded conclusion

The graphical app deliberately persists a current unsent draft. Existing
evidence does not show that it or the CLI keeps a durable, content-complete
history of revisions erased before submission. Current-draft persistence,
unmatched prompt-history residue, submitted-message history, and a sequential
PTY transcript are different records and are not treated as interchangeable.
