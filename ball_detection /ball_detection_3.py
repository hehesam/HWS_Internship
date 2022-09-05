import cv2
import imutils
import time
import math
import multiple_frames
from pygame import mixer

def gradient(pt1, pt2):
    if pt2[0]-pt1[0] == 0 :
        return (pt2[1]-pt1[1])/(pt2[0]-pt1[0] + 1)
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(all_centers,frame, index):
    pt1, pt2, pt3 = all_centers[-3:]
    print(pt1,pt2,pt3)

    m1 = gradient(pt2, pt1)
    m2 = gradient(pt2, pt3)
    if 1+(m2*m1) == 0 :
        m1 += 1
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    cv2.putText(frame,str(angD), (pt1[0]-40, pt1[1]-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255, 2))
    if abs(angD) > 17:
        cv2.putText(frame, "wall hit", (pt1[0] - 40, pt1[1] - 50), cv2.FACE_RECOGNIZER_SF_FR_COSINE, 1.5, (255, 0, 255, 2))
        mixer.init()
        sound = mixer.Sound("hit1.wav")
        sound.play()
        cv2.imwrite("pics/frame"+str(index)+".png", cv2.resize(frame, (int(height / 2), int(width / 2))))


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append([x,y])

# greenLower = (143, 144,140)
# greenUpper = (180, 255, 255)

greenLower = (46, 65, 50)
greenUpper = (80, 255, 255)

# greenLower = (29, 86, 6)
# greenUpper = (64, 255, 255)

vs = cv2.VideoCapture(2)
time.sleep(2.0)
all_centers = []
point_list = []
phase = 0
i = 0

ball_detected = False


while True:
    i += 1
    print("frame : ",i)
    _, frame = vs.read()

    if frame is None:
        break

    if phase == 0:
        for x,y in point_list:
            cv2.circle(frame, (x, y), 5, (0, 255, 255), cv2.FILLED)
        if len(point_list) == 2:
            x1, y1 = point_list[0]
            x2, y2 = point_list[1]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 4)
            phase = 1
        cv2.imshow("frame", frame)
        cv2.setMouseCallback("frame", mousePoints)

    elif phase == 1:
        x1, y1 = point_list[0]
        x2, y2 = point_list[1]
        frame = frame[y1:y2, x1:x2]
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)

        width, height = frame.shape[:2]

        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask1 = cv2.inRange(hsv, greenLower, greenUpper)

        mask2 = cv2.erode(mask1, None, iterations=4)

        mask3 = cv2.dilate(mask2, None, iterations=6)

        #  finding contours is like finding white object from black background.

        cnts = cv2.findContours(mask3.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts) # returns center
        center = None
        # print(cnts)
        if len(cnts) > 0:
            ball_detected = True
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # To see the centroid clearly
            print("R : ",radius)
            if radius > 1 and radius < 500:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 5)
                all_centers.append(center)
                for ii in all_centers:
                    cv2.circle(frame, ii, 5, (0, 0, 255), -1)
                if len(all_centers) >= 3:
                    getAngle(all_centers, frame, i)

        elif ball_detected == True :
            ball_detected = False
            all_centers.clear()

        imgStack = multiple_frames.stackImages(0.8, ([frame, mask1], [mask2, mask3]))
        cv2.imshow("Frame", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('c'):
        point_list.clear()

vs.release()
cv2.destroyAllWindows()