import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

while True :
    success, frame = cap.read()

    cv2.imshow("webcam", frame)

    cv2.waitKey(1)