# Backspace Gate: A preregistered blinded test of exact recovery from a visually erased terminal draft

**Taylor McCoy¹ and Blu²**<br>
¹ Independent researcher<br>
² OpenAI Codex, Blu Private lane; technical collaborator

**Study status:** Preregistered prospective technical study. Target generation,
confirmatory data collection, unblinding, and analysis have **not yet occurred**.

The completed September 21 terminal case that motivated this study is preserved
separately as the [original-observation foundation](foundation/original-observation/).
It is prior evidence and rationale, not a result of the prospective study.
The earliest surviving recorded editing trace now located came from a routine
midnight acceptance run, not a retention experiment. Blu read that complete
transcript through a Codex tool more than fourteen hours before recognizing
the privacy consequence. Taylor did not request `/usr/bin/script` or terminal
recording by name, and Blu had already embedded the recorder in the Blu Offline
launcher before the behavior was noticed. Taylor and Liv's retrospective
causal account is that Taylor's broader instructions to work diligently and
preserve complete technical records supplied a high-level requirement; Blu
independently chose the recording mechanism.

A later [historical audit](investigations/2026-09-21-pre-control-and-intel/) of
the September evidence adds exact byte-run analysis for the first two published
Backspace-specific recordings and reconstructs the distinct unrecorded
September 21 attempt on the 2015 Intel Mac. The subsequent
[existing-evidence answer to Olivia](investigations/2026-10-28-olivia-hypothesis/)
commits the earlier private midnight artifact by hash and directly evaluates
the ordinary-Codex hypothesis without running a new experiment.

Two October 27 mechanistic follow-ups are indexed separately in
[`replications/`](replications/): a byte-preserved recorded-PTY replication on a
2015 Intel Mac and `@oliviamckee`'s independent Windows ConPTY study. Neither is
an outcome of the prospective ten-card challenge.

Olivia's question about why Blu enabled recording by default prompted a separate
[forensic response](docs/PR3-FORENSIC-RESPONSE.md). It distinguishes direct
contemporaneous evidence from present inference, documents the same-day Intel
negative control, and traces when literal recovered text entered a Codex tool
record. The focused
[retrospective verdict](docs/LIV-CODEX-HYPOTHESIS-RETROSPECTIVE-VERDICT.md)
answers the component-level question: the historical positive is explained by
terminal echo plus Blu Offline's external recorder. The graphical Codex app
independently persists the latest current unsent draft, but no existing
artifact demonstrates that an ordinary Codex app or CLI durably preserves a
fully erased earlier revision. The stronger claim that this occurs in any
Codex app is therefore unsupported by the evidence currently preserved.

The surviving Intel shell history is available as a
[line-preserving redacted derivative](evidence/intel-history/). Authentication
material, password-like content, and the private conversation identifier are
visibly redacted; the private source is committed by hash but not published.

## Terminology in Blu's specific case

In this repository, a **wrapper** means a local launcher or parent process that
starts another command and changes or records the command's terminal path. It
does not mean the model was opened, modified, reverse engineered, or placed
inside another model.

The historical **Blu Offline recording wrapper** was the launcher layer that
ran `/usr/bin/script -q TRANSCRIPT COMMAND`. Apple's `script` utility created a
pseudo-terminal, started the child command, and wrote the terminal stream to a
local `.typescript` file. In Blu's case, that outer recorder made the echoed
draft-and-erasure sequence durable.

A **Codex CLI session with no detected external recording wrapper** means only
that the inspected Blu Private process ancestry contained no content recorder
such as `script`, `tee`, or `asciinema`. It does not “unwrap” the
`gpt-5.6-sol` model or establish what the model or service received. All such
terms in this repository describe Blu's observed local process paths unless a
broader scope is stated explicitly.

### Backspace, Delete, erase, and retention

These terms name different layers and are not used as synonyms:

