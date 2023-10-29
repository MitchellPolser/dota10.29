# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:14:47 2023

@author: Mitchell
"""

# historyupdate.py

import sqlite3
import pandas as pd
from datetime import datetime

def update_history():
    # Connect to the SQLite database
    conn = sqlite3.connect('leaderboards.db')

    # List of regions
    regions = ['americas', 'europe', 'se_asia', 'china']

    # Current system date
    current_date = datetime.now().date()

    # Loop over regions
    for region in regions:
        # Read the required data from the full data table into a dataframe
        df = pd.read_sql_query(f"SELECT Rank, Player_name FROM {region}_full_data", conn)

        # Add the current system date to the dataframe
        df['Date'] = current_date

        # Sort the dataframe by Rank, ascending
        df.sort_values(by='Rank', inplace=True)

        # Remove duplicates based on Player_name and Date, keep first occurrence which has the lowest Rank
        df.drop_duplicates(subset=['Player_name', 'Date'], keep='first', inplace=True)

        # If the history table does not exist, create it and append the dataframe to it
        # If it exists, simply append the new data
        df.to_sql(f'{region}_history', conn, if_exists='append', index=False)

    # Close the connection to the database
    conn.close()
