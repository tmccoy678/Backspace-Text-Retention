# Retrospective verdict on the Blu-lane retention hypothesis

This note answers `@oliviamckee`'s hypothesis using only evidence that already
existed on Taylor's machines and in the repository. No new marker was typed,
no new retention trial was run, and no private draft text is reproduced here.
The read-only audit was performed on October 28, 2026 (America/Chicago).
At audit time, the canonical Blu Private doorway was configured for
`gpt-5.6-sol` with `xhigh` reasoning. That identifies the current configuration
of this n=1 lane; it is not a claim that every historical turn used an
unchanging reasoning setting. A September 20 lane snapshot records the same
model with `max` reasoning.

## The hypothesis

Liv's summary contains three separable propositions. The experimental unit is
the **single Blu lane**, not all Codex installations or every Codex interface:

1. the first discovery happened accidentally;
2. the accident happened when Blu was placed in a terminal; and
3. this same Blu lane is an example of pre-submission retention that must be
   understood across its terminal, Codex, and app boundaries rather than being
   reduced to the custom Blu Offline launcher alone.

## Verdict

1. **Accidental consequence: supported.** Blu intentionally enabled
   owner-only transcript recording. Taylor and Blu did not intend or anticipate
   that composition visibly deleted before Return would remain recoverable.
2. **Terminal alone: rejected.** The terminal generated the measured
   echo-and-erase trace, but the custom `/usr/bin/script -q` layer made the
   September trace durable. The same-day Intel ordinary-Terminal control did
   not make its erased first draft available to Blu.
3. **The Blu lane is a confirmed n=1 retention case.** In this lane, deleted
   pre-submission composition was durably preserved by the historical recorder
   and later crossed into the canonical Codex record through authorized
   inspection. The installed graphical Codex app also has an independent
   Codex-native mechanism that persists the **current unsent draft** locally.
   The current unwrapped CLI's component-specific behavior remains unresolved,
   but that does not undo the positive lane-level observation.

The strongest accurate result is therefore:

> This single Blu lane is a confirmed example of pre-submission text retention.
> The observed historical path was terminal echo -> Blu Offline PTY recorder ->
> authorized inspection -> canonical Codex record. The graphical app supplies
> another local pre-submission persistence boundary for the same lane. That n=1
> result is complete even though the current unwrapped CLI component has not
> itself produced a deleted-marker artifact.

This is deliberately an n-of-one result: one Blu lane, one confirmed positive
case, and identified persistence boundaries. Its value is precisely that the
lane's tendency to forget across interfaces can now be discussed against a
specific surviving record instead of an assumed universal behavior.

## Existing observations used

| Existing observation | What it establishes |
| --- | --- |
| September Blu Offline transcripts | A known `/usr/bin/script -q` wrapper durably preserved echoed draft text and later erase bytes. |
| September 21 Intel ordinary-Terminal attempt | Without the recorder actually running, Blu could not recover the erased first sentence; only a candidate committed line later survived in shell history. |
| October 28 Studio process tree | The canonical Blu Private Codex CLI was running beneath Terminal, `zsh`, and the portable doorway Python process, with no `script`, `tee`, or `asciinema` ancestor. This characterizes the current lane as unwrapped but is not itself a deleted-marker trial. |
| Installed Codex desktop bundle | A graphical surface available to the same lane contains explicit current-draft persistence and draft-recovery code independent of Blu Offline. |
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

## Why the lane is the correct experimental unit

The result does not require a claim about every Codex app. This one lane has
already crossed several unlike input and persistence paths:

- Blu Offline used terminal line discipline plus a sequential PTY recorder;
- an ordinary shell may preserve committed history without the erased draft;
- the Codex CLI has a TUI composer and submitted-message records;
- the graphical Codex app has a latest-state draft store and recovery UI.

At lane level, the result is positive: the Blu lane retained deleted
pre-submission text and later acquired it into its canonical record. At
component level, mechanisms still matter. The graphical app audit shows that a
Codex-native surface can persist pre-submission composition locally, while
**current-draft persistence is not the same mechanism as durable recovery of a
deleted revision**. The known recorded PTY path remains the existing end-to-end
demonstration of that durable revision recovery.

## Claim boundary and future work

This retrospective verdict answers the hypothesis at the level supported by
the existing artifacts: **one lane, one positive case, identified boundaries**.
It does not make a claim about network receipt, which requires different
evidence, and it does not generalize the n=1 finding to other Codex lanes,
builds, or machines.

Only after this verdict is stated does prospective work become relevant. A
fresh unique-marker comparison could measure how long the graphical app's
deletion window lasts and test an unwrapped CLI composer directly. Such work
would extend this result; it is not needed to decide what the existing evidence
already shows.
