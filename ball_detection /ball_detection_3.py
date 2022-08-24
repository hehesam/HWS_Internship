import cv2
import imutils
import time
import math

def gradient(pt1, pt2):
    if pt2[0]-pt1[0] == 0 :
        return (pt2[1]-pt1[1])/(pt2[0]-pt1[0] + 1)
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(all_centers,frame):
    pt1, pt2, pt3 = all_centers[-3:]
    print(pt1,pt2,pt3)

    m1 = gradient(pt2, pt1)
    m2 = gradient(pt2, pt3)
    if 1+(m2*m1) == 0 :
        m1 += 1
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    cv2.putText(frame,str(angD), (pt1[0]-40, pt1[1]-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255, 2))
    if abs(angD) > 15:
        cv2.putText(frame, "wall hit", (pt1[0] - 40, pt1[1] - 50), cv2.FACE_RECOGNIZER_SF_FR_COSINE, 1.5, (255, 0, 255, 2))

    # return abs(angD)


greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
vs = cv2.VideoCapture("ball_vid_4.mp4")

time.sleep(2.0)
all_centers = []
i = 0
ball_detected = False


while True:
    i += 1
    print("frame : ",i)
    _, frame = vs.read()

    if frame is None:
        break

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    # cv2.imshow("blur", blurred)

    width, height = frame.shape[:2]

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", hsv)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    # cv2.imshow('binary', mask)

    mask = cv2.erode(mask, None, iterations=2)
    # cv2.imshow('mask2', mask)

    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('mask3', mask)

    #  finding contours is like finding white object from black background.
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts) # returns center
    center = None
    # print(cnts)
    if len(cnts) > 0:
        ball_detected = True
        c = max(cnts, key=cv2.contourArea)
        # print('C: ', c)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        # print("M",M)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # print("center",center)

        # To see the centroid clearly
        if radius > 1:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 5)
            cv2.imwrite("circled_frame.png", cv2.resize(frame, (int(height / 2), int(width / 2))))
            all_centers.append(center)
            for ii in all_centers:
                cv2.circle(frame, ii, 5, (0, 0, 255), -1)
            if len(all_centers) >= 3:
                getAngle(all_centers, frame)



    elif ball_detected == True :
        ball_detected = False
        all_centers.clear()

    cv2.imshow("Frame", frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


vs.release()
cv2.destroyAllWindows()