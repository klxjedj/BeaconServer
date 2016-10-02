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
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String)
    role=db.Column(db.String)

    def __repr__(self):
        return showItem(self)

class CareGiver(db.Model):
    __tablename__='CareGiver'
    id=db.Column(db.Integer,db.ForeignKey('Account.id'),primary_key=True)
    account=db.relationship('Account')
    
    name=db.Column(db.String)
    gender=db.Column(db.String)
    email=db.Column(db.String)
    contact=db.Column(db.String)
    date_of_birth=db.Column(db.DATETIME)
    highest_education_level=db.Column(db.String)
   
    expertise=db.Column(db.String)

    average_rating=db.Column(db.Float(precision=2),default=0)
    block_status=db.Column(db.Integer)
    service_frequency=db.Column(db.Integer)
    no_of_service_given=db.Column(db.Integer,default=0)

    current_service=db.Column(db.Integer,db.ForeignKey('CareRecord.record_id'))
    def __repr__(self):
        return showItem(self)

class Doctor(db.Model):
    __tablename__='Doctor'
    id=db.Column(db.Integer,db.ForeignKey('Account.id'),primary_key=True)
    account=db.relationship('Account')
    
    name=db.Column(db.String)
    clinic=db.Column(db.String)
    contact=db.Column(db.String)
    def __repr__(self):
        return showItem(self)

class CareRecipient(db.Model):
    __tablename__='CareRecipient'
    id=db.Column(db.Integer,db.ForeignKey('Account.id'),primary_key=True)
    account=db.relationship('Account')
    
    name=db.Column(db.String)
    gender=db.Column(db.String)
    address=db.Column(db.String)
    
    resident_contact=db.Column(db.String)
    mobile_contact=db.Column(db.String)
    
    contact_person_id=db.Column(db.Integer,db.ForeignKey('FamilyMember.id'))
    
    contact_person=db.relationship('FamilyMember',foreign_keys=[contact_person_id])
    
    doctor_id=db.Column(db.Integer,db.ForeignKey('Doctor.id'))
    doctor=db.relationship('Doctor')
    family_history=db.Column(db.String)
    beacon_id=db.Column(db.String)
    def __repr__(self):
        return showItem(self)

class FamilyMember(db.Model):
    __tablename__='FamilyMember'
    id=db.Column(db.Integer,db.ForeignKey('Account.id'),primary_key=True)
    account=db.relationship('Account')
    
    relationship=db.Column(db.String)
    carerecipient_id=db.Column(db.Integer,db.ForeignKey('CareRecipient.id'))
    carerecipient=db.relationship('CareRecipient',backref='family_member',foreign_keys=[carerecipient_id])
    def __repr__(self):
        return showItem(self)
    

class Administrator(db.Model):
    __tablename__='Administrator'
    id=db.Column(db.Integer,db.ForeignKey('Account.id'),primary_key=True)
    name=db.Column(db.String)
    account=db.relationship('Account')
    def __repr__(self):
        return showItem(self)

class CareRecord(db.Model):
    __tablename__='CareRecord'
    record_id=db.Column(db.Integer,primary_key=True)
    caregiver_id=db.Column(db.Integer,db.ForeignKey('CareGiver.id'))
    caregiver=db.relationship('CareGiver',backref='records',foreign_keys=[caregiver_id])
    carerecipient_id=db.Column(db.Integer,db.ForeignKey('CareRecipient.id'))
    carerecipient=db.relationship('CareRecipient',backref='records',foreign_keys=[carerecipient_id])

    appointment_time=db.Column(db.DATETIME)
    end_datetime=db.Column(db.DATETIME)
    duration=db.Column(db.Integer)

    location=db.Column(db.String)
    special_need=db.Column(db.String)
    record_status=db.Column(db.String)

    review=db.Column(db.String)
    rating=db.Column(db.DECIMAL(precision=2))
    def __repr__(self):
        return showItem(self)

class DoctorReferral(db.Model):
    __tablename__='DoctorReferal'
    id=db.Column(db.Integer,db.ForeignKey('Account.id'),primary_key=True)
    doctor_id=db.Column(db.Integer,db.ForeignKey('Doctor.id'))
    carerecipient_id=db.Column(db.Integer,db.ForeignKey('CareRecipient.id'))
    referral_reason=db.Column(db.String)
    referral_date=db.Column(db.DATE)
    def __repr__(self):
        return showItem(self)
