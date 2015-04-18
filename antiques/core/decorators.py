from functools import wraps

from flask import g, flash, redirect, url_for, request


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not (g.user.is_authenticated() and g.user.is_active()):
            flash(u'You need to be logged in.', 'info')
            return redirect(url_for('auth.login', next=request.path))
        return f(*args, **kwargs)
    return decorated


def logout_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if g.user.is_authenticated():
            return redirect('/')
        return f(*args, **kwargs)
    return decorated
