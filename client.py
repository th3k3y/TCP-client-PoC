#Importing required modules.

import socket

#Defining the client socket.

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Setting the port and getting the hostname of the client.

host = socket.gethostname(clientsocket)
port = 4444

#Connecting the client socket.

clientsocket.connect((host, port))

#Defining the maximum amount of data that can be received with this connection.

message = clientsocket.recv(1024)

#Closing the socket connection.

clientsocket.close()

#Converting the received data to ascii.

print(message.decode('ascii'))