
# Text Detection with EasyOCR and OpenCV

This project demonstrates how to detect and highlight text in images using EasyOCR and OpenCV.

## Requirements

Ensure you have the following Python packages installed:

- `opencv-python`
- `easyocr`
- `matplotlib`

Install these packages using pip:

```bash
pip install opencv-python easyocr matplotlib
```

## Code Overview

The Python script performs the following steps:

1. **Load the Image**: Reads an image from the specified file path using OpenCV.
2. **Initialize EasyOCR Reader**: Creates an EasyOCR reader instance to perform text detection. GPU acceleration can be enabled by setting `gpu=True` if you have a compatible GPU.
3. **Text Detection**: Uses EasyOCR to detect text in the image.
4. **Draw Bounding Boxes and Text**: Draws bounding boxes around detected text and overlays the text on the image if the confidence score exceeds a specified threshold.
5. **Display the Result**: Shows the processed image with detected text using Matplotlib.

## Explanation

- **Image Loading**: Uses `cv2.imread()` to load the image.
- **Text Detection**: Utilizes the `easyocr.Reader` object to detect text.
- **Bounding Boxes**: `cv2.rectangle()` draws bounding boxes around detected text areas.
- **Text Overlay**: `cv2.putText()` overlays the detected text on the image.
- **Display**: `plt.imshow()` displays the final image with detected text using Matplotlib.

## Running the Code

1. Ensure all required packages are installed.
2. Save the script to a `.py` file.
3. Run the script in your Python environment.
4. The processed image with detected text will be displayed.

## License

This project is licensed under the MIT License.
```

Feel free to adjust any sections based on additional details or specific requirements of your project.
