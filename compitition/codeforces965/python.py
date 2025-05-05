import socket

def talk_to_server():
    my_phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_phone.connect(('example.com', 80))
    my_phone.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n')
    
    reply = b""
    while True:
        part = my_phone.recv(4096)
        if not part:
            break
        reply += part
    
    my_phone.close()
    print(reply.decode())

talk_to_server()
