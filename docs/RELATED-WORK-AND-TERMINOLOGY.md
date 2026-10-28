# Related work and terminology

**Review date:** October 28, 2026

**Scope:** Narrative review of the closest terminal-recording, writing-process,
privacy, deletion, and secure-storage literature located for this repository.

This document defines the terms used throughout the repository and places the
measured result against prior work. It is not a systematic review and does not
establish patentability or historical priority. The articles discussed below
were read in full unless an entry is explicitly identified as a standard,
manual, or source-code reference.

## One editing action, several different layers

The words **Backspace**, **Delete**, and **erase** are often treated as
synonyms, but they can name different things: a physical key, an encoded input
byte, a terminal line-discipline function, a display instruction, a change to
application-visible input, or destruction of stored data. Claims in this
repository should identify the layer being described.

| Term | Definition in this repository | What it does **not** establish |
| --- | --- | --- |
| **Physical Backspace key** | A keyboard key or user action conventionally used to edit the character before the insertion point. Its label and emitted byte vary by keyboard, operating system, terminal, and configuration. | It does not identify a particular byte or prove that stored data was destroyed. |
| **Physical Delete key** | A key physically labeled Delete. On the Apple keyboard used in the foundation case, the principal Delete key performed a backward-edit action. Other keyboards and interfaces may use Delete for a forward-edit action. | The key label alone does not identify ASCII `DEL`, POSIX `ERASE`, or the direction of editing. |
| **ASCII `BS` (`0x08`)** | The Backspace format effector. RFC 20 defines it as moving the active printing position backward by one position (Cerf, 1969). ECMA-48 likewise defines `BS` as active-position movement (ECMA International, 1991, Section 8.3.5). | `BS` does not itself mean secure deletion, destruction of a stored byte, or removal from a log. |
| **ASCII `DEL` (`0x7f`)** | A different ASCII code, historically intended to obliterate an unwanted paper-tape position by punching all of its bits (Cerf, 1969). A terminal may configure this byte to invoke the POSIX `ERASE` function. | `DEL` is not ASCII `BS`, and receipt of `0x7f` does not universally imply any one editing behavior. |
| **POSIX `ERASE` / `VERASE`** | A configurable special input character. With canonical processing enabled, receipt of the configured `ERASE` character removes the last character from the current undelimited input line; the `ERASE` character itself is discarded (The Open Group, 2024, Sections 11.1.6 and 11.1.9). | It does not retract output already emitted, erase recorder history, or securely delete storage. |
| **POSIX `ECHOE`** | A terminal setting that asks the terminal to visually erase the last character when canonical `ERASE` processing occurs, if possible (The Open Group, 2024, Section 11.2.5). | The visual result does not establish what an application, recorder, or storage device retains. |
| **ECMA-48 `DCH`** | The Delete Character control function, which removes a character at the active display position and shifts the remaining displayed contents (ECMA International, 1991, Section 8.3.26). | It is not the same control function as ASCII `BS`, and it does not imply deletion from a transcript or other storage. |
| **Visual erasure** | A display no longer shows a character after cursor movement, overwriting, redrawing, or a display-delete function. In the measured macOS path, the repeated output was `08 20 08`: move backward, overwrite with a space, and move backward again. | It does not prove deletion from the canonical input queue, child-process input, a recording, backups, or physical media. |
| **Canonical input erasure** | POSIX `ERASE` removes a character from the current uncommitted input line before that line is returned to the reading application. | It does not imply that an echoed representation was never emitted or recorded. |
| **Commit / submission** | The boundary at which a completed line is made available to the child application, normally after Return in the measured canonical terminal path. | It is not necessarily the boundary at which another component begins observing or recording composition. |
| **Logical deletion** | A system no longer exposes an item at a particular interface or logical location. | It does not by itself establish immediate erasure of prior copies, logs, backups, or physical storage. |
| **Secure deletion** | A stronger storage claim: data has been rendered unrecoverable under a stated threat model. | Neither a Backspace/Delete key action nor disappearance from a display is evidence of secure deletion. |
| **Retention** | A representation remains recoverable at a named layer, such as a PTY recording. | Retention by one layer does not prove receipt by every other layer, including a child process, model, or network service. |

### Preferred descriptions for this repository

For the measured foundation case, the least ambiguous account is:

1. the user pressed the physical key labeled **Delete**, which performed a
   backward-edit action on that Apple keyboard;
2. the terminal input path produced `0x7f`, ASCII `DEL`;
3. the child PTY was configured with `erase = ^?`, so POSIX canonical
   `ERASE` processing removed the previous character from the uncommitted
   input line;
4. echo processing emitted `0x08 0x20 0x08` to visually erase the character;
5. the child application received only the separately committed line; and
6. `/usr/bin/script -q` preserved the earlier text echo and later
   visual-erasure output in its sequential recording.

