# 1. Generating dataset from file
import os
'''
Expected dataset example:
{
    'Jane': { 
        '10.11.2018': { 
            'apple': {
                'quantity':1,
                'price': 4.5
            } #, ...
        } #,...
    } #,...
}
'''
# Method 1. Column-wise read
'''
Temorary dataset example: {'Jane': [['10.11.2018', 'apple', '1', '4.5']] }
'''
def convert_2_dict(lst):
    '''
    Args:
        lst (list): list of lists for a curent column sub-dictionary
    '''
    if len(lst[0]) == 2:
        return {
            'quantity': lst[0][0],
            'price': lst[0][1]
        }
    dct = {}
    for sublst in lst:
        key = sublst[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(sublst[1:])
    for key in dct:
        dct[key] = convert_2_dict(dct[key])
    return dct
file = os.path.join("../data/task1.csv")
with open(file, encoding='utf-8') as f:
    f.readline()
    file = [[el.strip() for el in line.split(',')] for line in f]
    result = convert_2_dict(file)

print(result)


# Method 2. Row-wise read
def add_to_dict(dct, lst):
    '''
    Args:
        dct (dict): (sub)dictionary that is currently updated
        lst (list): list of items in a currently processed row
    '''
    if len(lst) == 3:
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

from functools import reduce
file = os.path.join("../data/task1.csv")
with open(file, encoding='utf-8') as f:
    f.readline()
    result = reduce(add_to_dict, map(convert_str, f), {})

print(result)


# 2. Extracting data from dataset
res = set()

for name, val in result.items():
    for date, val2 in val.items():
        res = res.union(set(val2.keys()))
for name in result:
    client_products = set()
    for date in result[name]:
        client_products = client_products.union(set(result[name][date].keys()))
    res = res.intersection(client_products)

print(res)


# 3. Extracting and plotting data series 
apples = {}

for _, dates in result.items():
    for date, products in dates.items():
        for prod, chars in products.items():
            if prod == 'apple':
                apples[date] = chars['price']
# this can also be written as
# apples = { 
#    date: chars['price'] 
#    for _, dates in result.items()
#    for date, products in dates.items()
#    for prod, chars in products.items()
#    if prod == 'apple'
# }

print(apples)

import plotly.offline as pl
import plotly.graph_objs as go

xs = sorted(list(apples.keys()))
ys = [apples[key] for key in xs]

pl.plot([go.Scatter(x=xs,y=ys)])
# same as
#
# pl.plot({
#    'data': [go.Scatter(x=xs,y=ys)]
# })
#
# or even
#
# series1 = go.Scatter(x=xs,y=ys)
# options = {
#    'data': [series1]
# }
# pl.plot(options)
