# How to photograph an invisible byte

An ASCII `BS` (Backspace) byte (`0x08`) is a control instruction, not a
printable glyph.
Opening the untouched transcript in an ordinary editor may therefore show an
apparently blank region or may move the cursor backward. No character encoding
can make that raw byte visibly print itself as `\b`, `^H`, or `08`; each of those
is a deliberate representation.

The strongest visual record keeps the original file untouched and places these
facts in one frame:

1. the file path, byte length, and SHA-256;
2. byte offsets and a hex rendering from `xxd` or `od`;
3. a second rendering such as `cat -v`, which writes byte `08` as `^H`;
4. a deterministic count of the `08 20 08` triplets; and
5. the command lines that produced the views.

The repository utility prints those fields without modifying the source:

```sh
python3 tools/inspect_typescript.py \
  evidence/transcripts/Blu-Offline-20260921-153748.typescript
```

Independent macOS tools can then reproduce the two representations:

```sh
xxd -g 1 -c 24 -s 995 -l 80 \
  evidence/transcripts/Blu-Offline-20260921-153748.typescript

LC_ALL=C sed -n '28p' \
  evidence/transcripts/Blu-Offline-20260921-153748.typescript | cat -v
```

In the hex view, each `08` is the original byte and each `20` is an original
space byte. In the caret view, `^H` is text emitted by `cat -v` to represent
`0x08`; the two visible characters `^` and `H` are not present in the source.

A screenshot documents what a particular viewer displayed at a particular
time. The `.typescript` file plus its SHA-256 is the byte-level evidence; the
screenshot is a human-readable record of its inspection.
