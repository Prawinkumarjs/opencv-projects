import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set the width
cap.set(4, 480)  # Set the height
cap.set(cv2.CAP_PROP_FPS, 60)  # Set the FPS

# Initialize the segmentor
segmentor = SelfiSegmentation()

# Load all images from the 'Images' folder
listImg = os.listdir("Images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)

print(len(imgList))

indexImg = 0

# Custom FPS counter
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Remove the background from the image
    imgOut = segmentor.removeBG(img, imgList[indexImg], cutThreshold=0.9)

    # Stack the original and output images side by side
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)

    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(imgStacked, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the stacked image
    cv2.imshow("Image", imgStacked)

    # Wait for key press
    key = cv2.waitKey(1)
    if key == ord('a'):  # Move to the previous image
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):  # Move to the next image
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('q'):  # Quit the program
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
