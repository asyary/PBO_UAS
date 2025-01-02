from utils import model as DbModel

class Jadwal:
    def __init__(self, stasiun_awal, stasiun_akhir, tanggal):
        self.db = DbModel.DbModel()
        
        self.stasiun_awal = stasiun_awal
        self.stasiun_akhir = stasiun_akhir
        self.tanggal = tanggal
        
        # Fetching all schedules matching the given stations
        self.jadwal_data = self.valid()
        
        # Store all schedules in a list
        self.jadwal_list = []
        
        # Initialize instance variables for each result
        if self.jadwal_data:
            for get_jadwal in self.jadwal_data:
                jadwal_info = {
                    'id_jadwal': get_jadwal.get('id_jadwal'),
                    'harga_eko': get_jadwal.get('harga_eko'),
                    'harga_bis': get_jadwal.get('harga_bis'),
                    'harga_eks': get_jadwal.get('harga_eks'),
                    'waktu': get_jadwal.get('waktu'),
                    's_awal': get_jadwal.get('s_awal'),
                    's_akhir': get_jadwal.get('s_akhir')
                }
                self.jadwal_list.append(jadwal_info)  # Append each schedule to the list
        else:
            # Set to an empty list if no data is found
            self.jadwals = []
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
            WHERE j.stasiun_awal = ? AND j.stasiun_akhir = ? AND j.waktu LIKE ?
        """
        self.db.cursor.execute(query, (self.stasiun_awal, self.stasiun_akhir, f"{self.tanggal}%"))
        rows = self.db.cursor.fetchall()
        
        result = [dict(row) for row in rows] if rows else None
        self.db.close()
        return result
    
    def new(self, waktu, stasiun_awal, stasiun_akhir, harga_eko=50000, harga_bis=70000, harga_eks=100000):
        """Inserts a new schedule record into the database."""
        self.db.connect()
        
        query = """
            INSERT INTO jadwal (waktu, stasiun_awal, stasiun_akhir, harga_eko, harga_bis, harga_eks)
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
