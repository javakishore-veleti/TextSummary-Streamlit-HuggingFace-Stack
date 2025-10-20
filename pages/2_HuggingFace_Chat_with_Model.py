import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(page_title="HuggingFace Chat")

st.title("💬 HuggingFace – Chat with Model")

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

user_input = st.text_input("Ask something:")
if st.button("Send"):
    if user_input:
        input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        output = model.generate(input_ids, max_length=500, pad_token_id=tokenizer.eos_token_id)
        st.write(tokenizer.decode(output[0], skip_special_tokens=True))
    else:
        st.warning("Please type a message.")
