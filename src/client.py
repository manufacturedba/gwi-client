'''
Interface for authentication, user management, and fetching data
'''
import pymongo

from auth import Authentication

from settings import DATABASE, SERVER

from log import Log as log

import requests

mongo_client = pymongo.MongoClient(DATABASE.HOST, DATABASE.PORT)
db = mongo_client.gwi

class Client(object):
    def __init__(self):
        self.db = db
        self.logger = log(db.log)
    
    def check_username(self, username):
        check = requests.get(SERVER + '/user/' + username + '/check')
        if check.text == "user exists":
            return True
        else:
            return False
            
    def create_user(self, username, password, profile_info):
        user_info = dict("username":username, "password":password,
                         **profile_info)
        user = requests.post(SERVER + '/user/' + 'create', 
                             user_info)
        
    def login(self, username, password):
        '''
        Login to server and receive session token. Based on user
        preferences, we will invalidate session token when needed.
        
        If for some reason the server does not respond (times out),
        we can login offline. However, we will be severely limited in
        what actions we can perform.
        
        We also need to make sure our own (stale) session token is
        dead.
        '''
        auth_handler = Authentication(username, password)
        user = User(self.db.users, username)
        try:
            token = auth_handler.signin()
            self.user = user.set_token(token)
        except InvalidCredentials as e:
            print("Something wrong with username/password")
            raise
        except ServerTimeout:
            self.user = user.signin(password)
        
    def logout(self):
        if not self.user.token:
            raise SomeLogOutError
        else:
            self.auth_handler.logout(self.user.token)
            
    def make_pw_hash(self, pw,salt=None):
        if salt == None:
            salt = self.make_salt();
        return hashlib.sha256(pw + salt).hexdigest()+","+ salt
        
    def create_user(self, new_user):
        pass
