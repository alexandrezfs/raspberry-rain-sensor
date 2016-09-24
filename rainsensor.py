#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO
import requests
import time

isRaining = False
supposedStoppedRainingTimestamp = 0
GPIO_NUMBER = 4
WS_URL = 'http://erp.librairielabourse.fr/postcall/rainsensor.postcall.php'

while True:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_NUMBER, GPIO.IN)
    state = GPIO.input(GPIO_NUMBER)

    if state == 0:

        print "Water detected !"

        if isRaining == False:
            print "Calling server..."
            isRaining = True;
            requests.post(WS_URL, data = {})
            sleep(1200)
    else:
        print "Water not detected..."

        if isRaining == True:
            print "It maybe stopped raining... let's wait some time."
            supposedStoppedRainingTimestamp = time.time()
            isRaining = False        
 
        if supposedStoppedRainingTimestamp != 0 and time.time() > (supposedStoppedRainingTimestamp + 600):
            print "It surely stopped raining. Calling server..."
            requests.post(WS_URL, data = {'stoppedRaining' : True})
            supposedStoppedRainingTimestamp = 0

        sleep(1)

