from __future__ import print_function

import cv2
import cv2 as cv
max_value = 255
max_type = 4
max_binary_value = 255
trackbar_type = 'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted'
trackbar_value = 'Value'
window_name = 'Threshold Demo'
def Threshold_Demo(val):
    #0: Binary
    #1: Binary Inverted
    #2: Threshold Truncated
    #3: Threshold to Zero
    #4: Threshold to Zero Inverted
    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)
    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    print(threshold_type)
    _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, threshold_type )
    # _, dst = cv.threshold(src_gray, 120, 255, 4)
    cv2.imwrite("binary.jpg", dst)
    cv.imshow(window_name, dst)

src = cv.imread("shrek.jpg")
src = cv.resize(src,(900,450))
src2 = cv.cvtColor(src, cv.COLOR_BGR2HLS)
# Convert the image to Gray
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv2.imwrite("gray_shrek.jpg", src_gray)
cv.namedWindow(window_name)
cv.createTrackbar(trackbar_type, window_name , 3, max_type, Threshold_Demo)
# Create Trackbar to choose Threshold value
cv.createTrackbar(trackbar_value, window_name , 0, max_value, Threshold_Demo)
# Call the function to initialize
Threshold_Demo(0)
# Wait until user finishes program
cv.waitKey()