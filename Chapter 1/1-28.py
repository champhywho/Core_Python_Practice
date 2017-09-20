import re

if __name__ == '__main__':
    m = re.match('(?:\d{3}-)?\d{3}-\d{4}', '800-555-1212')
    print(m.group())
    m = re.match('(?:\d{3}-)?\d{3}-\d{4}', '555-1212')
    print(m.group())