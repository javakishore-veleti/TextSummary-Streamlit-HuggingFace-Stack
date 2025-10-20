from transformers import pipeline, set_seed
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from tqdm import tqdm
import torch
import streamlit as st

nltk.download("punkt")

device = "cude" if torch.cuda.is_available() else "cpu"
print("f Using Device: {device}")

model_name = "google/pegasus-cnn_dailymail"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

dataset_samsum = load_dataset("samsum")


def convert_examples_to_features(example_batch):
    input_encodings = tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

    with tokenizer.as_target_tokenizer():
        target_encodings = tokenizer(example_batch["summary"], max_length=128, truncation=True)

    return {
        "input_ids": input_encodings["input_ids"],
        "attention_mask": input_encodings["attention_mask"],
        "labels": target_encodings["input_ids"]
    }

st.set_page_config(page_title="Google Pegasus CNN DailyMail Summarization")
st.title("📰 Google Pegasus CNN DailyMail – Text Summarization")