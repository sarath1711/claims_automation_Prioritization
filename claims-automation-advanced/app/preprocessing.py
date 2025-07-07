import pytesseract
from PIL import Image
import pdfplumber
import io
import os

def extract_text_from_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_any_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path, "rb") as f:
        content = f.read()

    if ext in ['.jpg', '.jpeg', '.png']:
        return extract_text_from_image(content)
    elif ext == '.pdf':
        return extract_text_from_pdf(content)
    elif ext == '.txt':
        return content.decode()
    else:
        raise ValueError(f"Unsupported file format: {ext}")