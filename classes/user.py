class User:
    def __init__(self, nik, nama, email, role = "user"):
       self.nik = nik
       self.nama = nama
       self.email = email
       self.role = role

class Admin (User):
    def __init__(self, nik, nama, email, role='admin'):
        super().__init__(nik, nama, email, role)