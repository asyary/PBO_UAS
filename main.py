import sys
from utils.helper import Utils
from utils.gui import GUI

def init():
	if Utils.cek_koneksi():
		print("Berhasil terhubung ke database")
	else:
		sys.exit("Error: Tidak dapat terhubung ke database")
	GUI()

if __name__ == "__main__":
    init()