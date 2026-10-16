"""
DeveloperOS Code Refactoring Suite - Interactive Application
"""

import streamlit as st
from core.regex_engine import test_regex_pattern
from ui.components import render_suite_header, render_suite_footer, render_main_promotional_banner

st.set_page_config(
    page_title="DeveloperOS - Code Refactor Suite",
    page_icon="💻",
    layout="wide",
)


def main():
    render_suite_header(
        title="Regular Expression Tester & Match Inspector",
        description="Test regular expressions interactively against sample text with real-time match group extraction.",
    )

    pattern = st.text_input("Regular Expression (Pattern):", value=r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    sample_text = st.text_area(
        "Test String:",
        value="Send an email to support@developeros.in or security@developeros.in for assistance.",
        height=100,
    )

    if pattern and sample_text:
        res = test_regex_pattern(pattern, sample_text)

        if res["is_valid"]:
            st.success(f"Matched {res['match_count']} occurrence(s).")
            for idx, match in enumerate(res["matches"], 1):
                st.markdown(f"**Match #{idx}:** `{match['matched_text']}` (Span: {match['start']}–{match['end']})")
                if match["groups"]:
                    st.caption(f"Capture groups: {match['groups']}")
        else:
            st.error(res["error"])

    render_main_promotional_banner()
    render_suite_footer()


if __name__ == "__main__":
    main()
