# Face Detection and Blurring using OpenCV

## Project Overview

This project demonstrates face detection using OpenCV's pre-trained Haar Cascade classifier. The program captures a live video feed from the webcam, detects faces, and applies a blur effect to the detected face region. The live video is displayed on the screen, and the face regions are highlighted with a rectangle and blurred in real-time.

## Requirements

To run this project, you will need to have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- Haar Cascade XML file for face detection (`haarcascade_frontalface_default.xml`)

## Installation

1. Install the required packages:

   ```bash
      pip install opencv-python


## Running the Project

1. Download the `haarcascade_frontalface_default.xml` file from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory.

2. Clone or download this repository.

3. Ensure you have the `haarcascade_frontalface_default.xml` file in the same directory as the script.

4. Run the Python script:

   ```bash
      python face_blur.py


## Code Explanation

**Face Detection:** The Haar Cascade classifier (haarcascade_frontalface_default.xml) is used for face detection. This classifier is pre-trained to recognize faces.

```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
```
**Video Capture:** The program captures the video feed from your webcam using OpenCV's VideoCapture class.

```python

video = cv2.VideoCapture(0)
```

**Face Detection in Real-Time:** For each frame captured from the webcam, the face is detected by converting the frame to grayscale and using the detectMultiScale method. This method returns the coordinates of the faces in the frame.

```python

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

**Blurring Detected Faces:** The detected face regions are blurred using the cv2.medianBlur function. The blur is applied only to the face, while the rest of the frame remains unaltered.

```python

img[y:y + h, x:x + w] = cv2.medianBlur(img[y:y + h, x:x + w], 55)
```
**Live Video Feed Display:** The modified frame (with blurred faces) is displayed on the screen. The program continues to capture and process frames in real-time until the q key is pressed.

```python
cv2.imshow("GOT CH!!!", frame)
```
**Exiting the Program:** The program waits for the user to press the q key to stop the video capture and close the window.

```python

key = cv2.waitKey(1)
if key == ord('q'):
    break
```    
## Conclusion
This project provides a simple example of face detection and applying a blur filter to the detected faces using OpenCV. It demonstrates how computer vision can be used to manipulate video streams in real-time.


## Future Improvements
- Add the ability to detect and blur multiple faces.
- Save the processed video to a file.
- Use more advanced face detection algorithms such as deep learning-based face detection for higher accuracy.
    
## Acknowledgement
Special thanks to the [OpenCV community]() for providing the [Haar Cascade classifier]() for face detection.

## License
This project is licensed under the [MIT License](). Feel free to use and modify it for your own projects.

