#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Define a data variable
x = np.random.randn(1000)
y = np.random.rand(1000)

data = [go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(symbol='o',
                color='rgb(51,204,153)'),
)]

# Define the layout
layout = go.Layout(
    title = 'Exercice 2',
    xaxis = dict(title = 'Some random x-values'),
    yaxis = dict(title = 'Some random y-values'),
    hovermode ='closest' # handles multiple points landing on the same vertical

)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='1-02E.html')
