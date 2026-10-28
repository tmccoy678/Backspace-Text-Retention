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
