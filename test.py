'''
Bluetooth/Pyjnius example
=========================
This was used to send some bytes to an arduino BLE.
The app must have BLUETOOTH and BLUETOOTH_ADMIN permissions.
Connect your device to your phone, via the bluetooth menu. After the
pairing is done, you'll be able to use it in the app.
'''

import kivy
kivy.require('1.8.0')

from jnius import PythonJavaClass, java_method
from jnius import autoclass
from jnius import cast
from kivy.lang import Builder
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import time
import struct

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
BluetoothGatt= autoclass('android.bluetooth.BluetoothGatt')
BluetoothGattCallback = autoclass('android.bluetooth.BluetoothGattCallback')
UUID = autoclass('java.util.UUID')
List = autoclass('java.util.List')
Context = autoclass('android.content.Context')
PythonActivity = autoclass('org.renpy.android.PythonActivity')
BluetoothGattService=autoclass('android.bluetooth.BluetoothGattService')
activity = PythonActivity.mActivity
btManager = activity.getSystemService(Context.BLUETOOTH_SERVICE)
Intent = autoclass('android.content.Intent')
BluetoothProfile = autoclass('android.bluetooth.BluetoothProfile')
Service=autoclass('android.app.Service')
etatconnexion=0

class PyBluetoothGattCallback(PythonJavaClass):
    __javainterfaces__ =["org/myapp/BluetoothGattImplem$OnBluetoothGattCallback"]
    __javacontext__ = 'app'

    @java_method('(Landroid/bluetooth/BluetoothGatt;II)V')
    def onConnectionStateChange(self, gatt, status, newstate):
        global etatconnexion
        Logger.info('%s' % newstate)
        etatconnexion=newstate
   
    @java_method('(Landroid/bluetooth/BluetoothGatt;I)V')
    def onServicesDiscovered(self, gatt, status):
        global servicesdiscovered
        Logger.info('%s' % status)
        servicesdiscovered=status#0 si discovered


BluetoothGattImplem = autoclass('org/myapp/BluetoothGattImplem')
pycallback = PyBluetoothGattCallback()
bg = BluetoothGattImplem()
bg.setCallback(pycallback)

def try_connect(name):
    global etatconnexion,servicesdiscovered
   
    servicesdiscovered=1
    BluetoothAdapter=btManager.getAdapter()
   
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
   
    if len(paired_devices)==0: #Existe-t-il des peripheriques appaires
        return None, None
   
    for device in paired_devices:
        if device.getName() == name:
            break
   
    if device.getName()!=name: #Existe-t-il un peripherique du nom 'HMSoft'
        return None, None
   
    BluetoothGatt=None
   
    BluetoothGatt = device.connectGatt(Service, 0, bg)
   
    compteur=0
    while etatconnexion!=2:#Il faudrait un autre thread ici !
        compteur+=1
        time.sleep(0.1)
        if compteur==100:#Delai de connexion depasse
            Logger.info('%s' % "Toto1")
            Logger.info('%s' % etatconnexion)
            return None, None
   
    BluetoothGatt.discoverServices()#Il faut que ca marche pour recup un service
   
    compteur=0
    while servicesdiscovered!=0:
        compteur+=1
        time.sleep(0.1)
        if compteur==100:#Delai de decouverte des services depasse
            return None, None
   
    service = BluetoothGatt.getService(UUID.fromString("0000ffe0-0000-1000-8000-00805f9b34fb"))
    try:
        characteristic = service.getCharacteristic(UUID.fromString("0000ffe1-0000-1000-8000-00805F9B34FB"))
    except:
        return None, None
   
    return BluetoothGatt, characteristic

class BluetoothApp(App):
    def build(self):
        #On cree une disposition pour l'affichage:
        Layout=BoxLayout(orientation='vertical',spacing=20,padding=(200,20))
        self.GD=BoxLayout(orientation='horizontal',spacing=20,padding=(0,0))
        self.BoutonConnect=Button(text='Connect')
        self.BoutonConnect.bind(on_press=self.connect)
        #On ajoute le bouton dans l'affichage:
        Layout.add_widget(self.BoutonConnect)
        #On cree des boutons pour les motifs:
        self.Bouton1=Button(text='Up')
        self.Bouton1.id='1'
        self.Bouton1.bind(on_press=self.send)
        self.Bouton1.bind(on_release=self.stop)
        #On ajoute le bouton dans l'affichage:
        Layout.add_widget(self.Bouton1)
       
        self.Bouton2=Button(text='Left')
        self.Bouton2.id='2'
        self.Bouton2.bind(on_press=self.send)
        self.Bouton2.bind(on_release=self.stop)
        #On ajoute le bouton dans l'affichage:
        self.GD.add_widget(self.Bouton2)
        self.Bouton3=Button(text='Right')
        self.Bouton3.id='3'
        self.Bouton3.bind(on_press=self.send)
        self.Bouton3.bind(on_release=self.stop)
        #On ajoute le bouton dans l'affichage:
        self.GD.add_widget(self.Bouton3)
        Layout.add_widget(self.GD)
        self.Bouton4=Button(text='Stop')
        self.Bouton4.id='4'
        self.Bouton4.bind(on_press=self.send)
        #On ajoute le bouton dans l'affichage:
        Layout.add_widget(self.Bouton4)
        self.gatt=None
        self.charac=None
       
        return Layout
   
    def connect(self,instance):
        try:
            BluetoothGatt.disconnect()
        except:
            pass
        instance.background_color=[1,1,0,1]
        instance.text="Wait for connexion"
        self.gatt, self.charac = try_connect('HMSoft')
        if self.charac!=None:
            instance.background_color=[0,1,0,1]
            instance.text="connected"
        else:
            instance.background_color=[1,0,0,1]
            instance.text="echec de connexion : un nouvel essai"

    def send(self, instance):
        global etatconnexion
        if self.charac!=None:
            nb=int(instance.id)
            if etatconnexion==2:
                self.charac.setValue(nb,17,0)
                BluetoothGatt.writeCharacteristic(self.charac)
            else:
                self.BoutonConnect.background_color=[1,0,0,1]
                self.BoutonConnect.text="echec de connexion : un nouvel essai"
               
    def stop(self, instance):
        global etatconnexion
        if self.charac!=None:
            nb=4
            if etatconnexion==2:
                self.charac.setValue(nb,17,0)
                BluetoothGatt.writeCharacteristic(self.charac)
            else:
                self.BoutonConnect.background_color=[1,0,0,1]
                self.BoutonConnect.text="echec de connexion : un nouvel essai"

if __name__ == '__main__':
    BluetoothApp().run()