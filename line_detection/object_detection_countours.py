import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True  :
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours :
        area = cv2.contourArea(contour)
        if area > 1000 :
            cv2.drawContours(frame, contour, -1, (0,255,0), 3)

    # cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    cv2.imshow("FRame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xff==ord("q"):
        break
