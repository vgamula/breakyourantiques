import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


env = os.environ.get('FLASK_ENV', 'development').lower()

app = Flask(__name__, static_folder='static')

if env == 'development':
    app.config.from_object('config.DevelopmentConfig')
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app)
elif env == 'production':
    app.config.from_object('config.ProductionConfig')

db = SQLAlchemy(app)
from antiques.accounts.models import User

@app.route("/")
def hello():
    return "hello, world!"


@app.route("/vova")
def hello2():
    return "my name is vova gamula!"


@app.route("/test")
def test():
    return "test"
