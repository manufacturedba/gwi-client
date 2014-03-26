from datetime import datetime

class Client(object):
    def __init__(self, user):
        self.username = user.username
        
    def get_contacts(self):
        self.contacts = db.contacts.find({"username":self.username})
        
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
