# coding=utf-8

'''
    Twisted Reactor 时间戳TCP服务器
'''

'''
    无语，示例代码过时好久了，要学的话去看官方文档，代码已经运行成功
'''

from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from time import ctime

PORT = 21567

class TSSerProtocol(Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('connected from:', clnt)
    def dataReceived(self, data):
        data = '[%s] %s' % (ctime(), data.decode('utf-8'))
        self.transport.write(bytes(data, 'utf-8'))

factory = Factory()
factory.protocol = TSSerProtocol
endpoint = TCP4ServerEndpoint(reactor, PORT)
print('waiting for connnction...')
endpoint.listen(factory)
reactor.run()