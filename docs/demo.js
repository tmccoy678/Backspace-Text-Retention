import {TerminalRecorderDemo} from './demo-engine.mjs?v=2';
import {loadRustTerminalRecorder} from './wasm-engine.mjs?v=2';

let demo;
let engineName;
try {
  demo = await loadRustTerminalRecorder();
  engineName = 'RUST/WASM ENGINE';
} catch (error) {
  console.warn('Rust/WASM engine unavailable; using the tested JavaScript fallback.', error);
  demo = new TerminalRecorderDemo();
  engineName = 'JAVASCRIPT FALLBACK';
}
const input = document.querySelector('#terminal-input');
const recorder = document.querySelector('#recorder-output');
const liveHex = document.querySelector('#live-hex-output');
const result = document.querySelector('#result');
const child = document.querySelector('#child-output');
const runs = document.querySelector('#erase-runs');
const hex = document.querySelector('#hex-output');
const status = document.querySelector('#status');
const copy = document.querySelector('#copy-report');
document.querySelector('#engine-badge').textContent = engineName;

function focusEnd() {
  input.focus();
  input.setSelectionRange(input.value.length, input.value.length);
}

function render() {
  input.value = demo.visible;
  recorder.textContent = demo.compressedComposition();
  liveHex.textContent = demo.hexDump();
  const counts = demo.eraseRuns();
  status.textContent = demo.committed === null
    ? `${counts.reduce((sum, count) => sum + count, 0)} visual erase triplets retained so far`
    : 'Recording frozen in browser memory';
  if (demo.committed !== null) {
    result.hidden = false;
    child.textContent = `<${demo.committed}>`;
    runs.textContent = counts.length
      ? `${counts.join(' + ')} = ${counts.reduce((sum, count) => sum + count, 0)} triplets`
      : 'No 08 20 08 run was detected.';
    hex.textContent = demo.hexDump();
    input.disabled = true;
    copy.disabled = false;
  }
}

input.addEventListener('keydown', event => {
  if (event.metaKey || event.ctrlKey || event.altKey) return;
  if (event.key === 'Backspace') {
    event.preventDefault();
    demo.backspace();
    render();
    return;
  }
  if (event.key === 'Enter') {
    event.preventDefault();
    demo.commit();
    render();
    return;
  }
  if (event.key.length === 1) {
    event.preventDefault();
    demo.type(event.key);
    render();
  }
});

input.addEventListener('paste', event => {
  event.preventDefault();
  demo.type(event.clipboardData.getData('text/plain'));
  render();
});

input.addEventListener('click', focusEnd);
input.addEventListener('focus', focusEnd);
document.querySelector('#reset').addEventListener('click', () => {
  demo.reset();
  input.disabled = false;
  result.hidden = true;
  copy.disabled = true;
  child.textContent = '';
  runs.textContent = '';
  hex.textContent = '';
  render();
  focusEnd();
});

copy.addEventListener('click', async () => {
  await navigator.clipboard.writeText(demo.report());
  copy.textContent = 'Copied';
  setTimeout(() => { copy.textContent = 'Copy report'; }, 1200);
});

render();
focusEnd();
