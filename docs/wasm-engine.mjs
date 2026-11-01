const decoder = new TextDecoder();

function wrapper(exports) {
  function rendered(kind) {
    exports.demo_render(kind);
    const start = Number(exports.demo_output_ptr());
    const length = Number(exports.demo_output_len());
    return decoder.decode(new Uint8Array(exports.memory.buffer, start, length));
  }

  return {
    reset() { exports.demo_reset(); },
    type(text) {
      for (const character of text.replace(/[\r\n]/g, ' ')) {
        exports.demo_type(character.codePointAt(0));
      }
    },
    backspace() { return Boolean(exports.demo_backspace()); },
    commit() { exports.demo_commit(); return this.committed; },
    get visible() { return rendered(0); },
    get committed() { return exports.demo_is_committed() ? rendered(5) : null; },
    compressedComposition() { return rendered(1); },
    hexDump() { return rendered(2); },
    report() { return rendered(3); },
    eraseRuns() {
      const value = rendered(4);
      return value ? value.split(',').map(Number) : [];
    },
  };
}

export async function createRustTerminalRecorder(bytes) {
  const {instance} = await WebAssembly.instantiate(bytes, {});
  const recorder = wrapper(instance.exports);
  recorder.reset();
  return recorder;
}

export async function loadRustTerminalRecorder() {
  const url = new URL('./wasm/backspace_demo_engine.wasm?v=2', import.meta.url);
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Rust/WASM engine failed to load (${response.status}).`);
  return createRustTerminalRecorder(await response.arrayBuffer());
}
