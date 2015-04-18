from flask import Blueprint, render_template

from antiques import route


accounts_module = Blueprint('user', __name__, template_folder='templates/accounts')


@route(accounts_module, '/login', methods=['GET', 'POST'])
def login():
    return render_template('accounts/login.html')
