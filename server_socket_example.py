import socket

# Create a, socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = '127.0.0.1' # Localhost
port = 5541 # Arbitrary non-privileged port
format = 'utf-8'

# Bind to the port
server_socket.bind((host, port))

# Start listening 
server_socket.listen()
print("Listening to port {}".format(port))

# Accept a connection
client_socket, addr = server_socket.accept()
print("Get a connection from {}".format(addr))

while True:
    message = client_socket.recv(1024).decode(format)
    if message:
        print(f"Message received from {addr}: {message}")
        client_socket.sendall(message.encode(format))

    if message == 'server -d':
        break

print('Closing server \n3\n2\n1')

server_socket.close()