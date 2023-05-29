import numpy as np
import cv2
img = cv2.imread('image_camera/cat.jpg', 1)      #Đường dẫn tới ảnh, 0-ảnh xám and 1-ảnh màu
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()