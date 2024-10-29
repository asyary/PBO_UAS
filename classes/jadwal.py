from utils import model as DbModel

class Jadwal:
    def __init__(self, stasiun_awal, stasiun_akhir):
        self.db = DbModel.DbModel()
        
        self.stasiun_awal = stasiun_awal
        self.stasiun_akhir = stasiun_akhir
        
        # Fetching all schedules matching the given stations
        self.jadwal_data = self.valid()
        
        # Initialize instance variables with data from the first result, if available
        if self.jadwal_data:
            for get_jadwal in self.jadwal_data:
                first_jadwal = get_jadwal
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
            
            #fungsi masukan ke db

    def valid(self):
        self.db.connect()
        query = """
            SELECT j.*, s_awal.nama AS s_awal, s_akhir.nama AS s_akhir
            FROM jadwal AS j
            JOIN stasiun AS s_awal ON j.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON j.stasiun_akhir = s_akhir.id
            WHERE j.stasiun_awal = ? AND j.stasiun_akhir = ?
        """
        self.db.cursor.execute(query, (self.stasiun_awal, self.stasiun_akhir))
        rows = self.db.cursor.fetchall()
        
        result = [dict(row) for row in rows] if rows else None
        self.db.close()
        return result
    
    def new(self, harga_eko, harga_bis, harga_eks, waktu):
        """Inserts a new schedule record into the database."""
        self.db.connect()
        
        query = """
            INSERT INTO jadwal (stasiun_awal, stasiun_akhir, harga_eko, harga_bis, harga_eks, waktu)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        
        # Execute the query with provided values
        try:
            self.db.cursor.execute(query, (self.stasiun_awal, self.stasiun_akhir, harga_eko, harga_bis, harga_eks, waktu))
            self.db.connection.commit()
            success = True
        except Exception:
            success = False
        finally:
            self.db.close()
            # self.clear()
        return success
    
    #
    # def show_jadwal(self):
    #     if not self.jadwal_data:
    #         print("No schedules found for the selected stations.")
    #         return
        
    #     # Display each schedule
    #     for index, jadwal in enumerate(self.jadwal_data, start=1):
    #         print(f"Schedule {index}:")
    #         print(f"  ID Jadwal      : {jadwal.get('id')}")
    #         print(f"  Stasiun Awal   : {jadwal.get('s_awal')}")
    #         print(f"  Stasiun Akhir  : {jadwal.get('s_akhir')}")
    #         print(f"  Harga Ekonomi  : {jadwal.get('harga_eko')}")
    #         print(f"  Harga Bisnis   : {jadwal.get('harga_bis')}")
    #         print(f"  Harga Eksekutif: {jadwal.get('harga_eks')}")
    #         print(f"  Waktu          : {jadwal.get('waktu')}\n")
