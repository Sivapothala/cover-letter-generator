import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from streamlit_quill import st_quill
from prompts import *  # Make sure this module has the `Other_prompt` variable or function
from xhtml2pdf import pisa
import io

# path_to_wkhtmltopdf = r"C://Users//IsmartSiva//Downloads//wkhtmltox-0.12.6-1.msvc2015-win64.exe"  # Replace with your actual path

# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

st.set_page_config(page_title="Interactive Cover Letter Generator", page_icon=":robot_face:")

# Hide the Streamlit default footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Google Generative AI Token
GoogleGenerativeAI_token = st.sidebar.text_input("Google Generative AI Token", key="chatbot_api_key", type="password")

# Display helpful links
st.sidebar.write("[Get Google Generative AI Token](https://aistudio.google.com/app/apikey)")

def get_gemini_response(input_text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def extract_text_from_pdf(resume_upload):
    reader = pdf.PdfReader(resume_upload)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# Function to generate PDF from HTML content with pdfkit
def create_html_pdf(html_content):
    pdf_io = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html_content), dest=pdf_io)
    pdf_io.seek(0)
    return pdf_io.read()

st.title("Interactive Cover Letter Generator")

# Input for job description and file upload for resume
job_description = st.text_area("Enter the Job Description Details")
resume_upload = st.file_uploader("Upload Your Resume here!", type="pdf", help="Please provide your resume in PDF format.")
job_description = jb
# Generate button
if st.button("Generate Cover Letter"):
    if not GoogleGenerativeAI_token:
        st.error("Please provide a valid Google Generative AI Token.")
    elif resume_upload is None:
        st.warning("Please upload your resume in PDF format.")
    else:
        pdf_content = extract_text_from_pdf(resume_upload)
        
        # Use the Other_prompt variable from prompts.py to format the request
        input_text = Other_prompt.format(job_description=job_description, text=pdf_content)
        st.session_state["generated_letter"] = get_gemini_response(input_text, GoogleGenerativeAI_token)

# Display editor if letter is generated
if "generated_letter" in st.session_state:
    st.success("Edit your Cover Letter:")
    
    # Use Streamlit Quill editor for rich text editing
    edited_letter = st_quill(value=st.session_state["generated_letter"], placeholder="Edit your cover letter here...", key="quill")

    # Download button for the customized cover letter
    if edited_letter:
        pdf_bytes = create_html_pdf(edited_letter)
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="cover_letter.pdf",
            mime="application/pdf"
        )
