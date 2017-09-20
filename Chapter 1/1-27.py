import re

if __name__ == '__main__':
    with open('redata.txt') as file:
        for line in file.readlines():
            s = re.search('.+? (.+?) (.+?) .+? (.+?)::', line)
            print(s.group(1) + ', ' + s.group(2) + ', ' + s.group(3))