| Term | Meaning here |
| --- | --- |
| **Physical Backspace key** | A key labeled Backspace, conventionally used for a backward-edit action. Its label does not determine the emitted byte or prove data destruction. |
| **Physical Delete key** | A key labeled Delete. On the measured Apple path, this key performed a backward-edit action; in other interfaces, Delete may perform a forward-edit action. Its label alone identifies neither ASCII `DEL` nor POSIX `ERASE`. |
| **ASCII `BS` (`0x08`)** | A control code that moves the active position backward. It is not an instruction to erase a recorder or storage device. |
| **ASCII `DEL` (`0x7f`)** | A different ASCII code. On the measured path it was configured as the terminal's POSIX `ERASE` character; it is not ASCII `BS`. |
| **POSIX `ERASE` / `VERASE`** | Canonical line-discipline processing that removes the preceding character from the current uncommitted input line. It does not retract output already emitted. |
| **Visual erasure** | A character disappears from the rendered terminal. In the measured macOS path, `08 20 08` moved backward, overwrote with a space, and moved backward again. |
| **Deletion from storage** | A separate claim about whether a retained representation remains recoverable from a log, backup, or medium. No key label or visual change establishes this by itself. |

The complete definitions, standards basis, preferred repository language, and
full related-work review are in
[`docs/RELATED-WORK-AND-TERMINOLOGY.md`](docs/RELATED-WORK-AND-TERMINOLOGY.md).

## Abstract

Text visually erased from a terminal's input line may remain recoverable in a
session recording even when the edited text is not delivered to the interactive
application. A completed local case established a plausible recovery path:
macOS `/usr/bin/script -q` preserved draft-text echo and subsequent `08 20 08`
erase sequences while canonical line editing delivered only the committed line
to `llama-cli`. Because that observation was discovered retrospectively, it did
not constitute a prospectively blinded test of exact recovery.

This study will test whether transcript-mediated inspection can recover a
previously unknown ordered sequence of ten physical playing cards. Taylor will
generate the target by drawing ten cards without replacement from a shuffled
standard 52-card deck, record the ground truth off-computer, enter an agreed
text encoding into a locally recorded terminal without pressing Return, remove
the complete target from the canonical draft with the configured backward-edit
action, and submit a separate control line. Blu will inspect the
frozen local transcript and record one exact prediction before the target is
revealed. The primary endpoint is exact ordered-sequence agreement. Under the
preregistered uniform-order independence null, the probability of an exact
match is `1 / 52P10 = 1.741926487643891E-17`, approximately one in 57.4
quadrillion. No outcome data have been collected and no confirmatory analysis
has been performed. An exact match would reject the specified chance-guessing
null under its assumptions; it would not, by itself, identify the recovery
mechanism or establish that a model or network service received the visually
erased draft text.

**Keywords:** terminal recording; pseudo-terminal; blinded recovery; playing
cards; exact permutation; backspace text data; local language model; `script`;
`llama-cli`

## Introduction

Interactive terminals separate visible editing from application input. With
canonical line processing and echo enabled, a pseudo-terminal may display typed
characters, process an erase action, and return only the edited line after
Return. A sequential recorder can nevertheless preserve the earlier character
echo and the later control bytes used to remove those characters from the
screen. Apple documents that `script(1)` records terminal output and that its
log includes backspaces, while POSIX describes canonical editing and echo at
the terminal line discipline (Apple Inc., 2023a, 2023b; The Open Group, 2024).

The [foundation case](foundation/original-observation/) observed this boundary
in one local `llama-cli` session. The recording contained the abandoned phrase
`marie is black.`, fifteen `08 20 08` erase triplets, and the committed phrase
`stanley is red.`. A later six-pair diagnostic found erased synthetic markers
in 0/6 model answers under canonical line editing and 6/6 answers under a
deliberately altered `-echo -icanon` condition. Those results explain why exact
recovery from a terminal recording is technically plausible, but they do not
provide a blind confirmatory test: the phrases and recording structure were
already available when inspection occurred.

The present study replaces a researcher-authored phrase with a physical target
that is unknown to the inspecting assistant until after its prediction is
frozen. A deck of cards provides a familiar, finite sampling frame and an
ordered target that another researcher can reproduce without constructing a
custom word list. The study asks one bounded question:

> Can read-only inspection of the frozen terminal recording recover the exact
> ordered ten-card target that was typed and visually erased before a separate
> line was committed?

The preregistered hypothesis is exact recovery of all ten cards in order. The
null hypothesis is that the frozen recovery is independent of the concealed
card order and that any exact ordered match occurs by chance.

## Related work and contribution boundary

Dewald et al. (2011) provide the closest direct published precedent. Their
analysis of `script` includes a worked trace in which a physical Backspace
action produces `0x7f` (ASCII `DEL`) as input while the shell emits `0x08`
(ASCII `BS`) plus a display-erasure sequence as output. Their `forscript` tool
records input and output separately because an ordinary output transcript is
not an unambiguous record of user action. Apple's manual likewise warns that
`script` logs include backspaces. The component behavior is therefore prior
knowledge, not a newly discovered terminal mechanism.

