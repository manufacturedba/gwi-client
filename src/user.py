from datetime import datetime

class User(object):
    def __init__(self, collection, username):
        self.collection = collection
        self.username = username
    
    def signin(self, password):
        '''
        This is actually for a case in which the server did not do as
        expected and we're forced to login manually.
        
        Server actions must be entirely cut off, but we should still
        be able to talk to other external services.
        '''
        
    def set_token(self, token):
        '''
        Sets token for passing to server and validating other requests
        '''
        user = self.collection.find_and_modify({'username'}, 
                                    {'$set':{'session_token':token}},
                                     new=True, fields={'_id':0})
        for key, value in user.iteritems():
            self[key] = value
        
    def get_contacts(self):
        '''
        Fetch locally stored contacts. Should only be used in 
        refreshing contacts. Client should only request user data
        only once as long as data is suspected as invalid/stale.
        Server can/will/should invalidate contacts added manually.
        
        This is just for retaining a contacts list locally without
        having to request from the server or pass around a contacts
        object all the time.
        '''
        user = coll.find({"username":self.username}, 
                            {"contacts":1})
        if user.count > 1:
            raise DBError("Username appears twice")
        else:
            return user[0]['contacts']
        
    def add_contact_request(self, username):
        '''
        Make request to server to add contact based on username.
        TODO:
            Already confused myself from "username". Perhaps I can 
            change the naming.
        '''
        for user in self.contacts:
            if username == user.username:
                if user.state == 'pending':
                    print "User already requested"
                    return
                print("User already in contacts")
                return
        com.add_contact_request(username)
        log.add_log("add_contact", username)
    
    def add_contact(self, user):
        db.contacts.insert(user)
        log.resolve("add_contact", user.username)
        
    def send_message(body):
        com.send_message(body)
        log.add_log("send_message", body)
