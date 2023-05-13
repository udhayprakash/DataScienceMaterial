import logging
import sqlite3

logging.basicConfig(level=logging.INFO)


def calculate_stats(conn):
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS weather_stats (
            id INTEGER PRIMARY KEY,
            year INTEGER,
            station_id TEXT,
            avg_max_temp REAL,
            avg_min_temp REAL,
            total_precipitation REAL
        )
    """
    )
    conn.commit()
    c.execute(
        "SELECT DISTINCT SUBSTR(date, 1, 4) AS year, station_id FROM weather_data"
    )
    results = c.fetchall()
    for result in results:
        year = int(result[0])
        station_id = result[1]
        c.execute(
            f"""
            SELECT AVG(max_temp), AVG(min_temp), SUM(precipitation)
            FROM weather_data
            WHERE SUBSTR(date, 1, 4) = ? AND station_id = ? AND max_temp != -9999 AND min_temp != -9999 AND
        """,
            (year, station_id),
        )
