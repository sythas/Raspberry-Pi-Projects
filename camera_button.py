#!/usr/bin/python
import os
import time
from picamera import PiCamera
from time import sleep

camera = PiCamera()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print GPIO.input(10)
while True:
   if ( GPIO.input(10) == False ):
      print("Button Pressed")
      os.system('date')
      print GPIO.input(10)
      camera.start_preview()
      sleep (10)
      camera.stop_preview()
      time.sleep(5)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
time.sleep(1)
