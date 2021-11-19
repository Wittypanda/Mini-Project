import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # or plotly.express as px


df = pd.read_csv('case_time_series.csv',parse_dates=['Date'])

fig = px.line(data_frame=df,x='Date',y=['DC','DR','DD'],template='plotly_dark')
fig_2 = px.line(data_frame=df,x='Date',y=['TC','TR','TD'],template='plotly_dark')


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[

    html.H1(children='Covid 19 Visualisation (india)'),
    
    html.Div(children=
    dcc.Graph(figure=fig)),

    html.Br(),

    html.Div(children=[
        dcc.Graph(figure=fig_2)
    ])
    
])


#app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, use_reloader=False)