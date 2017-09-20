# !usr/bin/env python3
# coding = utf-8

'''
	生成HTML。提供一个链接列表(以及可选的简短描述)，无论用户通过命令行方式提供、通过来自于其他脚本的输入，
	还是来自于数据库，都生成一个Web页面(.html),该页面包含作为超文本锚点的所有链接，它可以在Web浏览器中查看，
	允许用户单击这些链接，然后访问相应的站点。如果提供了简短的描述，就使用该描述作为超文本而不是URL。
'''

'''
    做了一个生成链接和打开链接的操作
'''

from pyh import *
import webbrowser

if __name__ == '__main__':
    page = PyH('link page')
    page << h1('link', cl='center')
    page << a('a link', href='http://www.baidu.com')
    page.printOut('page.html')
    webbrowser.open('page.html')
