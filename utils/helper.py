from .model import DbModel
from classes.user import User
from classes.stasiun import Stasiun
from classes.jadwal import Jadwal
from classes.pemesanan import Pemesanan
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
		if (user.status):
			print("Logged in as", user.nama)
		return user
	
	def register(email, password, nik, nama):
		user = User(email, password, nik, nama)
		if (user.status_reg):
			print("Registered", user.nama)
		return user
	
	def logout(user):
		User.logout(user)
		print("Logged out")

	def get_stasiun():
		print("Successfully get all stasiun")
		return Stasiun.get_all()
	
	def get_jadwal(stasiun_awal, stasiun_akhir, tanggal):
		print("Getting jadwal")
		return Jadwal(stasiun_awal, stasiun_akhir, tanggal)

	def get_history_user(user, id_input):
		return Pemesanan.load_all()

	def get_user(user):
		return user