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

  CONTENT_PATH = configParser.get('Content', 'CONTENT_PATH')
  CONTENT_FOLDERS = eval(configParser.get('Content', 'CONTENT_FOLDERS'))

  def make_path():
    path = configParser.get('Content', 'CONTENT_PATH')
    folders = eval(configParser.get('Content', 'CONTENT_FOLDERS'))
    for folder in folders:
      if not os.path.isdir(os.path.join(path,folder)):
        os.makedirs(os.path.join(path,folder))
