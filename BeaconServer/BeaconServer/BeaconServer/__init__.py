"""
The flask application package.
this script will be executed when start running the server.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config['WTF_CSRF_ENABLED']=False
app.config['SECRET_KEY']='klxjedj'
from BeaconServer.model import db
import BeaconServer.views
