import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "show_visual_evidence.zsh"


class ShowVisualEvidenceTests(unittest.TestCase):
    def test_runs_from_an_arbitrary_working_directory(self):
        env = os.environ.copy()
        env["TERM"] = "xterm"

        with tempfile.TemporaryDirectory() as workdir:
            completed = subprocess.run(
                ["/bin/zsh", str(SCRIPT)],
                cwd=workdir,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("STRUCTURED FOUNDATION BYTE EVIDENCE", completed.stdout)
        self.assertIn("later structured foundation transcript", completed.stdout)
        self.assertNotIn("discovery transcript", completed.stdout)

    def test_runs_when_term_is_unset(self):
        env = os.environ.copy()
        env.pop("TERM", None)

        with tempfile.TemporaryDirectory() as workdir:
            completed = subprocess.run(
                ["/bin/zsh", str(SCRIPT)],
                cwd=workdir,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("STRUCTURED FOUNDATION BYTE EVIDENCE", completed.stdout)


if __name__ == "__main__":
    unittest.main()
