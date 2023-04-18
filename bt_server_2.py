import bluetooth

# Create a Bluetooth server socket
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(('', 1))
server_sock.listen(1)

print('Waiting for connection...')

# Accept incoming connection
client_sock, client_info = server_sock.accept()
print('Connected:', client_info)

# Receive data from the client
data = client_sock.recv(1024)
print('Received:', data.decode())

# Send a response to the client
client_sock.send('Message received'.encode())

# Close the client socket and server socket
client_sock.close()
server_sock.close()
