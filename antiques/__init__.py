import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from antiques.core.utils import route


__all__ = ['route']


env = os.environ.get('FLASK_ENV', 'development').lower()

app = Flask(__name__, static_folder='static')

if env == 'development':
    app.config.from_object('config.DevelopmentConfig')
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app)
elif env == 'production':
    app.config.from_object('config.ProductionConfig')

# Setup database
db = SQLAlchemy(app)

# Setup login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@app.route("/")
def hello():
    return "hello, world!"


# Registering blueprints:
from antiques.auth.views import auth_module  # noqa
app.register_blueprint(auth_module, url_prefix='/auth')
