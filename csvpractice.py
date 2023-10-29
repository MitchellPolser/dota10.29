# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:14:20 2022

@author: Mitchell
"""

import csv
import pandas as pd
import DotaScraper

# field names

usa, eu, sea, china = DotaScraper.get_data()
#define fields  
fields = ['rank', 'player', 'team', 'team_count', 'country', 'country_count',]     
 
#get data for all fields
players = list(usa.players)
ranks = [*range(1, len(players), 1)]

teams = list(usa.team_tally.keys())
team_count = list(usa.team_tally.values())

countries = list(usa.country_tally.keys())
country_count = list(usa.country_tally.values())
while len(country_count) != len(players):
    teams.append('')
    team_count.append('')
    countries.append('')
    country_count.append('')
    

rows = zip(ranks, players, teams, team_count, countries, country_count)

with open('GFG.csv', 'w', encoding="utf-8") as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    
    for row in rows:
        write.writerow(row)
        
    #for player in players:
        #write.writerow([player])
        
p_df = pd.read_csv("GFG.csv", usecols = ['rank','player'])
print(p_df)
t_df = pd.read_csv("GFG.csv", usecols = ['team','team_count'])
print(t_df)    
c_df = pd.read_csv("GFG.csv", usecols = ['country','country_count'])
print(c_df)