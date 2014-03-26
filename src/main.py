from kivy.app import App

from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

Config.set('graphics', 'width', '780')
Config.set('graphics', 'height', '420')

class FrameWidget(GridLayout):
    pass
    
class mobileTicketApp(App):
    def build(self):
        return FrameWidget(cols=2)

if __name__ == "__main__":
    mobileTicketApp().run()
