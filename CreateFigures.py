import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash import dash, dcc, html, dash_table
import sqlite3
import plotly.io as pio
pio.renderers.default = "browser"

def main():
    pass

def get_fig(region, chart, count):
    if chart == 'countries':
        fig = countries(region, count)
    elif chart == 'teams':
        fig = teams(region, count)
    elif chart == 'players':
        fig = players(region, count)
    elif chart == 'history':
        fig = history(region, count)
    return fig

def teams(region, count):
    with sqlite3.connect('leaderboards.db') as conn:
        query = f'SELECT Team_name, CAST(Team_count AS INT) AS Team_count FROM {region}_{count}_data WHERE CAST(Team_count AS INT) > 2'
        df = pd.read_sql_query(query, conn)
        
    df = df.sort_values(by=['Team_count'], ascending=True)
    df.columns = ['Team name', 'Number of players on team']
    
    fig = px.bar(df, x="Number of players on team", y="Team name", orientation='h', title='Number of Players by Team')
    fig.update_layout(template='plotly_dark', height=800, title_x=0.5, title_y=0.93, plot_bgcolor='#000000', paper_bgcolor='#000000')
    return fig

def players(region, count):
    with sqlite3.connect('leaderboards.db') as conn:
        query = f'SELECT Rank, Player_name FROM {region}_{count}_data'
        df = pd.read_sql_query(query, conn)
        
    df = df.sort_values(by=['Rank'], ascending=True)
    df.columns = ['Rank', 'Player Name']
    
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='darkslategray',
                    align='center',
                    height=50),
        cells=dict(values=df.transpose().values.tolist(),
                   fill_color='darkslategray',
                   align='center',
                   height=50))
            ])

    fig.update_layout(template='plotly_dark', plot_bgcolor='#000000', paper_bgcolor='#000000')
    return fig

def countries(region, count):
    with sqlite3.connect('leaderboards.db') as conn:
        query = f'SELECT Country_name, CAST(Country_count AS INT) AS Country_count FROM {region}_{count}_data'
        df = pd.read_sql_query(query, conn)

    not_reported = int(df.loc[df['Country_name'] == 'Not Reported', 'Country_count'])
    df = df.loc[df["Country_name"] != 'Not Reported']
    display_count = len(df.index) + 1

    one_player_df = df.loc[df['Country_count'] == 1]
    one_player_count = len(one_player_df)
    df.loc[len(df.index)] = ['*Countries with only 1 player*', one_player_count]

    df = df.loc[df['Country_count'] > 1]
    df = df.sort_values(by=['Country_count'], ascending=False)

    fig = px.pie(
        df,
        values='Country_count',
        names='Country_name',
        color_discrete_sequence=px.colors.sequential.RdBu,
        title=region.capitalize() + " Top " + str(display_count) + ": Percentage of Players by Country <br> <sup> "
        + "This chart displays the " + str(display_count - not_reported) + " players that have country data available. (" + str(not_reported) + " players did not have country data available) </sup>")

    fig.update_layout(template='plotly_dark', height=800, title_x=0.50, title_y=0.93, legend=dict(yanchor="top", y=0.80, xanchor="right", x=.91), plot_bgcolor='#000000', paper_bgcolor='#000000')

    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig
    
def history(region, player):
    with sqlite3.connect('leaderboards.db') as conn:
        query = f'SELECT Date, Rank FROM {region}_history WHERE Player_name = ?'
        df = pd.read_sql_query(query, conn, params=[player])

    # Convert Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    fig = px.line(
        df, 
        x='Date', 
        y='Rank', 
        title=f'Player Rank Over Time for {player} in {region.capitalize()} Region',
        labels={'Date': 'Date', 'Rank': 'Player Rank'}
    )

    fig.update_layout(template='plotly_dark', height=800, title_x=0.50, title_y=0.93, plot_bgcolor='#000000', paper_bgcolor='#000000')
    fig.update_yaxes(autorange="reversed")  # Update y-axis to be descending

    return fig

############
# def biggest_rank_changes(region):
    with sqlite3.connect('leaderboards.db') as conn:
        query = f'SELECT Player_name, Rank, Date FROM {region}_history'
        df = pd.read_sql_query(query, conn)

    # Convert Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Calculate rank changes
    df['Rank Change'] = df.groupby('Player_name')['Rank'].diff()

    # Find the biggest winner and biggest loser
    biggest_winner = df.loc[df['Rank Change'].idxmin()]
    biggest_loser = df.loc[df['Rank Change'].idxmax()]

    return biggest_winner, biggest_loser
###############
main()
