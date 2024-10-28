import tkinter as tk
from tkinter import messagebox
from utils import model as DbModel
from utils import input_validators as validator 

class GUI:
	# Membuat jendela utama
window = tk.Tk()
window.title("Pemesanan Tiket Kereta")
window.geometry("300x150")

class User:
    def __init__(self, email, password, nik=None, nama=None):
        self.status = False
        self.status_reg = False
        self.db = DbModel.DbModel()
        self.email = email
        
        if not validator.email_handler(email):
            self.clear()
            return

        self.password = password

        if nik and nama:
            self.nik = nik
            self.nama = nama
            if not (validator.nik_handler(nik) and validator.name_handler(nama)):
                self.clear()
                return
            self.status_reg = self.register()
        else:
            user_data = self.login()
            if self.status:
                self.id = user_data.get('id')
                self.nik = user_data.get('nik')
                self.nama = user_data.get('nama')
                self.role = user_data.get('role')
            else:
                self.clear()

    def login(self):
        self.db.connect()
        query = "SELECT * FROM user WHERE email = ? AND password = ?"
        self.db.cursor.execute(query, (self.email, self.password))
        row = self.db.cursor.fetchone()
        result = dict(row) if row else None
        
        self.status = result is not None
        self.db.close()
        return result

    def register(self):
        self.db.connect()
        query = "INSERT INTO user (email, password, nik, nama) VALUES (?, ?, ?, ?)"
        try:
            self.db.cursor.execute(query, (self.email, self.password, self.nik, self.nama))
            self.db.connection.commit()
            success = True
        except Exception as e:
            print(f"Error during registration: {e}")  # Debugging
            success = False
        finally:
            self.db.close()
            self.clear()
        return success

    def clear(self):
        self.id = None
        self.email = None
        self.password = None
        self.nik = None
        self.nama = None
        self.role = None
        self.status = False
        self.status_reg = False

# Fungsi untuk menangani klik tombol Login
def on_login_click():
    login_window = tk.Toplevel(window)
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Email:").pack(pady=5)
    email_entry = tk.Entry(login_window)
    email_entry.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    def login():
        email = email_entry.get()
        password = password_entry.get()
        user = User(email, password)

        if user.status:
            role_msg = "Admin" if user.role == 'admin' else "User"
            messagebox.showinfo("Login", f"Login berhasil sebagai {role_msg}, {user.nama}!")
            login_window.destroy()
        else:
            messagebox.showerror("Login", "Login gagal. Email atau password salah.")

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=10)

# Fungsi untuk menangani klik tombol Register
def on_register_click():
    register_window = tk.Toplevel(window)
    register_window.title("Register")
    register_window.geometry("300x300")

    tk.Label(register_window, text="Nama:").pack(pady=5)
    nama_entry = tk.Entry(register_window)
    nama_entry.pack(pady=5)

    tk.Label(register_window, text="NIK:").pack(pady=5)
    nik_entry = tk.Entry(register_window)
    nik_entry.pack(pady=5)

    tk.Label(register_window, text="Email:").pack(pady=5)
    email_entry = tk.Entry(register_window)
    email_entry.pack(pady=5)

    tk.Label(register_window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack(pady=5)

    def register():
        nama = nama_entry.get()
        nik = nik_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        user = User(email, password, nik, nama)

        if user.status_reg:
            messagebox.showinfo("Register", "Akun berhasil dibuat!")
            register_window.destroy()
        else:
            messagebox.showerror("Register", "Gagal membuat akun. Cek input Anda.")

    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.pack(pady=10)

# Membuat label di jendela utama
label = tk.Label(window, text="PT H+3 Pensi Presiden")
label.pack(pady=10)

# Membuat frame untuk tombol Login dan Register agar sejajar
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Membuat tombol Login dan Register di dalam frame
login_button = tk.Button(button_frame, text="Login", command=on_login_click)
login_button.pack(side="left", padx=5)

register_button = tk.Button(button_frame, text="Register", command=on_register_click)
register_button.pack(side="left", padx=5)

# Menjalankan loop utama aplikasi
window.mainloop()


	def main_user(self):
		pass

	def main_admin(self):
		pass

	def menu_pilihan(self):
		pass

	def menu_pilih_kursi(self):
		pass
