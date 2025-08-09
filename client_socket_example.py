import socket

# Create a, socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = '127.0.0.1' # Localhost
port = 34412 # Arbitrary non-privileged port

# Bind to the port
client_socket.bind((host, port))

# Receive message from server
message = client_socket.recv(1024)

# print the received message
print(message.decode())

# close connection
client_socket.close()