import numpy as np
import cv2
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
cap = cv2.VideoCapture(0)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height=int(480/frame_width*frame_height)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(image=gray, patternSize=(6, 4),corners=None)
    print(corners)
    print('---------')
    if ret == True:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),criteria)
        cv2.drawChessboardCorners(img, (6, 4), corners2, ret)
    cv2.imshow('img', img)
    key = cv2.waitKey(delay=10)
    if key == ord("q"):
        break
cv2.destroyAllWindows()