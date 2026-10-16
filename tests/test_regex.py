"""
Unit tests for suite-code-refactor business logic.
"""

import sys
import unittest
from pathlib import Path

# Ensure suite root is in sys.path
SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.regex_engine import test_regex_pattern


class TestRegexEngine(unittest.TestCase):
    def test_valid_pattern_match(self):
        text = "Contact us at support@developeros.in or team@developeros.in"
        pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
        res = test_regex_pattern(pattern, text)
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["match_count"], 2)
        self.assertEqual(res["matches"][0]["matched_text"], "support@developeros.in")

    def test_invalid_pattern(self):
        res = test_regex_pattern("([a-z", "sample")
        self.assertFalse(res["is_valid"])
        self.assertIn("Invalid regular expression", res["error"])


if __name__ == "__main__":
    unittest.main()
