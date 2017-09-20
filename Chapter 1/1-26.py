import re

if __name__ == '__main__':
    email = 'abcdefg@163.com.cn'
    with open('redata.txt') as file:
        for line in file.readlines():
            result = s = re.sub('::(.+@.+)::', email, line)
            print(result, end='')