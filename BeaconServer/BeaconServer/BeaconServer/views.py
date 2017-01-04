"""
Routes and views for the flask application.
"""
import json
from datetime import datetime
from flask import render_template,request,redirect,url_for,flash,session
from BeaconServer import app
from BeaconServer.config import *
from BeaconServer.function import *
from BeaconServer.model import Account
from BeaconServer.form import *
from flask.ext.bootstrap import Bootstrap
from flask_wtf import Form


@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    form=loginForm(username='klxjedj')
    if form.validate_on_submit():
        session['username']=form.username.data
        return render_template('admin.html',admin_list=admin_list)
    return render_template('login.html',form=form,url='login')


@app.route('/add_caregiver',methods=['GET','POST'])
def add_caregiver():
    form=addCaregiverForm()
    if form.validate_on_submit():
        result=createCareGiver(form.data)
        return render_template('result.html',query_results=result)
    return render_template('caregiverform.html',form=form,url='add_caregiver')

@app.route('/create_carerecipient',methods=['GET','POST'])
def create_carerecipient():
    form=addCarerecipientForm()
    if form.validate_on_submit():
        return createCareRecipient(form.data)
    return render_template('carerecipientform.html',form=form,url='create_carerecipient')

@app.route('/create_family_member',methods=['GET','POST'])
def create_family_member():
    form=addFamilyMemberForm()
    if form.validate_on_submit():
        return createFamilyMember(form.data)
    return render_template('familymemberform.html',form=form,url='create_family_member')

@app.route('/create_doctor',methods=['GET','POST'])
def create_doctor():
    form=addDoctorForm()
    if form.validate_on_submit():
        return createDoctor(form.data)
    return render_template('doctorform.html',form=form,url='create_doctor')

@app.route('/create_admin',methods=['GET','POST'])
def create_admin():
    form=addAdministratorForm()
    if form.validate_on_submit():
        return createAdministrator(form.data)
    return render_template('adminform.html',form=form,url='create_admin')

@app.route('/block_bad_giver',methods=['GET','POST'])
def block_bad_giver():
    form=blockBadGiverForm()
    if form.validate_on_submit():
        return 'ok'
    return render_template('webapi.html',form=form,url='block_bad_giver')

@app.route('/edit_carerecipient_info',methods=['GET','POST'])
def edit_carerecipient_info():
    form=editCarerecipientInfoForm()
    if form.validate_on_submit():
        return 'ok'
    return render_template('webapi.html',form=form,url='edit_carerecipient_info')

@app.route('/test',methods=['GET','POST'])
def test():
    
    return str(type(request.get_json()))

@app.route('/api',methods=['GET','POST'])
def api():
    k=request.get_json()
    user_id=k['user_id']
    role=Account.query.filter_by(account_id=user_id).one().role
    action=k['action']
    return action_map[role][action](k)


@app.route('/api_login',methods=['POST'])
def api_login():
    k=request.get_json()
    return apiLogin(k)
        




'''
Testing
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
