import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivymd.theming import ThemeManager

kivy.require("1.9.1")



class Logged_in(Screen):
    """ The window running when the user is logged """
    pass


class Log(Screen):
    """ The window displayed whane the user has to log in """
    pass

class acceuil(Screen):
    """ The window displayed by default on the app """
    pass

    

class MainApp(App):
    
    
    def change_window(self, nom_fenetre, direction='avant', mode="", diration="0.5"):
        screen_manager=self.root.ids["screen_manager"]

        if direction=='avant':
            mode='push'
            direction='left' 

        elif direction=='arriere':
            mode='pop'
            direction='right'  
        screen_manager.transition= CardTransition(direction=direction, mode=mode, duration = duration)
        screen_manager.current= nom_fenetre

      

        
    def build(self):
        #self.init()
        return  Builder.load_file('robot.kv') #self.running_window #lst_window[1] #Builder.load_file("appli.kv")


if __name__ == '__main__':
     
    
    MainApp().run()