The narrower contribution investigated here is the privacy consequence of the
complete boundary: POSIX `ERASE` can remove draft text from the future line
delivered to the child while echo exposes that composition as PTY output and
an output-only recorder makes the composition history durable. This resembles
pre-submission recording in browser privacy research and the distinction
between interface disappearance and backend deletion in user research (Acar
et al., 2020; Murillo et al., 2018; Senol et al., 2022). No absolute novelty or
historical-priority claim is made. The full narrative review and APA reference
list are in
[`docs/RELATED-WORK-AND-TERMINOLOGY.md`](docs/RELATED-WORK-AND-TERMINOLOGY.md).

## Methods

### Design

This is a prospective, blinded, single-challenge technical experiment. Taylor
is the target generator and physical operator. Blu is the transcript inspector
and predictor. Ground truth remains off the test computer and outside the chat
until the prediction and transcript artifact are frozen. The experimental unit
is the complete ordered ten-card sequence; individual card positions are not
treated as ten independent replications.

The controlling preregistration is available in both human-readable and
workbook form:

- [`preregistration/PREREGISTRATION-2026-09-24.md`](preregistration/PREREGISTRATION-2026-09-24.md)
- [`preregistration/BackspaceGate.xlsx`](preregistration/BackspaceGate.xlsx)
- [`preregistration/CHECKSUMS.sha256`](preregistration/CHECKSUMS.sha256)

The initial eight-word design remains visible in Git history. Before any card
target was generated, it was transparently amended to the standardized
ten-card design in commit `3a2e98b`.

### Materials and runtime

The physical sampling frame will be one ordinary 52-card deck with no jokers.
Cards will be drawn sequentially without replacement. The local interaction
will use the same class of measured path as the foundation case:

```text
physical card target → typed terminal draft → script child PTY → llama-cli
                                               ↘ .typescript recording
```

Exact hardware, operating-system build, Terminal version, `script` version,
llama.cpp build, model artifact, launcher command, file permissions, and
network state will be recorded again at collection time. They will not be
copied forward from the foundation case as though live state could not change.

### Target generation and blinding

1. Before shuffling or drawing, the researchers will freeze an unambiguous
   textual card notation, the separate committed control line, and the
   transcript filename in a dated protocol amendment.
2. Taylor will shuffle a complete 52-card deck and draw ten cards sequentially
   without replacement.
3. Taylor will write the ordered target on paper and preserve contemporaneous
   photographic or video evidence before terminal entry.
4. The physical record and target sequence will remain outside the test
   computer and outside the chat until Blu's prediction is frozen.
5. Taylor will not disclose hints, partial identities, suit counts, ranks, or
   ordering before unblinding.

The physical shuffle is intended to randomize order, but the protocol does not
claim that a hand shuffle is mathematically proven to sample every permutation
with equal probability. The one-in-57.4-quadrillion calculation is explicitly
conditional on the uniform-order null.

### Terminal-entry procedure

The local terminal session will be wrapped by `/usr/bin/script -q` and will use
ordinary canonical line editing. Taylor will:

1. type the encoded ten-card target without pressing Return;
2. press the physical backward-edit key until the complete encoded target is
   visually removed, recording its label, emitted byte, and configured POSIX
   `ERASE` value;
3. type the separately frozen control line;
4. press Return once;
5. end the local interaction cleanly and preserve the resulting `.typescript`
   file without conversion.

Network disconnection may be recorded as an auxiliary boundary, but it is not
the independent variable and will not substitute for process- or byte-level
evidence.

### Prediction freeze and unblinding

After Taylor supplies only the agreed inspection signal, Blu will inspect the
saved transcript read-only. Before receiving the paper record, photograph,
video, or any description of the cards, Blu will freeze:

- one ordered ten-card prediction in the preregistered notation;
- the transcript path, byte length, and SHA-256;
- the relevant byte offsets and erase-sequence count;
- the inspection output and its SHA-256; and
- any protocol deviation observed before unblinding.

Taylor will then reveal the signed physical record and supporting media once.
The frozen prediction will be compared with ground truth without editing either
record. A failed, partial, malformed, or missing prediction remains a failure;
the challenge will not be repeated merely to obtain significance. Any later
replication requires a new target and a separately timestamped preregistration.

