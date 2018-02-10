#!/usr/bin/env python

'''
    UDP时间戳客户端
'''

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 根据习题2-4进行修改
host = input('Please input Host: ')
port_str = input('Please input Port: ')
if host and port_str:
    port = int(port_str)
ADDR = (host, port)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()