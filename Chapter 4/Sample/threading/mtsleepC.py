'''
    使用threading模块
    创建Thread的实例，并给它一个函数
'''

import threading
from time import sleep, ctime

loops = [4, 2]
def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    # start threads
    for i in nloops:
        threads[i].start()

    # wait for all threads to finish
    # when you have other things to do and you don't need to wait this thread, you should not call 'join' function
    for i in nloops:
        threads[i].join()

    print('all Done at:', ctime())

if __name__ == '__main__':
    main()