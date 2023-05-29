import cv2
import numpy as np
import imutils

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
     _,frame= cap.read()

     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     lower_yellow = np.array([25,70,120])
     upper_yellow = np.array([30,255,255])

     lower_green  = np.array([40,70,80])
     upper_green  = np.array([70,255,255])

     lower_red = np.array([0,50,120])
     upper_red = np.array([10,255,255])

     lower_blue = np.array([90,60,0])
     upper_blue = np.array([121,255,255])

     mask1 = cv2.inRange(hsv,lower_yellow,upper_yellow)
     mask2 = cv2.inRange(hsv,lower_red,upper_green)
     mask3 = cv2.inRange(hsv,lower_blue,upper_red)
     mask4 = cv2.inRange(hsv,lower_green,upper_blue)

     cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts1 = imutils.grab_contours(cnts1)

     cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts2 = imutils.grab_contours(cnts2)

     cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts3 = imutils.grab_contours(cnts3)

     cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts4 = imutils.grab_contours(cnts4)

     for c in cnts1:
        contours, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       
        approx1 = cv2.approxPolyDP(c, 0.02*cv2.arcLength(c, True), True)
        
        x1 = approx1.ravel()[0]
        y1 = approx1.ravel()[1]
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        area1 = cv2.contourArea(c)

        if area1 > 5000:

             cv2.drawContours(frame,[c],-1,(0,255,0), 3)

             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             cv2.putText(frame,"yellow", (cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 3)
        
        
        if area1 > 400:
            cv2.drawContours(frame, [approx1], 0, (0, 0, 0), 5)
            if len(approx1) == 3:
                cv2.putText(frame, "Triangle", (x1, y1), font, 1, (0, 0, 0))
            elif len(approx1) == 4:
                cv2.putText(frame, "Square", (x1, y1), font, 1, (0, 0, 0))
            elif 10 < len(approx1) < 20:
                cv2.putText(frame, "Circle", (x1, y1), font, 1, (0, 0, 0))


     for c in cnts2:
        
        contours, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        approx2 = cv2.approxPolyDP(c, 0.02*cv2.arcLength(c, True), True)
        
        x2 = approx2.ravel()[0]
        y2 = approx2.ravel()[1]
       
        font = cv2.FONT_HERSHEY_SIMPLEX
        area1 = cv2.contourArea(c)
    
        area2 = cv2.contourArea(c)
        if area2 > 5000:


             cv2.drawContours(frame,[c],-1,(0,255,0), 3)

             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             cv2.putText(frame,"green", (cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 3)

        if area2 > 400:
            cv2.drawContours(frame, [approx2], 0, (0, 0, 0), 5)
            if len(approx2) == 3:
                cv2.putText(frame, "Triangle", (x2, y2), font, 1, (0, 0, 0))
            elif len(approx2) == 4:
                cv2.putText(frame, "Square", (x2, y2), font, 1, (0, 0, 0))
            elif 10 < len(approx2) < 20:
                cv2.putText(frame, "Circle", (x2, y2), font, 1, (0, 0, 0))

     for c in cnts3:
       
        contours, _ = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       
        approx3 = cv2.approxPolyDP(c, 0.02*cv2.arcLength(c, True), True)
        
        
        x3 = approx3.ravel()[0]
        y3 = approx3.ravel()[1]
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        area1 = cv2.contourArea(c)
    
        area3 = cv2.contourArea(c)
        if area3 > 5000:

             cv2.drawContours(frame,[c],-1,(0,255,0), 3)

             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             cv2.putText(frame,"red", (cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 3)
      
        if area3 > 400:

            cv2.drawContours(frame, [approx3], 0, (0, 0, 0), 5)
            if len(approx3) == 3:
                cv2.putText(frame, "Triangle", (x3, y3), font, 1, (0, 0, 0))
            elif len(approx3) == 4:
                cv2.putText(frame, "Square", (x3, y3), font, 1, (0, 0, 0))
            elif 10 < len(approx3) < 20:
                cv2.putText(frame, "Circle", (x3, y3), font, 1, (0, 0, 0))
 
     for c in cnts4:
        
        contours, _ = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        approx4 = cv2.approxPolyDP(c, 0.02*cv2.arcLength(c, True), True)
        x4 = approx4.ravel()[0]
        y4 = approx4.ravel()[1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        area1 = cv2.contourArea(c)
    
        area4 = cv2.contourArea(c)
        if area4 > 5000:

             cv2.drawContours(frame,[c],-1,(0,255,0), 3)

             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             cv2.putText(frame,"blue", (cx-20,cy-20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 3)

        if area4 > 400:
            cv2.drawContours(frame, [approx4], 0, (0, 0, 0), 5)
            if len(approx4) == 3:
                cv2.putText(frame, "Triangle", (x4, y4), font, 1, (0, 0, 0))
            elif len(approx4) == 4:
                cv2.putText(frame, "Square", (x4, y4), font, 1, (0, 0, 0))
            elif 10 < len(approx4) < 20:
                cv2.putText(frame, "Circle", (x4, y4), font, 1, (0, 0, 0))

     cv2.imshow("result" , frame)        
     k = cv2.waitKey(5)
     if k == 27:
         break

cap.release()
cv2.destroyAllWindows()