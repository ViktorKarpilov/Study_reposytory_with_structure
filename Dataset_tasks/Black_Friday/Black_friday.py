import os
import time
import plotly
import threading
from functools import reduce

'''
    user_id:{
        product_id:{
                    'gender':gender,
                    'Age':age,
                    'ocupation':ocup,
                    'city':city,
                    'stay':years,
                    'status':status,
                    'category':category,
                    'Product_Category_1'
                    'Product_Category_2'
                    'Product_Category_3'
                    'Purchase' 
                    
'''
def add_in_dict(dataset,values):
    statick_values = {
                'gender': values[2],
                'Age': values[3],
                'ocupation': values[4],
                'city': values[5],
                'stay': values[6],
                'status': values[7],
                'Product_Category_1': values[8],
                'Product_Category_2': values[9],
                'Product_Category_3': values[10],
                'Purchase': values[11]
            }
    if values[0] in dataset:
        # if values[1] in dataset[values[0]]:
        #     dataset[values[0]][values[1]].update(statick_values)
        #     return dataset
        # else:
        dataset[values[0]].update({values[1]:statick_values})
        return dataset
    else:
        dataset[values[0]] = {values[1]:statick_values}
        return dataset

def make_dataset(filename):
    def msplit(string):
        string = (string.strip()).split(",")
        return string
    with open(filename,'r') as file:
        keys = file.readline()
        value = file.readlines()
        value =  list(map(msplit,value))
        dataset = reduce(add_in_dict,value,{})
        return dataset
def build_graphic(x,y,title=""):
    data = plotly.graph_objs.Bar(x=x,y=y,name=title)
    plotly.offline.plot([data])

def build_graphic_gender(dataset):
    local_set = {
        'M':{
            'count':0,
            'sum':0
        },
        'F': {
            'count': 0,
            'sum': 0
        }
    }
    avg = {}
    for values in dataset.values():
        for stapp in values.values():
            local_set[stapp['gender']]['count'] += 1
            local_set[stapp['gender']]['sum'] += int(stapp['Purchase'])
    for key in local_set.keys():
        avg[key] = local_set[key]['sum']/local_set[key]['count']

    build_graphic(list(avg.keys()),list(avg.values()),"Gender statisctic")

if __name__ == '__main__':
    time_before = time.time()
    filename = os.path.join("../../data/BlackFriday.csv")
    dataset = make_dataset(filename)

    city_stat = {}
    for purchase in dataset.values():
        for k in purchase.values():
            if k['city'] in city_stat:
                city_stat[k['city']]['counts'] += 1
                city_stat[k['city']]['sum'] += int(k['Purchase'])
            else:
                city_stat[k['city']] = {'counts':1,'sum':int(k['Purchase'])}
    dictionary = {}
    for key,value in city_stat.items():
        dictionary[key] = value['sum']/value['counts']
    threading.Thread(target=build_graphic_gender,args=[dataset]).start()
    build_graphic(list(dictionary.keys()),list(dictionary.values()),"Citys statistic")

    print(time.time()-time_before)