import socket
import threading

# Port number for the server
PORT = 5054

# use `ipconfig` on windows or `ifconfig` on macos to find your local ip address
IP_ADDRESS = "192.168.68.68"
print("Local IP address:", IP_ADDRESS)

ADDR = (IP_ADDRESS, PORT)
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg, encoding="utf-8"):
    # client.send(msg.encode(encoding))
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode(encoding)
    send_length += b' ' * (HEADER - len(send_length))  # Padding to HEADER size
    client.send(send_length)
    client.send(message)
    print(f"[{ADDR}] {msg}")
    print(client.recv(2048).decode(encoding))

DISCONNECT_MSG = "server -d"

send("server run")
send(f"Enter '{DISCONNECT_MSG}' to exit.")

client_msg = None
while client_msg != DISCONNECT_MSG:
    client_msg = input("-> ")
    send(client_msg)
