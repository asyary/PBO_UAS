import sqlite3
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.db = DbModel.DbModel()
        user_data = self.login()
		if user_data:
			self.id = user_data.get('id')
			self.nik = user_data.get('nik')
			self.nama = user_data.get('nama')
			self.role = user_data.get('role')
		else:
			self.id = None
			self.nik = None
			self.nama = None
			self.email = None
			self.password = None
			self.role = None
            
	def login(self):
		self.db.connect()
		query = "SELECT * FROM user WHERE email = ? AND password = ?"
		self.db.cursor.execute(query, (self.email, self.password))
		row = self.db.cursor.fetchone()
		result = dict(row) if row else None
		self.db.close()
		return result

class Admin (User):
    def __init__(self, email, password):
        super().__init__(email, password, role='admin')