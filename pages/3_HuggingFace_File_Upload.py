import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="HuggingFace File Upload")

st.title("📂 HuggingFace – File Upload and Summarization")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", text, height=200)
    if st.button("Summarize File"):
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]["summary_text"])
