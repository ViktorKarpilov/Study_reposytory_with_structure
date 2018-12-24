from data import dataset
from task1 import *
from task3 import recursionBySeconds
import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: на якій трасі ,який найкращий час
def get_set(raw_set):
    raw_set = dict(raw_set)
    for i,j in raw_set.items():
        raw_set[i] = min(j)
    return raw_set

datas = get_set(recursionBySeconds(dataset))
data = go.Bar(x=list(datas.keys()),y=list(datas.values()))
plotly.offline.plot([data])