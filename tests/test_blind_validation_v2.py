from __future__ import annotations

import csv
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "analysis" / "blind_validation_v2.R"
FIELDNAMES = (
    "fixture",
    "exact_recovery",
    "character_matches",
    "target_length",
    "recovered_erase_triplets",
    "erase_exact",
)


def valid_rows() -> list[dict[str, object]]:
    return [
        {
            "fixture": f"blind-v2-{number:02d}.typescript",
            "exact_recovery": 1,
            "character_matches": 15,
            "target_length": 15,
            "recovered_erase_triplets": 15,
            "erase_exact": 1,
        }
        for number in range(1, 11)
    ]


class BlindValidationV2Tests(unittest.TestCase):
    def run_analysis(
        self,
        rows: list[dict[str, object]],
        *,
        fieldnames: tuple[str, ...] = FIELDNAMES,
    ) -> tuple[subprocess.CompletedProcess[str], Path, tempfile.TemporaryDirectory[str]]:
        tempdir = tempfile.TemporaryDirectory()
        root = Path(tempdir.name)
        csv_path = root / "results.csv"
        output_dir = root / "output"
        with csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        result = subprocess.run(
            ["Rscript", str(SCRIPT), str(csv_path), str(output_dir)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        return result, output_dir, tempdir

    def assert_invalid(
        self,
        rows: list[dict[str, object]],
        expected_message: str,
        *,
        fieldnames: tuple[str, ...] = FIELDNAMES,
    ) -> None:
        result, output_dir, tempdir = self.run_analysis(rows, fieldnames=fieldnames)
        self.addCleanup(tempdir.cleanup)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(expected_message, result.stderr)
        self.assertFalse(
            output_dir.exists(),
            "invalid input must be rejected before the output directory is created",
        )

    def test_valid_ten_fixture_input_writes_expected_outputs(self) -> None:
        result, output_dir, tempdir = self.run_analysis(valid_rows())
        self.addCleanup(tempdir.cleanup)
        self.assertEqual(result.returncode, 0, result.stderr)
        summary_path = output_dir / "r-summary.csv"
        report_path = output_dir / "r-binom-test.txt"
        self.assertTrue(summary_path.is_file())
        self.assertTrue(report_path.is_file())

        with summary_path.open(encoding="utf-8", newline="") as handle:
            summary = {row["metric"]: row["value"] for row in csv.DictReader(handle)}
        self.assertEqual(summary["fixtures_exact"], "10")
        self.assertEqual(summary["fixtures_total"], "10")
        self.assertEqual(summary["character_matches_descriptive"], "150")
        self.assertEqual(summary["character_positions_descriptive"], "150")
        self.assertEqual(summary["erase_counts_exact"], "10")
        self.assertIn(
            "number of successes = 10",
            report_path.read_text(encoding="utf-8"),
        )

    def test_valid_nonexact_results_are_counted_without_being_rejected(self) -> None:
        rows = valid_rows()
        rows[0].update(
            exact_recovery=0,
            character_matches=14,
            recovered_erase_triplets=14,
            erase_exact=0,
        )
        result, output_dir, tempdir = self.run_analysis(rows)
        self.addCleanup(tempdir.cleanup)
        self.assertEqual(result.returncode, 0, result.stderr)
        with (output_dir / "r-summary.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            summary = {row["metric"]: row["value"] for row in csv.DictReader(handle)}
        self.assertEqual(summary["fixtures_exact"], "9")
        self.assertEqual(summary["erase_counts_exact"], "9")

    def test_missing_required_column_is_rejected(self) -> None:
        fields = tuple(field for field in FIELDNAMES if field != "target_length")
        self.assert_invalid(
            valid_rows(),
            "missing required column(s): target_length",
            fieldnames=fields,
        )

    def test_wrong_fixture_counts_are_rejected(self) -> None:
        for count in (0, 9, 11):
            with self.subTest(count=count):
                rows = valid_rows()
                if count == 0:
                    rows = []
                elif count == 9:
                    rows = rows[:9]
                else:
                    rows.append({**rows[-1], "fixture": "blind-v2-11.typescript"})
                self.assert_invalid(rows, "expected exactly 10 fixture rows")

    def test_duplicate_fixture_is_rejected(self) -> None:
        rows = valid_rows()
        rows[-1]["fixture"] = rows[0]["fixture"]
        self.assert_invalid(rows, "fixture values must be unique")

    def test_fixture_set_must_match_the_preregistered_names(self) -> None:
        rows = valid_rows()
        rows[-1]["fixture"] = "blind-v2-11.typescript"
        self.assert_invalid(
            rows,
            "fixture values must be exactly blind-v2-01.typescript through blind-v2-10.typescript",
        )

    def test_na_and_nonbinary_endpoints_are_rejected(self) -> None:
        for column, value in (
            ("exact_recovery", "NA"),
            ("exact_recovery", 2),
            ("erase_exact", ""),
            ("erase_exact", -1),
        ):
            with self.subTest(column=column, value=value):
                rows = valid_rows()
                rows[0][column] = value
                self.assert_invalid(rows, f"{column} must contain only 0 or 1")

    def test_character_matches_must_be_within_target(self) -> None:
        for value in (-1, 16):
            with self.subTest(value=value):
                rows = valid_rows()
                rows[0]["character_matches"] = value
                self.assert_invalid(
                    rows,
                    "character_matches must be an integer from 0 through target_length",
                )

    def test_target_length_must_match_the_fixed_protocol(self) -> None:
        rows = valid_rows()
        rows[0]["target_length"] = 14
        self.assert_invalid(rows, "target_length must equal 15 for every fixture")

    def test_exact_recovery_must_agree_with_character_matches(self) -> None:
        rows = valid_rows()
        rows[0]["exact_recovery"] = 0
        self.assert_invalid(
            rows,
            "exact_recovery must agree with character_matches == target_length",
        )

    def test_invalid_erase_counts_are_rejected(self) -> None:
        for value, flag, expected in (
            (-1, 0, "recovered_erase_triplets must be a nonnegative integer"),
            (15.5, 0, "recovered_erase_triplets must be a nonnegative integer"),
            (14, 1, "erase_exact must agree with recovered_erase_triplets == 15"),
        ):
            with self.subTest(value=value, flag=flag):
                rows = valid_rows()
                rows[0]["recovered_erase_triplets"] = value
                rows[0]["erase_exact"] = flag
                self.assert_invalid(rows, expected)


if __name__ == "__main__":
    unittest.main()
