from pathlib import Path
import hashlib
import unittest


ROOT = Path(__file__).resolve().parents[1]
REPLICATION = ROOT / "replications" / "intel-mac-2026-10-27"
TRANSCRIPT = (
    REPLICATION
    / "evidence"
    / "intel-script-experiment-20261027-231637.typescript"
)
METADATA = (
    REPLICATION
    / "evidence"
    / "intel-script-experiment-20261027-231637.metadata.txt"
)
CHILD_PTY = (
    REPLICATION
    / "evidence"
    / "intel-script-experiment-20261027-231637.child-pty.txt"
)
FIRST_ATTEMPT_OUTPUT = (
    REPLICATION
    / "evidence"
    / "intel-first-ordinary-shell-terminal-saved-output.txt"
)
ERASE = b"\x08\x20\x08"


class IntelReplicationTests(unittest.TestCase):
    def test_first_attempt_output_identity_and_scope(self) -> None:
        data = FIRST_ATTEMPT_OUTPUT.read_bytes()
        self.assertEqual(len(data), 128)
        self.assertEqual(
            hashlib.sha256(data).hexdigest(),
            "a90e2c11eb1e46f275f8dd5ab27ea7ae0aaa2265ef068f19b58004766b2492b8",
        )
        self.assertIn(b"piggy is running", data)
        self.assertIn(b"zsh: command not found: piggy", data)
        self.assertNotIn(b"Script started on", data)

    def test_transcript_identity_and_declared_boundaries(self) -> None:
        data = TRANSCRIPT.read_bytes()
        self.assertEqual(len(data), 353)
        self.assertEqual(
            hashlib.sha256(data).hexdigest(),
            "d416d107b5bc9e19e2819581e7ed5df457088cd3e6d2db6121efd97c4be6bd4f",
        )
        self.assertEqual(data[239:256], b"olivia is my girl")
        self.assertEqual(data[256:307], ERASE * 17)
        self.assertEqual(data[307:320], b"i love olivia")
        self.assertIn(b"CHILD_RECEIVED: i love olivia", data)
        self.assertNotIn(b"CHILD_RECEIVED: olivia is my girl", data)

    def test_metadata_matches_transcript(self) -> None:
        metadata = METADATA.read_text(encoding="utf-8")
        self.assertIn("METHOD=macos-script-canonical-line-edit-v1", metadata)
        self.assertIn("TRANSCRIPT_BYTES=353", metadata)
        self.assertIn(
            "TRANSCRIPT_SHA256="
            "d416d107b5bc9e19e2819581e7ed5df457088cd3e6d2db6121efd97c4be6bd4f",
            metadata,
        )
        self.assertIn("ProductVersion:\t12.7.6", metadata)
        self.assertIn("RELEASE_X86_64 x86_64", metadata)

    def test_child_was_canonical_with_echo_and_erase(self) -> None:
        child = CHILD_PTY.read_text(encoding="utf-8")
        self.assertIn("lflags: icanon", child)
        self.assertIn(" echo ", child)
        self.assertIn("erase = ^?", child)


if __name__ == "__main__":
    unittest.main()
