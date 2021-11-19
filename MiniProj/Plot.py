import plotly.express as pl
import pandas as pd
import numpy as np

df = pd.read_csv('case_time_series.csv',parse_dates=['Date'])

fig = pl.line(data_frame=df,x='Date',y=['DC','DR','DD'],)
fig.show()
fig = pl.line(data_frame=df,x='Date',y=['TC','TR','TD'],)
fig.show()