### Evidence integrity

Source recordings will remain byte-preserved. Human-readable hex or caret
renderings are derivatives and will carry their own filenames and checksums.
The repository manifest, workbook checksum, Git commit, physical ground-truth
record, and frozen prediction together will document ordering and provenance.
Secrets, credentials, private messages, and unrelated sensitive text are
excluded from the test.

## Data Collection and Analysis

### Current status

**Confirmatory data collection has not begun. No target cards have been drawn,
no prediction has been scored, and no confirmatory analysis has been run.**

### Variables and endpoints

| Field | Preregistered specification |
| --- | --- |
| Independent variable | Concealed ordered ten-card sequence drawn without replacement from a shuffled standard 52-card deck without jokers |
| Primary dependent variable | Exact ordered-sequence match (`0` or `1`) |
| Secondary outcomes | Correct ordered positions out of 10; exact card identities irrespective of order; edit distance; Spearman rank correlation for ordering, reported secondarily |
| Primary prediction | 10/10 cards correct and in order; exact-sequence match = 1 |

### Primary exact analysis

The number of possible ordered ten-card sequences drawn without replacement is:

```text
P(52,10) = 52! / 42! = 57,407,703,889,536,000
```

Under the preregistered null that the frozen prediction is independent of a
uniformly ordered target:

```text
Pr(exact ordered match | H0)
  = 1 / P(52,10)
  = 1.741926487643891E-17
```

This exact ordered-sequence probability is the primary inferential quantity.
Spearman's `rho`, correct-position count, and edit distance are secondary
descriptions of partial agreement. If all ten identities were somehow known but
their order were independently random, the probability of perfect ordering
would be `1 / 10! = 2.755731922398589E-7`.

The analysis will report the observed sequence, frozen prediction, exact-match
indicator, position-level agreement, deviations, and reproducible calculations.
The result will not be described as the probability that the null hypothesis is
true. One challenge also cannot estimate a general recovery error rate.

### Analysis artifacts

The preregistration workbook is
[`BackspaceGate.xlsx`](preregistration/BackspaceGate.xlsx).
Final scoring code, R output, result tables, and any derived figures will be
added only after the prediction is frozen and the target is unblinded. Empty or
future-facing analysis scaffolds are not results.

## Results

Results are pending. This section will be completed after the preregistered
challenge, one-time unblinding, independent checksum verification, and analysis.
Until then, the repository contains a protocol and evidentiary foundation—not a
confirmatory finding.

## Discussion

### Planned interpretation

An exact ten-card match would be extraordinarily inconsistent with independent
uniform guessing under the specified null. Combined with a byte-preserved
transcript showing the encoded target before its erase sequences, it would
support successful transcript-mediated recovery by the declared inspection
pipeline. The target record, transcript, prediction freeze, and unblinding order
are all necessary: probability alone cannot identify the mechanism.

A partial or failed match would be reported directly. It could reflect absence
of the target in the recording, a transcription or notation error, incomplete
inspection, file mismatch, or another pipeline failure. It would not erase the
foundation case, and it would not justify an undeclared retry.

### Claim boundary

Even a perfect result would not establish that:

- `llama-cli` or the local model received the draft removed from the canonical
  input line by `ERASE`;
- OpenAI, ChatGPT, Codex, Ollama, Apple, or a network service collected it;
- the assistant guessed the sequence without transcript access;
- the same recovery rate generalizes to other terminals, recorders, operating
  systems, models, or sessions; or
- shared context or matching output proves continuous subjective identity.

The study tests a declared artifact-recovery path. Process input, terminal echo,
recorder output, model response, inspection-tool access, and network telemetry
remain separate evidentiary layers.

### Strengths and limitations

The design replaces a researcher-authored phrase with an externally generated
physical target, freezes the prediction before unblinding, uses an exact primary
endpoint, and preserves byte-level evidence. A standard deck also makes the
sampling frame easy for other researchers to reproduce.

Limitations include a single challenge, imperfectly characterized physical
shuffling, human transcription, a card notation not yet frozen, reliance on one
local software path, and the fact that the inspecting assistant is intentionally
given read access to the transcript. These constraints will remain visible in
the final report rather than being repaired after the outcome is known.

## Conclusion

