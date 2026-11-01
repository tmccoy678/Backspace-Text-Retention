import assert from 'node:assert/strict';
import {test} from 'node:test';
import {TerminalRecorderDemo} from '../docs/demo-engine.mjs';

test('browser demo reproduces the three-run live demonstration', () => {
  const demo = new TerminalRecorderDemo();
  demo.type('Jimmy Neutrom');
  demo.backspace();
  demo.type('n: Boy Genius');
  for (let index = 0; index < 25; index += 1) demo.backspace();
  demo.type('F');
  demo.backspace();
  demo.type('The Sims 2: Night life');
  demo.commit();

  assert.deepEqual(demo.eraseRuns(), [1, 25, 1]);
  assert.equal(demo.committed, 'The Sims 2: Night life');
  assert.match(demo.compressedComposition(), /Jimmy Neutrom\[08 20 08 × 1\]n: Boy Genius/);
  assert.match(demo.report(), /TOTAL 08 20 08 TRIPLETS: 27/);
  assert.match(demo.hexDump(), /08 20 08/);
});

test('browser demo resets without retaining prior composition', () => {
  const demo = new TerminalRecorderDemo();
  demo.type('private synthetic draft');
  demo.backspace();
  demo.reset();
  assert.equal(demo.visible, '');
  assert.equal(demo.committed, null);
  assert.equal(demo.compressedComposition(), '>');
  assert.deepEqual(demo.eraseRuns(), []);
});
