from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import validators
from wtforms.fields import TextField, StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = EmailField('Email:', [validators.Required('Email address is required!')])
    name = StringField('Nickame:', [validators.Required('User name is required!')])
    password = PasswordField('Password:', [validators.Required('Password is required!')])