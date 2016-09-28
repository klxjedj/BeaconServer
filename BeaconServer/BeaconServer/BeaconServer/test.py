# this three line initiate the database, just run these in interactive window 
from BeaconServer.function import *
import datetime
db.drop_all() # remove all existing data
db.create_all() # create tables of the database

# care giver info
caregiver=[
    {
        'username':'johndeo1234',
        'password':'johndoe1234', 
        'name':'John Doe', 
        'gender':'M',
        'email':'john@doe.com',
        'contact':'98765432',
        'date_of_birth': datetime.datetime(1987, 5, 24),
        'highest_education_level':'Associate\'s Degree in Nursing',
        'expertise': 'Hmmmm'
    }
]

# creates a care giver
createCareGiver(caregiver[0])

# care recipient list
recipient_list = [
    {
        'username': 'username1',
        'password': 'password1',
        'name': 'Edward Lee',
        'gender': 'M',
        'address': 'BLK 359 Pasir Panjang Ave 6 #8-123',
        'resident_contact': '65543124',
        'mobile_contact': '87129618'
    },
     {
        'username': 'username2',
        'password': 'password2',
        'name': 'Megan Teo',
        'gender': 'F',
        'address': 'BLK 8 Ang Mo Kio Ave 7 #9-541',
        'resident_contact': '65431873',
        'mobile_contact': '98761253'
    },
     {
        'username': 'username3',
        'password': 'password3',
        'name': 'Tan Chee hong',
        'gender': 'M',
        'address': 'BLK 98 Maxwell Rd #01-02',
        'resident_contact': '60918233',
        'mobile_contact': '87123898'
    },
     {
        'username': 'username4',
        'password': 'password4',
        'name': 'Jenny Tan',
        'gender': 'F',
        'address': 'BLK 43 Sengkang Lane 3 #04-01',
        'resident_contact': '60876544',
        'mobile_contact': '97098232'
    },
     {
        'username': 'username5',
        'password': 'password5',
        'name': 'Benny Lim',
        'gender': 'M',
        'address': 'BLK 73 Kovan Street 21 #13-341',
        'resident_contact': '63129833',
        'mobile_contact': '98123873'
    }
]

# instantiate individual care recipients from the recipient list into the database
for careRecipient in recipient_list:
    createCareRecipient(careRecipient)

# care record list
care_record_list = [
    {
        'caregiver_id': 5,
        'user_id': 6,
        'appointment_time': datetime.datetime(2016, 10, 3, 14, 0, 0),
        'location': ''
    },
    {
        'caregiver_id': 5,
        'user_id': 7,
        'appointment_time': datetime.datetime(2016, 10, 6, 17, 0, 0),
        'location': ''
    },
    {
        'caregiver_id': 5,
        'user_id': 8,
        'appointment_time': datetime.datetime(2016, 10, 7, 11, 0, 0),
        'location': ''
    },
    {
        'caregiver_id': 5,
        'user_id': 9,
        'appointment_time': datetime.datetime(2016, 10, 7, 14, 0 , 0),
        'location': ''
    },
    {
        'caregiver_id': 5,
        'user_id': 10,
        'appointment_time': datetime.datetime(2016, 10, 7, 16, 0, 0),
        'location': ''
    }
]

# instantiate individual care requests from the care record list into the database
for careRecord in  care_record_list:
    createCareRequest(careRecord)

# list of care records that will be accepted
accepting_request_list = [
    {
        'record_id': 1,
        'user_id': 5
    },
    {
        'record_id': 2,
        'user_id': 5
    },
    {
        'record_id': 3,
        'user_id': 5
    }
]

# loop through the accepting_request_list to set these care records to an accept status
for acceptingRequest in accepting_request_list:
    acceptRequest(acceptingRequest)

# view service to perform (accepted care request by caregiver)
viewServiceToPerform({
    'user_id': 5
})