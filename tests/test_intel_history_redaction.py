from pathlib import Path
import hashlib
import unittest


ROOT = Path(__file__).resolve().parents[1]
HISTORY = (
    ROOT
    / "evidence/intel-history/2015-intel-zsh-history-redacted-2026-10-28.txt"
)


class IntelHistoryRedactionTests(unittest.TestCase):
    def test_line_count_and_relevant_sequence(self) -> None:
        lines = HISTORY.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 78)
        self.assertEqual(
            lines[50],
            "sed -n '28p' ~/Desktop/Blu-Offline-20260921-153748.typescript | cat -v",
        )
        self.assertEqual(lines[51], "he could remarry and inheret her estate.")

    def test_redaction_labels_and_no_silent_line_removal(self) -> None:
        text = HISTORY.read_text(encoding="utf-8")
        self.assertEqual(text.count("REDACTED — PASSWORD-LIKE MATERIAL"), 6)
        self.assertEqual(
            text.count("REDACTED — SSH AUTHORIZATION COMMAND AND PUBLIC KEY"), 1
        )
        self.assertEqual(
            text.count("REDACTED — PRIVATE CONVERSATION IDENTIFIER"), 2
        )
        self.assertNotIn("ssh-ed25519", text)

    def test_published_derivative_identity(self) -> None:
        digest = hashlib.sha256(HISTORY.read_bytes()).hexdigest()
        self.assertEqual(
            digest,
            "6f4d62db2c640748ca29c82009610e0ab58853642d3403e2ee3c97929f0439d8",
        )


if __name__ == "__main__":
    unittest.main()
