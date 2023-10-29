# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 21:56:50 2022

@author: Mitchell
"""

class DataSet:
    
    def __init__(self, r_name, players, team_tally, country_tally):
        self.r_name = r_name
        self.players = players
        self.team_tally = team_tally
        self.country_tally = country_tally
        
        
    def show(self):
        print(self.r_name, self.top_ten, self.team_tally, self.country_tally)
        