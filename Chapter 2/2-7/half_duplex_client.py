'''
    半双工客户端
'''

import socket
import sys

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
client = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        client = socket.socket(af, socktype, proto)
    except OSError as msg:
        client = None
        continue
    try:
        client.connect(sa)
    except OSError as msg:
        client.close()
        client = None
        continue
    break

if client is None:
    print('could not open socket')
    sys.exit(1)

with client:
    while True:
        send_data = input('client:')
        if send_data is None:
            print('data to send is None')
            break
        client.send(bytes(send_data, 'utf-8'))
        recv_data = client.recv(BUFSIZ)
        if recv_data is None:
            print('received data is None')
            break
        print('server:', recv_data.decode('utf-8'))
