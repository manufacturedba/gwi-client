'''
Authentication handler for Server
Will verify Github credentials only after user has logged in

'''
import requests
from settings import SERVER
from errors import CredentialsError

class Authentication(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def signin(self):
        auth_req = requests.post(SERVER, 
                      data={"username":self.username, 
                            "password":self.password}, 
                      verify=True)
        if auth_req.status_code != 200:
            raise CredentialsError("Invalid Credentials")
            return None
        return auth_req.session_token
        
    def signout(self, session_token):
        auth_req = requests.post(SERVER, 
                      data={"username":self.username, 
                            "password":session_token}, 
                      verify=True)
        if auth_req.status_code != 200:
            raise CredentialsError("Invalid Credentials")
            return False
        return True
