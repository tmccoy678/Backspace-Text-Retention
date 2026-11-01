const ENCODER = new TextEncoder();
const ERASE = [0x08, 0x20, 0x08];
const CHILD_MARKER = '\r\n\r\nCHILD PROCESS RECEIVED ONLY:\r\n';

function encoded(text) {
  return [...ENCODER.encode(text)];
}

export class TerminalRecorderDemo {
  constructor() {
    this.reset();
  }

  reset() {
    this.visible = '';
    this.committed = null;
    this.bytes = encoded('> ');
    this.compositionEnd = null;
  }

  type(text) {
    if (this.committed !== null || !text) return;
    const oneLine = text.replace(/[\r\n]/g, ' ');
    this.visible += oneLine;
    this.bytes.push(...encoded(oneLine));
  }

  backspace() {
    if (this.committed !== null || !this.visible) return false;
    this.visible = [...this.visible].slice(0, -1).join('');
    this.bytes.push(...ERASE);
    return true;
  }

  commit() {
    if (this.committed !== null) return this.committed;
    this.committed = this.visible;
    this.bytes.push(0x0d, 0x0a);
    this.compositionEnd = this.bytes.length;
    this.bytes.push(...encoded(`${CHILD_MARKER}<${this.committed}>\r\n`));
    return this.committed;
  }

  compositionBytes() {
    return this.bytes.slice(0, this.compositionEnd ?? this.bytes.length);
  }

  eraseRuns() {
    const data = this.compositionBytes();
    const runs = [];
    for (let index = 0; index < data.length;) {
      if (data[index] !== ERASE[0] || data[index + 1] !== ERASE[1] || data[index + 2] !== ERASE[2]) {
        index += 1;
        continue;
      }
      let count = 0;
      while (data[index] === ERASE[0] && data[index + 1] === ERASE[1] && data[index + 2] === ERASE[2]) {
        count += 1;
        index += ERASE.length;
      }
      runs.push(count);
    }
    return runs;
  }

  compressedComposition() {
    const data = this.compositionBytes();
    const output = [];
    for (let index = 0; index < data.length;) {
      if (data[index] === ERASE[0] && data[index + 1] === ERASE[1] && data[index + 2] === ERASE[2]) {
        let count = 0;
        while (data[index] === ERASE[0] && data[index + 1] === ERASE[1] && data[index + 2] === ERASE[2]) {
          count += 1;
          index += ERASE.length;
        }
        output.push(`[08 20 08 × ${count}]`);
        continue;
      }
      const byte = data[index++];
      if (byte === 0x0d || byte === 0x0a) output.push('\n');
      else if (byte >= 0x20 && byte < 0x7f) output.push(String.fromCharCode(byte));
      else output.push(`\\x${byte.toString(16).padStart(2, '0')}`);
    }
    return output.join('').replace(/\n+/g, '\n').trimEnd();
  }

  hexDump() {
    const rows = [];
    for (let offset = 0; offset < this.bytes.length; offset += 16) {
      const chunk = this.bytes.slice(offset, offset + 16);
      const hex = chunk.map(byte => byte.toString(16).padStart(2, '0')).join(' ').padEnd(47);
      const ascii = chunk.map(byte => byte >= 0x20 && byte < 0x7f ? String.fromCharCode(byte) : '.').join('');
      rows.push(`${offset.toString(16).padStart(8, '0')}  ${hex}  |${ascii}|`);
    }
    return rows.join('\n');
  }

  report() {
    const runs = this.eraseRuns();
    return [
      'RECORDER-RETAINED COMPOSITION HISTORY',
      this.compressedComposition(),
      '',
      `VISUAL-ERASE RUNS: ${runs.length ? runs.join(', ') : 'none detected'}`,
      `TOTAL 08 20 08 TRIPLETS: ${runs.reduce((sum, count) => sum + count, 0)}`,
      '',
      'CHILD PROCESS RECEIVED ONLY',
      `<${this.committed ?? 'not committed'}>`,
      '',
      'RAW BYTE TRANSCRIPT',
      this.hexDump(),
    ].join('\n');
  }
}
