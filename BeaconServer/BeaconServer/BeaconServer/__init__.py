"""
The flask application package.
"""

from flask import Flask
from flask_wtf.csrf import CsrfProtect
app = Flask(__name__)

ACCOUNT_ID=1
import BeaconServer.views
