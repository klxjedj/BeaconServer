#this three line initiate the database
from BeaconServer.function import *
db.drop_all()
db.create_all()

#data_list store info as a list of dict
data_list=[{'username':'jack','password':'abc'},]

#call the createXXX function to create data,take dict in data_list as parameter
createCaregiver(data_list[0])