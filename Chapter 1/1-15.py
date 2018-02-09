'''
    匹配信用卡（CC）号码，并验证格式是否正确
'''
import re

def get_CCNumber(ccNumber_with_hyphen):
    ccNumber_split_groups = re.split('-', ccNumber_with_hyphen)
    ccNumber = ''.join(ccNumber_split_groups)
    return ccNumber

def validate_ccNumber(ccNumber):
    sum = 0
    ccNumber_length = len(ccNumber)
    for i in range(ccNumber_length-1):
        if (ccNumber_length - 1 - i) % 2 == 1:
            number = int(ccNumber[i]) * 2
            if number > 9:
                number -= 9
            sum += number
        else:
            sum += int(ccNumber[i])
    sum += int(ccNumber[ccNumber_length-1])

    if sum % 10 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    ccNumber = get_CCNumber('4013-7356-3380-0642')
    if validate_ccNumber(ccNumber):
        print('your credit card number is valid')
    else:
        print('your credit card number is invalid')
