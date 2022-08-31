import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def empty(a):
    pass
cv2.namedWindow("Parameters")
cv2.createTrackbar("Threshold1", "Parameters", 0, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 0, 255, empty)


# cap = cv2.VideoCapture(2)
# while True :
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow("frame", img)
#     cv2.imwrite("1.jpg",img)
#     imgBlur = cv2.GaussianBlur(img, (7,7), 1)
#     cv2.imwrite("2.jpg",imgBlur)
#     imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite("3.jpg",imgGray)
#
#     threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#     threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
#     imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
#     cv2.imwrite("4.jpg", imgCanny)
#     imgStack = stackImages(0.8, ([img,imgBlur], [imgGray,imgCanny]))
#     cv2.imwrite("5.jpg", imgStack)
#
#
#     cv2.imshow("res", imgStack)
#
#
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

# image cropping


img = cv2.imread("image.jpg")

black = np.zeros((512, 512,3), np.uint8)
black[:] = 0,0,0
# cv2.line(black, (0,0), (512,512), (255,0,0), 3)
# cv2.rectangle(black, (200, 200), (300, 450), (125,125,0), cv2.FILLED)
# cv2.rectangle(black, (100,100), (200,250), (0,0,200), cv2.FILLED)
# cv2.circle(black, (270,250), 25, (100,15, 200), 3)
# cv2.circle(black, (250,0), 25, (100,15, 200), cv2.FILLED)
cv2.putText(black, "Shrek is love", (200, 250),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 4)

cv2.imshow("black",  black)
# print(black)

cv2.imwrite("black.jpg", black)

white = np.ones((512,512,3), np.uint8)
cv2.imshow("white", white)
print(white)
cv2.imwrite("white.jpg", white)
cv2.waitKey(0)