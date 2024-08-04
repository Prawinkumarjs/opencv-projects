# Background Remover with Webcam and Custom Images

This project demonstrates a background removal application using OpenCV and the `cvzone` library. The application captures video from the webcam and allows users to remove the background from the video feed using custom images loaded from a specified directory.
## Example:
![Background Remover with Webcam and Custom Images](https://github.com/Prawinkumarjs/opencv-projects/blob/main/Background%20Remover/virtual-background-green-screen-example.jpg)


## Features

- Real-time background removal using `cvzone.SelfiSegmentation`.
- Switch between different background images using keyboard inputs.
- Display the frames per second (FPS) of the application.

## Requirements

- Python 3.x
- OpenCV
- cvzone

## Installation

1. **Clone the repository:**

   ```bash
    git clone https://github.com/Prawinkumarjs/background-remover.git


2. **Navigate to the project directory:**

    ```bash
    cd background-remover


3. **Install the required libraries:**

    ```bash
    pip install opencv-python cvzone


## Usage


1. **Prepare the Images:**

Create a directory named Images in the project root directory. Place your background images (e.g., 1.jpg, 2.jpg, 3.jpg) inside this directory.

2. **Run the Application:**

    Execute the script:
    ```bash
    python main.py


3. **Controls:**

- 'a' key: Switch to the previous background image.

- 'd' key: Switch to the next background image.

- 'q' key: Quit the application.

## Code Explanation

Here is a brief explanation of how the code works:

1. **Imports and Initialization:**

    ```python

    import cv2
    import cvzone
    from cvzone.SelfiSegmentationModule import SelfiSegmentation
    import os
    import time


- Import necessary libraries and modules.
- Initialize webcam and background removal segmentor.

2. **Configure Webcam:**

    ```python

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height
    cap.set(cv2.CAP_PROP_FPS, 60)  # Set FPS

- Set up webcam capture with specified resolution and FPS.
    
3. **Load Background Images:**

    ```python

    listImg = os.listdir("Images")
    imgList = []
    for imgPath in listImg:
        img = cv2.imread(f'Images/{imgPath}')
        imgList.append(img)
        
- Load images from the "Images" directory and store them in a list.

4. **Main Loop:**

        ```python
        
        while True:
            success, img = cap.read()
            if not success:
                break

            imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)
            imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(imgStacked, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Image", imgStacked)

            key = cv2.waitKey(1)
            if key == ord('a'):
                if indexImg > 0:
                    indexImg -= 1
            elif key == ord('d'):
                if indexImg < len(imgList) - 1:
                     indexImg += 1
            elif key == ord('q'):
                 break
            cap.release()
            cv2.destroyAllWindows()


- Capture video frames, apply background removal, and display the result.
-  Allow users to switch between background images and quit the application using keyboard inputs.


## Acknowledgements

- [OpenCV](https://opencv.org/) - Open Source Computer Vision library
- [cvzone](https://github.com/cvzone/cvzone) - Utilities for Computer Vision

## License

The source code for the site is licensed under the MIT license, which you can find in
the MIT-LICENSE.txt file.

All graphical assets are licensed under the
[Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/).
