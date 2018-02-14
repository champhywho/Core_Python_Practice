from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import Request, urlopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}
user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'

def getRanking(isbn):
    print('%s%s' % (AMZN, isbn))
    headers = {'User-Agent': user_agent}
    req = Request('%s%s' % (AMZN, isbn), headers=headers) # or str.format()
    res = urlopen(req)
    data = res.read()
    return REGEX.findall(data.decode('utf-8'))[0]

def _showRanking(isbn):
    print('- %r ranked %s' % (
        ISBNs[isbn], getRanking(isbn)
    ))

def _main():
    print('At', ctime(), 'On Amazon...')
    for isbn in ISBNs:
        # _showRanking(isbn)
        Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()