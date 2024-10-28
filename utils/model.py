import sqlite3
import os

class DbModel:
    def __init__(self, db_name=None):
        if db_name is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.db_name = os.path.join(base_dir, 'db.db')
        else:
            self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()