from datetime import datetime
'''
Logs are created in the form of
timestamp: (time log is created)
log_type: (to distinguish between categories of logs)

'''
class Log(object):
    def __init__(self, username, collection):
        self.username = username
        self.col = collection
    
    def fetch_logs(self, log_type, include_resolved=False):
        '''
        TODO:
            Use log_type
            Return log array; not cursor
        '''
        if include_resolved:
            return col.find({'username': self.username})
        return col.find({'username': self.username, resolved:True})
        
    def add_log(self, log_type, body):
        col.insert({'timestamp': datetime.now(), 
                        'username': self.username,
                        'logType': log_type,
                        'message': body})
    
    def resolve_log(self, body):
        col.update({'username': self.username, 'message': body},
                        {'$set':{'resolved':True}})
    
