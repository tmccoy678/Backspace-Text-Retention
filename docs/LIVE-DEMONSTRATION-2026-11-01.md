# A spontaneous one-line Backspace Gate demonstration

**Date:** November 1, 2026  
**Status:** Public teaching demonstration; not confirmatory data  
**Participants:** Taylor as operator, an in-person observer, and Blu performing later read-only byte inspection

## Why this run is useful

The demonstration is smaller than the foundation case and contains no language
model. That makes the mechanical boundary unusually easy to see. The terminal
looked like an ordinary one-line interaction. Canonical line editing withheld
the erased composition from the child, while terminal echo had already exposed
that composition to the outer output recorder.

The unplanned text also shows that the recorder retained more than one abandoned
draft. It preserved a corrected typo, a complete title erased before Return,
and a one-character false start. A final-state screenshot or shell history would
collapse those events into the submitted line; the sequential recording did not.

## Layer-by-layer result

| Layer | Preserved result |
| --- | --- |
| Visible terminal at submission | `The Sims 2: Night life` |
| Canonical child input | `The Sims 2: Night life` |
| Output recording | `Jimmy Neutrom`, correction to `Jimmy Neutron: Boy Genius`, 25-character full erase, abandoned `F`, and final line |
| Visual-erasure output | Three runs: `08 20 08` repeated 1, 25, and 1 times |
| Model or network receipt | Not tested; no model was in the child path |

The [byte-preserved files](../evidence/demonstrations/2026-11-01/) and one-line
[`tools/backspace_demo.py`](../tools/backspace_demo.py) keep the observation and
the public teaching interface separate.

## Claim boundary

This run is not blinded, preregistered, or independent. It does not add an
accuracy estimate or a new causal claim. It is a transparent reproduction of
the already-documented POSIX canonical-editing, echo, and output-recording
mechanism. Its value is pedagogical: a visitor can watch text disappear, then
inspect the distinct record retained at another system layer.