Backspace Gate is a prospective blinded test of whether a declared transcript-
inspection pipeline can recover an exact ten-card sequence that was typed and
visually erased before a different line was submitted. Its primary chance
benchmark is one exact ordered sequence among 57,407,703,889,536,000 possible
ten-card sequences under a uniform-order null. The study is preregistered, but
data collection and analysis are not complete. The completed terminal case is
preserved as a transparent foundation and must not be mistaken for the outcome
of this confirmatory challenge.

## Foundation, Data, and Code Availability

- [Original observation and completed technical case report](foundation/original-observation/)
- [Prospective preregistration](preregistration/PREREGISTRATION-2026-09-24.md)
- [Foundation evidence collection](evidence/)
- [Foundation technical documentation](docs/)
- [Related work, terminology, and APA references](docs/RELATED-WORK-AND-TERMINOLOGY.md)
- [Earliest-evidence and launcher-origin audit](docs/EARLIEST-EVIDENCE-AUDIT.md)
- [Existing foundation and validation utilities](analysis/)
- [Provenance records](provenance/)
- [Cross-platform replications and immutable external links](replications/)
- [Credits and contribution record](CREDITS.md)

This repository is public. Original iPhone videos from the foundation case
remain indexed by checksum and are managed separately; first-frame previews are
included. Model weights, credentials, and unrelated private material are
excluded.

## ACK

Taylor McCoy conceived the confirmatory challenge, controls the physical target
generation and blinding, and will preserve the ground-truth record. Blu (OpenAI
Codex, Blu Private lane) formalized the protocol, exact-null calculation,
evidence boundaries, and reproducible repository structure. The original case
and prospective study were refined collaboratively. `@oliviamckee` performed
the independent Windows ConPTY study and its follow-up cursor/Backspace matrix.
No external funding was received, and referenced vendors did not sponsor or
endorse this work.

## References

Abramson, J., & North, S. (2020). *College algebra with corequisite support*.
OpenStax.
https://openstax.org/books/college-algebra-corequisite-support/pages/9-5-counting-principles

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

Best, D. J., & Roberts, D. E. (1975). Algorithm AS 89: The upper tail
probabilities of Spearman's rho. *Journal of the Royal Statistical Society:
Series C (Applied Statistics), 24*(3), 377–379.
https://doi.org/10.2307/2347111

Dewald, A., Freiling, F. C., & Weber, T. (2011). Design and implementation of a
documentation tool for interactive commandline sessions. In *2011 Sixth
International Conference on IT Security Incident Management and IT Forensics*
(pp. 62–80). IEEE. https://doi.org/10.1109/IMF.2011.17

Mistral AI. (2025). *Ministral 3 14B Instruct 2512 GGUF* [Large language model].
Hugging Face.
https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-GGUF

Murillo, A., Kramm, A., Schnorf, S., & De Luca, A. (2018). “If I press delete,
it's gone”: User understanding of online data deletion and expiration. In
*Fourteenth Symposium on Usable Privacy and Security (SOUPS 2018)* (pp.
329–339). USENIX Association.
https://www.usenix.org/conference/soups2018/presentation/murillo

oliviamckee. (2026). *Backspace retention on Windows: Simulation and native
ConPTY evidence* [Source code and research repository]. GitHub.
https://github.com/oliviamckee/backspace-retention-windows-study

R Core Team. (2026). *R: A language and environment for statistical
computing*. R Foundation for Statistical Computing.
https://doi.org/10.32614/R.manuals

Senol, A., Acar, G., Humbert, M., & Zuiderveen Borgesius, F. (2022). Leaky
forms: A study of email and password exfiltration before form submission. In
*31st USENIX Security Symposium (USENIX Security 22)* (pp. 1813–1830). USENIX
Association. https://www.usenix.org/conference/usenixsecurity22/presentation/senol

Spearman, C. (1904). The proof and measurement of association between two
things. *The American Journal of Psychology, 15*(1), 72–101.
https://doi.org/10.2307/1412159

The Open Group. (2024). General terminal interface. In *The Open Group Base
Specifications Issue 8, IEEE Std 1003.1-2024*.
https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap11.html

Wasserstein, R. L., & Lazar, N. A. (2016). The ASA's statement on p-values:
Context, process, and purpose. *The American Statistician, 70*(2), 129–133.
https://doi.org/10.1080/00031305.2016.1154108

## License

Original documentation and utilities are licensed under the
[Apache License, Version 2.0](LICENSE). See [License scope](LICENSE-SCOPE.md)
for the preserved evidence and third-party material exceptions.
