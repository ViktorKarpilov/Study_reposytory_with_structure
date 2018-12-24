import plotly
from scipy import interpolate
import numpy as np
x = np.arange(10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x,y)

xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)
znew = f(ynew)
# use interpolation function returned by `interp1d`
plotly.offline.plot([plotly.graph_objs.Scatter(x=x,y=y),plotly.graph_objs.Scatter3d(x=xnew,y=ynew,z=znew)],auto_open=True,filename="interpolation.html")
