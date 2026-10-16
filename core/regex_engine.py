"""
Pure business logic for regular expression matching and analysis.
Zero Streamlit or UI dependencies.
"""

import re
from typing import Dict, Any, List, Optional


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
    for match in compiled.finditer(test_string or ""):
        matches_data.append({
            "matched_text": match.group(0),
            "start": match.start(),
            "end": match.end(),
            "groups": match.groups(),
            "group_dict": match.groupdict(),
        })

    return {
        "is_valid": True,
        "error": None,
        "match_count": len(matches_data),
        "matches": matches_data,
    }


def replace_regex_pattern(
    pattern: str, replacement: str, test_string: str, flags: int = 0
) -> Dict[str, Any]:
    """Performs regex search and replace with substitution count."""
    if not pattern:
        return {
            "is_valid": False,
            "error": "Pattern cannot be empty.",
            "result": test_string or "",
            "substitution_count": 0,
        }

    try:
        compiled = re.compile(pattern, flags)
        result, count = compiled.subn(replacement or "", test_string or "")
        return {
            "is_valid": True,
            "error": None,
            "result": result,
            "substitution_count": count,
        }
    except re.error as err:
        return {
            "is_valid": False,
            "error": f"Invalid regular expression: {err.msg}",
            "result": test_string or "",
            "substitution_count": 0,
        }
