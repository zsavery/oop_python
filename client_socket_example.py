import socket

# Create a, socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = input('Enter inet ip address: ')# '127.0.0.1' # Localhost
port = 5541 # Arbitrary non-privileged port
format = 'utf-8'

# Bind to the port
client_socket.bind((host, port))

# Receive message from server
message = client_socket.recv(1024)

# print the received message
print(message.decode(format))

# close connection
client_socket.close()