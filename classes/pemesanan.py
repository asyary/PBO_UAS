class Pemesanan:
    def __init__(self, penumpang, jadwal, gerbong, kursi, harga):
       self.penumpang = penumpang
       self.jadwal = jadwal
       self.gerbong = gerbong
       self.kursi = kursi
       self.harga = harga

    def db_load():
        pass
    
    
    # def Kursi():
    #     daftar_kursi = []
    #     alphabet = ['A', 'B', 'C', 'D', 'E']
    #     for number in range(1, 25):  # Dari 1 hingga 24
    #      for letter in alphabet:  # Untuk setiap huruf A sampai E
    #          daftar_kursi.append(f"{number}{letter}")  # Menggabungkan angka dan huruf
