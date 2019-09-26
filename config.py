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
  SECRET_KEY = configParser.get('Security', 'SECRET_KEY')
  BASIC_AUTH_USERNAME = configParser.get('Security', 'BASIC_AUTH_USERNAME')
  BASIC_AUTH_PASSWORD = configParser.get('Security', 'BASIC_AUTH_PASSWORD')
  BASIC_AUTH_FORCE = configParser.get('Security', 'BASIC_AUTH_FORCE')

  TASKS_PATH = configParser.get('Content', 'TASKS_PATH')

  def make_path():
    content = configParser['Content']
    for folder in content:
      if not os.path.isdir(content[folder]):
        os.makedirs(content[folder])
