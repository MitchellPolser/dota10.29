# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:00:10 2023

@author: Mitchell
"""
from dash import html, dcc
from dash.dependencies import Input, Output

def layout():
    return html.Div([
        html.H1('Another Page'),
        dcc.Input(id='input-on-page-2', value='initial value', type='text'),
        html.Div(id='output-on-page-2', children='Enter something into the input')
    ])

def update_output(value):
    return f'You\'ve entered "{value}"'

