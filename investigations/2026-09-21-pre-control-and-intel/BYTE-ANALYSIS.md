# Pre-control byte analysis

Offsets are zero-based and inclusive. An erase triplet is the exact byte
sequence `08 20 08` (backspace, space, backspace). The counts below were
generated with the repository's read-only `tools/inspect_typescript.py` against
the SHA-256-identified source files.

## Partial 2:13 PM session

- File: `evidence/transcripts/Blu-Offline-20260921-141327.typescript`
- Bytes: 1,190
- SHA-256: `5cc08346d7de25988aa687d292eefc1bf994ba74d5031ff9b0cd7e3fc271cb5e`

| Run | Byte offsets | Triplets | Erase-output bytes |
| ---: | ---: | ---: | ---: |
| 1 | 1058–1072 | 5 | 15 |
| 2 | 1078–1167 | 30 | 90 |
| **Total** | — | **35** | **105** |

The input region contains the literal template
`My harmless target sentence is: [WRITE YOUR SENTENCE HERE].`, cursor-left
escape sequences, deletion output, and Control-C. It is a partial precursor,
not a completed target-sentence trial.

## First substantive 2:19 PM session

- File: `evidence/transcripts/Blu-Offline-20260921-141944.typescript`
- Bytes: 1,816
- SHA-256: `7175aea528876898938e13eb98432f0b0e7bc8170e9c62fb3fadecf80126b375`

| Run | Byte offsets | Triplets | Erase-output bytes | Adjacent composition evidence |
| ---: | ---: | ---: | ---: | --- |
| 1 | 1006–1038 | 11 | 33 | `the purple ` → `the doberman bit ` |
| 2 | 1056–1094 | 13 | 39 | deletes `doberman bit `, leaving `the `, then appends `doberman won best in show` |
| 3 | 1120–1206 | 29 | 87 | deletes the resulting `the doberman won best in show`, then appends `marie is a so` |
| 4 | 1220–1225 | 2 | 6 | deletes `so`, leaving `marie is a `, then appends `doberman ` |
| 5 | 1235–1267 | 11 | 33 | deletes `a doberman `, leaving `marie is `, then begins the final draft |
| 6 | 1308–1313 | 2 | 6 | corrects `sleepig ` while composing `sleeping on ...` |
| 7 | 1328–1330 | 1 | 3 | corrects `cour` to `couch.` |
| **Total** | — | **69** | **207** | — |

These are successive states within one composition stream, not seven
independent prompts. Resolving the edits yields the one committed line:

```text
marie is my favorite doberman and she is sleeping on the couch.
```

The model's answer addresses Marie sleeping on the couch. The recording proves
that the outer terminal transcript retained the abandoned drafts; it does not,
by itself, prove that the model received those abandoned drafts.
