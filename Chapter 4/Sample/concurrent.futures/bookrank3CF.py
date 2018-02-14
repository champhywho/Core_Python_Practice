'''
    使用了concurrent.futures模块的图书排名screenscraper
'''

from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import Request, urlopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundaments'
}
user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'

def getRanking(isbn):
    print('%s%s' % (AMZN, isbn))
    headers = {'User-Agent': user_agent}
    req = Request('%s%s' % (AMZN, isbn), headers=headers)
    res = urlopen(req)
    data = res.read()
    return REGEX.findall(data.decode('utf-8'))[0]

def _main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(
            ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r ranked %s' % (ISBNs[isbn], ranking))
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()