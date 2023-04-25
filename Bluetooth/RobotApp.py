import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder 
from kivymd.theming import ThemeManager


kivy.require("1.9.1")

class MyScreenManager(ScreenManager):
    pass

class Logged_in(Screen):
    """ The window running when the user is logged """
    pass


class Log(Screen):
    """ The window displayed whane the user has to log in """
    
    def logged_in(self):
        user_name = self.ids.user_id.text
        user_pwd = self.ids.user_pwd.text
        print(f"Vous êtes connecté ! : {user_name}, {user_pwd} ")
    
    pass

class Acceuil(Screen):
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
        sm = MyScreenManager()

        # Création des fenêtres
        acceuil = Acceuil(name='Acceuil')
        log = Log(name='Log')
        logged_in = Logged_in(name='Logged_in')
        
        

        sm.add_widget(acceuil)
        sm.add_widget(log)
        sm.add_widget(logged_in)



        return sm   #self.running_window #lst_window[1] #Builder.load_file("appli.kv")


if __name__ == '__main__':
     
    Builder.load_file('robot.kv')
    MainApp().run()