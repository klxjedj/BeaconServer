'''
this script defined all the function which are usered for handling the requests and other actions of user.
'''


from BeaconServer.model import *
from BeaconServer import *
import json
from datetime import datetime
from dateutil.parser import parse
import shelve

type_map={'a':Administrator,
          'g':CareGiver,
          'r':CareRecipient,
          'm':FamilyMember,
          'd':Doctor
          }


'''
General Function
'''

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

def mod2json(m):
    data={}
    for i in m.__dict__:
        if not i.startswith('_'):
            data[i]=m.__dict__[i]
            if isinstance(data[i],datetime):
                data[i]=str(data[i])
    return json.dumps(data)

def changePassword(k):
    account=Account.query.filter(Account.account_id==k['user_id']).one()
    if account.password==k['old_password']:
        account.password=k['new_password']
        db.session.add(account)
        db.session.commit()
        return 'Password Changed'
    else:
        return 'Incorrect Password'

'''
Create Data
'''
def createUser(type,k):
    
    acc_id=shelve.open('account_id')
    if not acc_id:
        ACCOUNT_ID=1
        db.create_all()
    else:
        ACCOUNT_ID=acc_id['id']

    new_acct=Account(account_id=ACCOUNT_ID,username=k['username'],password=k['password'],role=type)
    new_user=type_map[type](account_id=ACCOUNT_ID)
    for i in dir(new_user):
        if i in k:
            setattr(new_user,i,k[i])
    db.session.add_all([new_user,new_acct])
    db.session.commit()
    ACCOUNT_ID+=1
    acc_id['id']=ACCOUNT_ID
    
def createCareGiver(k):
    createUser('g',k)
    return viewCareGiver(k)

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

'''
Recipient Action
'''

def createCareRequest(k):
    record_id=shelve.open('record_id')
    if not record_id:
        RECORD_ID=1
    else:
        RECORD_ID=record_id['id']    
    cr=CareRecord(record_id=RECORD_ID)
    cr.appointment_time=parse(k['appointment_time'])
    cr.caregiver_id=k['caregiver_id']
    cg=CareGiver.query.filter_by(account_id=k['caregiver_id']).one()
    cr.caregiver_name=cg.name
    cr.carerecipient_id=k['user_id']
    cc=CareRecipient.query.filter_by(account_id=k['user_id']).one()
    cr.carerecipient_name=cc.name
    cr.record_status='on_request'
    cr.special_need=k['special_needs']
    db.session.add(cr)
    db.session.commit()
    RECORD_ID+=1
    record_id['id']=RECORD_ID
    return "success"

def DeleteRequests(k):
    crl=CareRecord.query.all()
    for cr in crl:
        db.session.delete(cr)
    db.session.commit()
    return "success"

def viewCareGivers(k):
    gl=CareGiver.query.all()
    return list2json(gl)

'''
Giver Action
'''

def viewRequests(k):
    rl=CareRecord.query.filter_by(caregiver_id=k['user_id']).filter_by(record_status='on_request').all()
    return list2json(rl)

def viewProfile(k):
    gm=CareGiver.query.filter_by(account_id=k['user_id']).one()
    return mod2json(gm)

def viewRequestToday(k):
    rl=CareRecord.query.filter_by(record_status='confirmed').all()
    return list2json(rl)

def getCancelLeft(k):
    return str(3)










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



def acceptRequest(k):
    rc=CareRecord.query.filter_by(record_id=k['record_id']).one()
    if rc.caregiver_id==k['user_id']:
        rc.record_status='confirmed'
        db.session.commit()
        return 'Request Accepted'
    else:
        return 'Incorrect Info'


def cancelRequest(k):
    rc=CareRecord.query.filter_by(record_id=k['record_id']).one()
    rc.record_status='cancelled'
    db.session.commit()
    return "cancelled"

def viewFullInfo(k):
    cr=CareRecipient.query.filter_by(beacon_id=k['beacon_id']).one()
    data={}
    for i in cr.__dict__:
        if not i.startswith('_'):
            data[i]=cr.__dict__[i]
    return json.dumps(data)
  




def showDoctorContact(k):
    recipient_id=k['recipient_id']
    cr=CareRecipient.query.filter_by(id=recipient_id).one()
    return cr.doctor.contact

def viewServiceToPerform(k):
    rl=CareRecord.query.filter_by(caregiver_id=k['user_id']).filter_by(record_status='confirmed').all()
    return list2json(rl)




def apiLogin(k):
    rl=Account.query.filter_by(username=k['username'], password=k['password']).one()
    if not rl:
        return 'result is null'
    else:
        return mod2json(rl)




def viewAccount(k):
    al=Account.query.all()
    return list2json(al)

def viewDoctor(k):
    al=Account.query.all()
    return list2json(al)

def viewCareRecipient(k):
    al=Account.query.all()
    return list2json(al)

def viewFamilyMember(k):
    al=Account.query.all()
    return list2json(al)

def viewCareRecord(k):
    al=CareRecord.query.all()
    return list2json(al)

def viewCareRecordById(k):
    al=CareRecord.query.filter_by(record_id=k['record_id']).one()
    return mod2json(al)

def viewRecordsByRecipient(k):
    rl=CareRecord.query.filter_by(recipient_id=k['carerecipient_id']).all()
    return list2json(rl)

def viewCareGiverById(k):
    al=CareGiver.query.filter_by(id=k['caregiver_id']).one()
    return mod2json(al)



def viewTodayService(k):
    al=CareRecord.query.filter_by(caregiver_id=k['user_id']).all()
    today=datetime.now().date()
    rl=[item for item in al if item.appointment_time.date==today]
    return list2json(rl)

