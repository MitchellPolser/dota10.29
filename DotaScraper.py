# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:49:23 2022

@author: Mitchell
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
from collections import Counter as howmany
from CountryDictionary import country_dict
import sqlite3
from historyupdate import update_history

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file"""
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn


def main():
    refresh_data()
    update_history()    

def refresh_data():
    regions = ['americas', 'europe', 'se_asia', 'china']
    html_text = get_html(regions)
    counts = [100, 1000, 'full']
    
    conn = create_connection("leaderboards.db")  # Create a connection to a SQLite database file

    for count in counts:
        usa_rows = sort_data(html_text[0], count)
        eu_rows = sort_data(html_text[1], count)
        sea_rows = sort_data(html_text[2], count)
        china_rows = sort_data(html_text[3], count)

        fields = ['Rank', 'Player_name', 'Team_name', 'Team_count', 'Country_name',
                  'Country_count']

        counter = 0
        while counter != 4:
            table_name = regions[counter] + '_' + str(count) + '_data'
            cur = conn.cursor()
            # Drop table if it already exists using execute() method.
            cur.execute("DROP TABLE IF EXISTS " + table_name)

            # Create table as per requirement
            cur.execute("CREATE TABLE " + table_name + " (Rank INTEGER, Player_name TEXT, Team_name TEXT, Team_count INTEGER, Country_name TEXT, Country_count INTEGER)")

            rows = usa_rows if counter == 0 else eu_rows if counter == 1 else sea_rows if counter == 2 else china_rows

            # insert data to table
            cur.executemany("INSERT INTO " + table_name + " VALUES (?, ?, ?, ?, ?, ?)", rows)

            counter = counter + 1
            
    conn.commit()
    conn.close()



def get_html(regions):
    html_text = [''] * 4
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    ##set selenium options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome(options=chrome_options)
    counter = 0
    for page in html_text:
        driver.get("https://www.dota2.com/leaderboards/#" + str(regions[counter]))
        sleep(5)
        html_text[counter] = driver.page_source
        counter = counter + 1
    return html_text


def sort_data(html_text, count):
    players = get_players(html_text, count)
    ranks = [*range(1, len(players), 1)]
    #get all teams data
    team_names, team_counts = tally_teams(html_text, count)
    
    #get all country data
    country_names, country_counts = tally_countries(html_text, count)
    
    while len(country_counts) != len(players):
        team_names.append('')
        team_counts.append('')
        country_names.append('')
        country_counts.append('')
    
    rows = zip(ranks, players, team_names, team_counts, country_names, country_counts)

    return list(rows)


def get_lines(html_text):
    soup = BeautifulSoup(html_text, "lxml")
    lines = soup.find_all('tr')
    return lines


def get_players(html_text, count):
    lines = get_lines(html_text)
    players = [''] * len(lines)
    counter = 0
    while counter != len(players) - 2:
        players[counter] = lines[counter].find("span", class_="player_name")
        player_text = str(players[counter])
        player_text = player_text.replace('<span class="player_name">', '')
        player_text = player_text.replace('</span>', '')
        players[counter] = player_text
        counter = counter + 1
    players.pop(0)
    if count != 'full':
        players = players[0 : count + 1]  # This line could cause error if count is 'full'
    return players


def get_teams(html_text):
    lines = get_lines(html_text)
    teams = [''] * len(lines)
    counter = 0
    while counter != len(teams) - 2:
        teams[counter] = lines[counter]("span", class_="team_tag")
        team_text = str(teams[counter])
        team_text = team_text.replace('[<span class="team_tag">', '')
        team_text = team_text.replace('.</span>]', '')
        teams[counter] = team_text
        counter = counter + 1

    teams.pop(0)
    
    counter = 0
    for team in teams:
        if teams[counter] == '[]':
            del teams[counter]
        counter = counter + 1
    return teams


def tally_teams(html_text, count):
    teams = get_teams(html_text)
    if count != 'full':
        teams = teams[0 : count]
    t = howmany(teams)
    # Delete all empty
    t.pop('[]', None)
    t = dict(t)
    team_names = list(t.keys())
    team_counts = list(t.values())
    return team_names, team_counts


def get_countries(html_text):
    lines = get_lines(html_text)
    countries = [""] * len(lines)
    counter = 0
    while counter != len(countries) - 1:
        countries[counter] = lines[counter]('div')
        country_text = str(countries[counter])
        country_text = country_text.replace('[<div style="float: right;"><img src="https://community.cloudflare.steamstatic.com/public/images/countryflags/', '')
        country_text = country_text[:2]
        countries[counter] = country_text.upper()
        counter = counter + 1

    countries.pop(0)
    countries = countries
    return countries


def tally_countries(html_text, count):
    countries = get_countries(html_text)
    if count != 'full':
        countries = countries[0 : count]
    c = howmany(countries)
    empty = c['[]']
    c.pop('[]', None)
    c.pop('', None)
    c = dict(c)
    key_list = list(c.keys())
    for cc in country_dict.keys():
        counter = 0
        while counter != len(list(c.keys())):
            if cc == key_list[counter]:
                c[country_dict[cc]] = c.pop(key_list[counter])
            counter = counter + 1

    c["Not Reported"] = empty 
    #if want_raw == True:
    country_names = list(c.keys())
    country_counts = list(c.values())
    return country_names, country_counts


main()
