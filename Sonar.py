import time
import RPi.GPIO as GPIO

class Sonar:

  def __init__(self, triggerPin, echoPin):
    self.triggerPin = triggerPin
    self.echoPin = echoPin
    GPIO.setup(triggerPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

  def getDistance(self):
    GPIO.output(self.triggerPin, False)
    # Allow module to settle
    time.sleep(0.5)
    # Send 10us pulse to trigger
    GPIO.output(self.triggerPin, True)
    time.sleep(0.00001)
    GPIO.output(self.triggerPin, False)
    start = time.time()
    while GPIO.input(self.echoPin)==0:
      start = time.time()
    while GPIO.input(self.echoPin)==1:
      stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300
    # That was the distance there and back so halve the value
    distance = distance / 2
    print("Distance : %.1f" % distance)
    return distance
