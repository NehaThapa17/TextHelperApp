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
    text = uploaded_file.read().decode("utf-8")

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
                text = to_upper(text)
            if st.button("lowercase"):
                text = to_lower(text)
        with col2:
            if st.button("strip (remove spaces)"):
                text = strip_spaces(text)
        with col3:
            st.markdown("**Replace Text**")
            old = st.text_input("Old text", key="old")
            new = st.text_input("New text", key="new")
            if st.button("Replace"):
                text = replace_text(text, old, new)
        
        substring = st.text_input("Count substring occurrences", key="count")
        if st.button("Count"):
            count = count_substring(text, substring)
            st.info(f"'{substring}' appears {count} times.")

        st.text_area("File Content", text, height=300)

        # ---- Append Mode Save ----
        if sub_mode == "Append":
            st.markdown("---")
            extra_text = st.text_area("Extra text to append:", height=100)
            if st.button("Save Edited File"):
                edited_text = append_text(text, extra_text)
                st.download_button(
                    label="Download Edited File",
                    data=edited_text.encode("utf-8"),
                    file_name=f"edited_{uploaded_file.name}",
                    mime="text/plain"
                )

    elif mode == "Preview Mode":
        st.subheader("👀 Preview Mode")
        lines = text.splitlines()
        preview = "\n".join(lines[:20])
        st.text_area("Preview (first 20 lines):", preview, height=300)
        stats = get_text_stats(text)
        st.markdown(f"**Line Count:** {stats['line_count']}  \n"
                    f"**Word Count:** {stats['word_count']}  \n"
                    f"**Character Count:** {stats['char_count']}")

else:
    st.warning("Please upload a valid .txt file.")
