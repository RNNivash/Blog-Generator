import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# 🧠 Configure Gemini API
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 🔄 Function to generate blog content
def get_gemini_response(input_text, no_words, blog_style):
    prompt = f"""
    Write a blog in the style of a {blog_style} on the topic "{input_text}".
    The blog should be concise and within {no_words} words.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# 🖼️ Streamlit App Interface
st.set_page_config(page_title="Blog Generator 🤖",
                   page_icon="🧠",
                   layout="centered")

st.title("🧠 Generate Blog with Gemini")
st.caption("© Nivash R N | 2025")

input_text = st.text_input("Enter Blog Topic")

col1, col2 = st.columns(2)

with col1:
    no_words = st.text_input("No. of Words", "100")
with col2:
    blog_style = st.selectbox("Writing for:", ["Researchers", "Data Scientist", "Common People"])

if st.button("Generate"):
    if input_text.strip() == "" or no_words.strip() == "":
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Generating..."):
            result = get_gemini_response(input_text, no_words, blog_style)
            st.subheader("📝 Generated Blog:")
            st.write(result)