#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

if __name__ == '__main__':
    file = open('redata.txt', 'w')

    for i in range(randrange(500, 1100)):
        dtint = randrange(2147483647)
        dtstr = ctime(dtint)
        llen = randrange(4, 8)
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen, 13)
        dom = ''.join(choice(lc) for j in range(dlen))
        file.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))