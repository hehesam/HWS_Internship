import cv2
import numpy as np
def empty(a):
    pass

# cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)

img = cv2.imread("shrek.jpg")
width, height = img.shape[:2]
img = cv2.resize(img, (int(height / 2), int(width / 2)))
cv2.imshow("shrek", img)
cv2.imwrite("res.jpg", img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayshrek',imgGray )
cv2.imwrite("grayres.jpg", imgGray)

imgBlur = cv2.GaussianBlur(imgGray, (17,17), 0)
cv2.imshow('blurres',imgBlur )
cv2.imwrite("blurres.jpg", imgBlur)

# threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
# threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

imgCanny = cv2.Canny(img, 70, 150)
cv2.imshow("canny", imgCanny)
cv2.imwrite("cannyres.jpg", imgCanny)

kernel = np.ones((5,5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("dialation", imgDialation)
cv2.imwrite("dialres.jpg", imgDialation)

imgErode = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("er", imgErode)
cv2.imwrite("eroderes.jpg", imgErode)
cv2.waitKey(0)