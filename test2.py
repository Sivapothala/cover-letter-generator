import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from streamlit_quill import st_quill
from prompts import *  # Make sure this module has the `Other_prompt` variable or function
import pdfkit
import tempfile
import io
import os

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

# Path to wkhtmltopdf executable
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # Replace with your actual path
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Path to the external CSS file
css_path = os.path.abspath("styles.css")   # Ensure styles.css is in the same directory

# Function to interact with Google Generative AI
def get_gemini_response(input_text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# Extract text from uploaded PDF
def extract_text_from_pdf(resume_upload):
    reader = pdf.PdfReader(resume_upload)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# Function to generate PDF from HTML content with pdfkit
def create_html_pdf(html_content):
    # Create a temporary file to store the PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        # Ensure the CSS file is accessible to wkhtmltopdf
        css_path = os.path.abspath("styles.css")  # Get the absolute path of styles.css
        options = {
    'enable-local-file-access': None  # Needed for wkhtmltopdf to access local CSS files
}
        # Generate PDF from HTML content, passing the correct CSS path
        pdfkit.from_string(html_content, tmp_file.name, configuration=config, options=options, css=css_path)
        tmp_file.seek(0)
        return tmp_file.read()

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

    # Check if edited letter has content before generating PDF
    if edited_letter:
        # HTML content with a link to the external CSS
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="file:///{os.path.abspath(css_path)}">  <!-- Absolute path -->
</head>
<body>
    {edited_letter}
</body>
</html>
"""
        
        # Generate PDF from the HTML content
        pdf_bytes = create_html_pdf(html_content)
        
        # Check if PDF generation was successful
        if pdf_bytes:
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name="cover_letter.pdf",
                mime="application/pdf"
            )
        else:
            st.error("There was an error generating the PDF. Please try again.")
