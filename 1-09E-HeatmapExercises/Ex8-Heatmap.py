#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######
# %%
# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
# Create a DataFrame from  "flights" data
df = pd.read_csv('../data/flights.csv')
# %%
# Define a data variable
trace = go.Heatmap(
    x=df['year'],
    y=df['month'],
    z=df['passengers']
)

data = [trace]

# Define the layout
layout = go.Layout(
    title='Evolution of the number of passengers in<br>\
        filghts in month and year'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='1-09E.html')