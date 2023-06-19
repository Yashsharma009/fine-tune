import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "shivam001/falcon-7b-qlora-chat-supportmodel-bot-faq-dei"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    st.title("Fine-Tuned Model Deployment")
    st.write("Ask a question and get a response!")

    input_text = st.text_input("Enter your question")
    if st.button("Get response"):
        with st.spinner("Generating response..."):
            response = generate_response(input_text)
            st.success(response)

if _name_ == "_main_":
    main()
