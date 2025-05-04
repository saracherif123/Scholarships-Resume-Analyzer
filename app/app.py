import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image #Python Imaging Library is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.
import google.generativeai as genai
from pdf2image import convert_from_path #to convert pdf to image
import pytesseract #Python library that recognizes text in images
import pdfplumber #Python library to extract text from pdf

# Load environment variables
load_dotenv()

# Configure Google Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # Try direct text extraction
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() #extract_text is a function from pdfplumber used to extract text from pdf
                if page_text:
                    text += page_text #text has

        if text.strip(): #condition to check if text is not empty
            return text.strip() #strip is used to remove leading and trailing whitespaces
    except Exception as e:
        print(f"Direct text extraction failed: {e}")

    # Fallback to OCR for image-based PDFs 
    print("Falling back to OCR for image-based PDF.") #Optical Character Recognition is a technology used to recognize text within images
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_string(image) #to extract text from image
            text += page_text + "\n"
    except Exception as e:
        print(f"OCR failed: {e}")

    return text.strip()

# Function to analyze scholarship resume
def analyze_scholarship_resume(resume_text, scholarship_description=None):
    if not resume_text:
        return {"error": "Resume text is required for analysis."}
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    base_prompt = f"""
    You are an experienced academic advisor specializing in reviewing scholarship applications.
    Your task is to evaluate the provided resume and provide feedback regarding the candidate's eligibility, strengths, and areas for improvement for scholarship applications.
    
    Please assess the following:
    - **Academic Qualifications:** Evaluate the candidate’s educational background, GPA, coursework, and any honors or distinctions.
    - **Research Experience:** Identify any projects, publications, or research work that support the candidate’s academic standing.
    - **Leadership & Extracurricular Activities:** Highlight any leadership roles, volunteer work, or community service.
    - **Skills & Personal Growth:** Identify strengths and suggest skills or courses that could improve the candidate’s application.
    - **Scholarship Suitability:** Based on the provided information, assess how well the candidate aligns with typical scholarship criteria and suggest ways to strengthen their application.

    Resume:
    {resume_text}
    """

    if scholarship_description:
        base_prompt += f"""
        Additionally, compare this resume to the following scholarship eligibility criteria:
        
        Scholarship Description:
        {scholarship_description}
        
        Highlight the candidate’s alignment with the criteria, strengths, and areas where they can improve their profile.
        """

    response = model.generate_content(base_prompt)

    analysis = response.text.strip()
    return analysis

# Streamlit app
st.set_page_config(page_title="Scholarship Resume Analyzer", layout="wide")

# Title
st.title("🎓 AI-Based Scholarship Resume Analyzer")
st.write("Analyze your resume and match it with scholarship requirements using Google Gemini AI.")

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
with col2:
    scholarship_description = st.text_area("🏆 Enter Scholarship Description:", placeholder="Paste the scholarship requirements here...")

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
else:
    st.warning("⚠️ Please upload a resume in PDF format.")

st.markdown("<div style='padding-top: 10px;'></div>", unsafe_allow_html=True)

if uploaded_file:
    # Save uploaded file locally for processing
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text from PDF
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing resume... ⏳"):
            try:
                # Analyze resume
                analysis = analyze_scholarship_resume(resume_text, scholarship_description)
                st.success("✅ Analysis complete!")
                st.write(analysis)
            except Exception as e:
                st.error(f"❌ Analysis failed: {e}")

# Footer
st.markdown("---")
# Sticky footer using CSS
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        🚀 Powered by Streamlit and <a href="https://console.cloud.google.com/marketplace/product/google/gemini-ai" target="_blank">Google Gemini AI</a>
    </div>
    """,
    unsafe_allow_html=True)