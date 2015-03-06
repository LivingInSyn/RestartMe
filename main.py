'''
Created by Jeremy Mill, originally for use in the hi tech classrooms at the University of CT

Licensed under the GPLv3

jeremymill@gmail.com
github.com/livinginsyn
'''

#put the graphics stuff up here so it'll change
from kivy.config import Config
Config.set('graphics','height',480)
Config.set('graphics','width',400)
Config.write()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
import subprocess

class Restart_Screen(Screen):
    pass
    
class Restart_App(App):
    icon = 'myicon.ico' 
    def build(self):
        self.icon = 'myicon.ico'
        self.title = "HTC Restart Utility"
        self.restart_screen = Restart_Screen(name='restart')
        self.transition = SlideTransition(duration=.35)
        root = ScreenManager(transition=self.transition)
        root.add_widget(self.restart_screen)
        return root
        
    def restart_me(self):
        #subprocess.Popen(["shutdown.exe","/r","/t 3"])
        print("would have restarted")
        
if __name__ == '__main__':
    Restart_App().run()