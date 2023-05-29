import numpy as np
import cv2

im = cv2.imread('phanvunganh/balloons.jpg')
blur=cv2.GaussianBlur(im,(3,3),0)       #Làm mờ hình ảnh bằng bộ lọc Gaussian.

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)       #Biến ảnh màu thành ảnh xám
cv2.imshow("imgray", imgray)


res, thresh = cv2.threshold(src=imgray, thresh=230, maxval=255, type=cv2.THRESH_BINARY)      #Chuyển ảnh xám thành ảnh nhị phân
#res, thresh = cv2.threshold(imgray, 0, 25, 0)
#res, thresh = cv2.threshold(imgray, 0, 100, 0)
#res, thresh = cv2.threshold(src=imgray,thresh=127,maxval=255,type=cv2.THRESH_BINARY)
#thresh = cv2.Canny(imgray, 60, 150)                     # nhị phân hóa ảnh

        #src=tham số đầu tiên là 1 ảnh xám,
        #thresh=tham số thứ 2 là giá trị ngưỡng,
        #maxval=tham số thứ 3 maxval là giá trị được gán nếu giá pixel lớn hơn giá trị ngưỡng, 
        #type=tham số thứ 4 là loại phân ngưỡng

cv2.imshow("thresh", thresh)

#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)       #Tìm đường viền trong ảnh nhị phân
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        #image : hình ảnh cần tìm biên, là ảnh nhị phân.
        #contours : lưu trữ các đường biên tìm được, mỗi đường biên được lưu trữ dưới dạng một vector của các điểm.
        #hierarchy :  chứa thông tin về hình ảnh như số đường viền, xếp hạng các đường viền theo kích thước, trong ngoài, ..

print("contours size: ", str(len(contours)))
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)       #Vẽ đường bao màu xanh dương

#img = cv2.drawContours(im, contours, 1, (0,255,0), 3)
#img = cv2.drawContours(im, contours, 3, (255, 0, 0), 3)

cv2.namedWindow("contour.jpg", 0)        #Mở 1 cửa sổ đặt tên là "contour.jpg"
cv2.imshow("contour.jpg", img)
cv2.waitKey(0)
