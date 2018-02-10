# Echo client program
import socket

# HOST = 'daring.cwi.nl'    # The remote host
HOST = 'localhost'
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # send 和 sendall的区别
    # send返回发送的字节大小，可能会小于发送的数据的实际长度，也就是说，可能不会发送完整的数据
    # sendall发送完整的TCP数据，成功返回None，失败抛出异常，也就是说，要么完整发送出去，要么发送失败
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', data.decode('utf-8'))