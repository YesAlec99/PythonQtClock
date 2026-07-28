import sqlite3

connection = sqlite3.connect("timer.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS timer_information(

id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
starting_time TEXT,
timer_length INTEGER,
time_completed INTEGER,
was_cancelled TEXT

)
""")
