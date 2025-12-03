from pdfminer.high_level import extract_text
import os

def extract_pdf_text(path: str):
    """
    Extract raw text from a PDF file.
    Returns a dictionary with file_name and pages content.
    """
    if not os.path.exists(path):
        raise FileNotFoundError("PDF not found")

    text = extract_text(path)

    return {
        "file_name": os.path.basename(path),
        "raw_text": text
    }
