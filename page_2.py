from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import CreateFigures

def display_biggest_rank_changes(region):
    biggest_winner, biggest_loser = CreateFigures.biggest_rank_changes(region)
    return html.Div([
        html.H3('Biggest Rank Changes', className="text-center", style={"color":"white"}),
        html.P(f'Biggest Winner: {biggest_winner["Player_name"]} with a rank change of {biggest_winner["Rank Change"]}', style={"color":"white"}),
        html.P(f'Biggest Loser: {biggest_loser["Player_name"]} with a rank change of {biggest_loser["Rank Change"]}', style={"color":"white"}),
    ])

def create_dropdown(id, options, value, searchable=False):
    return dcc.Dropdown(id=id, options=options, value=value, searchable=searchable)

def create_col(content, size=12, offset=0):
    return dbc.Col(content, md={'size': size, 'offset': offset})

region_dropdown = create_dropdown("slct_region", [
    {"label": "Americas", "value": "americas"},
    {"label": "Europe", "value": 'europe'},
    {"label": "SE Asia", "value": 'se_asia'},
    {"label": "China", "value": 'china'}
], 'americas')

player_dropdown = create_dropdown("slct_player", [], 'americas', True)

timeframe_dropdown = create_dropdown("slct_timeframe", [
    {"label": "Week", "value": "week"},
    {"label": "Month", "value": 'month'}
], 'week')


page2_layout = dbc.Container(
    children=[
        dbc.Row([
            create_col([html.A(html.Button('Home', id='link-button', style={'backgroundColor': '#000000', 'color': 'white'}), href='/')], 1),
            create_col([
                html.H1(children="Dota 2 Leaderboard Stats", className="text-center", style={"color":"white"}), 
                html.P(children="View statistics for the Dota 2 leaderboards.", className="text-center", style={"color":"white"}),
            ], 10),
            create_col([], 1),
        ], className="mb-4"),
        dbc.Row([
            create_col([html.H3('Select Region', className="text-center", style={"color":"white", "fontSize": "medium"}), region_dropdown], 4, 2),
            create_col([html.H3('Search or Select Player', className="text-center", style={"color":"white", "fontSize": "medium"}), player_dropdown], 4),
            create_col([], 4),
        ], className="mb-4"),
        dbc.Row([create_col([dcc.Graph(id='fig_display_page2', figure={},)], 12)]),
        #dbc.Row([create_col([display_biggest_rank_changes('americas')], 12)]),  # Add this line
    ],
    fluid=True,
    style={"backgroundColor": "#000000"},
)


def update_page2_graph(region_slctd, player_slctd):
    return CreateFigures.get_fig(region_slctd, "history", player_slctd)