import socket

Header = 64
port = 61467
Format = 'utf-8'
Disconnect_msg = 'Disconnect'
server = '192.168.100.112'
Addr = (server,port)

Client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Client.connect(Addr)

def send(msg):
    message = msg.encode(Format)
    msg_length = len(message)
    send_length = str(msg_length).encode(Format)
    send_length += b' ' * (Header - len(send_length))
    Client.send(send_length)
    Client.send(message)


send("Hi")
send("How Are You?")


send(Disconnect_msg)
