from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import inspect_typescript  # noqa: E402


class InspectTypescriptTests(unittest.TestCase):
    def test_finds_contiguous_erase_run(self) -> None:
        data = b"first" + (b"\x08 \x08" * 3) + b"second"
        self.assertEqual(inspect_typescript.erase_runs(data), [(5, 14, 3)])

    def test_structured_foundation_recording_identity_and_count(self) -> None:
        path = ROOT / "evidence/transcripts/Blu-Offline-20260921-153748.typescript"
        data = path.read_bytes()
        self.assertEqual(len(data), 1344)
        self.assertEqual(
            inspect_typescript.sha256(data),
            "e2e3e56c7f81420a870501594e55aa908ef63c01d46794ef2072e9123014f016",
        )
        self.assertIn((1010, 1055, 15), inspect_typescript.erase_runs(data))

    def test_first_published_precontrol_identity_and_erase_runs(self) -> None:
        path = ROOT / "evidence/transcripts/Blu-Offline-20260921-141327.typescript"
        data = path.read_bytes()
        self.assertEqual(len(data), 1190)
        self.assertEqual(
            inspect_typescript.sha256(data),
            "5cc08346d7de25988aa687d292eefc1bf994ba74d5031ff9b0cd7e3fc271cb5e",
        )
        self.assertIn(
            b"My harmless target sentence is: [WRITE YOUR SENTENCE HERE].", data
        )
        self.assertEqual(
            inspect_typescript.erase_runs(data),
            [(1058, 1073, 5), (1078, 1168, 30)],
        )

    def test_first_recognized_substantive_identity_and_erase_runs(self) -> None:
        path = ROOT / "evidence/transcripts/Blu-Offline-20260921-141944.typescript"
        data = path.read_bytes()
        self.assertEqual(len(data), 1816)
        self.assertEqual(
            inspect_typescript.sha256(data),
            "7175aea528876898938e13eb98432f0b0e7bc8170e9c62fb3fadecf80126b375",
        )
        self.assertEqual(
            inspect_typescript.erase_runs(data),
            [
                (1006, 1039, 11),
                (1056, 1095, 13),
                (1120, 1207, 29),
                (1220, 1226, 2),
                (1235, 1268, 11),
                (1308, 1314, 2),
                (1328, 1331, 1),
            ],
        )

    def test_caret_render_is_explicitly_a_representation(self) -> None:
        self.assertEqual(inspect_typescript.caret_render(b"A\x08 \x08B"), "A^H ^HB")

    def test_first_recognized_substantive_run_resolves_to_committed_line(self) -> None:
        path = (
            ROOT
            / "evidence"
            / "transcripts"
            / "Blu-Offline-20260921-141944.typescript"
        )
        data = path.read_bytes()
        start = data.index(b"\r\n> ") + len(b"\r\n> ")
        composition = data[start : data.index(b"\r\n", start)]
        screen: list[int] = []
        cursor = 0

        for byte in composition:
            if byte == 0x08:
                cursor = max(0, cursor - 1)
            elif 0x20 <= byte <= 0x7E:
                if cursor == len(screen):
                    screen.append(byte)
                else:
                    screen[cursor] = byte
                cursor += 1

        self.assertEqual(
            bytes(screen[:cursor]),
            b"marie is my favorite doberman and she is sleeping on the couch.",
        )


if __name__ == "__main__":
    unittest.main()
