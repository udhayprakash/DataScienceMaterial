# Data Ingestion

import glob
import logging
import os
import sqlite3

logging.basicConfig(level=logging.INFO)


def get_file_data(file_path):
    with open(file_path) as f:
        data = f.readlines()
        return [tuple(line.strip().split("\t")) for line in data]


def ingest_data(conn, data):
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM weather_data")
    existing_rows = c.fetchone()[0]
    logging.info(f"Found {existing_rows} existing rows in the table.")
    for row in data:
        c.execute(
            f"""
            INSERT OR IGNORE INTO weather_data (date, station_id, max_temp, min_temp, precipitation)
            VALUES (?, ?, ?, ?, ?)
        """,
            row,
        )
    new_rows = conn.total_changes
    conn.commit()
    logging.info(f"Inserted {new_rows} new rows into the table.")


def main():
    conn = sqlite3.connect("weather.db")
    data_dir = "wx_data"
    data_files = glob.glob(os.path.join(data_dir, "*.txt"))
    for file_path in data_files:
        logging.info(f"Processing file {file_path}")
        file_data = get_file_data(file_path)
        ingest_data(conn, file_data)
    conn.close()


if __name__ == "__main__":
    main()
