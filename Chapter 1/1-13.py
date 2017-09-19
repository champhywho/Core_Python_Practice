import re

def getObjectType(obj):
    type_str = type(obj)
    obj_type = re.match('<class \'(.+)\'>', str(type_str))
    return obj_type.group(1)

if __name__ == '__main__':
    obj_type = getObjectType(7)
    print(obj_type)