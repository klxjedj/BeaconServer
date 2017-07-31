'''
this script defined several examples of user data for test when developing.
running this script independently would clear the database and add the examples in this script.
'''


# this three line initiate the database, just run these in interactive window 
from BeaconServer.function import *
import datetime
db.drop_all() # remove all existing data
db.create_all() # create tables of the database

# care giver info
caregiver_list = [{
        'username':'johndeo1234',
        'password':'johndoe1234', 
        'name':'John Doe', 
        'gender':'M',
        'email':'john@doe.com',
        'contact':'98765432',
        'no_of_service_given': 2,
        'date_of_birth': datetime.datetime(1987, 5, 24),
        'highest_education_level':'Associate\'s Degree in Nursing',
        'expertise': 'Hmmmm'
 },
{
        'username':'janedoe',
        'password':'janedoe1234', 
        'name':'Jane Doe', 
        'gender':'F',
        'email':'jane@doe.com',
        'contact':'87654321',
        'no_of_service_given': 1,
        'date_of_birth': datetime.datetime(1984, 7, 16),
        'highest_education_level':'Associate\'s Degree in Nursing',
        'expertise': 'Hmmmmmmm'
}
]

# creates a care giver
for caregiver in caregiver_list:
    createCareGiver(caregiver)

# care recipient list
recipient_list = [{
        'username': 'username1',
        'password': 'password1',
        'name': 'Edward Lee',
        'gender': 'M',
        'address': 'BLK 359 Pasir Panjang Ave 6 #8-123',
        'resident_contact': '65543124',
        'mobile_contact': '87129618',
        'beacon_id': 1
    },
     {
        'username': 'username2',
        'password': 'password2',
        'name': 'Megan Teo',
        'gender': 'F',
        'address': 'BLK 8 Ang Mo Kio Ave 7 #9-541',
        'resident_contact': '65431873',
        'mobile_contact': '98761253',
        'beacon_id': 2
    },
     {
        'username': 'username3',
        'password': 'password3',
        'name': 'Tan Chee hong',
        'gender': 'M',
        'address': 'BLK 98 Maxwell Rd #01-02',
        'resident_contact': '60918233',
        'mobile_contact': '87123898',
        'beacon_id': 3
    },
     {
        'username': 'username4',
        'password': 'password4',
        'name': 'Jenny Tan',
        'gender': 'F',
        'address': 'BLK 43 Sengkang Lane 3 #04-01',
        'resident_contact': '60876544',
        'mobile_contact': '97098232',
        'beacon_id': 4
    },
     {
        'username': 'username5',
        'password': 'password5',
        'name': 'Benny Lim',
        'gender': 'M',
        'address': 'BLK 73 Kovan Street 21 #13-341',
        'resident_contact': '63129833',
        'mobile_contact': '98123873',
        'beacon_id': 5
    }]

# instantiate individual care recipients from the recipient list into the
# database
for careRecipient in recipient_list:
    createCareRecipient(careRecipient)

# care record list
care_record_list = [{
        'caregiver_id': 5,
        'user_id': 7,
        'appointment_time': '2016-10-20 11:30:00'
    },
    {
        'caregiver_id': 5,
        'user_id': 8,
        'appointment_time': '2016-10-21 10:30:00'
    },
    {
        'caregiver_id': 6,
        'user_id': 9,
        'appointment_time': '2016-10-10 14:30:00'
    },
    {
        'caregiver_id': 6,
        'user_id': 10,
        'appointment_time': '2016-10-11 09:30:00'
    },
    {
        'caregiver_id': 6,
        'user_id': 11,
        'appointment_time': '2016-10-10 09:30:00'
    }]

# instantiate individual care requests from the care record list into the
# database
for careRecord in  care_record_list:
    createCareRequest(careRecord)

# list of care records that will be accepted
accepting_request_list = [{
        'record_id': 1,
        'user_id': 5
    },
    {
        'record_id': 2,
        'user_id': 5
    },
    {
        'record_id': 3,
        'user_id': 6
    }]

# loop through the accepting_request_list to set these care records to an
# accept status
for acceptingRequest in accepting_request_list:
    acceptRequest(acceptingRequest)

# view service to perform (accepted care request by caregiver)
viewServiceToPerform({
    'user_id': 5
})

# view care reicpient record info section 1, 2, 3
viewRestrictedCareRecipientInfo({
    'recipient_id': 6
})

viewFullInfo({
   'beacon_id': 1
})

changePassword({
 "action": "change_password",
 "user_id": 5,
 "old_password": "johndoe1234",
 "new_password": "johndoe"
})

# rate and review 2 carerecords
rateReviewCareService({
    "record_id": 1,
    "rating": 4.5,
    "review": "asdasd"
})

rateReviewCareService({
    "record_id": 2,
    "rating": 2.5,
    "review": "asdasd"
})

rateReviewCareService({
    "record_id": 3,
    "rating": 4,
    "review": "asdasd"
})