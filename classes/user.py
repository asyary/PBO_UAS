class User:
    def __init__(self, nama, telp, email, role = "user"):
       self.nama = nama
       self.no_telp = telp
       self.email = email
       self.role = role

class Admin (User):
    def __init__(self, nama, telp, email, role='admin'):
        super().__init__(nama, telp, email, role)
    
