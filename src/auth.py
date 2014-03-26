'''
Authentication handler for Server
Will verify Github credentials only after user has logged in

'''
import requests
from settings import SERVER
from errors import CredentialsError

class Authentication(object):
    def __init__(self, username, password):
        auth_req = requests.post(SERVER, 
                      data={"username":username, 
                            "password":password}, 
                      verify=True)
        if auth_req != 200:
            raise CredentialsError("Invalid Credentials")
        
