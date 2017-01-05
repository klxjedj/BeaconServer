from BeaconServer import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data'
db=SQLAlchemy(app)

def showItem(item):
    s=''
    for i in item.__dict__:
        if isinstance(item.__dict__[i],str) or isinstance(item.__dict__[i],int):
            s+=i
            s+=':'
            s+=str(item.__dict__[i])
            s+='\n'
    return s

class Account(db.Model):
    __tablename__='Account'
    account_id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String)
    role=db.Column(db.String)

    def __repr__(self):
        return showItem(self)
    
class CareGiver(db.Model):
    __tablename__='CareGiver'
    account_id=db.Column(db.Integer,db.ForeignKey('Account.account_id'),primary_key=True)
    name=db.Column(db.String)
    gender=db.Column(db.String)
    email=db.Column(db.String)
    contact=db.Column(db.String)
    date_of_birth=db.Column(db.Date)
    highest_education_level=db.Column(db.String)
    no_of_service_given=db.Column(db.Integer)
    expertise=db.Column(db.String)
    block_status=db.Column(db.Integer)
    service_frequency=db.Column(db.Integer)

    def __repr__(self):
        return showItem(self)
    
class CareRecipient(db.Model):
    __tablename__='CareRecipient'
    account_id=db.Column(db.Integer,db.ForeignKey('Account.account_id'),primary_key=True)
    name=db.Column(db.String)
    gender=db.Column(db.String)
    address=db.Column(db.String)
    resident_contact=db.Column(db.String)
    mobile_contact=db.Column(db.String)
    contact_person_id=db.Column(db.Integer,db.ForeignKey('FamilyMember.account_id'))
    doctor_id=db.Column(db.Integer,db.ForeignKey('Doctor.account_id'))
    beacon_id=db.Column(db.String)
    def __repr__(self):
        return showItem(self)

class Doctor(db.Model):
    __tablename__='Doctor'
    account_id=db.Column(db.Integer,db.ForeignKey('Account.account_id'),primary_key=True)
    name=db.Column(db.String)
    clinic=db.Column(db.String)
    contact=db.Column(db.String)
    def __repr__(self):
        return showItem(self)

class FamilyMember(db.Model):
    __tablename__='FamilyMember'
    account_id=db.Column(db.Integer,db.ForeignKey('Account.account_id'),primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)
    contact_number=db.Column(db.String)

    def __repr__(self):
        return showItem(self)

class Administrator(db.Model):
    __tablename__='Administrator'
    id=db.Column(db.Integer,db.ForeignKey('Account.account_id'),primary_key=True)
    name=db.Column(db.String)
    def __repr__(self):
        return showItem(self)

  
class Bidding(db.Model):
    __tablename__='Bidding'
    bidding_id=db.Column(db.Integer,primary_key=True)
    record_id=db.Column(db.Integer,db.ForeignKey('CareRecord.record_id'))
    caregiver_id=db.Column(db.Integer,db.ForeignKey('CareGiver.account_id'))
    carerecipient_id=db.Column(db.Integer,db.ForeignKey('CareRecipient.account_id'))
    bidding_status=db.Column(db.String)  


class CareRecord(db.Model):
    __tablename__='CareRecord'
    record_id=db.Column(db.Integer,primary_key=True)
    caregiver_id=db.Column(db.Integer,db.ForeignKey('CareGiver.account_id'))
    caregiver_name=db.Column(db.String,db.ForeignKey('CareGiver.name'))
    carerecipient_id=db.Column(db.Integer,db.ForeignKey('CareRecipient.account_id'))
    carerecipient_name=db.Column(db.String,db.ForeignKey('CareRecipient.name'))
    appointment_time=db.Column(db.DATETIME)
    end_datetime=db.Column(db.DATETIME)

    special_need=db.Column(db.String)
    record_status=db.Column(db.String)
    review=db.Column(db.String)
    rate=db.Column(db.String)
    def __repr__(self):
        return showItem(self)

class DoctorReferral(db.Model):
    __tablename__='DoctorReferal'
    referal_id=db.Column(db.Integer,primary_key=True)
    doctor_id=db.Column(db.Integer,db.ForeignKey('Doctor.account_id'))
    carerecipient_id=db.Column(db.Integer,db.ForeignKey('CareRecipient.account_id'))
    referral_reason=db.Column(db.String)
    referral_date=db.Column(db.DATE)
    def __repr__(self):
        return showItem(self)
