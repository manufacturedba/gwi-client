'''
Interface for authentication, user management, and fetching data
'''
import pymongo

from auth import Authentication

from settings import DATABASE

from log import Log as log

mongo_client = pymongo.MongoClient(DATABASE.HOST, DATABASE.PORT)
db = mongo_client.gwi 

class Client(object):
    def __init__(self, username, password):
        self.db = db
        self.username = username
        self.password = password
        self.logger = log(username, db.log)

    def login(self, username, password):
        self.auth_handler = Authentication(username, password)
        token = self.auth_handler.signin()
        db.users.update({'username': username}, 
                        {'sessionToken':token})
    
    def logout(self):
        token = db.users.find({'username':username}, 
                              {'sessionToken'})
        if not token:
            raise SomeLogOutError
        else:
            self.auth_handler.logout(token)
            
    
