# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:35:25 2023

@author: Mitchell
"""
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import CreateFigures

home_layout = dbc.Container(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.A(
                            html.Button('Page 2', id='link-button', style={'backgroundColor': '#000000', 'color': 'white'}),
                            href='/page-2'
                        )
                    ],
                    md={'size': 1, 'offset': 0},
                    className="text-left"
                ),
                dbc.Col(
                    children=[
                        html.H1(children="Dota 2 Leaderboard Stats", className="text-center", style={"color":"white"}), 
                        html.P(children="View statistics for the Dota 2 leaderboards.", className="text-center", style={"color":"white"}),
                    ],
                    md={'size': 10, 'offset': 0},
                ),
                dbc.Col(md={'size': 1, 'offset': 0}),  # Empty column for centering
            ],
            className="mb-4",  # margin-bottom
        ),

        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dcc.Dropdown(
                            id="slct_chart",
                            options=[
                                {"label": "Show me: Country Data", "value": 'countries'},
                                {"label": "Show me: Team Data", "value": 'teams'},
                                {"label": "Show me: Player Data", "value": 'players'}
                            ],
                            value='countries',
                            searchable=False,
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    children=[
                        dcc.Dropdown(
                            id="slct_count",
                            options=[
                                {"label": "For the: Top 100 players", "value": 100},
                                {"label": "For the: Top 1,000 players", "value": 1000},
                                {"label": "For the: Full leaderboard", "value": 'full'}
                            ],
                            value=100,
                            searchable=False,
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    children=[
                        dcc.Dropdown(
                            id="slct_region",
                            options=[
                                {"label": "In the: Americas region", "value": "americas"},
                                {"label": "In the: Europe region", "value": 'europe'},
                                {"label": "In the: SE Asia region", "value": 'se_asia'},
                                {"label": "In the: China region", "value": 'china'}
                            ],
                            value='americas',
                            searchable=False,
                        ),
                    ],
                    md=4,
                ),
            ],
            className="mb-4",
        ),
        
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dcc.Graph(id='fig_display_home', figure={},),
                    ],
                    md=12,
                ),
            ],
        ),
    ],
    fluid=True,
    style={"backgroundColor": "#000000"},  # Changes the background color to black
)

def update_home_graph(region_slctd, chart_slctd, count_slctd):
    fig = CreateFigures.get_fig(region_slctd, chart_slctd, str(count_slctd))
    return fig
