"""
Pure business logic for regular expression matching and analysis.
Zero Streamlit or UI dependencies.
"""

import re
from typing import Dict, Any, List


def test_regex_pattern(pattern: str, test_string: str, flags: int = 0) -> Dict[str, Any]:
    """Tests a regular expression against an input string, returning matches and groups."""
    if not pattern:
        return {
            "is_valid": False,
            "error": "Pattern cannot be empty.",
            "match_count": 0,
            "matches": [],
        }

    try:
        compiled = re.compile(pattern, flags)
    except re.error as err:
        return {
            "is_valid": False,
            "error": f"Invalid regular expression: {err.msg}",
            "match_count": 0,
            "matches": [],
        }

    matches_data: List[Dict[str, Any]] = []
    for match in compiled.finditer(test_string):
        matches_data.append({
            "matched_text": match.group(0),
            "start": match.start(),
            "end": match.end(),
            "groups": match.groups(),
        })

    return {
        "is_valid": True,
        "error": None,
        "match_count": len(matches_data),
        "matches": matches_data,
    }
