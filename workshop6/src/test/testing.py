import plotly.graph_objs as go
import plotly.offline as po
from plotly import tools

fig = tools.make_subplots(rows=1,cols=3)
first = go.Pie(labels=['q','w'],values=[12,134])
fig.add_pie(labels=['q','w'],values=[12,134])
fig.add_bar(x=['b','c'],y=[12,15])
po.plot(fig)
