import cv2
import redis

point_list = []
r = redis.Redis(host='localhost', port=6379)
vs = cv2.VideoCapture(0)
i = 0
phase = 0

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append([x,y])


while True:
    i += 1
    print("frame : ",i)
    _, frame = vs.read()
    frame = cv2.resize(frame, (700,450))
    if frame is None:
        break

    if phase == 0:
        for x,y in point_list:
            cv2.circle(frame, (x, y), 5, (0, 255, 255), cv2.FILLED)
        if len(point_list) == 2:
            x1, y1 = point_list[0]
            x2, y2 = point_list[1]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 4)
            r.set("H", y2 - y1)
            r.set("W", x2 - x1)
            phase = 1
        cv2.imshow("frame", frame)
        cv2.setMouseCallback("frame", mousePoints)


    if phase == 1:
        cv2.destroyWindow("frame")

        x1, y1 = point_list[0]
        x2, y2 = point_list[1]


        frame = frame[y1:y2, x1:x2]
        cv2.imshow("frame2", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break