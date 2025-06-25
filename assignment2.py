import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyC6_8BSom2-v54CHO7SfNfQIbAr9YQobI8")


# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Streamlit App
st.title("Gemini 2.0 Flash Exp - AI Question Answering")

st.write("Ask anything! The model will generate an AI-based response.")

# General prompt input
prompt = st.text_input("🔍 Enter your question:", "What is Artificial Intelligence?")

# Generate button
if st.button("Generate Answer"):
    response = model.generate_content(prompt)
    st.markdown("### 🤖 Gemini's Answer:")
    st.write(response.text)