from datetime import datetime

'''
Logger should not determine the backend to log against.  Only provide 
an interface to log against.
'''

# More colors should be supported as well as other methods of 
# modifying text
colors = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m'
    }

color_mapping = {'debug': colors['green'], 
                     'info': colors['blue'], 
                     'warning': colors['yellow'], 
                     'error': colors['red']}
                     
class Log(object):

    def __init__(self, backend = None, mode_mapping = None):
        self.color_mapping = color_mapping
        if backend:
            try:
                import backend
                self.backend = backend
            except ImportError:
                print('Could not import backend')
            self.backend = None
        if isinstance(mode_mapping, dict):
            for mode in mode_mapping.keys():
                self.color_mapping[mode] = mode_mapping[mode]
                
    def log(self, mode, text):
        text_mod = self.color_mapping[mode]
        if self.backend:
            self.backend.log(text, text_mod)
        else:
            print(text_mod + mode.upper() + ':' + text)
