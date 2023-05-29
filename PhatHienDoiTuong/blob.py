import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("img.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      # chuyển ảnh thành ảnh grayscale
#cv2.imshow("gray", gray)
ret,thresh = cv2.threshold(gray,220,255,0)       # Nhị phân hóa bức ảnh bằng cách đặt ngưỡng, với giá trị của ngưỡng là 220
#thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,10)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)      # tìm contour

M = cv2.moments(thresh)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
#cv2.imshow("thresh", thresh)

cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)

# cv2.circle (hình ảnh, tọa độ tâm, bán kính, màu sắc, độ dày)
# Thông số:  
# image: Là hình ảnh mà vòng tròn sẽ được vẽ. 
# tọa độ center: Nó là tọa độ tâm của đường tròn. Các tọa độ được biểu diễn dưới dạng bộ giá trị của hai giá trị tức là ( giá trị tọa độ X , giá trị tọa độ Y ). 
# radius: Là bán kính của hình tròn. 
# color: Nó là màu của đường viền của hình tròn được vẽ. Đối với BGR , chúng tôi vượt qua một tuple. ví dụ: (255, 0, 0) cho màu xanh lam. 
# Độ dày: Là độ dày của đường viền hình tròn tính bằng px . Độ dày -1 pxsẽ tô màu cho hình tròn bằng màu được chỉ định.
# Giá trị trả về: Nó trả về một hình ảnh. 

cv2.drawContours(img, contours, -1, (0, 0, 255), 3)   # vẽ lại ảnh contour vào ảnh gốc

cv2.putText(img, "centroid", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
cv2.imshow("Image", img)
cv2.waitKey(0)