'''
    {
        city_category:{
            product_category:{products}
            }
    }
'''

'''global functions'''
line_number = 0
import re
import os
from functools import reduce
import plotly
def GetElement(string,n=1):
    result = re.split(r',', string, maxsplit=n)
    elem=result[n-1].strip()
    return elem ,result[n]

def GetProduct(string,key):
    number = key.index("Product_ID") + 1
    string,line = GetElement(string,number)
    return string

def GetCity(string,key):
    number = key.index("City_Category")+1
    string, line = GetElement(string, number)
    string = re.findall(r'[A-Z]{1}',string)[0]
    return string

def GetCategory(string,key):
    number = key.index("Product_Category_1") + 1
    string, line = GetElement(string, 9)
    if not string:
        return "NoCategory"
    return string

def Add_Key(dataset,city):
    if city in dataset:
        return dataset
    dataset[city]= {}
    return dataset

def Add_value(dataset,category,city):
    if category not in dataset[city]:
        dataset[city][category] = set()
    return dataset

def Add_value_set(dataset,product,category,city):
    dataset[city][str(category)].add(product)
    return dataset

def Update_dataset(dataset,city,category,product):
    dataset = Add_Key(dataset,city)
    dataset = Add_value(dataset,category,city)
    dataset = Add_value_set(dataset,product,category,city)
    return dataset

def make_dataset(filename,):

    with open(filename) as file:
        titles = file.readline().split(",")
        lines = file.readlines()
        dataset = {}
        for line in lines:
            global line_number
            line_number += 1
            if len(line)>2:
                category = GetCategory(line,titles)
                product = GetProduct(line,titles)
                city = GetCity(line,titles)
                dataset = Update_dataset(dataset,city,category,product)
        return dataset

def build_graphic(dataset,result_path):
    from plotly import tools
    import plotly.graph_objs as go
    local_dataset={}
    for i in range(len(list(dataset.values()))):
        keys = list(list(dataset.values())[i].keys())
        for category in keys:
            if category in local_dataset:
                local_dataset["category: "+category] += 1
            else:
                local_dataset["category: "+category] = 1
    lables = []
    values = []

    for key,value in local_dataset.items():
        lables.append(key)
        values.append(value)
    # graph = go.Pie(x=lables,y=values,domain= {'x': [0,0],'y': [0,0]})
    # something = go.Scatter(x=[1,2,3],y=[4,3,2])
    fig = tools.make_subplots(rows=1,cols=3)
    fig.add_pie(labels=lables,values=values,domain={'x':[0.3,0.7]})

    local_dataset = {}
    for i in dataset.keys():
        local_dataset[i] = len(list(dataset[i].keys()))
    lables = []
    values = []
    for key,value in local_dataset.items():
        lables.append(key)
        values.append(value)
    bar_graph1 = go.Bar(x=lables, y=values)
    fig.append_trace(bar_graph1, 1, 1)

    local_dataset = {}
    for i in dataset.keys():
        local_dataset[i] = sum(list(map(lambda x:len(x),list(dataset[i].values()))))

    lables = []
    values = []
    for key, value in local_dataset.items():
        lables.append(key)
        values.append(value)
    bar_graph2 = go.Bar(x=lables, y=values)
    fig.append_trace(bar_graph2,1,3)
    path_for_saving_plot = os.path.join(result_path)
    plotly.offline.plot(fig,filename=path_for_saving_plot)



def Main(file_path,result_path):
    try:
        filename = os.path.join(file_path)
        dataset = make_dataset(filename)
    except IOError as e :
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError as vl:
        print("Value error {0} in line {1}".format(vl, line_number))
    try:
        build_graphic(dataset,result_path)
    except Exception as excepton:
        print("You have a problem that looks like {0}".format(excepton))



if __name__ == '__main__':

    try:
        filename = os.path.join('../../data/friday.csv')
        dataset = make_dataset(filename)
    except IOError as e :
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError as vl:
        print("Value error {0} in line {1}".format(vl, line_number))
    print(dataset)
    try:
        build_graphic(dataset,"../../result/result_test.html")
    except Exception as excepton:
        print("You have a problem that looks like {0}".format(excepton))

