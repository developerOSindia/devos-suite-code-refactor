"""
Unit tests for suite-code-refactor regex engine.
"""

import sys
import unittest
import re
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.regex_engine import test_regex_pattern, replace_regex_pattern


class TestRegex(unittest.TestCase):
    def test_basic_match(self):
        res = test_regex_pattern(r"\d+", "DeveloperOS 2026 Tools v2")
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["match_count"], 2)
        self.assertEqual(res["matches"][0]["matched_text"], "2026")
        self.assertEqual(res["matches"][1]["matched_text"], "2")

    def test_capture_groups(self):
        res = test_regex_pattern(r"(\w+)@([\w\.]+)", "contact: kalash@developeros.in")
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["match_count"], 1)
        self.assertEqual(res["matches"][0]["groups"], ("kalash", "developeros.in"))

    def test_named_capture_groups(self):
        res = test_regex_pattern(r"(?P<year>\d{4})-(?P<month>\d{2})", "Date: 2026-10")
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["matches"][0]["group_dict"], {"year": "2026", "month": "10"})

    def test_case_insensitive_flag(self):
        res = test_regex_pattern(r"developer", "DEVELOPEROS is great", flags=re.IGNORECASE)
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["match_count"], 1)

    def test_invalid_syntax(self):
        res = test_regex_pattern(r"(unclosed_group", "some text")
        self.assertFalse(res["is_valid"])
        self.assertIn("Invalid regular expression", res["error"])

    def test_empty_pattern(self):
        res = test_regex_pattern("", "sample text")
        self.assertFalse(res["is_valid"])
        self.assertEqual(res["error"], "Pattern cannot be empty.")

    def test_regex_replace(self):
        res = replace_regex_pattern(r"\s+", "-", "DeveloperOS Modern Suite")
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["result"], "DeveloperOS-Modern-Suite")
        self.assertEqual(res["substitution_count"], 2)

    def test_regex_replace_invalid_pattern(self):
        res = replace_regex_pattern(r"[broken", "", "sample")
        self.assertFalse(res["is_valid"])
        self.assertIn("Invalid regular expression", res["error"])


if __name__ == "__main__":
    unittest.main()
