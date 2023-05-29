import numpy as np
import cv2
import imutils

#Đếm trong hình có bao nhiêu quả bóng

image = cv2.imread("balloons.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)       #Biến ảnh màu thành ảnh xám
thres = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,10)     #Chuyển ảnh xám thành ảnh nhị phân

contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)       #Tìm đường viền trong ảnh nhị phân
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=False)

number = 0
# loop over our contours
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # approximate the contour
    if (85<w<150) and(100<h<150):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number +=1

print("Number of Contours found = " + str(number))
#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


cv2.imshow('Pix',image)
#cv2.imshow('Thres',thres)
cv2.waitKey()
cv2.destroyAllWindows()