import socket

class Server:
    def __init__(self, host, port, format='utf-8'):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.server_format = format

    def run(self):
        print("Server started. Listening for connections...")
        client_socket, client_address = self.server_socket.accept()
        print(f"Connection established with {client_address}")

        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode(self.server_format)
            if data:
                print(f"Received from {client_address}: {data}")
                # Echo back the received message to the client
                client_socket.sendall(data.encode(self.server_format))
            if data == "exit()":
                break
        print("Server exited. 3 2 1")


# Initialize and run the server
ip_addr = '127.0.0.1'
port = 5541
server = Server(ip_addr, 5541)
server.run()
