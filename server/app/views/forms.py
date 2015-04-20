from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import validators
from wtforms.fields import TextField, StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = EmailField('email:', [validators.Required('Email address is required!')])
    name = StringField('name:', [validators.Required('User name is required!')])
    password = PasswordField('password:', [validators.Required('Password is required!')])