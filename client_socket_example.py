import socket

# Create a, socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = input('Enter inet ip address: ')# '127.0.0.1' # Localhost
port = 5541 # Arbitrary non-privileged port
format = 'utf-8'

# Connect to the port
client_socket.connect((host, port))

print("Start client.")
while True:
    # Receive message from server
    message = input("Enter message (or 'quit' to quit): ")
    if message.lower == 'quit':
        break

    client_socket.sendall(message.encode(format))

    # Response 
    response = client_socket.recv(1024)
    decoded_msg = response.decode(format)
    

    # print the received message
    print(decoded_msg)

print("Exit client.")


# close connection
client_socket.close()