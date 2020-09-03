#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######
#%%
# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

#%%
# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../Data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
df.drop(columns=['LST_DATE'], inplace=True) # we don't need that

# I set the index differently so that it will be easier to filter data
df.set_index(keys=['DAY', 'LST_TIME'], drop=True, inplace=True)

#%%
# Use a for loop (or list comprehension to create traces for the data list)
data = [go.Scatter(
    x=df.loc[day].index,
    y=df.loc[day]['T_HR_AVG'],
    mode = 'markers+lines',
    name = day
) for day in days]

# Define the layout
layout = go.Layout(
    title = 'Evolution of the temperature',
    xaxis = dict(title = 'Some random x-values'),
    yaxis = dict(title = 'Some random y-values'),
    hovermode ='closest' # handles multiple points landing on the same vertical
)


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='1-03E.html')
