#!/usr/bin/env python
'''
    Python3 TCP时间戳客户端
'''

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 根据习题2-4进行修改
host = input('Please input Host: ')
port_str = input('Please input Port: ')
if host and port_str:
    port = int(port_str)
    ADDR = (host, port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()