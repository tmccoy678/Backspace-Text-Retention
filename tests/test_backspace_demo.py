import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "backspace_demo.py"
SPEC = importlib.util.spec_from_file_location("backspace_demo", MODULE_PATH)
assert SPEC and SPEC.loader
demo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(demo)


class BackspaceDemoTests(unittest.TestCase):
    def test_compresses_runs_and_separates_child_input(self):
        data = (
            b"> erased draft"
            + demo.ERASE_TRIPLET * 12
            + b"committed\r\n\r\nCHILD PROCESS RECEIVED ONLY:\r\n<committed>\r\n"
        )
        self.assertEqual(demo.erase_runs(demo.composition_bytes(data)), [12])
        self.assertIn("[08 20 08 x 12]", demo.compressed_view(data))
        self.assertEqual(demo.committed_line(data), "committed")

    def test_preserves_multiple_correction_runs(self):
        data = b"> typo" + demo.ERASE_TRIPLET + b"e" + demo.ERASE_TRIPLET * 5 + b"final"
        self.assertEqual(demo.erase_runs(data), [1, 5])
        self.assertEqual(demo.compressed_view(data).count("[08 20 08 x"), 2)


if __name__ == "__main__":
    unittest.main()
