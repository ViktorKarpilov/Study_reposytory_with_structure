import os
import plotly
path = os.path.join("../data/task1.csv")

def make_list(file):

    titles = file.readline().replace("\n","").split(", ")

    file = file.read().splitlines()
    result = []

    for line in file:
        result.append(dict(zip(titles, line.split(","))))
    return result

def Add_person(person,dataset):
    if person['client'] in dataset:
        if person['date'] in dataset[person['client']]:
            dataset[person['client']][person['date']].update({person['product']:[person['quantity'],person['price']]})
        else:
            dataset[person['client']].update({
                person['date']:{
                    person['product']:[person['quantity'],person['price']]
                }
            })
    else:
        dataset.update({
            person['client']:{
                person['date']:{
                    person['product']:[person['quantity'],person['price']]
                }
            }
        })
'''
products = {
    product1:{
        price={data1:price1,data2:price2},
        buys=int,
        buyers=int
        }
}
'''
'''
    dataset = {
        client:{
            data:{
                product:[quantiti,price]
            }
        }
    }
'''
def Add_product(product,owner,data,dataset):
    # TODO later
    pass

# def Make_products_set(dataset):
#     products_set = {}
#     dataset = set(dataset)
#     for person in dataset.values():
#         for date in dataset[person].values():
#             Add_person(dataset[person][date],products_set)


def Make_dataset_list(dataset,i):
    result = []
    for date in list(dataset.values())[i].values():
        result += date.keys()
    return set(result)


def Find_popular_meal(dataset):
    result = Make_dataset_list(dataset,0)
    for i in range(1,len(list(dataset.values()))):
        result = result.intersection(Make_dataset_list(dataset,i))
    if result:
        return list(result)
    return []


def Make_graphic(dataset,search_product):
    print(list(dataset.values())[0])
    result = {}
    for person in list(dataset.values()):
        for date,products in person.items():
            if date not in result:
                if search_product in products:
                    result[date] = products[search_product][1]

    plotly.offline.plot([plotly.graph_objs.Bar(x=list(result.keys()),y=list(result.values()))])


def Make_persons_statistic(dataset):
    # list(dataset.keys())
    # list(dataset.values())[0]
    result = {}
    for person,shops in dataset.items():
        result[person] = Person_expensen(shops)
    return result

def Person_expensen(shops):
    result = 0
    for products in list(shops.values()):
        for i in products.values():
            result += float(i[0])*float(i[1])

    return result

def Build_graphic_expenses(dataset):
    expenses = Make_persons_statistic(dataset)
    data = plotly.graph_objs.Bar(x=list(expenses.keys()),y=list(expenses.values()))
    plotly.offline.plot([data])

'''
    apple:{
        price:4.5,
        count:4
        }
'''
def Make_products_list(dataset):
    result = {}
    for shops in dataset.values():
        for products in list(shops.values()):
            for product,value in products.items():
                if product in result:
                    result[product]["count"] += 1
                else:
                    result[product] = {
                        "count":1,
                        "price":value[1]
                    }
    return result

def find_max(data):
    max = 0
    product = ""
    for key,value in data.items():
        if value["count"] > max:
            max = value["count"]
            product = key
    return {product:max}
def find_min(data):

    min = list(data.values())[0]['count']
    product = list(data.keys())[0]
    for key,value in data.items():
        if value["count"] < min:
            min = value["count"]
            product = key
    return {product:min}
def find_max_pice(data):
    max = 0
    product = ""
    for key,value in data.items():

        if float(value["price"]) > max:
            max = float(value["price"])
            product = key
    return {product:max}
def Build_buys_graph(data):
    dta = {}
    for i,j in data.items():
        dta[i] = j['count']


    print(dta)
    figure = plotly.graph_objs.Bar(x=list(dta.keys()),y=list(dta.values()))
    plotly.offline.plot([figure])

if __name__ == '__main__':
    with open(path, "r") as file:
        dataset = {}
        data = make_list(file)
        for person in data:
            Add_person(person,dataset)
        print(Find_popular_meal(dataset))






