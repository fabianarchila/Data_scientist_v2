# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# its necessary the transactions.csv and users.csv files

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from users_code import fig_1,fig_2, fig_5, fig_6
from dash.dependencies import Input, Output
from transactions_code import fig_3, fig_4

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'b_2':'#EFEAEA',
}


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Data Scientist challenge',
        style={
            'textAlign': 'center',
            'color': 'DarkRed',
            'font-family': 'serif',
            'font-weight': 'bold',
        }
    ),

    dcc.RadioItems(
        id='select_date_ouput',
        options=[{'label': x, 'value': x} 
                 for x in ['Daily', 'Monthly']],
        value='Daily',
        labelStyle={'display': 'inline-block','color': 'DarkRed','font-family': 'serif',
            'font-weight': 'bold'}
    ),
    dcc.Graph(
        id='graph'
    ),
    html.Div([
        html.Div([
            dcc.Graph(id='transaction_graph',figure=fig_3)
        ],className='four columns'),
        html.Div([
            dcc.Graph(id='ecosystem_graph',figure=fig_5)
        ],className='four columns'),
        html.Div([
            dcc.Graph(id='ecosystem_saved_graph',figure=fig_6)
        ],className='four columns')

        
    ],className='row'),
    dcc.Graph(id='variation_graph',figure=fig_4)
    
    
])
@app.callback(
    Output("graph", "figure"), 
    [Input("select_date_ouput", "value")])
def display_graph(marginal):
    fig=0
    if marginal=='Daily':
        fig=fig_1
    elif marginal=='Monthly':
        fig=fig_2

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)