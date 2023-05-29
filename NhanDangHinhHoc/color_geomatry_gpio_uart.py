import cv2
import numpy as np
import serial
import time
import RPi.GPIO as GPIO
import lcddriver

LedPin1 = 1
LedPin2 = 2
LedPin3 = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin1, GPIO.OUT)
GPIO.setup(LedPin2, GPIO.OUT)
GPIO.setup(LedPin3, GPIO.OUT)

GPIO.output(LedPin1, GPIO.HIGH)
GPIO.output(LedPin2, GPIO.HIGH)
GPIO.output(LedPin3, GPIO.HIGH)


ser = serial.Serial(
   	port ='/dev/ttyTHS0',
   	baudrate=9600,
   	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
  	bytesize=serial.EIGHTBITS,
    timeout=1)

lcd = lcddriver.lcd()

def nothing(x):
    # any operation
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 66, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 134, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 243, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX
while True:
	_, frame = cap.read(0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	l_h = cv2.getTrackbarPos("L-H", "Trackbars")
	l_s = cv2.getTrackbarPos("L-S", "Trackbars")
	l_v = cv2.getTrackbarPos("L-V", "Trackbars")
	u_h = cv2.getTrackbarPos("U-H", "Trackbars")
	u_s = cv2.getTrackbarPos("U-S", "Trackbars")
	u_v = cv2.getTrackbarPos("U-V", "Trackbars")

	lower_red = np.array([l_h,l_s,l_v])
	upper_red = np.array([u_h,u_s,u_v])

	lower_red = np.array([0,60,60])
	upper_red = np.array([10,255,255])

	mask = cv2.inRange(hsv, lower_red, upper_red)

	kernel = np.ones((5, 5), np.uint8)
	mask = cv2.erode(mask, kernel)

	GPIO.output(LedPin1, GPIO.LOW)  
	GPIO.output(LedPin2, GPIO.LOW)  
	GPIO.output(LedPin3, GPIO.LOW)
    
	if int(cv2.__version__[0]) > 3:
		contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	else:
		_,contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		area = cv2.contourArea(cnt)
		approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
		x = approx.ravel()[0]
		y = approx.ravel()[1]
		GPIO.output(LedPin1, GPIO.LOW)
		GPIO.output(LedPin2, GPIO.LOW)
		GPIO.output(LedPin3, GPIO.LOW)
		       
		if area > 400:
			cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

			if len(approx) == 3:
				cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
				GPIO.output(LedPin1, GPIO.HIGH)  
				GPIO.output(LedPin2, GPIO.LOW)  
				GPIO.output(LedPin3, GPIO.LOW)
				lcd.lcd_clear()
				lcd.lcd_display_string("     Triangle", 2)
				
				ser.write(b'#1P1600#2P1600#6P1200T1000D500\r\n')
				time.sleep(2)
				ser.write(b'#1P1600#2P1600#6P1200T1000D500\r\n')
				time.sleep(2)
				
			elif len(approx) == 4:
				cv2.putText(frame, "Square", (x, y), font, 1, (0, 0, 0))
				GPIO.output(LedPin1, GPIO.HIGH) 
				GPIO.output(LedPin2, GPIO.HIGH) 
				GPIO.output(LedPin3, GPIO.LOW)
				lcd.lcd_clear()
				lcd.lcd_display_string("     Square", 2)
				
				ser.write(b'#1P1600#2P1600#6P1200T1000D500\r\n')
				time.sleep(2)
				ser.write(b'#1P1600#2P1600#6P1200T1000D500\r\n')
				time.sleep(2)
				
			elif 6 < len(approx) < 20:
				cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
				GPIO.output(LedPin1, GPIO.HIGH)  
				GPIO.output(LedPin2, GPIO.HIGH)
				GPIO.output(LedPin3, GPIO.HIGH)
				lcd.lcd_clear()
				lcd.lcd_display_string("     Circle", 2)

				ser.write(b'#1P1600#2P1600#6P1200T1000D500\r\n')
				time.sleep(2)
				ser.write(b'#1P1600#2P1600#6P1200T1000D500\r\n')
				time.sleep(2)
                   
	cv2.imshow("Camera", frame)
	#cv2.imshow("Mask", mask)

	key = cv2.waitKey(1)
	if key == 27:
		break
cap.release()
cv2.destroyAllWindows()
