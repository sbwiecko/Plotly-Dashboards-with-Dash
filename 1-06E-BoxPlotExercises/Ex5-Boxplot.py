#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######
# %%
# Perform imports here:
from os import replace
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')
# %%
# take two random samples of different sizes:
sample_1 = df['rings'].sample(n=100, replace=True)
sample_2 = df['rings'].sample(n=100, replace=True)

# create a data variable with two Box plots:
data = [go.Box(y=sample_1,
               name='Sample 1'),
        go.Box(y=sample_2,
               name='Sample 2')]

# add a layout
layout = go.Layout(
    title = 'Comparison of the distribution of 10-samples from the same population'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box-1-06E.html')
