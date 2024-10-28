class Jadwal:
    def __init__(self, stasiun_awal, stasiun_akhir):
        self.stasiun_awal = stasiun_awal
        self.stasiun_akhir = stasiun_akhir
        
        
        self.id_jadwal = None
        self.harga_eko = None
        self.harga_bis = None
        self.harga_eks = None
        self.waktu = None