import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="HuggingFace Text Summarization")

st.title("🤗 HuggingFace – Text Summarization")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

input_text = st.text_area("Enter text to summarize:")
if st.button("Summarize"):
    if input_text.strip():
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
        st.subheader("📝 Summary")
        st.write(summary[0]["summary_text"])
    else:
        st.error("Please enter some text first!")
