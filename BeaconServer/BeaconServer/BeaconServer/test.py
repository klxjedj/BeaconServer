#this three line initiate the database, just run these in interactive window 
from BeaconServer.function import *
db.drop_all() #remove all existing data
db.create_all() # create tables of the database

#data_list store info as a list of dict
data_list=[{'username':'jack','password':'abc'},]

#call the createXXX function to create data,take dict in data_list as parameter
createCaregiver(data_list[0])