import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.io as io

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# Prepare the data
x = np.linspace(1, 12)
y2017=x;
y2018=x;
y2018=x;


df=pd.read_csv('IST_South_Tower_2017_Ene_Cons.csv')
df1=pd.read_csv('IST_South_Tower_2018_Ene_Cons.csv')
df2=pd.read_csv('IST_meteo_data_2017_2018_2019.csv')
dg=pd.read_csv('Feature SelectionP1.csv')
df3=pd.read_csv('FeatureSelectionP1.csv')
df4=pd.read_csv('FeatureSelectionP1.csv')
df5=pd.read_csv('FeatureSelectionP1.csv')
df6=pd.read_csv('FeatureSelectionP1.csv')
df7=pd.read_csv('FeatureSelectionP1.csv')
dh=pd.read_csv('TableForecast.csv')


def generate_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Plot the data

fig4=px.line(df, x='Date', y='Power_kW') 
fig5=px.line(df1, x='Date', y='Power_kW')
fig6=px.line(df2, x='Date', y='temp_C') 
fig20=px.line(df2, x='Date', y='solarRad_W/m2')
fig21=px.line(df2, x='Date', y='windSpeed_m/s')

fig7=px.line(df3, x='Date', y='PowerkW')
fig8=px.line(df4, x='Date', y='TempC')
fig9=px.line(df5, x='Date', y='Power~1')
fig10=px.line(df6, x='Date', y='Month')
fig11=px.line(df7, x='Date', y='SolarRad')


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div([
    #html.Img(src=app.get_asset_url('IST.png')),
    html.Img(src=app.get_asset_url('assets/IST.png'), style={"display": "flex",
                               "justifyContent": "center"}),
    html.H1('IST South Tower Energy Forecast Project', style={"display": "flex",
                               "justifyContent": "center"}),
    html.H5('...by Samuel Jibril Sulemanu - 98015'),
   
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Raw Data', value='tab-1'),
        dcc.Tab(label='Merged Data (Clean)', value='tab-2'),
        dcc.Tab(label='Clustering Outputs', value='tab-3'),
        dcc.Tab(label='Feature Selection', value='tab-4'),
        dcc.Tab(label='Regression Scores', value='tab-5'),
        dcc.Tab(label='Reg. Visualization', value='tab-6'),
    ]),
    html.Div(id='tabs-content')
])


def generate_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
 ##            
def render_content(tab):

    if tab == 'tab-1':
        return html.Div([
            html.H3('Raw Data Selection'),
            dcc.RadioItems( 
        id='dropd',
        options=[
            {'label': 'Power [kW] - 2017', 'value': 2030},
            {'label': 'Power [kW] - 2018', 'value': 2031},
            {'label': 'Temperature [oC]', 'value': 2032},
            {'label': 'Solar Rad [W/m2]', 'value': 2033},
            {'label': 'WindSpeed [m/s]', 'value': 2034},
            
              ],
        value=2030
        ),
        html.Div(id='graphyear_html'),
                    
        ])
       
##
    
    elif tab == 'tab-2': 
        return html.Div([
            html.H2('Clean Data Plots'),
            html.H5('Select Clean Data plot to view:'),
            dcc.Dropdown( 
        id='dropdown',
        options=[
            {'label': 'Power', 'value': 2016},
            {'label': 'Temperature', 'value': 2017},
            {'label': 'Power -1', 'value': 2018},
            {'label': 'Month', 'value': 2019},
            {'label': 'SolarRad', 'value': 2020},
           
              ], 
        value=2020
        ),
        html.Div(id='graphyear1_html'),
                
        ])
       ### 
    elif tab == 'tab-3':
        return html.Div([
            html.H2('Clustering'),
            html.H5('Choose cluster feature to view:'),
            dcc.Dropdown( 
        id='Clust',
        options=[
            {'label': 'Cluster Elbow Curve', 'value': 2040},
            {'label': 'Power/Hour Map', 'value': 2041},
            {'label': 'Cluster vs. Power Plot', 'value': 2042},
          
              ], 
        value=2040
        ),
        html.Div(id='graphyear2_html'),])
   
    ###
    
    elif tab == 'tab-4':
        return html.Div([  
            html.H3('Choose Feature Information below:'),
                    
                dcc.Dropdown( 
                    id='Feat',
                    options=[
                        {'label': 'Feature Scores', 'value': 2050},
                        {'label': 'Selected Feature Info', 'value': 2051},
           
                      ], 
                      value=2050, 
                      ), 
            
            html.Div(id='graphyear3_html'),  
            
            html.H3('Sample Data of Features for Selection:'),
            html.Div([generate_table(dg)], style = {'width': '25%', 'display': 'inline-block'}),
            html.Div(id='graphyear6_html'),
            ])
          
            
    ##Regression Results
    elif tab == 'tab-5':
     return html.Div([
            html.H3(children='Results Table'),
            generate_table(dh),])
