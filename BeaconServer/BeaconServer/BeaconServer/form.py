from flask_wtf import Form
from wtforms import PasswordField,TextField,SubmitField

class loginForm(Form):
    username=TextField('Username')
    password=PasswordField('Password')
    submit=SubmitField()