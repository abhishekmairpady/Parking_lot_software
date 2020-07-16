import kivy
from kivy.app import App

from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image




class Container(Screen):
    pass
    
    



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("mainfront.kv")
 
class mainfront(App):
    
    def build(self):
        
        return kv

if __name__ == '__main__':
    
    mainfront().run()

