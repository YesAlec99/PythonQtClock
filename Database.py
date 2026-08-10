import sqlite3


class Database:

    def __init__(self, db_file="timer.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS timer_information (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                starting_time TEXT,
                timer_length INTEGER,
                time_completed INTEGER,
                was_cancelled INTEGER
            )
        """)

        self.conn.commit()

    def add_timer(self, date, starting_time, timer_length,
                  time_completed, was_cancelled):

        self.cursor.execute("""
            INSERT INTO timer_information
            (date, starting_time, timer_length, time_completed, was_cancelled)
            VALUES (?, ?, ?, ?, ?)
        """, (
            date,
            starting_time,
            timer_length,
            time_completed,
            was_cancelled
        ))

        task_id = self.cursor.lastrowid
        self.conn.commit()

        return task_id

    def close(self):
        self.conn.close()