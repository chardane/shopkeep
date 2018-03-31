import RPi.GPIO as GPIO
import time
import requests
from datetime import datetime

PIR1 = 11
LED = 3

API_ENDPOINT = "

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR1, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(LED, GPIO.OUT)         #LED output pin
GPIO.output(LED,0)

curr1 = 0
timestamp = 0
while True:
    i1=GPIO.input(PIR1)

    if i1==0:                 #When output from motion sensor is LOW
        if curr1==1:
            print "1: No intruders",curr1
            curr1 = 0

        GPIO.output(LED,0)

        #time.sleep(0.1)

    elif i1==1:  #When output from motion sensor is HIGH
        if curr1==0:
            print "1: Intruder detected",curr1
            print "time", datetime.now().time()
            print "epochtime", int(time.time())
            timestamp = int(time.time())
            now = datetime.now()
            year = now.year
            month = now.month
            day = now.day
            hour = now.hour
            print now, year, month, day, hour
            # call to thingspeak/shopkeep
            # call to shopkeep


            curr1 = 1

        GPIO.output(LED,1)
        #time.sleep(0.1)