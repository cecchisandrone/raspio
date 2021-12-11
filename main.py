import time
import atexit
import os
from flask import Flask
from DeviceManager import DeviceManager
from DeviceController import DeviceController
import configparser

devicesConfig = configparser.ConfigParser()
devicesConfig.read(os.getenv("RASPIO_CONFIG_FILE", default='config.ini'))
deviceManager = DeviceManager(devicesConfig)
deviceController = DeviceController(deviceManager)

@atexit.register
def exit():
  deviceManager.cleanup()

if __name__ == '__main__':  
  app = Flask(__name__)
  app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
  app.route('/devices', methods=['GET'])(deviceController.devicesList)
  app.route('/devices/sonar/<name>', methods=['GET'])(deviceController.getDistance)
  app.route('/devices/relay/<name>', methods=['PUT'])(deviceController.toggleRelay)
  app.run(host='0.0.0.0', port=6000)
