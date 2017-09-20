#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	亚马逊爬虫脚本。创建一个脚本，帮助你追踪你最喜欢的书，以及这些书在亚马逊上的表现（或者能够追踪图书排名的任何其他的在线书店）。
	例如，亚马逊对于任何一本图书提供以下链接：http://amazon.com/dp/ISBN(例如，http://amazon.com/dp/0132678209)。
	读者可以改变域名，检查亚马逊在其他国家的站点上相同的图书排名，例如BeautifulSoup、lxml或者html5lib来解析排名，
	然后让用户传入命令行参数，指明输出是否应当在一个纯文本中，也许包含在一个电子邮件正文中，还是用于Web的格式化HTML中。
'''

import requests
from bs4 import BeautifulSoup
import re
import html.parser

proxies = {
    "http": "dev-proxy.oa.com:8080",
    "https": "dev-proxy.oa.com:8080",
}

def getDataByISBN(ISBN):
    result = requests.get('http://amazon.com/dp/0132678209', proxies=proxies)
    return result.text

def getRank(data):
    soup = BeautifulSoup(data, 'lxml')
    lis = soup.find_all('li', {'class': 'zg_hrsr_item'})
    for li in lis:
        rank_search = re.search('<.+>#(\d+)', str(li))
        if rank_search is not None:
            print(rank_search.group(1) + ': ', end='')

        book_class_search = re.findall('<a href=.+?>(.+?)</a>', str(li))
        book_class = ''
        for i in range(len(book_class_search)):
            book_class += book_class_search[i]
            if i != len(book_class_search) - 1:
                book_class += '> '
        # 处理转义字符
        print(html.parser.unescape(book_class))

if __name__ == '__main__':
    ISBN = '0132678209'
    data = getDataByISBN(ISBN)
    getRank(data)