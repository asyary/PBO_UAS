import sqlite3
import os
from pathlib import Path

class DbModel:
	def __init__(self):
		APP_NAME = "Kereta KJT"
		appdata_path = os.path.join(os.getenv('APPDATA'), APP_NAME)
		self.db_name = Path(appdata_path) / "db.db"

	def connect(self):
		self.connection = sqlite3.connect(self.db_name)
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()

	def close(self):
		if self.connection:
			self.connection.close()