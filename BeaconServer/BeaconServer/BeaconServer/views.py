"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,redirect,url_for,flash,session
from BeaconServer import app
from BeaconServer.config import *
from BeaconServer.function import *
from BeaconServer.model import Account
from BeaconServer.form import *
from flask.ext.bootstrap import Bootstrap

Bootstrap(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    d={'logged':False}
    form=loginForm()
    if request.method=='POST':
        app.logger.debug('kdajodijadlfja')
        return render_template('admin.html')
    return render_template('a.html',form=form)


@app.route('/add_caregiver')
def add_caregiver():
    return 'add caregiver'

@app.route('/create_carerecipient')
def create_carerecipient():
    return 'create_carerecipient'

@app.route('/create_family_member')
def create_family_member():
    return 'create_family_member'

@app.route('/create_doctor')
def create_doctor():
    return 'create_doctor'

@app.route('/create_admin')
def create_admin():
    return 'create_admin'

@app.route('/block_bad_giver')
def block_bad_giver():
    return 'block_bad_giver'

@app.route('/edit_carerecipient_info')
def edit_carerecipient_info():
    return 'edit_carerecipient_info'






















'''
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
'''
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
    
