import os
path = os.path.join("../data/task1.csv")

def convert_2_dict(lst):
    if len(lst[0])==2:
        return{
            "quantity":lst[0][0],
            "price":lst[0][1]
        }
    dict = {}
    for sublist in lst:
        key = sublist[0]
        if key not in dict:
            dict[key] = []
        dict[key].append(sublist[1:])
    for key in dict:
        dict[key] = convert_2_dict(dict[key])
    return dict

if __name__ == '__main__':
    with open(path, "r") as file:
        file = [[el.strip() for el in line.split(",")]for line in file]
        result = convert_2_dict(file)
    print(result)

def add_to_dict(dict,lst):
    if len(list) == 3:
        dict[lst[0]] = {
            'quantiti':lst[1],
            'price':lst[2]
        }
        return dict
    key = lst[0]
    if key not in dict:
        dict[key] = {}
    add_to_dict(dict,lst[1:])
    return dict
from functools import reduce
if __name__ == '__main__':
    with open(path, "r") as file:
        def convert_string(s):
            return list(map(str.strip,s.split(",")))
        result = reduce(add_to_dict,map(convert_string,file),{})

    print(result)
    slice = {}
    for name in result:
        slice[name] = set()
        for date in result[name]:
            slice[name].union(set(result[name][date].keys()))