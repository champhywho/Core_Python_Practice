import re

if __name__ == '__main__':
    regex = '((?:\d{3}-)|(\(\d{3}\)))?\d{3}-\d{4}'
    m = re.match(regex, '800-555-1212')
    print(m.group())
    m = re.match(regex, '555-1212')
    print(m.group())
    m = re.match(regex, '(800)555-1212')
    print(m.group())