import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from kivy.uix.button import Button
import bt_fun as bt
from kivy.uix.popup import Popup


class remote(BoxLayout):

    def build(self):
        
        #self.orientation="horizontal"
       pass

class choose_device(BoxLayout):

    def choose_bluetooth(self, button):
        """ This function is used to choose the name of the bluetooth device we want to get connected to """
        # selecting the bluetooth device we want to conect to
        print(f"set up connection with {button.text}")
        self.bluetooth_name = button.text

    def connecting(self, truc):
        """ This function creat the socket to connect to the selected device """
        print("bluetooth port selected")
        if self.bluetooth_name !="":
            print(f'connecting bluetooth : {self.bluetooth_name, self.dico[self.bluetooth_name]}')
            self.client = bt.crea_client_bt("dc:a6:32:2f:9f:79", 1028) #self.dico[self.bluetooth_name]
            popup = CustomPopup()
            popup.open()
            bt.send_bt(self.client, "tentative connexion")
            #self.client.close()
        else :
            print("pas de selection bluetooth")

    def un_boutton(self, text, name, fun=0):
        """ This fuction create a button """
        button = Button()
        button.text = name

        if fun ==0:
            button.bind(on_press = self.choose_bluetooth )
        else :
            button.bind(on_press = self.connecting )

        self.add_widget(button)
        

    def buttons_devices(self):
        """ This function create a button for each bluetooth device found """
        for name, addr in self.dico.items():
            print(name)
            self.un_boutton( name, name)
    
    def get_client_side(self):
        """ This function return the socket's client side 
        Output:
            self.client : a socket object, the client's side
        """
        return self.client
    
    def build(self):
        self.orientation='vertical'
        self.dico = bt.find_bt()
        self.bluetooth_name =""
        self.client=""
        self.buttons_devices()
        self.action_bluetooth = self.un_boutton('connexion', 'connexion', 1)
        


class MainApp(App):

    def build(self):
        #Creating the remote window
        #self.client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.window = choose_device()
        self.window.build()
        return self.window 


if __name__ == '__main__':
     
    Builder.load_file('remote.kv')
    MainApp().run()