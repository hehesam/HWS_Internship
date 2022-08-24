import numpy as np
import cv2
import numpy.random
import random
cap = cv2.VideoCapture(0)

while 1 :
    _, img = cap.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours , hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of contours = " + str(len(contours)))
    # print(contours[0])

    for i in range(len(contours)):
        cv2.drawContours(img, contours, i, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 3)
        cv2.drawContours(img, contours, i, (255, 0, 255), 3)


    cv2.imshow("Image", img)
    cv2.imshow("Gray", imgray)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyWindow()