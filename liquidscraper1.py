from liquipediapy import dota
import pandas as pd
import sqlite3
import time

def main():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('leaderboards.db')

    # Create the dota object
    dota_obj = dota("your_app_name")  # replace your_app_name with your actual app name

    # Query the tables
    tables = ['americas_100_data', 'china_100_data', 'europe_100_data', 'se_asia_100_data']
    for table in tables:
        df = pd.read_sql(f'SELECT Player_name FROM {table}', conn)
        
        for player_name in df['Player_name']:
            try:
                # Get player info from the API
                data = dota_obj.get_player_info(player_name, True)

                if data is not None and 'info' in data:
                    # Flatten the data dictionary and convert it into a pandas DataFrame
                    flattened_data = {}
                    for key, value in data.items():
                        if isinstance(value, dict):
                            for subkey, subvalue in value.items():
                                flattened_data[f"{key}_{subkey}"] = subvalue
                        else:
                            flattened_data[key] = value

                    df_data = pd.DataFrame([flattened_data])

                    # Create a connection to the SQLite database
                    conn_liquipedia = sqlite3.connect('liquipedia.db')

                    cursor = conn_liquipedia.cursor()
                    
                    # Retrieve table information
                    cursor.execute("PRAGMA table_info(player_data)")
                    columns = [column[1] for column in cursor.fetchall()]

                    # If column not in table, add it
                    for column in df_data.columns:
                        if column not in columns:
                            cursor.execute(f"ALTER TABLE player_data ADD COLUMN '{column}'")
                    
                    conn_liquipedia.commit()

                    # Write the DataFrame to the database
                    df_data.to_sql('player_data', conn_liquipedia, if_exists='append', index=False)

                    print(f'Data appended to database successfully for player {player_name}.')
                else:
                    print(f'No data found or unexpected data format for player {player_name}.')
            except Exception as e:
                print(f'An error occurred for player {player_name}: {str(e)}')
                continue
            time.sleep(2)

if __name__ == '__main__':
    main()
