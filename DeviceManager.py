import RPi.GPIO as GPIO
from Sonar import Sonar 
from Relay import Relay

class DeviceManager:
  
  deviceClasses = {'sonar': Sonar, 'relay': Relay}  

  def __init__(self, devicesConfig): 
    GPIO.setmode(GPIO.BCM)
    self.devicesConfig = devicesConfig
    self.deviceInstances = {}
    for section in self.devicesConfig.sections():
      deviceClassName = section.split('.')[0]
      deviceName = section.split('.')[1]      
      deviceClass = DeviceManager.deviceClasses[deviceClassName]      
      args = []
      for (key, val) in self.devicesConfig.items(section):        
        args.append(val)
      instance = None
      
      if(section == 'sonar'):
        instance = deviceClass(int(args[0]), int(args[1]))
      else:
        instance = deviceClass(int(args[0]), int(args[1]))
      
      self.deviceInstances[deviceName] = instance    

  def cleanup(self):
    GPIO.cleanup()

