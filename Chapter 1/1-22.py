import re

if __name__ == '__main__':
    with open('redata.txt') as file:
        for line in file.readlines():
            m = re.match('.+ (\d+)::', line)
            print(m.group(1))