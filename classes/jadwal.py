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
<<<<<<< HEAD
            first_jadwal = get_jadwal
            self.id_jadwal = first_jadwal.get('id_jadwal')
            self.harga_eko = first_jadwal.get('harga_eko')
            self.harga_bis = first_jadwal.get('harga_bis')
            self.harga_eks = first_jadwal.get('harga_eks')
            self.waktu = first_jadwal.get('waktu')
=======
            self.id_jadwal = get_jadwal.get('id')
            self.harga_eko = get_jadwal.get('harga_eko')
            self.harga_bis = get_jadwal.get('harga_bis')
            self.harga_eks = get_jadwal.get('harga_eks')
            self.waktu = get_jadwal.get('waktu')
>>>>>>> 707e75ee24973372d32cb04c3ab63d417764407d
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
<<<<<<< HEAD
            SELECT j.*, s_awal.nama AS s_awal, s_akhir.nama AS s_akhir
            FROM jadwal AS j
            JOIN stasiun AS s_awal ON j.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON j.stasiun_akhir = s_akhir.id
            WHERE j.stasiun_awal = ? AND j.stasiun_akhir = ?
=======
            SELECT id, stasiun_awal, stasiun_akhir, harga_eko, harga_bis, harga_eks, waktu 
            FROM jadwal
            WHERE stasiun_awal = ? AND stasiun_akhir = ?
>>>>>>> 707e75ee24973372d32cb04c3ab63d417764407d
        """
        self.db.cursor.execute(query, (self.stasiun_awal, self.stasiun_akhir))
        rows = self.db.cursor.fetchall()

        # Convert rows to dictionaries assuming fetchall() returns rows with column names as keys
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
            print(f"  ID Jadwal      : {jadwal.get('id')}")
<<<<<<< HEAD
            print(f"  Stasiun Awal   : {jadwal.get('s_awal')}")
            print(f"  Stasiun Akhir  : {jadwal.get('s_akhir')}")
=======
            print(f"  Stasiun Awal   : {jadwal.get('stasiun_awal')}")
            print(f"  Stasiun Akhir  : {jadwal.get('stasiun_akhir')}")
>>>>>>> 707e75ee24973372d32cb04c3ab63d417764407d
            print(f"  Harga Ekonomi  : {jadwal.get('harga_eko')}")
            print(f"  Harga Bisnis   : {jadwal.get('harga_bis')}")
            print(f"  Harga Eksekutif: {jadwal.get('harga_eks')}")
            print(f"  Waktu          : {jadwal.get('waktu')}\n")
