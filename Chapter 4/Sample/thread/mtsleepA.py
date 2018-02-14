'''
    使用thread模块
'''

import _thread
from time import ctime, sleep

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # 加入这个语句是因为如果不阻止主线程继续运行，那么主线程会直接运行完毕，并终止子线程，更好的方式是加入锁
    sleep(6)
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()