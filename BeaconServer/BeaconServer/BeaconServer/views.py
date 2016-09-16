"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from BeaconServer import app
from BeaconServer.config import *
from BeaconServer.model import Account
@app.route('/')
def helloworld():
    return 'hello world'

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api',methods=['POST'])
def api():
    user_id=request.form['user_id']
    action=request.form['action']
    k=request.form
    role=Account.query.filter(id=user_id).one().role
    if action not in action_map[role]:
        return 'Permission Denied'
    else:
        action_map[role][action](k)
    
