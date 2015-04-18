from flask import Blueprint, render_template

from antiques import route, login_manager
from antiques.core.decorators import logout_required

from .models import User


auth_module = Blueprint('auth', __name__, template_folder='templates/auth')


@login_manager.user_loader
def load_user(user_id):
    return User.find_one(id=int(user_id))


@route(auth_module, '/login', methods=['GET', 'POST'])
@logout_required
def login():
    return render_template('auth/login.html')
