'''
    匹配1-12月
'''
import re

if __name__ == '__main__':
    result = re.match(r'\b((1[0-2])|(0?[1-9]))\b', '12')
    if result is not None:
        print(result.group())
    else:
        print('no match')