import RPi.GPIO as GPIO
import time
import requests
from datetime import datetime
from pytz import timezone
import pytz

PIR1 = 11
LED = 3

API_ENDPOINT = "https://api.thingspeak.com/update.json"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR1, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(LED, GPIO.OUT)         #LED output pin
GPIO.output(LED,0)

curr1 = 0
timestamp = 0
pacific = timezone("US/Pacific-New")
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
            now = datetime.now(tz=pacific)
            year = now.year
            month = now.month
            day = now.day
            hour = now.hour
            print "now: ", now
            print "hour: ", hour
            print "day: ", day
            print "month: ", month
            print "year: ", year
            # call to thingspeak/shopkeep
            # call to shopkeep


            curr1 = 1

        GPIO.output(LED,1)
        #time.sleep(0.1)
