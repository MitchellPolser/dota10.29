import sqlite3
import datetime

# Connect to the database
conn = sqlite3.connect('leaderboards.db')
c = conn.cursor()

# Get the current system date
current_date = datetime.date.today()

# Specify the tables to remove entries from
tables = ['china_history', 'americas_history', 'se_asia_history', 'europe_history']

# Iterate over the tables and delete entries with the current date
for table in tables:
    c.execute(f"DELETE FROM {table} WHERE date = ?", (current_date,))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"All entries with the date {current_date} have been deleted from the specified tables.")
