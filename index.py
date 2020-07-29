import kivy
from kivy.app import App
import sqlite3
from datetime import datetime
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
    def entertableinfo(self,vehicleno,fourwheeler,valetparking,lotno):
        self.vehicleno=vehicleno
        self.fourwheeler=fourwheeler
        self.valetparking=fourwheeler
        self.lotno=lotno
        pstatus="Parked"
        now = datetime.now()
        datet= now.strftime("%H:%M:%S")
        cur.execute(''' INSERT INTO vehicledetails(vehicleno,fourwheeler,datetime,valetparking,pstatus,lotno) VALUES(?,?,?,?,?,?)''',(vehicleno,fourwheeler,datet,valetparking,pstatus,lotno,))
        print("inserted")

        sql = '''UPDATE lotdetails SET vehicleno = ? WHERE lotno = ?'''
        val = (vehicleno,lotno)
        print(val)
        cur.execute(sql,val)
        
    
    



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("mainfront.kv")
 
class mainfront(App):
    
    def build(self):
        
        return kv

if __name__ == '__main__':
    
    conn = sqlite3.connect('parkinglot.sqlite')
    cur = conn.cursor()

    mainfront().run()

    conn.commit()
    cur.close()

