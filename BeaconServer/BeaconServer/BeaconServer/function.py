from BeaconServer.model import *
from BeaconServer import *
from sqlalchemy.sql import func
import json
from datetime import datetime
from flask import Flask, request, jsonify

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

def object2json(object):
    data={}
    for i in object.__dict__:
        if not i.startswith('_'):
            data[i]=object.__dict__[i]
            if isinstance(data[i],datetime):
                    data[i]=str(data[i])
    return json.dumps(data)

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

def editCareGiverInfo(k):
    caregiver_id=k['caregiver_id']
    target=CareGiver.query.filter_by(id=caregiver_id).one()
    for i in target.__dict__:
        if i in k:
            target.__setattr__(i,k[i])
    db.session.commit()
    return 'Info Changed'

def createCareRequest(k):
    global RECORD_ID
    cr=CareRecord()
    appointment_datetime=k['appointment_time']
    if isinstance(appointment_datetime, str) :
        cr.appointment_time=datetime.strptime(appointment_datetime, '%Y-%m-%d %H:%M:%S')
    else:
        cr.appointment_time=appointment_datetime
    cr.caregiver_id=k['caregiver_id']
    cr.carerecipient_id=k['user_id']
    cr.record_status='on_request'
    cr.location=CareRecipient.query.filter_by(id=k['user_id']).first().address
    db.session.add(cr)
    db.session.commit()
    RECORD_ID+=1
    return 'success'

def rateReviewCareService(k):
    rowsUpdated=db.session.query(CareRecord).filter(CareRecord.record_id==k['record_id']).update({"rating": k['rating'], "review": k['review']})
    db.session.commit()
    return rowsUpdated

def acceptRequest(k):
    rc=CareRecord.query.filter_by(record_id=k['record_id']).one()
    caregiver_id=k['user_id']
    if rc.caregiver_id==caregiver_id:
        # no_of_service_given=CareGiver.query.with_entities(CareGiver.no_of_service_given).filter_by(id=caregiver_id).first()[0] + 1
        # db.session.query(CareGiver).filter(CareGiver.id==caregiver_id).update({"no_of_service_given": no_of_service_given})
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
    return object2json(cr)
  
def viewAllRequest(k):
    returnArray = []
    requestList = CareRecord.query.with_entities(CareRecord.record_id, CareRecord.appointment_time, CareRecord.location, 
        CareRecord.carerecipient_id).filter(CareRecord.record_status=="on_request", CareRecord.caregiver_id==k['user_id'])\
        .order_by(CareRecord.appointment_time).all()
    for index, request in enumerate(requestList):
        index -= 1
        dict = {}
        dict['record_id'] = requestList[index].record_id
        dict['appointment_time'] = str(requestList[index].appointment_time)
        dict['location'] = requestList[index].location
        careRecipient = CareRecipient.query.with_entities(CareRecipient.name).filter_by(id=requestList[index].carerecipient_id).first()
        dict['carerecipient_id'] = requestList[index].carerecipient_id
        dict['name'] = careRecipient.name
        returnArray.append(dict)
    return str(returnArray)

def showDoctorContact(k):
    recipient_id=k['recipient_id']
    cr=CareRecipient.query.filter_by(id=recipient_id).one()
    return cr.doctor.contact

# TODO add sorting functionality to method to enabe filtering by day, week and month
def viewServiceToPerform(k):
    rl=CareRecord.query.filter_by(caregiver_id=k['user_id']).filter_by(record_status='confirmed').all()
    return list2json(rl)

def apiLogin(k):
    acc=Account.query.filter_by(username=k['username'], password=k['password']).first()
    if acc is not None:
        return object2json(acc)
    else:
        return 'Incorrect Login credentials'

def viewRestrictedCareRecipientInfo(k):
    cr=CareRecipient.query.filter_by(id=k['recipient_id']).one()
    return object2json(cr)

def saveServiceSummary(k):
    return

def viewCareGiver(k):
    gl=CareGiver.query.all()
    return list2json(gl)

def viewCareGiverById(k):
    caregiver = CareGiver.query.filter_by(id=k['caregiver_id']).first();
    return object2json(caregiver)

def viewAvailableCareGivers(k):
    # TODO get available Caregivers instead of all existing caregivers
    caregiverList = CareGiver.query.all()
    if len(caregiverList) > 1:
        for index, caregiver in enumerate(caregiverList):
            index -= 1
            caregiver = caregiverList[index]
            avgRating = CareRecord.query.with_entities(CareRecord.caregiver_id, func.avg(CareRecord.rating)).filter_by(record_status='confirmed',caregiver_id=caregiver.id).all()
            caregiverAvgRating = avgRating[index]
            if caregiver.id == caregiverAvgRating[0]:
                caregiver.average_rating = caregiverAvgRating[1]
        return list2json(caregiverList)
    else:
        caregiverList[0].average_rating = avgRating[0][1]
        return object2json(caregiverList[0])

def getSummarisedProfile(k):
    profile = CareGiver.query.filter_by(id=k['user_id']).first()
    return object2json(profile)