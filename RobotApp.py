import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder 

kivy.require("1.9.1")


class fenetre(BoxLayout):
    def crea_button(self, text, function=0):
        button = Button()
        button.text = text
        if function !=0 :
            button.bind(on_press=function)
        self.add_widget(button)
        return button
    
    def crea_Label(self, text):
        label = Label()
        label.text = text
        self.add_widget(label)
        return label

    def crea_TextInput(self, text):
        input_name = TextInput()
        input_name.text = text
        self.add_widget(input_name)
        return input_name

    def context (self, app, num):
        self.num = num
        self.app= app

class Loged(fenetre):
    """ The window running when the user is logged """

    def build(self):
        self.orientation="vertical"
        
    def log_out(self):
        self.app.change_window(1)


class Log(fenetre):
    """ The window displayed whane the user has to log in """
    def build(self):
        self.orientation="vertical"
        #self.texte = self.crea_Label("Connexion : ")
        #self.user_name = self.crea_TextInput("Saisisez votre nom d'utilisateur : ")
        #self.user_mdp = self.crea_TextInput("Saisisez votre mot de passe : ")
        #self.Connexion = self.crea_button("Log in", self.log_in )

    def log_in(self):
        self.app.change_window(2)

class acceuil(fenetre):
    """ The window displayed by default on the app """
    def build(self):
        self.orientation="vertical"
        #self.label = self.crea_Label(" Welcome ! ")
        #self.Connexion = self.crea_button("Log in", self.to_log )
        
    def to_log (self, truc):
        self.app.change_window(1)
        print(truc)

    

class MainApp(App):
    
    def init(self):
        self.init = True
        self.lst_window=[acceuil(), Log(),Loged() ]
        for window in self.lst_window:

            window.context(self, self.lst_window.index(window))
            window.build()

        self.running_window = self.lst_window[0]

    def change_window(self, next_win_num):
        self.running_window = self.lst_window[next_win_num]

        
    def build(self):
        self.init()
        return self.running_window #lst_window[1] #Builder.load_file("appli.kv")


if __name__ == '__main__':
     
    Builder.load_file('robot.kv')
    MainApp().run()