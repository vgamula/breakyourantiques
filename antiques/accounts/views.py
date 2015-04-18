from flask import Blueprint, render_template

from antiques import route, login_manager

from .models import User


accounts_module = Blueprint('user', __name__, template_folder='templates/accounts')


@login_manager.user_loader
def load_user(user_id):
    return User.find_one(id=int(user_id))


@route(accounts_module, '/login', methods=['GET', 'POST'])
def login():
    return render_template('accounts/login.html')
