from .model import DbModel
from .kode_generator import generate_random_alphanumeric as kode_gen
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
	
	def add_pesanan(id_user, id_jadwal, gerbong, kursi):
		print("Adding pesanan")
		pesanan = Pemesanan(id_user, id_jadwal, gerbong, kursi)
		pesanan = pesanan.new()
		return pesanan
	
	def cek_jadwal(id_user, id_jadwal):
		print("Checking jadwal")
		pesanan = Pemesanan(id_user, id_jadwal, None, None)
		found = pesanan.cari()
		return found is not None
	
	def history_pesanan(id_user):
		print("Getting history pesanan")
		pesanan = Pemesanan(id_user, None, None, None)
		print(f"user id : {pesanan.id_user}")
		pesanan_data = pesanan.load_all()
		print(f"Type of pesanan_data: {type(pesanan_data)}")
		return pesanan_data
	def history_admin():
		print("Getting history pesanan")
		pesanan = Pemesanan(None, None, None, None)
		pesanan_data = pesanan.load_history_admin()
		return pesanan_data

	def load_acc_pesanan():
		print("Loading acc pesanan")
		pesanan = Pemesanan(None, None, None, None)
		return pesanan.load_acc_admin()

	def acc_pesanan(kode):
		print(f"Accepting pesanan {kode}")
		pesanan = Pemesanan(None, None, None, None)
		pesanan.acc(kode)
		return pesanan

  