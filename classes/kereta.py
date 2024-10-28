class Kereta:
    def __init__(self, no_kereta, stasiun_awal, stasiun_akhir):
        self.no_kereta = no_kereta
        self.stasiun_awal = stasiun_awal
        self.stasiun_akhir = stasiun_akhir
        self.jadwal = {
            'SENIN': [],
            'SELASA': [],
            'RABU': [],
            'KAMIS': [],
            'JUMAT': [],
            'SABTU': [],
            'MINGGU': [],
        }
        
    def ubah_rute(self, baru_awal, baru_akhir):
        if baru_awal:    
            self.stasiun_awal = baru_awal
        if baru_akhir:
            self.stasiun_awal = baru_akhir
            
    def __str__(self) -> str:
        return (f"No Kereta: {self.train_number} | Rute: {self.start_station} - {self.end_station} | "
                f"Berangkat: {self.departure_time} | Sampai: {self.arrival_time}")





#CONTOH sama class station
# start_station = Station("Surabaya Gubeng", "Surabaya", "SGU")
# end_station = Station("Malang", "Malang", "MLG")
# train = Train(
#     train_number="101",
#     start_station=start_station,
#     end_station=end_station,
#     departure_time="08:00",
#     arrival_time="10:30"
# )