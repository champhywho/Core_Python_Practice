#!/usr/bin/env python

'''
    UDP时间戳服务器
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# IPv4
udpSerSock = socket(AF_INET, SOCK_DGRAM)
# IPv6
udpSerSock = socket(AF_INET6, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    data = '[%s] %s' % (ctime(), data.decode('utf-8'))
    udpSerSock.sendto(bytes(data, 'utf-8'), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
