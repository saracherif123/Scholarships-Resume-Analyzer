# 🎓 Resume-Analyzer

**AI-Powered Scholarship Resume Analysis Web App using Google Gemini and Streamlit**

Easily assess how well your resume aligns with scholarship requirements. Upload your PDF resume, optionally provide a scholarship description, and get detailed, personalized feedback — all powered by cutting-edge AI.

---

## 🌐 Live Demo

👉 [Click here to launch the Streamlit App](https://scholarships-resume-analyzer-k78jpyqbzzejyvavspbna6.streamlit.app)

---

## 📌 Features

- 📄 Upload a resume in PDF format
- 🧠 Analyze academic qualifications, research experience, leadership, and skills
- 🏆 Match resume content against scholarship descriptions
- 🔍 Dual-mode text extraction: direct text (`pdfplumber`) and OCR fallback (`pytesseract`)
- ⚡ Powered by Google Gemini AI (`gemini-1.5-flash`)
- 🌐 User-friendly web interface built with Streamlit

---

## 🧠 How It Works

1. Upload your resume (PDF format)
2. *(Optional)* Paste a scholarship description in the input box
3. Click the **"Analyze Resume"** button
4. Receive a detailed analysis including:
   - Academic strengths
   - Skill and experience evaluation
   - Areas for improvement
   - Alignment with provided scholarship criteria

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/yourusername/Resume-Analyzer.git
cd Resume-Analyzer
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 🔑 Set Up Environment Variables

Create a `.env` file inside the `Resume-Analysis/` directory with the following content:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

### ▶️ Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---


## ⚠️ Disclaimer

- The application does **not** store or share any uploaded files.
- All feedback is **AI-generated** and intended to supplement—not replace—human judgment.

---

## 🛠️ Powered By

- [Google Gemini AI](https://cloud.google.com/ai/generative-ai)
- [Streamlit](https://streamlit.io/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [pytesseract](https://github.com/madmaze/pytesseract)

---

## 👩‍💻 Author

**Sara Saad**  
[LinkedIn Profile](https://www.linkedin.com/in/sara-sherif-daoud/)
