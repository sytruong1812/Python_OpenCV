import cv2
import numpy as np
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

low_yellow = np.array([21,39,64])
up_yellow = np.array([40,255,255])

low_green  = np.array([40,39,64])
up_green  = np.array([80,255,255])

low_red = np.array([170,50,50])
up_red = np.array([180,255,255])

low_blue = np.array([90,60,0])
up_blue = np.array([121,255,255])

while True:
    _,img= cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv, low_blue, up_blue)
    mask_red = cv2.inRange(hsv, low_red, up_red)
    #mask_yellow = cv2.inRange(hsv, low_yellow, up_yellow)
    #mask_green = cv2.inRange(hsv, low_green, up_green)

    if int(cv2.__version__[0]) > 3:
        contours, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area= cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt,.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if area > 400:
            cv2.drawContours(img, [approx], 0, (0, 0, 0), 3)
            if 6 < len(approx) < 20:
                cv2.putText(img, "Circle", (x, y), font, 1, (0, 0, 0))
    if int(cv2.__version__[0]) > 3:
        contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area= cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt,.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if area > 400:
            cv2.drawContours(img, [approx], 0, (0, 0, 0), 3)
            if len(approx)==3:
                cv2.putText(img, "Triangle", (x, y), font, 1, (0, 0, 0))
    cv2.imshow("camera",img)
    #cv2.imshow("image",mask_blue|mask_red)
    key =cv2.waitKey(1)
    if key == ord('q'): # =esc or ord('q')
            break
cap.release()
cv2.destroyAllWindows()