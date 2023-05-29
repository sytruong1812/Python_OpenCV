import cv2

cam = cv2.VideoCapture(0)      #Mở camera

cv2.namedWindow("Camera")       #Mở 1 cửa sổ đặt tên là "Camera"

img_counter = 0

while True:
    ret, frame = cam.read()        #Đọc ảnh
    #ret: Kết quả trả về
    #frame: Khung hình đọc từ camera
    if not ret:
        print("failed to grab frame")       #Không thể lấy khung ảnh
        break
    cv2.imshow("Camera", frame)         #Hiện thị ảnh trên của sổ "Camera"

    k = cv2.waitKey(1)      #Hàm chờ 1 phím được nhấn. Nếu không được nhấn thì giá trị là -1

    if k % 256 == 27:       #Mã phím ESC trong bảng ASCII: 27
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:      #Mã phím SPACE trong bảng ASCII: 32
        # SPACE pressed
        img_name = "image_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)        #Lưu hình ảnh vào một file được chỉ định
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()       #Ngừng việc sử dung camera

cv2.destroyAllWindows()     #Xóa tất cả cử sổ