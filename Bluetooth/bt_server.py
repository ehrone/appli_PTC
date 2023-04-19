import socket 
import bluetooth as bt
from bluetooth import BluetoothSocket

from getmac import get_mac_address as gma

# we get the mac address of our raspberry
interface_mac_add =gma()
print(gma())

# creating a bluetooth socket, the tipe of socket , ....., and the protocol
server = BluetoothSocket(bt.RFCOMM) #socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

server.bind( ("",0))#( ("2c:3b:70:5c:48:03", 1028) )
print('done')
server.listen(1)

client, addr = server.accept()
run=True
try:
    while run:
        msg = client.recv(1024)
        print(f"Message : {msg.decode('utf-8')}")
        if not msg :
            break
        else :
            run = False
        

except OSError as e :
    pass

