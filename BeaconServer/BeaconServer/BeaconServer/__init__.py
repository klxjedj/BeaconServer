"""
The flask application package.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config['WTF_CSRF_ENABLED']=False
app.config['SECRET_KEY']='klxjedj'
from BeaconServer.model import db
import BeaconServer.views
