# Rust/WASM browser engine

This dependency-free Rust state machine powers the GitHub Pages terminal demo.
It models the measured one-byte printable-ASCII path and retains only in-memory
visible text and sequential output bytes. The browser loads the committed
WebAssembly binary from `docs/wasm/`; no typed text is sent to a server or
durable browser store.

Build from the repository root:

```sh
rustup target add wasm32-unknown-unknown
cargo test --manifest-path web-demo-rust/Cargo.toml
cargo build --release --target wasm32-unknown-unknown \
  --manifest-path web-demo-rust/Cargo.toml
cp web-demo-rust/target/wasm32-unknown-unknown/release/backspace_demo_engine.wasm \
  docs/wasm/backspace_demo_engine.wasm
node --test tests/test_web_demo.mjs tests/test_wasm_demo.mjs
```

`docs/wasm-engine.mjs` is the small JavaScript boundary around the exported
state-machine functions. `docs/demo-engine.mjs` remains a tested fail-open
fallback and parity oracle. The two engines must produce identical visible
state, erase-run counts, compressed composition history, byte dump and report.
