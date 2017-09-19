from collections import Counter

if __name__ == '__main__':
    file = open('redata.txt', 'r')
    lines = file.readlines()

    data = []
    for line in lines:
        day = line[0:3]
        data.append(day)

    c = Counter(data)
    for key, value in c.items():
        print(key + ':' + str(value))