class User:
    def __init__(self, id_user, nik, nama, email, role = "user"):
       self.id_user = id_user
       self.nik = nik
       self.nama = nama
       self.email = email
       self.role = role

class Admin (User):
    def __init__(self, id_user, nik, nama, email, role='admin'):
        super().__init__(id_user, nik, nama, email, role)