import DeviceManager
from flask import jsonify
from flask import request

class DeviceController:
  
  def __init__(self, deviceManager):
    self.deviceManager = deviceManager

  def devicesList(self):
    devices = {}
    for key, value in self.deviceManager.deviceInstances.iteritems():
      devices[key] = value.__class__.__name__.lower()
    return jsonify(devices), 200

  def getDistance(self, name):
    device = self.deviceManager.deviceInstances.get(name)
    if(device == None):
      return "Device not found", 404
    else:
      distance = device.getDistance()
      return jsonify(distance), 200

  def toggleRelay(self, name):
    device = self.deviceManager.deviceInstances.get(name)
    if(device == None):
      return "Device not found", 404
    else:
      status = request.args.get('status')
      if(status == None):
        return "Missing status query param", 409
      status = int(status)
      duration = request.args.get('duration')      
      if(duration != None):
        duration = int(duration)      
      device.toggle(status, duration)
      return "ok", 200
