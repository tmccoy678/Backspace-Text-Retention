import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {test} from 'node:test';
import {TerminalRecorderDemo} from '../docs/demo-engine.mjs';
import {createRustTerminalRecorder} from '../docs/wasm-engine.mjs';

const wasm = await readFile(new URL('../docs/wasm/backspace_demo_engine.wasm', import.meta.url));

function runSequence(demo) {
  demo.type('Jimmy Neutrom');
  demo.backspace();
  demo.type('n: Boy Genius');
  for (let index = 0; index < 25; index += 1) demo.backspace();
  demo.type('F');
  demo.backspace();
  demo.type('The Sims 2: Night life');
  demo.commit();
  return demo;
}

test('Rust/WASM and JavaScript engines produce the same evidence views', async () => {
  const rust = runSequence(await createRustTerminalRecorder(wasm));
  const javascript = runSequence(new TerminalRecorderDemo());
  assert.equal(rust.visible, javascript.visible);
  assert.equal(rust.committed, javascript.committed);
  assert.deepEqual(rust.eraseRuns(), javascript.eraseRuns());
  assert.equal(rust.compressedComposition(), javascript.compressedComposition());
  assert.equal(rust.hexDump(), javascript.hexDump());
  assert.equal(rust.report(), javascript.report());
});
