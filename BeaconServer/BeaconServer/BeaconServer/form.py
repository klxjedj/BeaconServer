from flask_wtf import Form
from wtforms import TextField,BooleanField,StringField,PasswordField,validators,FileField,TextAreaField,SubmitField,IntegerField,HiddenField
from wtforms.validators import DataRequired

class loginForm(Form):
    username=StringField('username',[DataRequired()])
    password=PasswordField('password',[DataRequired()])
    submit=SubmitField('Login')


class addCaregiverForm(Form):
    username=StringField('username',[DataRequired()])
    password=PasswordField('password',[DataRequired()])
    name=StringField('name')
    password_confirm=PasswordField('password confirm',[DataRequired()])
    demo_info=TextAreaField('demo_inof')
    expertise=StringField('expertise')
    contact=StringField('contact')
    submit=SubmitField('submit')

class addCarerecipientForm(Form):
    username=StringField('username',[DataRequired()])
    password=PasswordField('password',[DataRequired()])

    password_confirm=PasswordField('password confirm',[DataRequired()])
    name=StringField('name')

    address=StringField('address')
    resident_contact=StringField('resident_contact')
    mobile_contact=StringField('mobile_contact')
    contact_person_id=IntegerField('contact_person_id')
    doctor_id=IntegerField('doctor_id')
    family_history=StringField('family_history')
    beacon_id=StringField('beacon_id')
    submit=SubmitField('submit')

class addFamilyMemberForm(Form):
    username=StringField('username',[DataRequired()])
    password=PasswordField('password',[DataRequired()])
    password_confirm=PasswordField('password confirm',[DataRequired()])

    name=StringField('name')

    carerecipienet_id=IntegerField('carerecipient_id')
    submit=SubmitField('submit')


class addAdministratorForm(Form):
    username=StringField('username',[DataRequired()])
    password=PasswordField('password',[DataRequired()])
    password_confirm=PasswordField('password confirm',[DataRequired()])

    name=StringField('name')
    submit=SubmitField('submit')

class addDoctorForm(Form):
    username=StringField('username',[DataRequired()])
    password=PasswordField('password',[DataRequired()])
    password_confirm=PasswordField('password confirm',[DataRequired()])

    name=StringField('name')
    clinic=StringField('clinic')
    contact=StringField('contact')
    submit=SubmitField('submit')

class blockBadGiverForm(Form):
    caregiver_id=IntegerField('giver_id')
    submit=SubmitField('submit')

class editCarerecipientInfoForm(Form):
    carerecipient_id=IntegerField('carerecipient_id')
    resident_contact=StringField('resident_contact')
    mobile_contact=StringField('mobile_contact')
    contact_person_id=IntegerField('contact_person_id')
    doctor_id=IntegerField('doctor_id')
    family_history=StringField('family_history')
    beacon_id=StringField('beacon_id')
    submit=SubmitField('submit')