Accordingly, repository prose should prefer **physical Delete-key action**,
**`0x7f` input byte**, **POSIX `ERASE` processing**, **`08 20 08`
visual-erasure output**, **child-visible committed line**, and **recorder-
retained composition history** over an unqualified statement that text “was
deleted.”

## Closest direct prior work

### `script` and `forscript`

Dewald, Freiling, and Weber (2011) are the closest published technical
precedent. They analyze the Unix `script` utility and build `forscript`, a
forensic recorder that separates user input, terminal output, timing, and
environment metadata. Their worked hexadecimal example describes a user
pressing Backspace after typing an unwanted character: the input is `0x7f`
(ASCII `DEL`), while the output contains `0x08` (ASCII `BS`) and an escape
sequence that removes the character from the rendered line. The example
therefore contains the same key-label, byte-name, editing-function, and display-
effect distinction measured here.

That paper also explains an important evidentiary boundary. Ordinary `script`
records terminal output, not necessarily raw keyboard input. Echo can transform
draft input into PTY output before `script` records it. An output-only
transcript may therefore preserve composition history without being configured
as a keystroke logger, while still being insufficient to reconstruct user
intent unambiguously.

Apple's `script(1)` manual independently warns that a typescript includes
linefeeds and backspaces and may not match a naive user's expectation (Apple
Inc., 2023b). The implementation copies bytes read from the PTY master to both
the visible terminal and the typescript in ordinary recording mode (Apple Inc.,
2023a). These sources mean that the broad fact that `script` logs backspace-
affected terminal output is established prior knowledge.

The contribution boundary for this repository is narrower: it isolates and
privacy-frames the complete path in which canonical `ERASE` prevents abandoned
draft text from reaching the child as part of the committed line while echo
exposes composition history as PTY output and an output-only recorder makes
that history durable.

### Command logging at a later boundary

Švábenský et al. (2021) present a toolset that logs shell commands for
cybersecurity education. Their design records a command after the shell has
read it and before execution, and their limitations explicitly note that edits
made before the user presses Enter are not recorded. It is a useful contrasting
architecture: executed-command logging observes the committed command, whereas
PTY-output recording can preserve pre-commit composition through echo.

Hassan (2020) uses terminal-session recording software for cybersecurity
teaching and notes that terminal recordings contain raw control and escape
sequences. That work concerns planned pedagogical demonstrations rather than
the privacy consequences of retaining abandoned composition.

## Composition-history research

Van Waes, Leijten, and van Weijen (2009) describe Inputlog, which records
keystrokes and mouse activity to reconstruct writing processes. Their examples
distinguish a correction made with Backspace at the current insertion point
from a correction made after cursor movement with Delete. A normalized
revision analysis may classify both as the same textual substitution, while
the linear event log preserves different actions. This is a direct parallel to
the repository's terminology rule: key event, semantic edit, final text, and
retained event history are different representational layers.

Inputlog is intentional research instrumentation. It does not present the same
expectation problem as a recorder described only as retaining terminal output.
The closely related 2013 *Written Communication* Inputlog article was not
available as open full text during this review, so it is not used as evidence
here; the open 2009 article was reviewed in full.

## Pre-submission privacy parallels

Acar, Englehardt, and Narayanan (2020) show that session-replay and other third-
party scripts can collect DOM contents, key presses, and sensitive fields
before a user submits a web form. Senol et al. (2022) later measure email and
password exfiltration before submission at scale, including session-replay
scripts that transmit input incrementally. The shared privacy structure is
that the user's commit or submission boundary is not necessarily the
observer's recording boundary.

The terminal mechanism differs materially. The measured foundation case does
not require malicious JavaScript, third-party transmission, or explicit input
logging. Ordinary terminal echo turns draft input into PTY output; an ordinary
output recorder then preserves that output locally.

## Deletion expectations and lower-layer persistence

Murillo et al. (2018) distinguish **UI-based** deletion models, in which
disappearance from an interface is treated as deletion, from **backend-aware**
models that account for storage, copies, derived data, and time. Their study
deliberately excludes automatically generated data such as logs. This
repository occupies much of that excluded space: an edit disappears from the
interactive line yet remains in an automatically generated transcript.

Eng (2025) provides a close forensic analogue by recovering text deleted from
Windows Notepad through application-maintained TabState and undo data. That
mechanism is application autosave/undo state, whereas the mechanism here is
sequential PTY output.

At the storage layer, Reardon et al. (2011) show that logical deletion on a
log-structured file system does not guarantee prompt physical erasure. That is
an architectural analogy, not a direct terminal precedent: the present result
concerns composition exposed before commit, not remnants of a deleted file.

## Synthesis and claim boundary

The literature supports four conclusions:

