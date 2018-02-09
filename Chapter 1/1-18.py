from time import ctime
import re

if __name__ == '__main__':
    with open('redata.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            pieces = line.split('::')
            result = re.match('\d+', pieces[2])
            if result is not None:
                dtstr = result.group()
                timestamp_str = ctime(int(dtstr))
                if timestamp_str == pieces[0]:
                    print('success: ' + timestamp_str)
                else:
                    print('error: ' + timestamp_str)
            else:
                print('error: the number of seconda not exist!')
