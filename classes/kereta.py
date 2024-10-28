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
        }
        
    def ubah_rute(self, baru_awal, baru_akhir):
        if baru_awal:    
            self.stasiun_awal = baru_awal
        if baru_akhir:
            self.stasiun_awal = baru_akhir    