##

    elif tab == 'tab-6':
        return html.Div([  
            html.H1('Methods and Output'),
            html.H5('Choose Regression Method below:'),
            dcc.RadioItems(
                id='RegMeth',
                options=[
                    {'label': 'Random Forest', 'value': 2060},
                    {'label': 'Decision Tree Regressor', 'value': 2061},
                    {'label': 'Support Vector', 'value': 2062}
                ], 
                value=2060),
                
        html.Div([
                  html.Div(id='graph_regression'),  
        ], 
        style={'width': '40%', 'display': 'inline-block'}),
    
       ])

   
  #RawData  
@app.callback(Output('graphyear_html', 'children'), 
              Input('dropd', 'value'))
def render_figure_html(dropdown_year):
    
    if dropdown_year == 2030:
        return html.Div([dcc.Graph(figure=fig4),
        ])               

    if dropdown_year == 2031:
        return html.Div([dcc.Graph(figure=fig5),
        ])               

    if dropdown_year == 2032:
        return html.Div([dcc.Graph(figure=fig6),
        ])     
          
    if dropdown_year == 2033:
        return html.Div([dcc.Graph(figure=fig20),
        ])     
    
    if dropdown_year == 2034:
        return html.Div([dcc.Graph(figure=fig21),
        ])   
    
@app.callback(Output('graph_regression', 'children'), 
              Input('RegMeth', 'value'))

def render_figure_html(dropdown_yea):
    
    if dropdown_yea == 2060:
        return html.Img(src=app.get_asset_url('./assets/ForestR.png'), width=1000),
           
    if dropdown_yea == 2061:
        return html.Img(src=app.get_asset_url('./assets/TreeD1.png'), width=1000),
    
    if dropdown_yea == 2062:
        return html.Img(src=app.get_asset_url('./assets/VectorS.png'), width=1000),

#Clean Data
@app.callback(Output('graphyear1_html', 'children'), 
              Input('dropdown', 'value'))
def render_figure_html(dropdown_ye):
    
    if dropdown_ye == 2016:
        return html.Div([dcc.Graph(figure=fig7),
        ])               

    if dropdown_ye == 2017:
        return html.Div([dcc.Graph(figure=fig8),
        ])               

    if dropdown_ye == 2018:
        return html.Div([dcc.Graph(figure=fig9),
        ])               

    if dropdown_ye == 2019:
        return html.Div([dcc.Graph(figure=fig10),
        ])               

    if dropdown_ye == 2020:
        return html.Div([dcc.Graph(figure=fig11),
        ])               


#Clustering
@app.callback(Output('graphyear2_html', 'children'), 
              Input('Clust', 'value'))  
def render_figure_html(dropdown_y):
    
    if dropdown_y == 2040:
        return html.Img(src=app.get_asset_url('./assets/Elbow Curve.png'), width=1000),
    elif dropdown_y == 2041:
        return html.Img(src=app.get_asset_url('./assets/Clustering kW - Hr.png'), width=1000),
    elif dropdown_y == 2042:
        return html.Img(src=app.get_asset_url('./assets/Cluster Power Plot.png'), width=1000),

    
#Feature Selection

@app.callback(Output('graphyear3_html', 'children'), 
              Input('Feat', 'value'))  
def render_figure_html(dropdown_):
    
    if dropdown_ == 2050:
        return html.Img(src=app.get_asset_url('./assets/FS - kBest.png'), width=600),
    elif dropdown_ == 2051:
        return html.Img(src=app.get_asset_url('./assets/FS - Table.png'), width=600),
#
         
                      
#if __name__ == '__main__':
   #app.run_server(debug=True)
if __name__ == '__main__':
    app.run_server(debug=False,dev_tools_ui=False,dev_tools_props_check=False)
