'''
    获取对象类型
'''
import re

def getObjectType(obj):
    type_str = str(type(obj))
    print(type_str)
    # obj_type = re.match('<class \'(.+)\'>', type_str)
    obj_type = re.search('\'(.+)\'', type_str)
    return obj_type.group(1)

if __name__ == '__main__':
    obj_type = getObjectType(7)
    print(obj_type)