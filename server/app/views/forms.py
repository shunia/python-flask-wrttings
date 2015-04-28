from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import validators
from wtforms.fields import TextField, StringField, PasswordField

class LoginForm(Form):
    email = EmailField('Email:', [validators.InputRequired('Email address is required!'), validators.Email('Email address is not valid!')])
    password = PasswordField('Password:', [validators.InputRequired('Password is required!')])

class RegisterForm(LoginForm):
    nickname = StringField('NickName:', [validators.InputRequired('Can not be empty!')])

class ProfileForm(Form):
    id = StringField('id')
    nickname = StringField('Nickname:', [validators.InputRequired('Can not be empty!')])
    email = EmailField('Email:', [validators.InputRequired('Can not be empty!')])
    age = StringField('Age:', [validators.InputRequired('Can not be empty!')])