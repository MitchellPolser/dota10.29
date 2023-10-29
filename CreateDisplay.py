# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:34:50 2022

@author: Mitchell
"""

import DotaScraper

from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)

#DotaScraper.refresh_data()

#get dataframes for current stats
"""counter = 0
while counter != 4:
    if counter == 0:
        usa_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['rank','player'])
        usa_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['team','team_count'])
        usa_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['country','country_count'])
    elif counter == 1:
        eu_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['rank','player'])
        eu_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['team','team_count'])
        eu_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['country','country_count'])   
    elif counter == 2:
        sea_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['rank','player'])
        sea_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['team','team_count'])
        sea_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['country','country_count'])
    elif counter == 3:
        china_pdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['rank','player'])
        china_tdf = pd.read_csv(DotaScraper.regions[counter] + "_data.csv", usecols = ['team','team_count'])
        china_cdf = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['country','country_count'])
    counter = counter + 1"""
        

##======================================================================================
## app layout 
app.layout = html.Div([

    html.H1("Dota 2 Leaderboard Statistics", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_rgn",
                 options=[
                     {"label": "Americas", "value": 'americas'},
                     {"label": "Europe", "value": 'europe'},
                     {"label": "Southeast Asia", "value": 'se_asia'},
                     {"label": "China", "value": 'china'}],
                 multi=False,
                 value='Americas',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})
])


##=====================================================================================
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)


def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The region chosen by user was: {}".format(option_slctd)

    dff = option_slctd
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    """fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )"""
    
    counter = 0
    df = pd.read_csv(DotaScraper.regions[counter] +  "_data.csv", usecols = ['Team_name','Number_of_players_on_team'])
    df = df.sort_values(by=['Number_of_players_on_team'], ascending=False)
    df = df.loc[df["Number_of_players_on_team"] > 1 ]

    
    fig = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
)

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)    
  




    
