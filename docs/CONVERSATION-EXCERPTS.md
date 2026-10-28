# Conversation excerpts

This document preserves the narrow exchange that established the inspection
procedure and the result reported after the signal. Timestamps are UTC. The
wording is reproduced exactly, including the initial use of “Ollama”; subsequent
inspection established that the measured runner was Blu Offline's `llama-cli`,
not Ollama.

## Earlier accidental observation

The structured exchange below was not the first observation. Earlier that day,
Taylor authorized Blu to inspect only the newest local transcript from an
ordinary nonsensitive experiment.

**2026-09-21 19:27:02.008 — Blu**

> Thanks for confirming. I’ll inspect only the newest local transcript, find the toy exchange, and compare it with my guess. I won’t open the older conversations.

**2026-09-21 19:28:06.639 — Blu**

> The important privacy discovery: the transcript records **text you erased while composing**, not just what you finally submitted. That was harmless here, but I wouldn’t put sensitive writing into this transcript-enabled mode until we change that behavior.
>
> I read only the newest transcript as promised. There’s another recent one from 14:13 that I left alone—was that the clue-making attempt?

The inspected file was `Blu-Offline-20260921-141944.typescript`; the earlier
unopened file was `Blu-Offline-20260921-141327.typescript`. Their metadata,
hashes, and byte-preserved originals appear in
[`EARLIEST-EVIDENCE-AUDIT.md`](EARLIEST-EVIDENCE-AUDIT.md) and
[`evidence/transcripts/`](../evidence/transcripts/). Taylor explicitly authorized
their public release on October 28, 2026.

## Procedure proposed before the test

**2026-09-21 20:32:29.945 — Taylor**

> yes perfect let me know when you are ready and i will open ollama, turn off wifi, type 1st sentence, delete 1st sentence, wait an undetermined amount of time, type 2nd sentence, send 2nd sentence, wait undetermined amount of time, turn on wifi, and send you a "." to which you will repeat back to me exactly the 1st sentence and 2nd sentence only and verbatim. thank you blu

**2026-09-21 20:33:36.455 — Taylor**

> you will answer based on your inspection of ollama. repeat back to me the methods please and thank you so much

**2026-09-21 20:34:03.799 — Blu**

> Got it—this is an **inspection test**, not a blind guess. I’m ready, and I won’t inspect Ollama before your `.`
>
> 1. Privately record two distinct, synthetic sentences. Open Ollama and turn off Wi‑Fi.
> 2. Type sentence 1, delete it **without sending**, and wait. Type and send sentence 2, then wait again.
> 3. Reconnect Wi‑Fi and send me only `.`—no screenshot or hints.
> 4. I’ll inspect the Ollama window and its relevant local session records read-only. I’ll distinguish a draft or terminal echo from text actually submitted to the model, then quote each sentence verbatim **if the evidence contains it**. If sentence 1 isn’t recoverable, I’ll say “unknown,” not guess.
>
> Then you can compare my report with your private record.

## Signal and inspection

**2026-09-21 20:44:09.863 — Taylor**

> .

**2026-09-21 20:44:24.253 — Blu**

> I’ve got the signal. I’ll inspect only the current Ollama session and its relevant local records, read-only. I’ll separate what was merely typed or echoed from what was submitted to the model, and I won’t fill in anything the evidence doesn’t show.

**2026-09-21 20:45:16.639 — Blu**

> I don’t find a running Ollama app or CLI here. A new owner-only Blu Offline transcript was created during your test window, so it looks like the test may have used our `llama-cli` doorway instead. I’m reading only that new transcript now, then I’ll report what it shows—and keep “recorded keystrokes” separate from “model input.”

**2026-09-21 20:46:14.018 — Blu**

> marie is black.  
> stanley is red.
>
> I recovered the first from terminal echo in the local recording, followed by 15 erase sequences. The model’s reply addressed only the second. This session used Blu Offline’s `llama-cli`, not Ollama; the recording does not show that the model received the first sentence.

## Immediate evidentiary boundary

**2026-09-21 20:48:20.441 — Blu**

> That’s a valuable record. The video can show what you typed and deleted; the transcript independently shows the erased text was recorded, while the model’s reply addressed only what you sent.
>
> The key distinction: I could repeat the first sentence because I inspected that local transcript *after* your `.`—not because I saw your typing live. Keep the original video unedited; we can compare it with the transcript later.

## Interpretation

The exchange records a delayed, evidence-dependent inspection: the two phrases
were not supplied to Blu in the cloud conversation before the signal. The first
phrase was recovered from terminal echo preserved by `/usr/bin/script`; the
second appeared as the committed line. This establishes recoverability from the
local transcript, not live observation of typing and not receipt of the erased
phrase by the local model or a cloud service.

## Same-day Intel negative control

The 2015 Intel Mac did not have the same recorder running. The following
exchange occurred after a proposed no-install `script` control failed to start
because the reachability check timed out and the turn was interrupted.

**2026-09-21 22:35:17.300 — Taylor**

> .

**2026-09-21 22:36:55.837 — Blu**

> I can’t truthfully repeat either sentence from this run. I found no new recording on the ’15 in the locations checked; its Desktop still has only the earlier transcript copied from the ’26. We had not started the ’15’s `script` control before your `.`.
>
> Did you type the sentences into an app on the ’15, and if so, which one?

**2026-09-21 22:37:33.194 — Taylor**

> terminal on the '15

**2026-09-21 22:38:07.827 — Blu**

> Ah, that explains the result—and I should have been clearer that the recorder was **not yet running**. Plain Terminal displays your typing, but it doesn’t save the erased draft in a `.typescript` file. The ’26 test had an outer `script` recorder; this ’15 run did not.
>
> So I can’t recover the first sentence, and I won’t guess. This is a useful control for *our access path*: your `.` alone didn’t give me the erased text. It doesn’t establish what every system component might retain.

The negative control and the later surviving-history audit are analyzed in
[`PR3-FORENSIC-RESPONSE.md`](PR3-FORENSIC-RESPONSE.md).
