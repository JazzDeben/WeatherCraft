# Reading an analogue sensor with
# a single GPIO pin

# Author : Matt Hawkins
# Distribution : Raspbian
# Python : 2.7
# GPIO   : RPi.GPIO v3.1.0a

import RPi.GPIO as GPIO, time

from telnetapi import day, night

# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

# Define function to measure charge time
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement
def foreverlight(user, password, targetip, portnumber):
  # Main program loop

  lightswitch = None  
  daylight = None
  nighttime = None

  while True:
    time.sleep(5.0)
    light = RCtime(4)
    print (light)
    if(light>1000):
      if not nighttime:
        night(user, password, targetip, portnumber)
      daylight = False
      nighttime = True
    elif(light<=1000):
      if not daylight:
        day(user, password, targetip, portnumber)
      daylight =  True
      nighttime = False

