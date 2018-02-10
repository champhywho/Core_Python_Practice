'''
    support both IPv4 and IPv6
'''
# Echo server program
import socket
import sys
import time
import os
import re

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
# AF_UNSPEC指family参数未指定，可以同时支持IPv4和IPv6
# AI_PASSIVE 套接字地址用于监听绑定
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        recv_data = conn.recv(1024)
        if not recv_data: break
        cmd = recv_data.decode('utf-8').strip()
        send_data = cmd
        if cmd == 'date':
            send_data = time.ctime()
        elif cmd == 'os':
            send_data = os.name
        elif cmd == 'ls':
            send_data = '\n'.join(os.listdir())
        elif cmd.startswith('ls '):
            path = cmd[3:]
            if path:
                send_data = '\n'.join(os.listdir(path))
        conn.send(bytes(send_data, 'utf-8'))