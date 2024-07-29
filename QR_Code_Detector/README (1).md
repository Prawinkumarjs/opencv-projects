# QR Code Detector

This repository contains a Google Colab notebook that detects and decodes QR codes from an uploaded image using OpenCV and Pyzbar.

## Requirements

Before running the code, ensure you have the following packages installed:

- OpenCV
- NumPy
- Pyzbar

If you're using Google Colab, you can install the required packages using the following commands:

- !apt-get update
- !apt-get install -y libzbar0
- !pip install pyzbar



## Usage

1. **Upload the Image File to Colab**:

   Use the `files.upload()` function from the `google.colab` module to upload an image file.

2. **Process the Uploaded Image File**:

   - Read the uploaded image using `cv2.imread()`.
   - Decode any QR codes in the image using `pyzbar.decode()`.
   - Draw a polygon around the detected QR codes using `cv2.polylines()`.
   - Display the decoded information on the image using `cv2.putText()`.
   - Display the final image using `cv2_imshow()` from `google.colab.patches`.

## Explanation

   1. **Install Dependencies**:

      Install the required libraries using `apt-get` for the `libzbar0` library and `pip` for the `pyzbar` library.

   2. **Upload Image File**:

      Use the `files.upload()` function from the `google.colab` module to upload an image file.

   3. **Process and Display Image**:

      - Read the uploaded image using `cv2.imread()`.
      - Decode any QR codes in the image using `pyzbar.decode()`.
      - Draw a polygon around the detected QR codes using `cv2.polylines()`.
      - Display the decoded information on the image using `cv2.putText()`.
      - Display the final image using `cv2_imshow()` from `google.colab.patches`.

## Conclusion

   This notebook demonstrates how to detect and decode QR codes from an uploaded image using OpenCV and Pyzbar in Google Colab. It covers the installation of necessary dependencies, uploading the image, processing the image to detect QR codes, and displaying the results.

   Feel free to modify and expand upon this notebook to suit your needs.
                                       