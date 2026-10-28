# Blinded byte-recovery validation protocol

**Declared before generation and decoding on 2026-09-24.**

## Purpose

This validation estimates whether the repository's read-only byte-inspection
pipeline can recover previously unseen synthetic draft strings from the same
byte structure observed in the two-sentence foundation transcript. It tests
fixture parsing and exact transcription. It does not estimate the probability
that every interpretation of the historical experiment is correct, and it does
not test a cloud model's access to unsubmitted typing.

## Blinding and fixation

1. Generate ten targets with Python's `secrets` module without printing them.
2. Make each target 15 ASCII characters long, with mixed-case letters, digits,
   spaces, and the punctuation characters `.`, `-`, and `_` available to the
   generator. The first and last characters are alphanumeric.
3. Store each target in a transcript-like fixture as:

   ```text
   non-printing boundary + target + 15 * (08 20 08) + committed string + boundary
   ```

4. Save the hidden target table and its SHA-256 commitment before decoding.
5. Commit the protocol, generator, targets, fixtures, and commitment to Git
   before inspecting fixture contents.
6. Run the existing read-only inspection tool on each fixture. Freeze the ten
   reported `BEFORE` values and erase counts in a separate recovery file.
7. Only after that recovery file is fixed, compare it with the hidden target
   table and verify the target-table commitment.

The blinding is procedural rather than cryptographic: the target file exists on
the same machine and could technically be opened, but it must not be read or
displayed before the recoveries are frozen.

## Endpoints

Primary endpoints, scored per fixture:

- exact target recovery, including case, spaces, punctuation, and length;
- exact recovery of fifteen `08 20 08` erase triplets.

Report the number correct out of ten and every mismatch. A result of 10/10 is
an observed error count of 0/10, not proof that the pipeline's general error
rate is zero. No *t* test applies because the outcomes are paired exact-match
indicators, not continuous means.

