import os
import configparser

configParser = configparser.RawConfigParser()
configFilePath = r'config.cfg'
configParser.read(configFilePath)

class Config(object):
  SECRET_KEY = configParser.get('Settings', 'SECRET_KEY')
  BASIC_AUTH_USERNAME = configParser.get('Settings', 'BASIC_AUTH_USERNAME')
  BASIC_AUTH_PASSWORD = configParser.get('Settings', 'BASIC_AUTH_PASSWORD')
  BASIC_AUTH_FORCE = configParser.get('Settings', 'BASIC_AUTH_FORCE')
