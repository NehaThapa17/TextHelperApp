import streamlit as st
from datetime import datetime
from text_utils import (
    to_upper, to_lower, strip_spaces, replace_text,
    count_substring, get_text_stats, append_text
)

st.set_page_config(page_title="Text File String Editor", page_icon="📝", layout="centered")
st.title("📝 Text File String Editor")

# ---- File Upload ----
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file:
    # Initialize text in session_state only once
    if "original_text" not in st.session_state:
        st.session_state.original_text = uploaded_file.read().decode("utf-8")
        st.session_state.edited_text = st.session_state.original_text

    # ---- Mode Selection ----
    st.sidebar.header("Mode Settings")
    mode = st.sidebar.selectbox("Select Mode", ["Open Mode", "Preview Mode"])

    if mode == "Open Mode":
        st.subheader("🔧 Open Mode")
        sub_mode = st.radio("Select Sub Mode", ["Read", "Append"])

        # --- String operations ---
        st.markdown("### String Operations")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("UPPERCASE"):
                st.session_state.edited_text = to_upper(st.session_state.edited_text)
            if st.button("lowercase"):
                st.session_state.edited_text = to_lower(st.session_state.edited_text)

        with col2:
            if st.button("strip (remove spaces)"):
                st.session_state.edited_text = strip_spaces(st.session_state.edited_text)

        with col3:
            st.markdown("**Replace Text**")
            old = st.text_input("Old text", key="old")
            new = st.text_input("New text", key="new")
            if st.button("Replace"):
                st.session_state.edited_text = replace_text(st.session_state.edited_text, old, new)

        substring = st.text_input("Count substring occurrences", key="count")
        if st.button("Count"):
            count = count_substring(st.session_state.edited_text, substring)
            st.info(f"'{substring}' appears {count} times.")

        st.text_area("File Content", st.session_state.edited_text, height=300)

        # ---- Append Mode Save ----
        if sub_mode == "Append":
            st.markdown("---")
            extra_text = st.text_area("Extra text to append:", height=100)
            if st.button("Save Edited File"):
                final_text = append_text(st.session_state.edited_text, extra_text)
                st.download_button(
                    label="Download Edited File",
                    data=final_text.encode("utf-8"),
                    file_name=f"edited_{uploaded_file.name}",
                    mime="text/plain"
                )

    elif mode == "Preview Mode":
        st.subheader("👀 Preview Mode")
        lines = st.session_state.original_text.splitlines()
        preview = "\n".join(lines[:20])
        st.text_area("Preview (first 20 lines):", preview, height=300)
        stats = get_text_stats(st.session_state.original_text)
        st.markdown(
            f"**Line Count:** {stats['line_count']}  \n"
            f"**Word Count:** {stats['word_count']}  \n"
            f"**Character Count:** {stats['char_count']}"
        )

else:
    st.warning("Please upload a valid .txt file.")
