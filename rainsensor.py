#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
state = GPIO.input(4)

while true:
    if state == 0:
        print "Water detected!"
        r = requests.get("http://erp.librairielabourse.com/postcall/rainsensor.postcall.php")
    else:
        print "Water not detected"