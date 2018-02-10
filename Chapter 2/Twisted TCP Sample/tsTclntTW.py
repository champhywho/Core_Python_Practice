# coding=utf-8

'''
    Twisted Reactor 时间戳TCP客户端
'''

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending %s...' % data)
            self.transport.write(bytes(data, 'utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()

class TSClntFactory(ClientFactory):
    protocol = TSClntProtocol
    clientConnetcionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()