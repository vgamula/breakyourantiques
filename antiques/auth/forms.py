from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, StopValidation

from .models import User


class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message=u'You should enter your email address.')])
    password = PasswordField('Password', [Required(message=u'You should provide a password.')])


class RegisterForm(LoginForm):
    email = TextField('Email Address', [Email(), Required(message=u'You should enter your email address.')])
    first_name = TextField('First Name', [Required(message=u'You should enter your first name.')])
    last_name = TextField('First Name', [Required(message=u'You should enter your last name.')])

    def validate_email(self, field):
        user = User.find_one(email=field.data)
        if user:
            raise StopValidation('Email must be unique.')

    def save(self):
        user = User()
        user.email = self.email.data
        user.first_name = self.first_name.data
        user.last_name = self.last_name.data
        user.set_password(self.password.data)
        user.save()
        return user
