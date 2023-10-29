# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:30:46 2023

@author: Mitchell
"""

import sqlite3

def create_table():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('liquipedia.db')

    # Create the table if it doesn't exist
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS player_data (
                        player_ID TEXT PRIMARY KEY
                    )''')
    conn.commit()

    # Close the connection
    conn.close()

if __name__ == '__main__':
    create_table()
