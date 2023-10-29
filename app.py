# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:33:43 2023

@author: Mitchell
"""

from dash import Dash, Input, Output, dcc, html
import dash_bootstrap_components as dbc
import sqlite3

from home_page import home_layout, update_home_graph
from page_2 import page2_layout, update_page2_graph

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    return page2_layout if pathname == '/page-2' else home_layout

@app.callback(Output('fig_display_home', 'figure'),
              [Input('slct_region', 'value'),
               Input('slct_chart', 'value'),
               Input('slct_count', 'value')])
def update_home_page(*args):
    return update_home_graph(*args)

@app.callback(Output('fig_display_page2', 'figure'),
              [Input('slct_region', 'value'),
               Input('slct_player', 'value')])
def update_page_2(*args):
    return update_page2_graph(*args)

@app.callback(Output('slct_player', 'options'), [Input('slct_region', 'value')])
def update_player_options(region):
    with sqlite3.connect('leaderboards.db') as conn:
        c = conn.cursor()
        c.execute(f"SELECT MAX(Date) FROM {region}_history")
        most_recent_date = c.fetchone()[0]
        c.execute(f"SELECT Player_name, Rank FROM {region}_history WHERE Date = ?", (most_recent_date,))
        players = c.fetchall()

    return [{'label': f'{player[0]} (#{player[1]})', 'value': player[0]} for player in players]

if __name__ == "__main__":
    app.run_server(debug=False)