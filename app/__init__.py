from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
basic_auth = BasicAuth(app)

Config.make_path()

from app import routes
