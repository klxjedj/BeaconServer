from flask_wtf import Form
from wtforms import PasswordField,TextField

class loginForm(Form):
    username=TextField('username')
    password=PasswordField('password')