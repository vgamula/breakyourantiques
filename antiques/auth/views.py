import urllib
from flask import Blueprint, render_template, request, redirect
from flask.ext.login import login_user, logout_user

from antiques import route, login_manager
from antiques.core.decorators import login_required, logout_required

from .forms import RegisterForm, LoginForm
from .models import User


auth_module = Blueprint('auth', __name__, template_folder='templates/auth')


@login_manager.user_loader
def load_user(user_id):
    return User.find_one(id=int(user_id))


@route(auth_module, '/login', methods=['GET', 'POST'])
@logout_required
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.find_one(email=form.email.data)
        if user.check_password(form.password.data):
            login_user(user)
            return redirect('/')
        else:
            import ipdb; ipdb.set_trace()
            a = 2
    return render_template('auth/login.html', form=form)


@route(auth_module, '/register', methods=['GET', 'POST'])
@logout_required
def register():
    next = urllib.quote(request.args.get('next', ''))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = form.save()
        login_user(user)
        return redirect('/')
    return render_template(
        'auth/register.html',
        title='Sign Up',
        form=form,
        next=next
    )


@route(auth_module, '/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
