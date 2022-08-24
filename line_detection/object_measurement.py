
import cv2
import numpy as np
import utlis

webcam = True
path = '1.jpg'
pathvid = "ball_vid_4.mp4"
cap = cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
scale = 3
wP = 210 * scale
hP = 297 * scale

while True :
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    imgCountours, conts = utlis.getContours(img, showCanny=True,draw=True,minArea=50000, filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        print(biggest)
        imgWarp = utlis.warpImg(img, biggest, wP, hP)
        cv2.imshow("A4",imgWarp)
        imgCountours2, conts2 = utlis.getContours(imgWarp, showCanny=True, draw=True, minArea=2000, filter=4, cThr=[50,50])
        if len(conts2) != 0 :
            for obj in conts2:
                cv2.polylines(imgCountours2, [obj[2]], True, (0,255,0), 2)
                nPoints = utlis.reorder(obj[2])
                mW = round((utlis.findDis(nPoints[0][0]//scale, nPoints[1][0]//scale)/10),1)
                nH = round((utlis.findDis(nPoints[0][0]//scale, nPoints[2][0]//scale)/10),1)
        cv2.imshow("A6",imgWarp)

    img = cv2.resize(img, (0,0), None, 1, 1)
    cv2.imshow("original",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break