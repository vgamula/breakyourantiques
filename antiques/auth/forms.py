from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email


class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message=u'You should enter your email address.')])
    password = PasswordField('PasswordField', [Required(message=u'You should provide a password.')])
