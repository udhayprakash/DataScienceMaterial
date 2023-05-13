# Data Modelling

import sqlite3

conn = sqlite3.connect("weather.db")
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY,
        date TEXT,
        station_id TEXT,
        max_temp REAL,
        min_temp REAL,
        precipitation REAL
    )
"""
)

conn.commit()
conn.close()
