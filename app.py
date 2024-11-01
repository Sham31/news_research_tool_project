import streamlit as st
import fitz  # PyMuPDF
from docx import Document
from io import BytesIO

# Function to extract text from PDF
def extract_from_pdf(pdf_file):
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Function to extract text from DOCX
def extract_from_docx(doc_file):
    text = ""
    document = Document(doc_file)
    for para in document.paragraphs:
        text += para.text + "\n"
    return text

# Streamlit UI
st.title("File Feature Extractor")
st.write("Upload a PDF or DOC file to extract features.")

# File upload
uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx'])

if uploaded_file is not None:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    st.write(file_details)

    # Process PDF files
    if uploaded_file.type == "application/pdf":
        st.write("Extracting text from PDF...")
        pdf_text = extract_from_pdf(uploaded_file)
        st.text_area("Extracted Text", pdf_text, height=300)
    
    # Process DOCX files
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        st.write("Extracting text from DOCX...")
        docx_text = extract_from_docx(uploaded_file)
        st.text_area("Extracted Text", docx_text, height=300)
    
    else:
        st.error("Unsupported file type. Please upload a PDF or DOCX file.")
