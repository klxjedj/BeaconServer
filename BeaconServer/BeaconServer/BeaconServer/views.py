"""
Routes and views for the flask application.
"""
import json
from datetime import datetime
from flask import render_template,request,redirect,url_for,flash,session
from BeaconServer import app
from BeaconServer.config import *
from BeaconServer.function import *
'''
this script defines all the designed requests and how they are handled
'''
from BeaconServer.model import Account
from BeaconServer.form import *
from flask.ext.bootstrap import Bootstrap
from flask_wtf import Form


@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    '''
    this view process the login request from admin website, role check are not implemented yet.
    In fact only administrator account should be allowed here.
    If user logging from here is the system administrator, return the admin function page.
    '''
    form=loginForm(username='klxjedj')
    if form.validate_on_submit():
        session['username']=form.username.data
        return render_template('admin.html',admin_list=admin_list)
    return render_template('login.html',form=form,url='login')


@app.route('/add_caregiver',methods=['GET','POST'])
def add_caregiver():
    '''
    this view provide a form to submit caregiver data to add the infomation of a caregiver to the system,
    when added successfully,information of all the caregivers are rendered in JSON format. 
    '''
    form=addCaregiverForm()
    if form.validate_on_submit():
        result=createCareGiver(form.data)
        return render_template('result.html',query_results=result)
    return render_template('caregiverform.html',form=form,url='add_caregiver')

@app.route('/create_carerecipient',methods=['GET','POST'])
def create_carerecipient():
    '''
    this view provide a form to submit carerecipient data to add the infomation of a carerecipient to the system,
    when added successfully,information of all the carerecipients are rendered in JSON format. 
    '''
    form=addCarerecipientForm()
    if form.validate_on_submit():
        return createCareRecipient(form.data)
    return render_template('carerecipientform.html',form=form,url='create_carerecipient')

@app.route('/create_family_member',methods=['GET','POST'])
def create_family_member():
    '''
    this view provide a form to submit family member data to add the infomation of a family member to the system,
    when added successfully,information of all the family member are rendered in JSON format. 
    '''
    form=addFamilyMemberForm()
    if form.validate_on_submit():
        return createFamilyMember(form.data)
    return render_template('familymemberform.html',form=form,url='create_family_member')

@app.route('/create_doctor',methods=['GET','POST'])
def create_doctor():
    '''
    this view provide a form to submit family member data to add the infomation of a doctor to the system,
    when added successfully,information of all the doctors are rendered in JSON format. 
    '''
    form=addDoctorForm()
    if form.validate_on_submit():
        return createDoctor(form.data)
    return render_template('doctorform.html',form=form,url='create_doctor')

@app.route('/create_admin',methods=['GET','POST'])
def create_admin():
    '''
    this view provide a form to submit administrator data to add the infomation of a administrator to the system,
    when added successfully,information of all the administrators are rendered in JSON format. 
    '''
    form=addAdministratorForm()
    if form.validate_on_submit():
        return createAdministrator(form.data)
    return render_template('adminform.html',form=form,url='create_admin')

@app.route('/block_bad_giver',methods=['GET','POST'])
def block_bad_giver():
    '''
    this view are designed to block the bad caregivers,but the function are not implemented.
    '''
    form=blockBadGiverForm()
    if form.validate_on_submit():
        return 'ok'
    return render_template('webapi.html',form=form,url='block_bad_giver')

@app.route('/edit_carerecipient_info',methods=['GET','POST'])
def edit_carerecipient_info():
    '''
    this view are designed to edit carerecipient info but not implemented yet.
    '''
    form=editCarerecipientInfoForm()
    if form.validate_on_submit():
        return 'ok'
    return render_template('webapi.html',form=form,url='edit_carerecipient_info')

@app.route('/test',methods=['GET','POST'])
def test():
    '''
    this view are designed to debug in the development process.
    '''
    
    return str(type(request.get_json()))

@app.route('/api',methods=['GET','POST'])
def api():
    '''
    this is the api designed for data transmission between the app and the server.
    data is received in JSON format.
    two info are in the data, one is the userid of the user who are using the app, action is what the app want the server to do.
    a map from user role and permitted action are designed to control the behavior of different users.
    when info is extracted from request, this view get the user role and action allowed and call the action function. 
    '''
    k=request.get_json()
    user_id=k['user_id']
    role=Account.query.filter_by(account_id=user_id).one().role
    action=k['action']
    return action_map[role][action](k)


@app.route('/api_login',methods=['POST'])
def api_login():

    '''
    this view handle the request of login from app when user are logging in the app.
    '''
    k=request.get_json()
    return apiLogin(k)
        




'''
the following views are just to view the information in the database conveniently.
'''

@app.route('/ggg',methods=['GET'])
def view_giver():
    return viewCareGiver({})

@app.route('/aaa',methods=['GET'])
def view_account():
    return viewAccount({})

@app.route('/ddd',methods=['GET'])
def view_doctor():
    return viewDoctor({})

@app.route('/rrr',methods=['GET'])
def view_recipient():
    return viewCareRecipient({})

@app.route('/mmm',methods=['GET'])
def view_member():
    return viewFamilyMember({})

@app.route('/rcd',methods=['GET'])
def view_record():
    return viewCareRecord({})
