from utils import model as DbModel

class Jadwal:
    def __init__(self, stasiun_awal, stasiun_akhir):
        self.db = DbModel.DbModel()
        
        self.stasiun_awal = stasiun_awal
        self.stasiun_akhir = stasiun_akhir
        
        # Fetching all schedules matching the given stations
        self.jadwal_data = self.valid()
        
        # Initialize instance variables with data from the first result, if available
        for get_jadwal in self.jadwal_data:
            first_jadwal = get_jadwal[0]
            self.id_jadwal = first_jadwal.get('id_jadwal')
            self.harga_eko = first_jadwal.get('harga_eko')
            self.harga_bis = first_jadwal.get('harga_bis')
            self.harga_eks = first_jadwal.get('harga_eks')
            self.waktu = first_jadwal.get('waktu')
        else:
            # Set to None if no data is found
            self.id_jadwal = None
            self.harga_eko = None
            self.harga_bis = None
            self.harga_eks = None
            self.waktu = None

    def valid(self):
        self.db.connect()
        query = """
            SELECT jadwal.*, s_awal.nama AS stasiun_awal, s_akhir.nama AS stasiun_akhir 
            FROM jadwal
            JOIN stasiun AS s_awal ON jadwal.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON jadwal.stasiun_akhir = s_akhir.id
            WHERE jadwal.stasiun_awal = ? AND jadwal.stasiun_akhir = ?
        """
        self.db.cursor.execute(query, (self.stasiun_awal, self.stasiun_akhir))
        rows = self.db.cursor.fetchall()
        
        result = [dict(row) for row in rows] if rows else None
        self.db.close()
        return result
    
    def show_jadwal(self):
        if not self.jadwal_data:
            print("No schedules found for the selected stations.")
            return
        
        # Display each schedule
        for index, jadwal in enumerate(self.jadwal_data, start=1):
            print(f"Schedule {index}:")
            print(f"  ID Jadwal      : {jadwal.get('id_jadwal')}")
            print(f"  Stasiun Awal   : {jadwal.get('stasiun_awal')}")
            print(f"  Stasiun Akhir  : {jadwal.get('stasiun_akhir')}")
            print(f"  Harga Ekonomi  : {jadwal.get('harga_eko')}")
            print(f"  Harga Bisnis   : {jadwal.get('harga_bis')}")
            print(f"  Harga Eksekutif: {jadwal.get('harga_eks')}")
            print(f"  Waktu          : {jadwal.get('waktu')}\n")
