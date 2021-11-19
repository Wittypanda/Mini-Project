import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # or plotly.express as px


df = pd.read_csv('case_time_series.csv',parse_dates=['Date'])
dff = pd.read_csv('state_wise.csv')
#pdf = pd.rea


#state = str(input())
fig = px.line(data_frame=df,x='Date',y=['DC','DR','DD'],template='plotly_dark')
fig_2 = px.bar(data_frame=dff,x='State' ,y=['CNF','ACT','RCV','DED'],template='plotly_dark')
fig_3 = px.line(data_frame=df,x='Date',y=['TC','TR','TD'],template='plotly_dark')


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[

    html.H1(children='Covid 19 Visualisation (india)',style={'text-align':'center'}),
    
    html.H3('DUring the wake of the year 2020, covid 19 hitted India.It made its first debute in India in the sate of kerala in the the mont of january, after which it devestaed the country of india for a lomng period of time and its been torrmenting to withness such level of mass desturuction.'),

    html.Div(children=
    dcc.Graph(figure=fig)),

    html.Br(),

    html.Div(children=[
        dcc.Graph(figure=fig_2)
    ]),

    html.Br(),

    html.Div(children=[
        dcc.Graph(figure=fig_3)
    ])
    
])


#app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, use_reloader=False)