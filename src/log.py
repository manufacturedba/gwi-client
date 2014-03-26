from datetime import datetime

'''
Logs are created in the form of
timestamp: (time log is created)
log_type: (to distinguish between categories of logs)

'''
class Log(object):
    def __init__(self, collection, **kwargs):
        
        self.col = collection
    
    def fetch_logs(self, **params):
        '''
        TODO:
            Use log_type
            Return log array; not cursor
        '''
        parameters = self.parameters
        
        if type:
            parameters['type'] = type
            

        return col.find({'username': self.username, resolved:True})
        
    def add_log(self, body, **params):
        col.insert({'timestamp': datetime.now(), 
                    'message': body})
    
    def resolve_log(self, body, **params):
        col.update({'username': self.username, 'message': body},
                        {'$set':{'resolved':True}})
    
