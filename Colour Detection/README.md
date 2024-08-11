
# Color Object Detection using OpenCV

This project demonstrates how to detect multiple colored objects in a video feed using OpenCV. The code detects specific colors (yellow, red, green, and blue) and draws bounding boxes around the detected objects.

## Installation

Before running the code, ensure that you have the following libraries installed:

    ``` bash
    pip install opencv-python pillow numpy
    ```

## How It Works

1. **Color Detection**: The code detects specific colors by converting the video feed from BGR to HSV color space.
2. **Bounding Box**: For each detected color, a bounding box is drawn around the object.
3. **Real-Time Processing**: The video feed is processed in real-time, and the results are displayed on the screen.

### Detected Colors

The following colors are detected by the code: 
- **Yellow**: `(BGR: [0, 255, 255])`

    `(or)`

- **Red**: `(BGR: [0, 0, 255])`

    `(or)`
- **Green**: `(BGR: [0, 255, 0])`

    `(or)`
- **Blue**: `(BGR: [255, 0, 0])`


## Usage

1. Clone the repository or download the script.
2. Run the script in your Python environment.
3. A window will appear displaying the video feed from your webcam.
4. Objects with the specified colors will be highlighted with bounding boxes.
5. Press `q` to exit the video feed.

## Additional Information

- **HSV Color Space**: The code uses the HSV (Hue, Saturation, Value) color space to improve color detection accuracy.
- **Bounding Box**: The bounding box color matches the detected object color for easy identification.

## License

This project is licensed under the MIT License.

---

This `README.md` file provides a clear and concise explanation of the project, 
including how it works, the code, and how to use it. You can modify it according to your needs or add more details if required.
