from utils import model as DbModel, input_validators as validator
import hashlib

class User:
	"""
	Kelas User untuk mengelola operasi login dan registrasi pengguna.
	Atribut:
		status (bool): Status login pengguna.
		status_reg (bool): Status registrasi pengguna.
		db (DbModel): Objek model database.
		email (str): Email pengguna.
		password (str): Password pengguna yang telah di-hash.
		nik (str, optional): Nomor Induk Kependudukan pengguna.
		nama (str, optional): Nama pengguna.
		id (int, optional): ID pengguna.
		role (str, optional): Peran pengguna.
	Metode:
		__init__(email, password, nik=None, nama=None):
			Inisialisasi objek User dengan email, password, dan opsi nik serta nama.
		login():
			Melakukan login pengguna berdasarkan email dan password.
		register():
			Melakukan registrasi pengguna baru ke dalam database.
		logout():
			Melakukan logout pengguna dan membersihkan data pengguna yang ada di sesi tersebut.
		clear():
			Membersihkan semua atribut pengguna.
	"""
    
	def __init__(self, email, password, nik = None, nama = None):
		self.status = False
		self.status_reg = False
		self.db = DbModel.DbModel()
		self.email = email
		if not validator.email_handler(email):
			self.clear()
			return None
		self.password = hashlib.md5((password + "m}&^p!B]0<").encode()).hexdigest()
		if nik is not None and nama is not None:
			self.nik = nik
			self.nama = nama
			if not validator.nik_handler(nik) or not validator.name_handler(nama):
				self.clear()
				return None
			self.status_reg = self.register()
		else:
			user_data = self.login()
			if self.status:
				self.id = user_data.get('id')
				self.nik = user_data.get('nik')
				self.nama = user_data.get('nama')
				self.role = user_data.get('role')
			else:
				self.clear()
				return None
            
	def login(self):
		self.db.connect()
		query = "SELECT * FROM user WHERE email = ? AND password = ?"
		self.db.cursor.execute(query, (self.email, self.password))
		row = self.db.cursor.fetchone()
		result = dict(row) if row else None
		if result is not None:
			self.status = True
		else:
			self.status = False
		self.db.close()
		return result
	
	def register(self):
		self.db.connect()
		query = "INSERT INTO user (email, password, nik, nama) VALUES (?, ?, ?, ?)"
		try:
			self.db.cursor.execute(query, (self.email, self.password, self.nik, self.nama))
			self.db.connection.commit()
			success = True
		except Exception:
			success = False
		finally:
			self.db.close()
			self.clear()
		return success

	def logout(self):
		self.clear()

	def clear(self):
		self.id = None
		self.email = None
		self.password = None
		self.nik = None
		self.nama = None
		self.role = None
		self.status = False
		self.status_reg = False