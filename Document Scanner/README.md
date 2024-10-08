
# Document Scanner With OpenCV

This project uses OpenCV to create a simple document scanner that captures images from a webcam, processes them, and saves the scanned images. The script can also be used to process images from a file.

## Feature


- Real-time image processing using a webcam.
- Detects and highlights the biggest contour in the image.
- Warps the perspective to get a top-down view of the detected document.
- Applies adaptive thresholding to enhance the document's readability.
- Saves the scanned document when the 's' key is pressed.
- Stops the video capture when the 'q' key is pressed.
## Requirements


- Python 3.x
- OpenCV 4.x
- NumPy
## Installation

1. Clone the repository or download the source code.
2. Install the required packages:
   ```bash
      pip install opencv-python-headless numpy
## Usage

1. Ensure you have a webcam connected to your computer.
2. Place your document within the camera's view.
3. Run the main1.py script:
bash
Copy code
python main1.py

4. Press 's' to save the scanned document.
5. Press 'q' to stop the video capture and close the application.
## File Structure 

- **main1.py: Main script that captures and processes the image.**

- **utlis.py: Utility functions used in main1.py.**

- **README.md: This readme file.**

- **images.jpeg: Sample image used if webcam is not available.**
## Acknowledgment 


This project was inspired by various OpenCV tutorials and examples available online. Special thanks to the OpenCV community for their invaluable resources and support.
