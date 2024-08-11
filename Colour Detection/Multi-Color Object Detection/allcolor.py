import cv2
from PIL import Image
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])  # Convert the BGR color to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

# Define colors in BGR and their corresponding rectangle colors
colors = {
    'yellow': ([0, 255, 255], (0, 255, 255)),
    'red': ([0, 0, 255], (0, 0, 255)),
    'green': ([0, 255, 0], (0, 255, 0)),
    'blue': ([255, 0, 0], (255, 0, 0))
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (bgr_color, rect_color) in colors.items():
        lowerLimit, upperLimit = get_limits(color=bgr_color)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), rect_color, 5)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
