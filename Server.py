import socket
import threading

Header = 64
port = 61467
server = socket.gethostbyname(socket.gethostname())
Addr = (server,port)
Format = 'utf-8'
Disconnect_msg = 'Disconnect'

SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SERVER.bind(Addr)

def handle_client(conn,addr):
    print(f"New Connection {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(Header).decode(Format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(Format)
            if msg == Disconnect_msg:
                connected = False

            print(f"{addr}: {msg}")
    conn.close()

def start():
    SERVER.listen()
    print(f"Server is listening to: {server}")
    while True:
        conn, addr = SERVER.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\nActive Threads At The Moment {threading.activeCount()-1}")


print("Starting Server...")
start()
