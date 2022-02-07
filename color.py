import cv2
import numpy as np
from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("COM6")
#from object_detect import *

url = "http://192.168.0.102:4747/video"
cap = cv2.VideoCapture(url)
#cap.set(CV2_CAP_PROP_BUFFERSIZE, 3)

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame,(5,5),0)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)


    low_red = np.array([0,150,20]) #161,55,84 red
    high_red = np.array([15,255,255]) #179,255,255 red
    red_mask = cv2.inRange(hsv_frame,low_red,high_red)
    contours1, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours1, -1, (0, 255, 0), 3)
    if len(contours1) != 0:
        for contour in contours1:
            if cv2.contourArea(contour) > 1000:
                arduino.sendData([1])
                #sleep(3)

                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(frame, "RED", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    '''
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                a,b,c,d = cv2.boundingRect(contour)
                cv2.rectangle(frame, (a,b),(a+c,b+d),(0,255,0),3)
                cv2.putText(blue_mask, "BLUE", (int(a), int(b)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    '''
    #cv2.drawContours(frame,contours,-1,(0,255,0),3)
    #detector = HomogeneousBgDetector()

    low_green = np.array([40, 50, 30])
    high_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                arduino.sendData([2])
                #sleep(3)


                a, b, c, d = cv2.boundingRect(contour)
                cv2.rectangle(frame, (a, b), (a + c, b + d), (0, 255, 0), 3)
                cv2.putText(frame, "GREEN", (int(a), int(b)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    '''
    for cnt in contours:
        cv2.polylines(blue,[cnt],True,(255,0,0),2)
        (x,y),(w,h), angle = cv2.minAreaRect(cnt)
    cv2.putText(blue, "BLUE", (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    for cnt1 in contours1:
        cv2.polylines(red,[cnt1],True,(255,0,0),2)
        (x,y),(i,j), angle1 = cv2.minAreaRect(cnt1)
    cv2.putText(red, "RED", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    '''
    #cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
    #cv2.putText(blue,"BLUE",(0,10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    #cv2.putText(frame, "RED", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    #cv2.putText(frame, "GREEN",(int(a), int(b)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    if len(contours) == 0:
        arduino.sendData([0])

    print(len(contours))
    cv2.imshow("test",frame)
    key = cv2.waitKey(1)
    if key == 27 or key == 'q':
        break

#cap.release()
#cv2.destroyAllWindows()



