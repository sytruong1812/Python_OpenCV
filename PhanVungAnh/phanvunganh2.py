import numpy as np
import cv2

im = cv2.imread('balloons.jpg')
blur=cv2.GaussianBlur(im,(3,3),0)       #Làm mờ hình ảnh bằng bộ lọc Gaussian.

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)       #Biến ảnh mày thành ảnh màu xám
cv2.imshow("imgray", imgray)

thresh = cv2.Canny(imgray, 200, 200)                     # nhị phân hóa ảnh
cv2.imshow("thresh", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
print('len(contours)', len(contours))
cnt = contours[0]

(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print((x, y), (MA, ma), angle)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)

img = cv2.drawContours(im, contours, -1, (0,255,0), 3)       #Vẽ đường bao màu xanh dương

cv2.namedWindow("contour.jpg", 0)        #Mở 1 cửa sổ đặt tên là "contour.jpg"
cv2.imshow("contour.jpg", img)
cv2.waitKey(0)