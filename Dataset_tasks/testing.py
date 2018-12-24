import  os
from functools import reduce
# sample = ["a",'b','c','d','e','f','g','j']
# def func(a,b):
#     print(a,b)
#     a[b] = 0
#     return a[b]
# bofer = reduce(func,sample,{})
#
# print(bofer)

def add_to_dict(dct, lst):
    '''
    Args:
        dct (dict): (sub)dictionary that is currently updated
        lst (list): list of items in a currently processed row
    '''
    if len(lst) <10:
        dct[lst[0]] = {
            'quantity': lst[1],
            'price': lst[2]
        }
        return dct
    key = lst[0]
    if key not in dct:
        dct[key] = {}
    add_to_dict(dct[key], lst[1:])
    return dct

def convert_str(s):
    return list(map(str.strip, s.split(',')))


file = os.path.join("../data/BlackFriday.csv")
with open(file, encoding='utf-8') as f:
    f.readline()
    bofer = map(convert_str,f)
    result = reduce(add_to_dict, bofer,{})

print(result)