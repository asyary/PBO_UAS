from .model import DbModel
from classes.user import User

class Utils:
	def cek_koneksi():
		try :
			db = DbModel()
			db.connect()
			db.close()
			return True
		except Exception as e:
			print(e)
			return False

	def login(email, password):
		user = User(email, password)
		return user
	
	def register(email, password, nik, nama):
		user = User(email, password, nik, nama)
		return user