import socket
import threading

# Port number for the server
PORT = 5054

# use `ipconfig` on windows or `ifconfig` on macos to find your local ip address
IP_ADDRESS = "192.168.68.68"

# Get the local IP address automatically
# Note: socket.gethostbyname(socket.gethostname()) may return '127.0.0.1' on some systems.
# IP_ADDRESS = socket.gethostbyname(socket.gethostname())  # Attempts to get the local IP address
print("Local IP address:", IP_ADDRESS)

ADDR = (IP_ADDRESS, PORT)

HEADER = 64
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)  # Bind the socket to the address and port


def handle_client(conn:socket.socket, addr:tuple[str, int], encoding="utf-8",
                  disconnect_msg="server -d"):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = int(conn.recv(HEADER).decode(encoding))
        if msg_length:
            msg = conn.recv(msg_length).decode(encoding)
            if msg == disconnect_msg:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message received.".encode(encoding))

        
    conn.close()
    print(f"[EXIT] Goodbye {addr}")

def start():
    server.listen()
    print(f"[LISTENING] on Server {server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1} ")

print("[STARTING] server is starting...")
start()