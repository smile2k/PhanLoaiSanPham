import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, Text, Button, LabelFrame, VERTICAL, E, NS, Scrollbar, Tk
#from tkinter import messagebox
import PIL.Image, PIL.ImageTk
import cv2
import numpy as np
import serial
import time

from cvzone.SerialModule import SerialObject
from time import sleep
#arduino = SerialObject("COM5")
#arduino = serial.Serial(port = 'COM5', timeout=0)
arduino = serial.Serial(port='COM6',timeout=.1)


window = Tk()
window.title("Computer Vision")
window.geometry("888x600")
url = "http://192.168.0.103:4747/video"
video = cv2.VideoCapture(url)
#video = cv2.VideoCapture(1)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) // 1
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) // 1
canvas = Canvas(window, width = canvas_w, height = canvas_h )

#canvas.create_rectangle()
canvas.pack()
canvas.create_rectangle(200, 200, 250, 250,  fill="red")
# add label
lbl=Label(window, text="PHÂN LOẠI ", font=50)
lbl.place(x=0, y=0)
lbl=Label(window, text="MÀU SẮC", font=50)
lbl.place(x=0, y=30)
lbl=Label(window, text="HUST ", font=50)
lbl.place(x=200, y=0)
dem=0
count = 0
count2 = 0
count3 = 0
tong = 0
congtac = 0
congtac1 = 0
congtac2 = 0
congtac3 = 0
value = 0
value1 = 1
value11 = 0
value2= 1
value22 = 0
value3 = 1
value33 = 0
thamso = -1
# add textbox
#txt=Entry(window, width=20)
#txt.grid(column=0, row=1)
#photo = None
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data


def update_frame():
    global tong
    global count1, count2, count3
    global dem
    global congtac, congtac1, congtac2, congtac3
    global value,thamso, value1, value11, value2, value22, value3, value33

    global canvas, photo
    # đọc từ camera
    ret, frame = video.read()
    # resize
    frame = cv2.resize(frame, dsize=None, fx=1, fy=1 )
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#RED
    low_red = np.array([0, 150, 20])  # 161,55,84 red
    high_red = np.array([15, 255, 255])  # 179,255,255 red
    # phân ngưỡng
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    contours1, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours1, -1, (0, 255, 0), 3)
    if len(contours1) != 0:
        thamso = thamso + 1
        for contour1 in contours1:
            if cv2.contourArea(contour1) > 1000:
                congtac1 = 1
                value1 = 1
                value11 = value11 + 1
                write_read("1")
                #arduino.write(str.encode('1'))
                # sleep(3)
                # tọa độ trên cùng bên trái
                x, y, w, h = cv2.boundingRect(contour1)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(frame, "RED", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
                #lbl = tkinter.Label(window, text="RED:   "+str(dem), fg= "red", font=50)
                #lbl.place(x=0, y=100)

        if(value11==0):
            value1 = 0
    value11 = 0
#
    low_green = np.array([40, 50, 30])
    high_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    contours2, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours2) != 0:

        for contour2 in contours2:
            if cv2.contourArea(contour2) > 1000:
                congtac2 = 1
                value2 = 1
                value22 = value22 + 1
                write_read("2")
                #arduino.sendData("2")
                # sleep(3)

                a, b, c, d = cv2.boundingRect(contour2)
                cv2.rectangle(frame, (a, b), (a + c, b + d), (0, 255, 0), 3)
                cv2.putText(frame, "GREEN", (int(a), int(b)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

                #lbl = tkinter.Label(window, text="GREEN: "+str(count), fg="green",font=50)
                #lbl.place(x=0, y=150)
        if (value22 == 0):
            value2 = 0
    value22 = 0
#YELLOW
    low_yellow = np.array([20, 100, 100])
    high_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    contours3, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours3) != 0:

        for contour3 in contours3:
            if cv2.contourArea(contour3) > 1000:
                congtac3 = 1
                value3 = 1
                value33 = value33 + 1
                # arduino.sendData([2])
                # sleep(3)

                g, h, j, k = cv2.boundingRect(contour3)
                cv2.rectangle(frame, (g, h), (g + j, h + k), (0, 255, 0), 3)
                cv2.putText(frame, "YELLOW", (int(g), int(g)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

                # lbl = tkinter.Label(window, text="GREEN: "+str(count), fg="green",font=50)
                # lbl.place(x=0, y=150)
        if (value33 == 0):
            value3 = 0
    value33 = 0
    #chuyển hệ màu
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # chuyển thành imageTk
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show
    canvas.create_image(0,0, image = photo, anchor = tkinter.NW)

    #lbl = tkinter.Label(window, text="Yellow: "+str(dem),fg="yellow", font=50)
    #lbl.place(x=0, y=200)

    if (congtac1 == 1):

        if(value1==0):
            dem = dem + 1
            lbl1 = tkinter.Label(window, text="RED:   " + str(dem), fg="red", font=50)
            lbl1.place(x=1, y=100)
            congtac1 = 0
    if (congtac2 == 1):
        if (value2 == 0 ):
            count2 = count2 + 1
            lbl2 = tkinter.Label(window, text="GREEN: " + str(count2), fg="green", font=50)
            lbl2.place(x=0, y=150)
            congtac2 = 0
    if (congtac3 == 1):
        if (value3 == 0 ):
            count3 = count3 + 1
            lbl3 = tkinter.Label(window, text="YELLOW: " + str(count3), fg="yellow",bg="blue", font=50)
            lbl3.place(x=0, y=200)
            congtac3 = 0
            '''
    if (congtac1 == 1 or congtac1 == 1 or congtac1 == 1):
        if (value1 == 0 or value2 == 0 or value3 == 0):
            tong = tong + 1
            lbl0 = tkinter.Label(window, text="TOTAL: " + str(dem+count2+count3), fg="blue", font=50)
            lbl0.place(x=2, y=250)
            congtac = 0
        '''
    lbl0 = tkinter.Label(window, text="TOTAL: " + str(dem + count2 + count3), fg="blue", font=50)
    lbl0.place(x=2, y=250)
    # add button
    btn = Button(window, text="RESET",fg="red",font=120, command=reset)
    btn.place(x=500, y=500)
    print("congtac=",congtac1)
    print(value1)
    window.after(15, update_frame)

def reset():
    dem = 0
    count2 = 0
    count3 = 0
    global lbl1
    lbl1 = lbl1.configure(text="RED:   " + str(dem))
    # lbl1 = tkinter.Label(window, text="RED:   " + str(dem), fg="red", font=50)
    # lbl1.place(x=1, y=100)
    return


update_frame()
window.mainloop()
