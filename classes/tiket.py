#gambaran umum yang kupahami soal pemilihan jadwal kereta
class Pesan:
   def __init__(self, stasiun_Awal, stasiun_Tujuan, penumpang, jadwal):
       self.stasiun_Awal = stasiun_Awal
       self.stasiun_Tujuan = stasiun_Tujuan
       self.penumpang = penumpang
       self.jadwal = jadwal
    
    

class Tiket(Pesan):
   def __init__(self, stasiun_Awal, stasiun_Tujuan, penumpang, jadwal):
       super().__init__(stasiun_Awal, stasiun_Tujuan, penumpang, jadwal)
       self.time1 = "04:28 - 08:29"
       self.time2 = "10:07 - 13:56"
       self.time3 = "14:13 - 18:21"
       self.time4 = "17:30 - 21:24"
       self.time = "15:41 - 21:57"

def JadwalKereta(tiket):
   print("Pilih nomor jadwal (1-5):")
   n = int(input())  # Mengubah input ke tipe integer

   if n == 1:
       print(f"Commuter Line Sampangan (287)\nStasiun Awal: {tiket.stasiun_Awal}\nStasiun Tujuan: {tiket.stasiun_Tujuan}\nJadwal: {tiket.time1}")
   elif n == 2:
       print(f"Commuter Line Sampangan (657)\nStasiun Awal: {tiket.stasiun_Awal}\nStasiun Tujuan: {tiket.stasiun_Tujuan}\nJadwal: {tiket.time2}")
   elif n == 3:
       print(f"Commuter Line Sampangan (723)\nStasiun Awal: {tiket.stasiun_Awal}\nStasiun Tujuan: {tiket.stasiun_Tujuan}\nJadwal: {tiket.time3}")
   elif n == 4:
       print(f"Commuter Line Sampangan (008)\nStasiun Awal: {tiket.stasiun_Awal}\nStasiun Tujuan: {tiket.stasiun_Tujuan}\nJadwal: {tiket.time4}")
   elif n == 5:
       print(f"Commuter Line Sampangan (956)\nStasiun Awal: {tiket.stasiun_Awal}\nStasiun Tujuan: {tiket.stasiun_Tujuan}\nJadwal: {tiket.time}")
   else:
       print("Nomor jadwal tidak valid. Silakan pilih antara 1-5.")

#gambaran kursi di kereta
def Kursi():
   daftar_kursi = []
   alphabet = ['A', 'B', 'C', 'D', 'E']

   for number in range(1, 25):  # Dari 1 hingga 24
    for letter in alphabet:  # Untuk setiap huruf A sampai E
        daftar_kursi.append(f"{number}{letter}")  # Menggabungkan angka dan huruf


# # Membuat objek Tiket dengan data yang diberikan
# tiket_kereta = Tiket("Wlingi", "Wonokromo", penumpang=1, jadwal=None)

# # Menjalankan fungsi JadwalKereta dengan objek tiket_kereta
# JadwalKereta(tiket_kereta)
