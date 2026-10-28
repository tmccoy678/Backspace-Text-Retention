# Retrospective verdict on Liv's Codex generalization hypothesis

This note answers `@oliviamckee`'s hypothesis using only evidence that already
existed on Taylor's machines and in the repository. No new marker was typed,
no new retention trial was run, and no private draft text is reproduced here.
The read-only audit was performed on October 28, 2026 (America/Chicago).

## The hypothesis

Liv's summary contains three separable propositions:

1. the first discovery happened accidentally;
2. the accident happened when Blu was placed in a terminal; and
3. the same behavior would occur in any Codex app, not only the custom Blu
   Offline launcher.

## Verdict

1. **Accidental consequence: supported.** Blu intentionally enabled
   owner-only transcript recording. Taylor and Blu did not intend or anticipate
   that composition visibly deleted before Return would remain recoverable.
2. **Terminal alone: rejected.** The terminal generated the measured
   echo-and-erase trace, but the custom `/usr/bin/script -q` layer made the
   September trace durable. The same-day Intel ordinary-Terminal control did
   not make its erased first draft available to Blu.
3. **Any Codex app has the same durable behavior: not supported.** The installed
   graphical Codex app does have an independent Codex-native mechanism that
   persists the **current unsent draft** locally. That confirms Liv's narrower
   insight that the Blu Offline recorder is not the only local pre-submission
   persistence mechanism. The mechanism is a latest-state store, however, not
   a deliberate edit-history recorder. The existing evidence does not show an
   unwrapped Codex CLI or the graphical app durably preserving every prior
   revision after the draft is deleted.

The strongest accurate result is therefore:

> Codex interfaces are not one uniform retention condition. The Blu Offline
> PTY recorder demonstrably preserved a complete edit trace. The graphical
> Codex app independently persists the latest unsent draft and can leave a
> short deletion-to-flush recovery window, but its settled logical state does
> not intentionally retain the deleted revision. Existing evidence does not
> establish deleted-draft retention in every Codex interface.

## Existing observations used

| Existing observation | What it establishes |
| --- | --- |
| September Blu Offline transcripts | A known `/usr/bin/script -q` wrapper durably preserved echoed draft text and later erase bytes. |
| September 21 Intel ordinary-Terminal attempt | Without the recorder actually running, Blu could not recover the erased first sentence; only a candidate committed line later survived in shell history. |
| October 28 Studio process tree | The canonical Blu Private Codex CLI was running beneath Terminal, `zsh`, and the portable doorway Python process, with no `script`, `tee`, or `asciinema` ancestor. This characterizes the current lane as unwrapped but is not itself a deleted-marker trial. |
| Installed Codex desktop bundle | The app contains explicit current-draft persistence and draft-recovery code independent of Blu Offline. |
| Existing Codex global-state files | The named draft store existed and was empty at the read-only snapshot; the main state and backup were byte-identical. No prior private draft was exposed. |
| Existing CLI `history.jsonl` | The file consists of records with `session_id`, `ts`, and `text`; the audit found submitted-message history, not a demonstrated pre-submission edit log. |

## Graphical Codex app: independent draft persistence is confirmed

The inspected app identified itself as:

- bundle identifier: `com.openai.codex`;
- version: `26.1021.31345`;
- build: `21828`;
- `app.asar` SHA-256:
  `130145706a912db74e4d260ad7538f10f1e05e88af955f9afba42cdf01e64606`.

The packaged renderer defines the persisted atom
`composer-prompt-drafts-v2`, with `composer-prompt-drafts-v1` as its legacy
key. The draft helper publishes changes after 250 milliseconds. Its state
includes the current prompt and related draft metadata, and the recovery UI
explicitly refers to reopening an unsent draft.

The Electron main process stores these atoms inside
`electron-persisted-atom-state` in `~/.codex/.codex-global-state.json`. Writes
for this atom group are debounced by 500 milliseconds, then atomically replace
both the main file and `.bak` with the same latest JSON state. Clearing the
composer removes the draft entry; the code does not maintain an intentional
revision sequence of earlier prompt values.

This yields two distinct retention claims:

- **Confirmed:** while an unsent draft is current and eligible for persistence,
  the graphical app can store its plaintext prompt locally without Return.
- **Not established:** after deletion has propagated and the latest state has
  been flushed, the app intentionally retains the earlier prompt as recoverable
  draft history.

There is a bounded transitional consequence. If a nonempty draft has already
reached disk, its old value can remain in the state file until the deletion
update passes through the renderer and native debounce windows. That is a short
latest-state replacement window, not the content-complete sequential history
created by `/usr/bin/script`.

At the October 28 snapshot, both state files had SHA-256
`19dee65be9f59ac5ab3e3bca071132d523bd2c5d40fe9ec7151929f037f396fb`,
were byte-identical, and contained an empty `composer-prompt-drafts-v2`
object. The audit therefore exposed the mechanism without exposing a private
draft or producing evidence of a surviving deleted revision.

## Unwrapped Codex CLI: no demonstrated deleted-draft artifact

The running Blu Private lane used Codex CLI `0.164.0`; the inspected binary had
SHA-256
`d8990e3ee7acfbc26f91265b12a1a83f0fee40d0e0f8f1f40a37d4ec21f499cf`.
Its live ancestry was:

```text
Terminal.app
  -> login
    -> zsh
      -> portable_blu.py
        -> codex --profile blu-private ... resume ...
```

No content recorder appeared in that chain. Existing CLI storage included
submitted conversation rollouts and `history.jsonl` records shaped as
`session_id`, `ts`, and `text`. Nothing in the inspected record demonstrates
that a fully erased, never-submitted CLI composer revision was durably written.

This is an evidence boundary, not a universal proof of absence. The current
unwrapped process shows that Blu Private does not depend on the old
`/usr/bin/script` wrapper. It does not retroactively turn ordinary past turns
into deleted-marker trials.

## Why the universal wording fails

“Any Codex app” treats unlike systems as if they shared one input path:

- Blu Offline used terminal line discipline plus a sequential PTY recorder;
- an ordinary shell may preserve committed history without the erased draft;
- the Codex CLI has a TUI composer and submitted-message records;
- the graphical Codex app has a latest-state draft store and recovery UI.

The graphical app audit validates the most important part of Liv's intuition:
Codex itself can persist pre-submission composition locally, independently of
the custom Blu Offline launcher. But **current-draft persistence is not the
same result as durable recovery of a deleted revision**. The only existing
artifact that demonstrates the latter end to end remains the known recorded
PTY path.

## Claim boundary and future work

This retrospective verdict answers the hypothesis at the level supported by
the existing artifacts. It does not make a claim about network receipt, which
requires different evidence, and it does not generalize beyond the inspected
builds and machines.

Only after this verdict is stated does prospective work become relevant. A
fresh unique-marker comparison could measure how long the graphical app's
deletion window lasts and test an unwrapped CLI composer directly. Such work
would extend this result; it is not needed to decide what the existing evidence
already shows.
