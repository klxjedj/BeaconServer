"""
The flask application package.
"""

from flask import Flask
from flask_wtf.csrf import CsrfProtect
app = Flask(__name__)
CsrfProtect(app)
app.config['SECRET_KEY']='klxjedj'
app.config['WTF_CSRF_SECRET_KEY']='klxjedj'

ACCOUNT_ID=1
import BeaconServer.views
