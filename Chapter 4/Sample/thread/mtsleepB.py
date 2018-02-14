'''
    使用线程和锁
'''

import _thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()

def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    # 不在该循环中开启线程，因为获取锁需要时间
    for i in nloops:
        # 获取锁对象
        lock = _thread.allocate_lock()
        # 上锁
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

if __name__ == '__main__':
    main()