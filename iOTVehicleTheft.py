import numpy as np
import argparse
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import serial
from atttachem import sendMail
import smtplib
import RPi.GPIO as GPIO

i=0
data=""
GPIO.setmode(GPIO.BOARD)
buzzer=15
sw1=19
sw2=21
gas=11
motor=13
ir=7
count=0
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(ir,GPIO.IN)
GPIO.setup(gas,GPIO.IN)
GPIO.setup(sw1,GPIO.IN)
GPIO.setup(sw2,GPIO.IN)
GPIO.output(motor, 0)
camera = PiCamera()
camera.resolution = (640, 480)
##
##                        GPIO.output(buzzer, True)
##                        sleep(3)
##                        GPIO.output(buzzer, 0)
##                        camera.start_preview()
##                  
##                        sleep(2)
##                        camera.capture('image2.png')
##                        camera.stop_preview()
ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=.8)
ser.write(str.encode('AT'+'\r'))
print(ser.read(20))
sleep(1)
ser.write(b'ATE0\r')
print(ser.read(10))
##ser.write(b'ATD8660296977;\r')
##
##ser.write(b'AT+CMGF=1\r')
##print(ser.read(10))
##sleep(2)
ser.write(b'AT+CNMI=2,2,0,0,0\r')
##print(ser.read(30))
##ser.write(b'AT+CMGS="9632871904"\r\n')
##print(ser.read(30))
##sleep(2)
##ser.write(str.encode('HIiii\r\n'))
##ser.write(b'\x1A')
##for i in range (10):
##    print(ser.read(10))  
          
while (True):
    data=ser.readline()
    data=data.decode('utf-8').rstrip()
##    print(data)
    if(data=="stop"):
        print("entered")
        GPIO.output(motor, 0)
        
    if(GPIO.input(sw1)== 0):
        camera.start_preview()
        GPIO.output(motor, True)
        sleep(2)
        camera.capture('image2.png')
        camera.stop_preview()
        print("on")
        ser.write(str.encode('AT'+'\r'))
        print(ser.read(20))
        sleep(1)
        ser.write(b'ATE0\r')
        print(ser.read(10))
 ##ser.write(b'ATD8660296977;\r')

        ser.write(b'AT+CMGF=1\r')
        print(ser.read(10))
        sleep(2)
        ser.write(b'AT+CNMI=2,2,0,0,0\r')
        print(ser.read(30))
        ser.write(b'AT+CMGS="7618731414"\r\n')
        print(ser.read(30))
        sleep(2)
        ser.write(str.encode('Vehicle started\r\n'))
        ser.write(b'\x1A')
        for i in range (10):
            print(ser.read(10)) 
        sendMail( ["hrshubhashree@gmail.com"],
                  "Anti-theft",
                  "Unauthorized person detected and location https://www.google.com/maps/?q=12.907336,77.530227",
                  ["image2.png","main.py"] )       
    if(GPIO.input(sw2)== 0):
        count=count+1
        if count==1:
            GPIO.output(motor, 1)
            print("Authorized person and motor ON")
        if count==2:
            GPIO.output(motor, 0)
            count=0


    if(GPIO.input(gas)== 0):
        count=0
        GPIO.output(buzzer, True)
        GPIO.output(motor, 0)
        print("off")
        sleep(3)
        GPIO.output(buzzer, 0)
        ser.write(str.encode('AT'+'\r'))
        print(ser.read(20))
        sleep(1)
        ser.write(b'ATE0\r')
        print(ser.read(10))
        ##ser.write(b'ATD8660296977;\r')

        ser.write(b'AT+CMGF=1\r')
        print(ser.read(10))
        sleep(2)
        ser.write(b'AT+CNMI=2,2,0,0,0\r')
        print(ser.read(30))
        ser.write(b'AT+CMGS="7618731414"\r\n')
        print(ser.read(30))
        sleep(2)
        ser.write(str.encode('Alcohol deteted\r\n'))
        ser.write(b'\x1A')
        for i in range (10):
            print(ser.read(10)) 
    if(GPIO.input(ir)== 0):
        k=0
        print("Alert")
        for k in range (5):
            
            GPIO.output(buzzer, 1)
            sleep(0.3)
            GPIO.output(buzzer, 0)
            sleep(0.3)
