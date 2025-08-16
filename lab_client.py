import socket

class Client:
    def __init__(self, host, port, format='utf-8'):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def run(self):
        while True:
            # Send data
            data = input("Enter message (or 'exit' to quit): ")
            if data.lower() == 'exit':
                break

            self.client_socket.sendall(data.encode())

            # Receive echo response
            response = self.client_socket.recv(1024)
            print("Received:", response.decode())

        self.client_socket.close()

# Initialize and run the client
client = Client('127.0.0.1', 5541)
client.run()
