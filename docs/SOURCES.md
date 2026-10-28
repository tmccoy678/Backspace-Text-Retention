# Technical sources

## llama.cpp

The installed Homebrew formula reported llama.cpp revision
`b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` (short form `b29c606e2`).

- [`common/console.cpp` terminal-mode branch, lines 130–145](https://github.com/ggml-org/llama.cpp/blob/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/common/console.cpp#L130-L145)
- [`readline_simple` and `std::getline`, lines 1046–1087](https://github.com/ggml-org/llama.cpp/blob/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/common/console.cpp#L1046-L1087)
- [llama.cpp repository](https://github.com/ggml-org/llama.cpp)

The formula metadata captured on the experiment machine is preserved at
[`provenance/Homebrew-llama.cpp-formula.json`](../provenance/Homebrew-llama.cpp-formula.json).

## macOS terminal tools

The local `script(1)` manual distinguishes ordinary terminal recording from its
separate key-recording option. The experiment invoked `/usr/bin/script -q` and
did **not** invoke `-k`. On macOS, inspect the installed manual with:

```sh
man 1 script
man 1 stty
man 4 termios
```

The exact experimental terminal-mode command is preserved in
[`tools/original-raw-tty-wrapper.zsh`](../tools/original-raw-tty-wrapper.zsh).

## Local model

The model was Mistral AI's `Ministral-3-14B-Instruct-2512-Q5_K_M.gguf`.
Its name, size, SHA-256, license, and observed runtime are recorded in
[`provenance/MODEL-MANIFEST.md`](../provenance/MODEL-MANIFEST.md). The 9.6 GB
weight file is not included.

## Independent Windows replication

Olivia's public repository preserves the independent Windows ConPTY study,
native host source, exact transcripts, metadata, SHA-256 manifest, and verifier:

- [`oliviamckee/backspace-retention-windows-study`](https://github.com/oliviamckee/backspace-retention-windows-study)
- [Cursor and Backspace byte matrix, immutable commit `5815c0136ff8`](https://github.com/oliviamckee/backspace-retention-windows-study/commit/5815c0136ff88b03c7d6c455962aacb7e2a8bd60)

The Windows artifacts remain external rather than being copied into this
repository. The cross-repository comparison is summarized in
[`replications/README.md`](../replications/README.md).
