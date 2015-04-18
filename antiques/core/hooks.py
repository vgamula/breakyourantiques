from flask import g
from flask.ext.login import current_user


def before_request():
    g.user = current_user
