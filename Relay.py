import time
import RPi.GPIO as GPIO

class Relay:

  def __init__(self, pinNumber, initValue):
    self.pinNumber = pinNumber
    GPIO.setup(self.pinNumber, GPIO.OUT, initial=initValue)

  def toggle(self, status, duration):
    GPIO.output(self.pinNumber, status)
    if(duration != None):
      time.sleep(duration)
      GPIO.output(self.pinNumber, not status)
