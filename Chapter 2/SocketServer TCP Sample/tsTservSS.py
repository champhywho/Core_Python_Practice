#!/urs/bin/env python

'''
    SocketServer 时间戳TCP服务器
'''

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('connected from: ', self.client_address)
        data = '[%s] %s' % (ctime(), self.rfile.readline().decode('utf-8'))
        self.wfile.write(bytes(data, 'utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()