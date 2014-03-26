from datetime import datetime
'''
Logs are created in the form of
timestamp: (time log is created)
log_type: (to distinguish between categories of logs)

'''
class Log(object):
    def __init__(self, username):
        self.username = username
    
    def fetch_logs(self, log_type, include_resolved=False):
        '''
        TODO:
            Use log_type
            Return log array; not cursor
        '''
        if include_resolved:
            return db.logs.find({'username': self.username})
        return db.logs.find({'username': self.username, resolved:True})
        
    def add_log(self, log_type, body):
        db.logs.insert({'timestamp': datetime.now(), 
                        'username': self.username,
                        'logType': log_type,
                        'message': body})
    
    def resolve_log(self, body):
        db.logs.update({'username': self.username, 'message': body},
                        {'$set':{'resolved':True}})
    
