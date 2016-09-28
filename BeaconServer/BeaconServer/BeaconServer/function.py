from BeaconServer.model import *
from BeaconServer import *
import json
from datetime import datetime

type_map={'a':Administrator,
          'g':CareGiver,
          'r':CareRecipient,
          'm':FamilyMember,
          'd':Doctor
          }

def createUser(type,k):
    global ACCOUNT_ID
    new_acct=Account(id=ACCOUNT_ID,username=k['username'],password=k['password'],role=type)
    new_user=type_map[type](id=ACCOUNT_ID)
    for i in dir(new_user):
        if i in k:
            setattr(new_user,i,k[i])
    db.session.add_all([new_user,new_acct])
    db.session.commit()
    ACCOUNT_ID+=1
    

def list2json(l):
    lr=[]
    for request in l:
        data={}
        for i in request.__dict__:
            if not i.startswith('_'):
                data[i]=request.__dict__[i]
                if isinstance(data[i],datetime):
                    data[i]=str(data[i])
        lr.append(data)
    return json.dumps(lr) 

def createCareGiver(k):
    createUser('g',k)
    return viewCareGiver()

def createCareRecipient(k):
    createUser('r',k)
    return list2json(db.session.query(CareRecipient).all())

def createFamilyMember(k):
    createUser('m',k)
    return list2json(db.session.query(FamilyMember).all())

def createDoctor(k):
    createUser('d',k)
    return list2json(db.session.query(Doctor).all())

def createAdministrator(k):
    createUser('a',k)
    return list2json(db.session.query(Administrator).all())

def changePassword(k):
    account=Account.query.filter(Account.id==k['user_id']).one()
    if account.password==k['old_password']:
        account.password=k['new_password']
        db.session.add(account)
        db.session.commit()
        return 'Password Changed'
    else:
        return 'Incorrect Password'

def blockBadGiver(k):
    giver_id=k['giver_id']
    CareGiver.query.filter(id=giver_id).one().block_status='block'
    db.session.commit()

def editCareRecipientInfo(k):
    recipient_id=k['recipient_id']
    target=CareRecipient.query.filter_by(id=recipient_id).one()
    for i in target.__dict__:
        if i in k:
            target.__setattr__(i,k[i])
    db.session.commit()
    return 'Info Changed'

def createCareRequest(k):
    global RECORD_ID
    cr=CareRecord(record_id=RECORD_ID)
    cr.appointment_time=k['appointment_time']
    cr.caregiverid=k['caregiver_id']
    cr.carerecipientid=k['user_id']
    cr.record_status='on_request'
    cr.location=k['location']
    db.session.add(cr)
    db.session.commit()
    RECORD_ID+=1

def acceptRequest(k):
    rc=CareRecord.query.filter_by(record_id=k['record_id']).one()
    if rc.caregiverid==k['user_id']:
        rc.record_status='confirmed'
        db.session.commit()
        return 'Request Accepted'
    else:
        return 'Incorrect Info'
    
def cancelRequest(k):
    rc=CareRecord.query.filter_by(record_id=k['record_id']).one()
    rc.record_status='cancelled'

def viewFullInfo(k):
    cr=CareRecipient.query.filter_by(beacon_id=k['beacon_id']).one()
    data={}
    for i in cr.__dict__:
        if not i.startswith('_'):
            data[i]=cr.__dict__[i]
    return json.dumps(data)
  
def viewRequest(k):
    rl=CareRecord.query.filter_by(caregiverid=k['user_id']).filter_by(record_status='on_request').all()
    return list2json(rl)

def showDoctorContact(k):
    recipient_id=k['recipient_id']
    cr=CareRecipient.query.filter_by(id=recipient_id).one()
    return cr.doctor.contact

def viewServiceToPerform(k):
    rl=CareRecord.query.filter_by(caregiverid=k['user_id']).filter_by(record_status='confirmed').all()
    return list2json(rl)

def apiLogin(k):
    rl=Account.query.filter_by(username=k['username'], password=k['password']).all()
    return list2json(rl)

def viewRestrictedCareRecipientInfo(k):
    return 

def viewTrackingInfo(k):
    return

def saveServiceSummary(k):
    return

#define
def viewCareGiver(k):
    gl=CareGiver.query.all()
    return list2json(gl)