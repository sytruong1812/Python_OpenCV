#ADD thư viện cần sử dụng
import numpy as np
import cv2
#Tìm đường viền
img = cv2.imread('D:\\Python_XLA\\phathiendoituong\\imgs.png')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)          #Chuyển ảnh xám thành ảnh grayscale
#img1 = img.copy()
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)        #Chuyển ảnh xám thành ảnh grayscale
ret,thrash = cv2.threshold(imgGry, 240, 255, cv2.CHAIN_APPROX_NONE)     #Nhị phân hóa bức ảnh bằng cách đặt ngưỡng, với giá trị của ngưỡng là 240
contours, hierachy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)     #Tìm contour
#Bắt đầu vòng lặp tìm contour từng hình
for contour in contours:
    M = cv2.moments(contour)        # Tính toán trung tâm của đường viền
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])

    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)       #Tính xấp xỉ đường viền để xác định hình 
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)  #Vẽ lại ảnh contour vào ảnh gốc
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:            #Hình tam giác có 3 đỉnh
        cv2.putText(img, "Tam Giac", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:      #Hình chữ nhật, hình vuông có 4 đỉnh
        x, y, w, h = cv2.boundingRect(approx)           #Tính toán giới hạn của đường bao và tỉ lệ khung hình để xác đinh hình vuông hay hình chữ nhật
        AspectRatio = float(w) / h      #Tính tỉ lệ khung hình
        if AspectRatio >= 0.95 and AspectRatio < 1.05:   #Hình vuông tỉ lệ khung hình gần bằng 1, ngược lại là hình chữ nhật
            cv2.putText(img, "Hinh Vuong", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))     #Viết một chuỗi kỹ tự lên bức hình
        else:
            cv2.putText(img, "Hinh Chu Nhat", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:      #Hình ngũ giác có 5 đỉnh
        cv2.putText(img, "Ngu Giac", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:        #Hình ngôi sao 10 đỉnh
        cv2.putText(img, "Ngoi Sao", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))       #Viết một chuỗi kỹ tự lên bức hình
    elif len(approx) == 7:      #Hình mũi tên có 7 đỉnh
        cv2.putText(img, "Mui Ten", (x-90, y-60), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 11:   #Hình tia sét có 11 đỉnh
        cv2.putText(img, "Tia Set", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) > 11 and len(approx) < 13 :    #Hình tròn
        cv2.putText(img, "Hinh Tron", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:    #Hình trái tim
        cv2.putText(img, "Heart", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    pixel_center = hsv_frame[cY, cX]       #Tọa độ trung tâm
    hue_value = pixel_center[0]     #Giá trị tông màu HUE

    color = 'undefined'
    if hue_value <10:
        color = "DO"
    elif hue_value <22:
        color = "CAM"
    elif hue_value <33:
        color = "VANG"
    elif hue_value < 80:
        color = "LUC"
    elif hue_value <100:
        color = "XANH DA TROI"
    elif hue_value <150:
        color = "LAM"
    elif hue_value <170:
        color = "TIM"
    elif hue_value <171:
        color = "HONG"
    else:
        color = "DO"

    #pixel_center_bgr = img[cY, cX]
    #b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(img, color, (cX+10, cY+10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)        #Viết một chuỗi ký tự name color
    cv2.circle(img, (cX,cY),3,(255,255,255),-1)     #Vẽ đường viền 
cv2.imshow('image',img)
cv2.waitKey(0)