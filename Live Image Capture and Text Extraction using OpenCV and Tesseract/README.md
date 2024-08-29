# Live Image Capture and Text Extraction using OpenCV and Tesseract

## Overview

This project captures live images from a webcam, detects specific logos in real-time, and extracts text from the captured images using Tesseract OCR. The main purpose of the project is to demonstrate the integration of OpenCV for live image processing and Tesseract OCR for text extraction.

## Features

- **Real-Time Image Capture**: Continuously captures frames from a webcam.
- **Logo Detection**: Detects a specific logo in the captured frames using template matching.
- **Text Extraction**: Extracts text from the captured image once the logo is detected.
- **Simple User Interface**: Displays live video feed and allows image capture using a single key press.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- OpenCV 4.0 or higher
- Pillow (PIL)
- Tesseract OCR installed on your system

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Prawinkumarjs/opencv-projects.git
    cd "Live Image Capture and Text Extraction using OpenCV and Tesseract"
     ``````

2. **Install Required Python Packages**:
    ```bash
    pip install opencv-python pillow pytesseract
    ```

3. **Install Tesseract OCR**:
- Download and install Tesseract OCR from [this link](https://github.com/tesseract-ocr/tesseract).
- Make sure to add Tesseract to your system's PATH, or specify the path in the code.

## Usage

1. **Run the Script**:
- Ensure your webcam is connected and functioning.
- Place the logo template image (`label.jpg`) in the same directory as the script.
- Execute the script using Python:
```bash
    python main.py
```

2. **Capture and Extract Text**:
- The webcam feed will be displayed in a window.
- The script will continuously scan for the specified logo in the video feed.
- Once the logo is detected, the image will be captured, and text will be extracted using Tesseract OCR.
- The extracted text will be printed in the console.

3. **Key Controls**:
- Press `s` to manually capture an image.
- Press `q` to quit the video feed and close the application.

## Code Explanation

### 1. `detect_logo(frame, logo_template)`

This function takes a frame from the webcam and a logo template as input. It converts both to grayscale and uses OpenCV's `matchTemplate` function to find the logo in the frame. If the matching score exceeds the threshold, the logo is considered detected.

### 2. `capture_image_and_extract_text(camera, logo_template, path_to_tesseract)`

This function captures live frames from the webcam, checks for the logo's presence, and saves the frame when the logo is detected. It then uses Tesseract OCR to extract and print the text from the saved image.

### 3. `tesseract()`

This function handles the Tesseract OCR part. It sets the path to the Tesseract executable, opens the captured image, and extracts text using Tesseract's `image_to_string` method.

## Acknowledgments

- **OpenCV**: For providing an extensive library for computer vision tasks.
- **Tesseract OCR**: For the powerful text extraction capabilities.
- **Pillow**: For image handling in Python.
- **I Know Python Tutorial**: For helpful tutorials and guidance.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. Contributions, bug reports, and feature requests are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

