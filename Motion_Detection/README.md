# Motion Detection Project

This project implements a basic motion detection system using OpenCV. The program captures video from a webcam, processes each frame to detect motion, and highlights the areas where motion is detected.

## Concept

The motion detection algorithm works as follows:

1. **Initial Setup**: The first frame captured from the webcam is used as the reference frame. This frame will serve as the baseline to detect motion in subsequent frames.

2. **Frame Processing**: Each frame captured from the webcam is converted to grayscale and then blurred using Gaussian Blur to reduce noise and detail. This helps in focusing on the overall movement rather than small changes.

3. **Motion Detection**: The difference between the current frame and the reference frame is calculated to identify areas with significant changes. These changes are interpreted as motion.

4. **Thresholding**: The difference image is converted to a binary image using thresholding. This helps in isolating the regions of motion from the background.

5. **Contour Detection**: Contours are detected in the binary image, and for each contour that meets a minimum size criterion, a bounding rectangle is drawn on the original frame to indicate the detected motion.

6. **Displaying the Result**: The processed frames with motion highlighted are displayed in real-time. The user can exit the program by pressing the 'q' key.

## Dependencies

- Python 3.x
- OpenCV 4.x

You can install the required dependencies using pip:

    ```bash
    pip install opencv-python



## Usage
**Run the following command to start the motion detection program:**

    ```bash

    python main.py



## Acknowledgments

This project was inspired by the tutorial provided by [I Know Python](https://www.youtube.com/watch?v=oxmZ9zczptg&list=PL288dDBJtFXAsIohAOBShGe8NLqJ9Zwsk&index=3). Their explanation and guidance were invaluable in creating this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.