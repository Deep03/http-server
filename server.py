import socket
from config import server_addr

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object
server_socket.bind(server_addr) # bind it to server_addr
server_socket.listen(5) # listen to at most 5 incomming connections
client_socket, client_addr = server_socket.accept() # starts accepting
recieved_data = client_socket.recv(1024).decode()
print(recieved_data)
