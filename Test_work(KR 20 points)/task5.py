from data import dataset
from task3 import recursionBySeconds
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: на якій трасі скільки заїздів
def get_set(raw_set):
    raw_set = dict(raw_set)
    for i,j in raw_set.items():
        raw_set[i] = len(j)
    return raw_set

data = get_set(recursionBySeconds(dataset))


diagram =go.Pie(labels=list(data.keys()), values=list( data.values()))

plotly.offline.plot([diagram], filename = "auto.html")