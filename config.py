import os
import configparser

configParser = configparser.ConfigParser()
configFile = 'config.ini'
configDefault = 'config.default'
if os.path.isfile(configFile):
  configParser.read(configFile)
else:
  configParser.read(configDefault)
  with open(configFile, 'w') as conf:
    configParser.write(conf)

class Config(object):
  SECRET_KEY = configParser.get('Settings', 'SECRET_KEY')
  BASIC_AUTH_USERNAME = configParser.get('Settings', 'BASIC_AUTH_USERNAME')
  BASIC_AUTH_PASSWORD = configParser.get('Settings', 'BASIC_AUTH_PASSWORD')
  BASIC_AUTH_FORCE = configParser.get('Settings', 'BASIC_AUTH_FORCE')
