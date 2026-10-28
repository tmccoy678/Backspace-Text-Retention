from copy import deepcopy
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "analysis"))

import summarize_trials  # noqa: E402


class SummarizeTrialsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = summarize_trials.load_rows()

    def test_declared_counts(self) -> None:
        result = summarize_trials.summarize(self.rows)
        self.assertEqual(result["canonical"]["model_exact_marker"], (0, 6))
        self.assertEqual(result["raw"]["model_exact_marker"], (6, 6))
        self.assertEqual(result["canonical"]["transcript_input_echo"], (6, 6))
        self.assertEqual(result["raw"]["transcript_input_echo"], (0, 6))
        self.assertEqual(result["canonical"]["model_none"], (6, 6))
        self.assertEqual(result["raw"]["model_none"], (0, 6))

    def test_rejects_unknown_condition(self) -> None:
        rows = deepcopy(self.rows)
        rows[0]["condition"] = "mystery"
        with self.assertRaisesRegex(ValueError, "Unknown condition"):
            summarize_trials.summarize(rows)

    def test_rejects_duplicate_and_missing_trial_pair(self) -> None:
        rows = deepcopy(self.rows)
        rows[1]["trial"] = "1"
        with self.assertRaisesRegex(ValueError, "Duplicate trial"):
            summarize_trials.summarize(rows)

    def test_rejects_missing_trial_row(self) -> None:
        with self.assertRaisesRegex(ValueError, "Expected 12 rows"):
            summarize_trials.summarize(self.rows[:-1])

    def test_rejects_nonbinary_endpoint(self) -> None:
        rows = deepcopy(self.rows)
        rows[0]["model_exact_marker"] = "2"
        with self.assertRaisesRegex(ValueError, "model_exact_marker"):
            summarize_trials.summarize(rows)

    def test_rejects_blank_endpoint(self) -> None:
        rows = deepcopy(self.rows)
        rows[0]["model_none"] = ""
        with self.assertRaisesRegex(ValueError, "model_none"):
            summarize_trials.summarize(rows)

    def test_rejects_missing_column(self) -> None:
        rows = deepcopy(self.rows)
        del rows[0]["marker"]
        with self.assertRaisesRegex(ValueError, "Missing required column.*marker"):
            summarize_trials.summarize(rows)

    def test_rejects_marker_pair_mismatch(self) -> None:
        rows = deepcopy(self.rows)
        rows[6]["marker"] = "DIFFERENT_MARKER"
        with self.assertRaisesRegex(ValueError, "Marker mismatch"):
            summarize_trials.summarize(rows)

    def test_rejects_marker_reuse_across_trials(self) -> None:
        rows = deepcopy(self.rows)
        rows[1]["marker"] = rows[0]["marker"]
        rows[7]["marker"] = rows[6]["marker"]
        with self.assertRaisesRegex(ValueError, "Marker reused"):
            summarize_trials.summarize(rows)

    def test_rejects_paired_marker_outside_preregistered_sequence(self) -> None:
        rows = deepcopy(self.rows)
        rows[0]["marker"] = "NOT_THE_PREREGISTERED_MARKER"
        rows[6]["marker"] = "NOT_THE_PREREGISTERED_MARKER"
        with self.assertRaisesRegex(ValueError, "preregistered marker"):
            summarize_trials.summarize(rows)

    def test_rejects_invalid_clear_schedule(self) -> None:
        rows = deepcopy(self.rows)
        rows[0]["clear_before_trial"] = "1"
        with self.assertRaisesRegex(ValueError, "clear_before_trial"):
            summarize_trials.summarize(rows)

        rows = deepcopy(self.rows)
        rows[1]["clear_before_trial"] = "NA"
        with self.assertRaisesRegex(ValueError, "clear_before_trial"):
            summarize_trials.summarize(rows)


if __name__ == "__main__":
    unittest.main()
