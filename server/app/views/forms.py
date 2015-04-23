from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import validators
from wtforms.fields import TextField, StringField, PasswordField

class LoginForm(Form):
    email = EmailField('Email', [validators.InputRequired('Email address is required!'), validators.Email('Email address is not valid!')])
    password = PasswordField('Password', [validators.InputRequired('Password is required!')])