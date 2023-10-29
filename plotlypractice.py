# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:30:05 2022

@author: Mitchell
"""

import DotaScraper

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import numpy

pio.renderers.default='browser'

app = Dash(__name__)
#DotaScraper.refresh_data()

#get dataframes for current stats
"""counter = 0
while counter != 4:
    if counter == 0:
        usa_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Rank','Player_name'])
        usa_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Team_name','Number_of_players_on_team'])
        usa_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Country name','Number of players in country'])
    elif counter == 1:
        eu_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Rank','Player name'])
        eu_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Team name','Number of players on team'])
        eu_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Country name','Number of players in country'])   
    elif counter == 2:
        sea_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Rank','Player name'])
        sea_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Team name','Number of players on team'])
        sea_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Country name','Number of players in country'])
    elif counter == 3:
        china_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Rank','Player name'])
        china_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['Team name','Number of players on team'])
        china_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Country name','Number of players in country'])
    counter = counter + 1"""
    
##this loop creates country bar for each region
"""counter = 0
while counter < 4:
    df = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Country name','Number of players in country'])
    df = df.sort_values(by=['Number of players in country'], ascending=False)
    not_reported = int(df['Number of players in country'].values[0])
    df = df.loc[df["Country name"] != 'Not Reported' ]
    df = df.head(5)
    
    
    fig = px.bar(df, x="Country name", y="Number of players in country", title="Americas Top 100: Countries with the Most Players <br> <sup> (" + str(not_reported) +" players did not have country data available) </sup>")
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_traces(marker=dict(color='DarkSlateGrey'))
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    if counter == 0: 
        usa_cfig = fig
    elif counter == 1:
        eu_cfig = fig
    elif counter == 2:
        sea_cfig = fig
    elif counter == 3:
        china_cfig = fig
    counter = counter + 1"""


"""counter = 0
while counter < 4:
    df = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Team name','Number of players on team'])
    df = df.sort_values(by=['Number of players on team'], ascending=False)
    not_reported = int(df['Number of players on team'].values[0])
    df = df.head(10)
    
    
    fig = px.bar(df, x="Team name", y="Number of players on team", title="Americas Top 100: Teams with the Most Players")
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_traces(marker=dict(color='DarkSlateGrey'))
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    if counter == 0: 
        usa_tfig = fig
    elif counter == 1:
        eu_tfig = fig
    elif counter == 2:
        sea_tfig = fig
    elif counter == 3:
        china_tfig = fig
    counter = counter + 1
usa_tfig.show()"""

"""counter = 0
while counter != 4:
    
    df = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Team_name','Number_of_players_on_team'])
    df = df.sort_values(by=['Number_of_players_on_team'], ascending=False)
    df = df.loc[df["Number_of_players_on_team"] > 1 ]
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='DarkSlateGray',
                    line_color='white',
                    font = dict(color='white'),
                    align='left'),
        cells=dict(values=[df.Team_name, df.Number_of_players_on_team],
                   fill_color='DarkSlateGray',
                   line_color = 'white',
                   font =  dict(color='white'),
                   align='left')),
    ])
    fig.update_layout(title_text='test')

    fig.show()
    counter = counter + 1"""