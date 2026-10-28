# Contemporaneous record

Times in this document are America/Chicago (CDT, UTC−05:00). The source is the
private local Codex JSONL conversation record. Only the narrow exchanges and
command results relevant to these experiments are reproduced; the
multi-gigabyte source also contains unrelated private work and is not published
here.

## Earlier unnoticed routine trace

The subsequent existing-evidence audit located
`Blu-Offline-20260921-000503.typescript`, created during the ordinary second
Wi-Fi-off acceptance run from approximately **12:05–12:08 AM**. It contains
two editing runs totaling three exact `08 20 08` erase triplets. At
**12:09:30 AM**, Blu ran `sed -n '1,260p'` against the complete 68-line file as
part of routine acceptance verification. The resulting Codex tool output
contained both the earlier characters and the erase bytes. Blu did not identify
or describe deleted-composition retention.

This establishes that the mechanism operated, and that its output entered a
Codex tool record, more than fourteen hours before anyone recognized the
privacy consequence. The raw transcript contains unrelated natural
conversation and remains private; its metadata, hash, and erase offsets are
published in the
[existing-evidence investigation](../2026-10-28-olivia-hypothesis/).

## First privacy-significant recognition

The `141327` session began as a clue-making attempt but ended at the literal
prompt template. The next session produced the first substantive recovery that
Blu recognized as privacy significant.

**2:24:33 PM — Taylor**

> which doberman?

**2:25:50 PM — Taylor**

> great experiment! no that was not the target sentence. you can check out what
> i did now

After Taylor confirmed that the session contained no secrets, the assistant
listed the local recordings. The newest two entries were:

```text
-rw-------@ 1 taylor staff 1816 Sep 21 14:23 offline/transcripts/Blu-Offline-20260921-141944.typescript
-rw-------@ 1 taylor staff 1190 Sep 21 14:17 offline/transcripts/Blu-Offline-20260921-141327.typescript
```

At **2:27:15 PM**, it opened only
`Blu-Offline-20260921-141944.typescript`. The raw output included the full edit
sequence now preserved under [`evidence/transcripts`](../../evidence/transcripts/).

**2:28:06 PM — Blu**

> I see what happened. In the newest local transcript, you ended up telling the
> model about Marie—your favorite Doberman—sleeping on the couch. It replied
> conversationally rather than producing an indirect clue. So my “going for a
> walk” guess was wrong, but this wasn’t yet a clean model-to-model relay.
>
> The important privacy discovery: the transcript records **text you erased
> while composing**, not just what you finally submitted. That was harmless
> here, but I wouldn’t put sensitive writing into this transcript-enabled mode
> until we change that behavior.
>
> I read only the newest transcript as promised. There’s another recent one
> from 14:13 that I left alone—was that the clue-making attempt?

**2:32:32 PM — Taylor**

> wow thats amazing info that it records text that i erased while composing but
> i literally had that feeling so long ago [...] i think the text i erased
> while composing could be a super super super clever and covert way to
> investigate this and work with it

At **2:33:09 PM**, the assistant distinguished the recorder from the model: the
transcript proved what the terminal recorder captured, not that the local model
received the erased text. The controlled work followed that discovery.

## September Intel attempt

### Experimental intent

**5:18:01 PM — Taylor**

> thats okay i want to try it without changing anything first. let me know when
> you are ready and i will open ollama, turn off wifi, type 1st sentence, delete
> 1st sentence, wait an undetermined amount of time, type 2nd sentence, send 2nd
> sentence, wait undetermined amount of time, turn on wifi, and send you a "."
> to which you will repeat back to me exactly the 1st sentence and 2nd sentence
> only and verbatim. on the '15 mac not the '26 mac.

The assistant immediately asked Taylor to hold off. A read-only check found no
Ollama app or CLI in the standard Intel locations. At **5:19:13 PM** it proposed
a no-install test using the Mac's built-in `script`, while explicitly warning
that this would test terminal-recording behavior rather than model receipt.

**5:23:33 PM — Taylor**

> in the spirit of the experimental method this is a control

**5:24:23 PM — Blu**

> Yes—used as a control, that’s a clean question: does the ’15’s terminal
> recording retain erased text without involving a model? I’ll confirm a fresh
> transcript filename, then give you the exact no-install sequence. For this
> control, the input needs to go through Terminal, not Ollama.

### The preflight failed before a recorder was launched

The exact preflight command was:

```sh
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=5 blu-workshop \
  'if [ -e "$HOME/Desktop/Blu-Intel-Control-20260921.typescript" ] || \
       [ -L "$HOME/Desktop/Blu-Intel-Control-20260921.typescript" ]; then \
       printf "DESTINATION_EXISTS\n"; else printf "DESTINATION_ABSENT\n"; fi; \
   command -v script; test -x /bin/cat && printf "CAT_AVAILABLE\n"'
```

