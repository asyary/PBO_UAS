from utils import model as DbModel
from utils.kode_generator import generate_random_alphanumeric as kode_gen
class Pemesanan:
    def __init__(self, id_user, id_jadwal, gerbong, kursi):
       self.db = DbModel.DbModel()
       self.gerbong = gerbong
       self.kursi = kursi
       self.id_user = id_user
       self.id_jadwal = id_jadwal
       
       self.pemesanan_data = self.valid()
       
       if self.pemesanan_data:
           self.kode_pemesanan = self.pemesanan_data.get('kode')
           self.status = self.pemesanan_data.get('status') 
       else:
           self.kode_pemesanan = None
           self.status = None
       
    def valid(self): #for ticket info
        self.db.connect()
        query = """
            SELECT p.*, u.nama AS nama, u.nik AS nik, s_awal.nama AS stasiun_awal, s_akhir.nama AS stasiun_akhir, j.waktu AS waktu
            FROM pemesanan AS p
            JOIN jadwal AS j ON p.id_jadwal = j.id
            JOIN user AS u ON p.id_user = u.id
            JOIN stasiun AS s_awal ON j.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON j.stasiun_akhir = s_akhir.id
            WHERE p.id_user = ? AND p.id_jadwal = ? AND p.gerbong = ? AND p.kursi = ?
        """
        self.db.cursor.execute(query, (self.id_user, self.id_jadwal, self.gerbong, self.kursi))
        row = self.db.cursor.fetchone()
        result = dict(row) if row else None
        self.db.close()
        return result
    
    # def history(self, id_user):
    #     self.pemesanan_history = self.load_all()
    #     #took all things idk
    #     for get_pemesanan in self.pemesanan_history:
    #         self.gerbong = get_pemesanan.get('gerbong')
    #         self.kursi = get_pemesanan.get('kursi')
    #         self.kode_pemesanan = get_pemesanan.get('kode')
    #         self.status = get_pemesanan.get('status') 
    #     else:
    #          # Set to None if no data is found
    #         self.gerbong = None
    #         self.kursi = None
    #         self.kode_pemesanan = None
    #         self.status = None
            
        # # print all
        # for index, pemesanan in enumerate(self.pemesanan_history, start=1):
        #     print(f"{index}:")
        #     print("Reservation Details:")
        #     print(f"  Name           : {pemesanan.get('nama')}")
        #     print(f"  NIK            : {pemesanan.get('nik')}")
        #     print(f"  Stasiun Awal   : {pemesanan.get('stasiun_awal')}")
        #     print(f"  Stasiun Akhir  : {pemesanan.get('stasiun_akhir')}")
        #     print(f"  Waktu Keberangkatan : {pemesanan.get('waktu')}")
        #     print(f"  Gerbong        : {pemesanan.get('gerbong')}")
        #     print(f"  Kursi          : {pemesanan.get('kursi')}")
        #     print(f"  Status         : {pemesanan.get('status')}")
    
    
    
    def load_all(self): #for history
        self.db.connect()
        query = """
            SELECT p.*, u.nama AS nama, u.nik AS nik, s_awal.nama AS stasiun_awal, s_awal.kode as kode_stasiun_awal, s_akhir.nama AS stasiun_akhir, s_akhir.kode as kode_stasiun_akhir, j.waktu AS waktu,
            case when p.gerbong = 'EKS' then j.harga_eks 
                when p.gerbong = 'BIS' then j.harga_bis 
                else j.harga_eko 
            end as harga
            
            FROM pemesanan AS p
            JOIN jadwal AS j ON p.id_jadwal = j.id
            JOIN user AS u ON p.id_user = u.id
            JOIN stasiun AS s_awal ON j.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON j.stasiun_akhir = s_akhir.id
            WHERE p.id_user = ?
            ORDER BY j.waktu DESC
        """
        self.db.cursor.execute(query, (self.id_user,))
        rows = self.db.cursor.fetchmany(10)
        result_all = [dict(row) for row in rows] if rows else None
        self.db.close()
        return result_all
    
    def load_acc_admin(self):
        self.db.connect()
        query = """
            SELECT p.*, u.nama AS nama, u.nik AS nik, s_awal.nama AS stasiun_awal, s_awal.kode as kode_stasiun_awal, s_akhir.nama AS stasiun_akhir, s_akhir.kode as kode_stasiun_akhir, j.waktu AS waktu,
            case when p.gerbong = 'EKS' then j.harga_eks 
                when p.gerbong = 'BIS' then j.harga_bis 
                else j.harga_eko 
            end as harga
            
            FROM pemesanan AS p
            JOIN jadwal AS j ON p.id_jadwal = j.id
            JOIN user AS u ON p.id_user = u.id
            JOIN stasiun AS s_awal ON j.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON j.stasiun_akhir = s_akhir.id
            WHERE p.status = 0
            ORDER BY j.waktu DESC
        """
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        result_all = [dict(row) for row in rows] if rows else None
        self.db.close()
        return result_all
    
    def load_history_admin(self): #for history
        self.db.connect()
        query = """
            SELECT p.*, u.nama AS nama, u.nik AS nik, s_awal.nama AS stasiun_awal, s_awal.kode as kode_stasiun_awal, s_akhir.nama AS stasiun_akhir, s_akhir.kode as kode_stasiun_akhir, j.waktu AS waktu,
            case when p.gerbong = 'EKS' then j.harga_eks 
                when p.gerbong = 'BIS' then j.harga_bis 
                else j.harga_eko 
            end as harga
            
            FROM pemesanan AS p
            JOIN jadwal AS j ON p.id_jadwal = j.id
            JOIN user AS u ON p.id_user = u.id
            JOIN stasiun AS s_awal ON j.stasiun_awal = s_awal.id
            JOIN stasiun AS s_akhir ON j.stasiun_akhir = s_akhir.id
            ORDER BY j.waktu DESC
        """
        self.db.cursor.execute(query, ())
        rows = self.db.cursor.fetchmany(30)
        result_all = [dict(row) for row in rows] if rows else None
        self.db.close()
        return result_all        
    
    # show one latest jadwal
    # def show_jadwal(self):
    #     # Check if pemesanan data is available
    #     if not self.pemesanan_data:
    #         print("Belum ada pemesanan yang sesuai.")
    #         return
    #     # Display reservation details
    #     print("Reservation Details:")
    #     print(f"  Name           : {self.pemesanan_data.get('nama')}")
    #     print(f"  NIK            : {self.pemesanan_data.get('nik')}")
    #     print(f"  Stasiun Awal   : {self.pemesanan_data.get('stasiun_awal')}")
    #     print(f"  Stasiun Akhir  : {self.pemesanan_data.get('stasiun_akhir')}")
    #     print(f"  Waktu Keberangkatan : {self.pemesanan_data.get('waktu')}")
    #     print(f"  Gerbong        : {self.pemesanan_data.get('gerbong')}")
    #     print(f"  Kursi          : {self.pemesanan_data.get('kursi')}")
    #     print(f"  Status         : {self.pemesanan_data.get('status')}")
        
    def new(self):
        self.db.connect()
        self.kode_pemesanan = kode_gen()
        query = """
            INSERT INTO pemesanan (id_user, id_jadwal, kode, gerbong, kursi, status)
            VALUES (?, ?, ?, ?, ?, 0)
        """
        self.db.cursor.execute(query, (self.id_user, self.id_jadwal, self.kode_pemesanan, self.gerbong, self.kursi))
        self.db.connection.commit()
        self.db.close()
        return self.kode_pemesanan
        # print("Booking inserted successfully.")

    def delete(self):
        self.db.connect()
        query = """
            DELETE FROM pemesanan
            WHERE kode = ?
        """
  
        self.db.cursor.execute(query, (self.kode_pemesanan))
        self.db.connection.commit()
        self.db.close()
        # print("Booking deleted successfully.")

    def acc(self,kode_pemesanan):
        self.db.connect()
        query = """
            UPDATE pemesanan
            SET status = 1
            WHERE kode = ?
        """
        self.db.cursor.execute(query, (kode_pemesanan,))
        self.db.connection.commit()
        self.db.close()
        #try except
     
    def back(self):
        self.clear()
            
    def clear(self):
        self.id = None
        self.id_user = None
        self.id_jadwal = None
        self.kode_pemesanan = None
        self.gerbong = None
        self.kursi = None
        self.status = None
    
   