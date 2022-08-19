import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True :
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canimg = cv2.Canny(gray, 50,200)

    lines = cv2.HoughLines(canimg, 1, np.pi/180 ,80, np.array([]))
    print(lines)
    flag = np.any(lines)
    if flag:

        for line in lines :
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a*rho
            y0 = b*rho

            x1 = int(x0+1000*(-b))
            y1 = int(y0+1000*(a))
            x2 = int(x0-1000*(-b))
            y2 = int(y0 - 1000 * (1))

            cv2.line(img, (x1, y1), (x2,y2), (0,0,255), 2)

    cv2.imshow("Lines detected ", img)

    cv2.imshow("cannt detection", canimg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyWindow()
