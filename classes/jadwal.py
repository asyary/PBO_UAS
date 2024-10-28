class Jadwal:
    def __init__(self, id_jadwal, stasiun_awal, stasiun_akhir):
        self.id_jadwal = id_jadwal
        self.stasiun_awal = stasiun_awal
        self.stasiun_akhir = stasiun_akhir
        self.waktu = ["04:28 - 08:29","10:07 - 13:56","14:13 - 18:21","17:30 - 21:24"]

    def show_jadwal(self):
        for index, waktu in enumerate(self.waktu, start=1):
            print(f"{index}.) {waktu}")

