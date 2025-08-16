import socket

# Create a, socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = '127.0.0.1' # Localhost
port = 5541 # Arbitrary non-privileged port

# Bind to the port
server_socket.bind((host, port))

# Start listening 
server_socket.listen()

print("Listening to port {}".format(port))

# Accept a connection
client_socket, addr = server_socket.accept()
print("Get a connection from {}".format(addr))

# Send a message to the ckient
client_socket.send(b'Hello client!')