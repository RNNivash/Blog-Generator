
# 🤖 Gemini Blog Generator 🧠

Generate custom, professional blog content instantly using **Google's Gemini Flash 1.5** — a lightning-fast LLM from Google AI — all in a simple and clean Streamlit web app.
<img width="1029" alt="Image" src="https://github.com/user-attachments/assets/36947b36-75e5-44df-aa24-8f361e4d10c9" />
---

## 📌 Project Overview

The **Gemini Flash Blog Generator** is a Streamlit-based app that allows users to:

- ✍️ Input a blog topic
- 🧑‍🏫 Choose a writing style (Researchers, Data Scientists, Common People)
- 🔢 Specify a word count limit

Using this input, it generates a concise and intelligent blog using **Gemini Flash 1.5** via Google's Generative AI SDK.

---

## 🚀 Features

- 🚄 Powered by **Gemini Flash 1.5** (fast & cost-efficient)
- 📄 Custom blog generation on any topic
- 🧠 Role-specific writing tone
- ✅ Streamlit UI with clean layout
- 🔐 Secure API key integration (via `.env` or direct env variable)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-flash-blog-generator.git
cd gemini-flash-blog-generator
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can run:

```bash
pip install streamlit google-generativeai python-dotenv
```

---

### 3. Set Your Gemini API Key

Get your API key from:  
👉 [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

#### Option A: Using `.env` (recommended)

1. Create a file named `.env` in the root directory:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

2. Make sure `app.py` loads the key like this:
```python
from dotenv import load_dotenv
load_dotenv()
```

#### Option B: Hardcode in `app.py`

```python
import os
os.environ["GOOGLE_API_KEY"] = "your_actual_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

The app will launch in your default browser at `http://localhost:8501`

---

## 📂 Project Structure

```
gemini-flash-blog-generator/
├── app.py               # Streamlit application
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── .env                 # API key file (not pushed to GitHub)
```

---

## 🙋‍♂️ Author

Made with ❤️ by **Nivash R N**  
🔗 [LinkedIn](https://www.linkedin.com/in/nivash-r-n/)  
📧 hello.nivashinsights@gmail.com

---

## 📜 License

© 2025 Nivash R N. All rights reserved.  
Feel free to fork, star, and contribute ⭐
