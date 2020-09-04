#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
# -------------------------------------------------------------------------
# FOR THIS EXERCICE I WANTED TO USE MY OWN DATASET FROM THE ADCC MANUSCRIPT
# -------------------------------------------------------------------------
######
# %%
# Perform imports here:
import pandas as pd
from functools import reduce # for merging multiple dataframes
import plotly.graph_objs as go
import plotly.offline as pyo
# %%
# create a DataFrame from the .csv file:
# flow cytometry HLA-DR and CD16 data from experiment fc022-c_REVISION
file_hladr = '../Data/table_fc022-c_REVISION.csv'
data_hladr = pd.read_csv(file_hladr,
                         skipfooter=2,  # drop the 2 last rows (FlowJo stats)
                         dtype={'TUBE NAME': str},
                         engine='python'
                        )

data_hladr.set_index('TUBE NAME', drop=True, inplace=True)
data_hladr.index.name = 'donor'
# drop all columns with 'Unnamed'
data_hladr.drop(columns=[col for col in data_hladr.columns if col.startswith('Unnamed')],
                inplace=True)

# -----
# results of the genotyping for all donors
file_allo = '../Data/allotypes_pbmcs.csv'
allotype = pd.read_csv(file_allo,
                       comment='#',
                       usecols=['donor', 'FCGR3A'],
                       dtype={'donor': str})
allotype.set_index('donor', drop=True, inplace=True)

# -----
# ADCC data from experiment tx007 using isolated CD56+ cells
file_adcc = '../Data/metaanalysis_tx007.csv'
data_adcc = pd.read_csv(file_adcc,
                        comment='#',
                        index_col=[0],
                        dtype={'donor': str})
data_adcc.set_index('donor', drop=True, inplace=True)

# some more preparations of the datasets
data_hladr['hla-dr+|nk'] = data_hladr['hladr+,cd16-|nk'] + data_hladr['hladr+,cd16+|nk']
data_hladr.rename(columns={'pct_nk|live': 'CD11c/CD14/CD20/CD3'}, inplace=True)
data_adcc_hladr = reduce(lambda df1, df2: pd.merge(df1.reset_index(), df2.reset_index(), on='donor'),
    [data_hladr, data_adcc, allotype])
data_adcc_hladr['donor'].astype(str)
data_adcc_hladr.set_index('donor', inplace=True)
data_adcc_hladr.rename(columns={'top': 'max % ADCC'}, inplace=True) # best for the legend title
#%%
# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(
            x=data_adcc_hladr['hladr+,cd16+|nk'],
            y=data_adcc_hladr['EC50'],
            text=data_adcc_hladr.index,
            mode='markers',
            marker=dict(size=.3*data_adcc_hladr['max % ADCC'],
                        color=data_adcc_hladr['FCGR3A'],
                        colorscale='Viridis')
    )]

"""
### SUBPLOT D - Bubble plot
ax4 = fig.add_subplot(224)

sns.scatterplot(x='hladr+,cd16+|nk',y='EC50',
                alpha=.7,
                size='max % ADCC',
                sizes=(5, 150),
                hue='FCGR3A',
                data=data_adcc_hladr,
                ax=ax4)

for donor in data_adcc_hladr.index:
    plt.annotate(donor, (data_adcc_hladr.loc[donor, 'hladr+,cd16+|nk'],
                         data_adcc_hladr.loc[donor, 'EC50']),
                 fontsize=6)

plt.xlabel("%HLA-DR$^+$,CD16$^+$ of total CD56+|lineages$^-$",
           fontdict={'size': 8, 'weight': 'bold'})
plt.ylabel(r"log$_{10}$EC$_{50}$",
           fontdict={'size': 8, 'weight': 'bold'})
"""

# create a layout with a title and axis labels
layout = go.Layout(
    title='Bubble plot example with data from the ADCC manuscript',
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')
