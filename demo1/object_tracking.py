import cv2
import time
from tracker import *

# create a tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("ball_vid_2.mp4")

# object detection using stable camera

object_detector = cv2.createBackgroundSubtractorMOG2(history=100)
font = cv2.FONT_HERSHEY_COMPLEX

while True :
    s = time.time()
    ret, frame = cap.read()
    roi = frame[0:720, 0:500]

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detections = []
    for cnt in contours :
        # Calculate area and remove small elements
        # print(f"type : {type(cnt)} \n contour : {cnt}")
        area = cv2.contourArea(cnt)
        if area > 3000:
            # cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x+w, y+h), (0, 0, 255), 3)
            detections.append([x,y,w,h])

    boxes_ids = tracker.update(detections)
    # print(boxes_ids)

    for box_id in boxes_ids:
        x,y,w,h,id = box_id
        cv2.putText(roi, str(id), (x,y -15), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 2)

    cv2.imshow("show", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    # print(time.time()-s)
cap.release()
cv2.destroyWindow()