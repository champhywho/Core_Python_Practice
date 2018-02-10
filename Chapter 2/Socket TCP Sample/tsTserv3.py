#!/urs/bin/env python
'''
    Python3 TCP时间戳服务器
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        # if not x 和 if x is None 的区别：
        # if not x 包括判断if x is None 和 if x == 对应类型的空值，比如当x = ''时，not x为True，而x is None为False
        if not data:
            break
        data = '[%s] %s' % (ctime(), data.decode('utf-8'))
        tcpCliSock.send(bytes(data, 'utf-8'))

    tcpCliSock.close()
tcpSerSock.close()