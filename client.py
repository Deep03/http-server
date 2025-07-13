import socket
from config import server_addr

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object
client_socket.connect(server_addr) #connect to server_addr

for i in range(0, 10):
    data = str(i)
    client_socket.send(data.encode())
client_socket.close()