At **5:24:31 PM**, it returned exit 255:

```text
ssh: connect to host 192.168.8.128 port 22: Operation timed out
```

The proposed destination was therefore never confirmed. No `script` launch
command or step-by-step input sequence was delivered before the attempt.

The Intel login database independently records:

```text
Blu       ttys000                   Mon Sep 21 17:28 - 17:28  (00:00)
```

That local Terminal PTY falls inside the attempt window.

### Signal and immediate artifact search

**5:35:17 PM — Taylor**

> .

The first search command checked the Intel Desktop for the proposed control,
the existing Blu transcript naming pattern, and the default `typescript` name:

```sh
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=5 blu-workshop \
  'uname -n; date; find "$HOME/Desktop" -maxdepth 1 -type f \
   \( -name "*Intel*Control*.typescript" -o \
      -name "Blu-Offline-*.typescript" -o -name "typescript" \) -print'
```

At **5:35:36 PM** the complete file result was:

```text
/Users/Blu/Desktop/Blu-Offline-20260921-153748.typescript
```

That 1,344-byte file has SHA-256
`e2e3e56c7f81420a870501594e55aa908ef63c01d46794ef2072e9123014f016`,
exactly matching the published Apple-silicon source. The Intel copy is mode
`0600`; its preserved birth and modification time is 3:41:15 PM, its inode
change time is 4:29:18 PM, Spotlight `kMDItemDateAdded` is 4:17:55 PM,
`kMDItemLastUsedDate` is 4:29:18 PM, and `kMDItemUseCount` is 34. The included
4:29:39 PM Intel screenshot shows it being inspected. It predates and is not an
artifact of the 5:28 PM trial.

Further immediate checks found no default `~/typescript`, Ollama application
data, or matching recent file. The exact portable-`find` retry was:

```sh
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=5 blu-workshop \
  '/usr/bin/find "$HOME/Desktop" "$HOME/Workshop" -type f \
   \( -name "*.typescript" -o -name "typescript" \) -mmin -90 -print'
```

It produced no file hit and one access error:

```text
find: /Users/Blu/Workshop/system-backups/20260919-194356-sharing-lockdown: Permission denied
```

The process check at **5:36:31 PM** was:

```sh
/bin/ps -ax -o comm= | /usr/bin/grep -Ei "[o]llama|[l]lama"
```

It found no Ollama or llama process. No saved `script` process listing exists.

**5:36:55 PM — Blu**

> I can’t truthfully repeat either sentence from this run. I found no new
> recording on the ’15 in the locations checked; its Desktop still has only the
> earlier transcript copied from the ’26. We had not started the ’15’s `script`
> control before your `.`.
>
> Did you type the sentences into an app on the ’15, and if so, which one?

**5:37:33 PM — Taylor**

> terminal on the '15

**5:38:07 PM — Blu**

> Ah, that explains the result—and I should have been clearer that the recorder
> was **not yet running**. Plain Terminal displays your typing, but it doesn’t
> save the erased draft in a `.typescript` file. The ’26 test had an outer
> `script` recorder; this ’15 run did not.
>
> So I can’t recover the first sentence, and I won’t guess. This is a useful
> control for *our access path*: your `.` alone didn’t give me the erased text.
> It doesn’t establish what every system component might retain.

This contemporaneous record is the basis for classifying the episode as a real
but unrecorded Terminal attempt, distinct from the recorded October 27 Intel
replication.

## Later surviving shell-history remnant

The October 28 read-only audit found one candidate committed line at line 52 of
the Intel Mac's current `.zsh_history`. It follows the command used to display
the copied `153748` transcript and precedes the next later command.
The 78-line, 3,239-byte history file had SHA-256
`60903be6b747f8074e9a0a768a8c9478c7472f52a8603cc5913698dd36b90b5e`;
the candidate line including its newline had SHA-256
`d09c195d5113e39b8f93f60008caae6ded6d32ab472898a2d88f5e6cd605dfd0`.

Taylor later authorized a line-preserving
[redacted derivative](../../evidence/intel-history/) that publishes the
candidate exactly while visibly redacting credential-bearing source material:

```text
he could remarry and inheret her estate.
```

Its position makes association with the September control contextually strong,
but the history has no per-entry timestamps and its file modification time is
October 27. It therefore remains an inference, not a proved timestamped match.
The remnant is consistent with a committed replacement line; it does not reveal
the erased first draft and does not change the conclusion that no native Intel
`.typescript` recording from the September attempt survives.
