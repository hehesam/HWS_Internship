import cv2
import numpy as np
import math

pointList = []

img = cv2.imread('angle_sample2.png')
img = cv2.resize(img, None, fx=1, fy=1)


def mousePoints(event, x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointList)
        if size != 0 and size % 3 != 0:
            index = round((size-1)/3) * 3
            cv2.line(img,tuple(pointList[-1]),(x,y), (0,0,255), 2)
        cv2.circle(img,(x,y), 5, (0,0,255), cv2.FILLED)
        pointList.append([x,y])

def gradient(pt1, pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle():
    pt1, pt2, pt3 = pointList[-3:]
    print(pt1,pt2,pt3)

    m1 = gradient(pt2, pt1)
    m2 = gradient(pt2, pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = -round(math.degrees(angR))
    # print(angD)
    cv2.putText(img,str(angD), (pt1[0]-40, pt1[1]-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255, 2))


while True :

    if len(pointList) % 3 == 0 and len(pointList) != 0 :
        getAngle()
    cv2.imshow("angle", img)
    cv2.setMouseCallback('angle', mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        pointList.clear()
        img = cv2.imread('angle_sample2.png')
        img = cv2.resize(img, None, fx=0.4, fy=0.4)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break