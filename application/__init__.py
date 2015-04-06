import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


env = os.environ.get('FLASK_ENV', 'development').lower()

app = Flask(__name__, static_folder='static')
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "hello, world!"
