import cv2
import pytesseract
import numpy as np
import os

def extract_image_text(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError("Image not found")

    img = cv2.imread(path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    text = pytesseract.image_to_string(thresh)

    return {
        "file_name": os.path.basename(path),
        "ocr_text": text
    }
