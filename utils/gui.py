import tkinter as tk
from tkinter import messagebox
import model as DbModel
import input_validators as validator 

class GUI:
    def __init__(self):
        # Set up main window
        self.window = tk.Tk()
        self.window.title("Pemesanan Tiket Kereta")
        self.window.geometry("300x150")

        # Create label in main window
        label = tk.Label(self.window, text="PT H+3 Pensi Presiden")
        label.pack(pady=10)

        # Create frame for Login and Register buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        # Create Login and Register buttons in the frame
        login_button = tk.Button(button_frame, text="Login", command=self.on_login_click)
        login_button.pack(side="left", padx=5)

        register_button = tk.Button(button_frame, text="Register", command=self.on_register_click)
        register_button.pack(side="left", padx=5)

        # Run the main application loop
        self.window.mainloop()

    # Function to handle Login button click
    def on_login_click(self):
        login_window = tk.Toplevel(self.window)
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
            user = DbModel.User(email, password)

            if user.status:
                role_msg = "Admin" if user.role == 'admin' else "User"
                messagebox.showinfo("Login", f"Login berhasil sebagai {role_msg}, {user.nama}!")
                login_window.destroy()
            else:
                messagebox.showerror("Login", "Login gagal. Email atau password salah.")

        login_button = tk.Button(login_window, text="Login", command=login)
        login_button.pack(pady=10)

    # Function to handle Register button click
    def on_register_click(self):
        register_window = tk.Toplevel(self.window)
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
            user = DbModel.User(email, password, nik, nama)
            
            if user.status_reg:
                messagebox.showinfo("Register", "Akun berhasil dibuat!")
                register_window.destroy()
            else:
                messagebox.showerror("Register", "Gagal membuat akun. Cek input Anda.")

        register_button = tk.Button(register_window, text="Register", command=register)
        register_button.pack(pady=10)

    # Placeholder functions for additional GUI components
    def main_user(self):
        pass

    def main_admin(self):
        pass

    def menu_pilihan(self):
        pass

    def menu_pilih_kursi(self):
        pass

# Instantiate the GUI application
app = GUI()
