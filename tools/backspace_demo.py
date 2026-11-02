#!/usr/bin/env python3
"""Run a temporary macOS output-only terminal-recording demonstration."""

from __future__ import annotations

import hashlib
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ERASE_TRIPLET = b"\x08 \x08"
CHILD_MARKER = b"CHILD PROCESS RECEIVED ONLY:"


def erase_runs(data: bytes) -> list[int]:
    runs: list[int] = []
    index = 0
    while index < len(data):
        if not data.startswith(ERASE_TRIPLET, index):
            index += 1
            continue
        count = 0
        while data.startswith(ERASE_TRIPLET, index):
            count += 1
            index += len(ERASE_TRIPLET)
        runs.append(count)
    return runs


def composition_bytes(data: bytes) -> bytes:
    return data.split(CHILD_MARKER, 1)[0].rstrip(b"\r\n")


def committed_line(data: bytes) -> str | None:
    match = re.search(rb"CHILD PROCESS RECEIVED ONLY:\r?\n<([^>]*)>", data)
    return match.group(1).decode("utf-8", "replace") if match else None


def compressed_view(data: bytes) -> str:
    source = composition_bytes(data)
    output: list[str] = []
    index = 0
    while index < len(source):
        if source.startswith(ERASE_TRIPLET, index):
            count = 0
            while source.startswith(ERASE_TRIPLET, index):
                count += 1
                index += len(ERASE_TRIPLET)
            output.append(f"[08 20 08 x {count}]")
            continue
        byte = source[index]
        if byte in (10, 13):
            output.append("\n")
        elif 32 <= byte < 127:
            output.append(chr(byte))
        else:
            output.append(f"<{byte:02X}>")
        index += 1
    return "".join(output)


def run_demo() -> int:
    if platform.system() != "Darwin" or not Path("/usr/bin/script").is_file():
        print("This one-line demonstration currently supports macOS Terminal.", file=sys.stderr)
        return 2
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        print("Run this demonstration interactively in Terminal.", file=sys.stderr)
        return 2

    print("BACKSPACE GATE — ONE-LINE TERMINAL DEMO")
    print("Output-only recorder · canonical line editing · temporary local file")
    print()
    print("Use synthetic, non-sensitive ASCII text. The temporary transcript is deleted")
    print("after the result is displayed.")
    print()
    print("At the > prompt:")
    print("  1. Type any harmless draft, but do not press Return.")
    print("  2. Erase it completely with the backward-edit key.")
    print("  3. Type a different harmless line and press Return once.")
    print()

    with tempfile.TemporaryDirectory(prefix="backspace-gate-demo-") as directory:
        transcript = Path(directory) / "demo.typescript"
        child = (
            'printf "> "; IFS= read -r committed; '
            'printf "\\nCHILD PROCESS RECEIVED ONLY:\\n<%s>\\n" "$committed"'
        )
        result = subprocess.run(
            ["/usr/bin/script", "-q", str(transcript), "/bin/zsh", "-f", "-c", child],
            check=False,
        )
        if result.returncode:
            print(f"Recorder exited with status {result.returncode}.", file=sys.stderr)
            return result.returncode
        data = transcript.read_bytes()
        runs = erase_runs(composition_bytes(data))

        print()
        print("RECORDER-RETAINED COMPOSITION HISTORY")
        print(compressed_view(data))
        print()
        print(f"VISUAL-ERASE RUNS: {runs or 'none detected'}")
        print(f"TOTAL 08 20 08 TRIPLETS: {sum(runs)}")
        print()
        print("CHILD PROCESS RECEIVED ONLY")
        print(f"<{committed_line(data) or 'not found'}>")
        print()
        print("Visual disappearance changed the screen and future child input; it did")
        print("not retract the earlier echo from the sequential output recording.")
        print(f"Temporary transcript SHA-256: {hashlib.sha256(data).hexdigest()}")
        print("Temporary transcript deleted on exit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_demo())
