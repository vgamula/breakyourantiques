import os

from flask import Flask
from flask.ext.assets import Environment
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from webassets.loaders import YAMLLoader

from antiques.core.utils import route


__all__ = ['route']

current_dir = os.path.dirname(os.path.realpath(__file__))
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

# Setup assets
assets_env = Environment(app)
yaml_loader = YAMLLoader(current_dir + '/assets.yml')
for name, bundle in yaml_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

# Registering blueprints:
from antiques.core.views import *  # noqa
from antiques.auth.views import auth_module  # noqa
app.register_blueprint(auth_module, url_prefix='/auth')
