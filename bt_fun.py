import socket
import bluetooth

def find_bt():
    """ This function display all the nearby bluetooth devices found and return a dict with all of them
    Output : 
        dico : {bluetooth_device_name : mac_address}
    """
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))
    dico={}
    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
        dico[name]=addr
    return dico

#interface_mac_add = 
#port_num = 
def crea_serv_bt(interface_mac_add,port_num):
    """ This function creates the server side of the communication
    Input:
        interface_mac_add :  a string of the mac address of the bluetooth device that will receive msg
        port_num : an int, the number of the server's port it will listen on
    Output:
        client : the client socket side created"""
    # creating a bluetooth socket, the tipe of socket , ....., and the protocol
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    server.bind( (interface_mac_add, port_num) )

    return server
    
def recv_bt(server):
    """ This function read the receved message on the socket
    Input:
        server : a side of the socket where we want to read 
    """
    # waiting for an incoming message
    server.listen()
    client, addr = server.accept()

    try:
        while True:
            msg = client.recv(1024)
            if not data :
                break
            print(f"Message : {msg.decode('utf-8')}")
            return msg.decode('utf-8')

    except OSError as e :
        pass
    
def crea_client_bt(interface_mac_add,port_num):
    """ This function create the client side of the socket 
    Input:
        interface_mac_add :  a string of the mac address of the device we want to talk to
        port_num : an int, the number of the server's port given in the socket creation
    Output:
        client : the client socket side created
    """
    print("appel bluetooth ")
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((interface_mac_add, port_num))
    return client 

def send_bt(client, message):
    """ This function send the message, client to serveur
    Input:
        client : a socket side
        message : a string, the message to send to the server
    """
    try :

        client.send( message.encode("utf-8") )

    except OSError as e :
        pass

def close_bt(lst):
    """ This function closes the soket's side within the list
    Input :
        lst : the list with all the sockets sides to close """
    for bt_link in lst :
        bt_link.close()