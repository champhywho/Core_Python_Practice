'''
    半双工服务器
'''

import socket
import sys

HOST = None
PORT = 21567
BUFSIZ = 1024
server = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        server = socket.socket(af, socktype, proto)
    except OSError as msg:
        server = None
        continue
    try:
        server.bind(sa)
        server.listen(1)
    except OSError as msg:
        server.close()
        server = None
        continue
    break

if server is None:
    print('could not open socket')
    sys.exit(1)

client, addr = server.accept()
with client:
    while True:
        recv_data = client.recv(BUFSIZ)
        if recv_data is None:
            print('received data is None')
            break
        print('client:', recv_data.decode('utf-8'))
        send_data = input('server: ')
        if send_data is None:
            print('data to send is None')
            break
        client.send(bytes(send_data, 'utf-8'))

client = None
server.close()
server = None
