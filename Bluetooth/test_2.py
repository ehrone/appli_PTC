import bluetooth
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class BluetoothClientApp(App):
    def __init__(self, **kwargs):
        super(BluetoothClientApp, self).__init__(**kwargs)

    def build(self):
        # Create UI components
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Click the button to send message to Raspberry Pi')
        button = Button(text='Send Message', on_press=self.send_message)

        # Add UI components to the layout
        layout.add_widget(label)
        layout.add_widget(button)

        return layout

    def send_message(self, instance):
        # Raspberry Pi's Bluetooth address
        SERVER_MAC_ADDRESS = 'dc:a6:32:2f:9f:79'

        # UUID for the service to connect to
        SERVICE_UUID = '00001101-0000-1000-8000-00805F9B34FB'

        # Message to send to the server
        MESSAGE = 'Hello, Raspberry Pi!'

        # Connect to the server
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((SERVER_MAC_ADDRESS, 1026))

        # Send the message
        sock.send(MESSAGE)

        # Close the connection
        sock.close()

        print('Message sent to Raspberry Pi:', MESSAGE)


if __name__ == '__main__':
    BluetoothClientApp().run()
