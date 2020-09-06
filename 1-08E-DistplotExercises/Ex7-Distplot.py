#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######
# %%
# Perform imports here:
import pandas as pd
import numpy as np # for vectorization
import plotly.offline as pyo
import plotly.figure_factory as ff
# create a DataFrame from the .csv file:
file = '../data/iris.csv'
df = pd.read_csv(file)
# %%
# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
#df[df['class']=='Iris-some-flower-class']['petal_length']
clsses = df['class'].unique()

# Define a data variable
data = [df[df['class']==clss]['petal_length'] for clss in clsses]

# Create a fig from data and layout, and plot the fig
vfunc = np.vectorize(lambda x: x[5:].capitalize()) # to strip the Iris class name
fig = ff.create_distplot(hist_data=data, group_labels= vfunc(clsses))
pyo.plot(fig, filename='1-08E.html')
