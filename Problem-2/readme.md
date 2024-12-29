# License Plate Recognition System

This project is a Python-based application for detecting and recognizing license plates from images and video files using OpenCV and Tesseract OCR.

---

## Features
- **Image Processing**: Detect license plates in images.
- **Video Processing**: Detect and recognize plates from video frames in real-time.
- **Enhanced OCR**: Uses preprocessing techniques for better recognition accuracy.
- **Validation**: Filters and validates extracted license plate text.

---

## Requirements
Ensure the following are installed:

- Python 3.7 or later
- Required libraries:
  - `opencv-python`
  - `pytesseract`
  - `numpy`
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system:
  - Default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`
- Haar Cascade file for detecting license plates:
  - Included in OpenCV: `haarcascade_russian_plate_number.xml`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/license-plate-recognition.git
   cd license-plate-recognition
2. Install the Dependicies:
   pip install opencv-python pytesseract numpy