1. **The component behavior is not newly discovered.** Standards distinguish
   `BS`, `DEL`, POSIX `ERASE`, display deletion, and storage deletion. Apple's
   manual and Dewald et al. (2011) document backspace-affected `script` output.
2. **The labels are central to the expectation gap.** “Delete” may refer to a
   physical key, a byte named `DEL`, a logical editing operation, disappearance
   from a display, or destruction of stored data. Those propositions are not
   equivalent.
3. **The closest privacy precedent is pre-submission recording.** Browser
   research establishes that content may cross a recording boundary before the
   user crosses the expected submission boundary.
4. **A plausible research gap remains, but not an absolute priority claim.** In
   the literature reviewed here, no peer-reviewed paper centers this complete
   privacy chain:

   ```text
   canonical draft input
       → POSIX ERASE removes a character from the future child-visible line
       → echo exposes the draft and visual correction as PTY output
       → an output-only recorder durably preserves the composition history
   ```

The most defensible contribution is therefore not “backspaces appear in
`script` logs.” It is the controlled separation and privacy interpretation of
visual state, canonical input state, child-process receipt, and recorder state.
A broader novelty claim would require a reproducible systematic search across
additional databases, terminology, patents, manuals, and non-English sources.

## References

Acar, G., Englehardt, S., & Narayanan, A. (2020). No boundaries: Data
exfiltration by third parties embedded on web pages. *Proceedings on Privacy
Enhancing Technologies, 2020*(4), 220–238.
https://doi.org/10.2478/popets-2020-0070

Apple Inc. (2023a). *script.c* (shell_cmds-302.0.1) [Source code]. Apple Open
Source.
https://github.com/apple-oss-distributions/shell_cmds/blob/e256b9a97f9bbd751305b7af36cf751668fbb849/script/script.c

Apple Inc. (2023b). *script(1): Make typescript of terminal session* [Manual
page]. Apple Open Source.
https://github.com/apple-oss-distributions/shell_cmds/blob/e256b9a97f9bbd751305b7af36cf751668fbb849/script/script.1

Cerf, V. G. (1969). *ASCII format for network interchange* (RFC 20). RFC
Editor. https://doi.org/10.17487/RFC0020

Dewald, A., Freiling, F. C., & Weber, T. (2011). Design and implementation of a
documentation tool for interactive commandline sessions. In *2011 Sixth
International Conference on IT Security Incident Management and IT Forensics*
(pp. 62–80). IEEE. https://doi.org/10.1109/IMF.2011.17

ECMA International. (1991). *Control functions for coded character sets* (5th
ed.; ECMA-48).
https://ecma-international.org/wp-content/uploads/ECMA-48_5th_edition_june_1991.pdf

Eng, C. (2025). Is that Windows Notepad window really empty? *DFIR Review*.
https://doi.org/10.21428/b0ac9c28.a8c471f1

Hassan, I. (2020). Teaching cybersecurity to computer science students
utilizing terminal sessions recording software as a pedagogical tool. In *2020
IEEE Frontiers in Education Conference (FIE)* (pp. 1–8). IEEE.
https://doi.org/10.1109/FIE44824.2020.9274268

Murillo, A., Kramm, A., Schnorf, S., & De Luca, A. (2018). “If I press delete,
it's gone”: User understanding of online data deletion and expiration. In
*Fourteenth Symposium on Usable Privacy and Security (SOUPS 2018)* (pp.
329–339). USENIX Association.
https://www.usenix.org/conference/soups2018/presentation/murillo

Reardon, J., Marforio, C., Capkun, S., & Basin, D. (2011). *Secure deletion on
log-structured file systems* [Preprint]. arXiv.
https://doi.org/10.48550/arXiv.1106.0917

Senol, A., Acar, G., Humbert, M., & Zuiderveen Borgesius, F. (2022). Leaky
forms: A study of email and password exfiltration before form submission. In
*31st USENIX Security Symposium (USENIX Security 22)* (pp. 1813–1830). USENIX
Association. https://www.usenix.org/conference/usenixsecurity22/presentation/senol

Švábenský, V., Vykopal, J., Tovarňák, D., & Čeleda, P. (2021). Toolset for
collecting shell commands and its application in hands-on cybersecurity
training. In *2021 IEEE Frontiers in Education Conference (FIE)* (pp. 1–9).
IEEE. https://doi.org/10.1109/FIE49875.2021.9637052

The Open Group. (2024). General terminal interface. In *The Open Group Base
Specifications Issue 8, IEEE Std 1003.1-2024*.
https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap11.html

Van Waes, L., Leijten, M., & van Weijen, D. (2009). Keystroke logging in
writing research: Observing writing processes with Inputlog. *German as a
Foreign Language, 2–3*, 41–64.
https://repository.uantwerpen.be/docman/irua/e8d12b/b39f88f0.pdf
