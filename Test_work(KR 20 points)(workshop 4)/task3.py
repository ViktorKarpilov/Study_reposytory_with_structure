
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#проходить по датасету і повиртає словник змагання: секунди
def recursionBySeconds(dataset,values=False,result={},i=0):
    if i >= len(dataset):
        return None
    if not values:
        values = list(dataset.values())
    # print(values)
    car = values.pop()
    keys = list(car.keys())
    points = list(car.values())
    # print(keys,points)
    for key in keys:
        points[0] = points[0].replace("[", "")
        # points[0] = points[0].replace("]", "")
        point = float(points[0].replace("]", ""))
        points.remove(points[0])
        if key in result:
            result[key].append(point)
        else:
            result[key] =[point]
    # print(result)
    recursionBySeconds(dataset,values,result,i+1)
    return result
    #TODO

if __name__ == '__main__':
    print(recursionBySeconds(dataset))



