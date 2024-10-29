import tkinter as tk
from tkinter import messagebox
from .helper import Utils

class GUI:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Pemesanan Tiket Kereta")
		self.window.geometry("300x150")
		self.center_window(self.window)
		self.window.resizable(False, False)

		label = tk.Label(self.window, text="PT KJT", font=("Times New Roman", 16))
		label.pack(pady=30)

		button_frame = tk.Frame(self.window)
		button_frame.pack()

		login_button = tk.Button(button_frame, text="Login", command=self.on_login_click)
		login_button.pack(side="left", padx=5)

		register_button = tk.Button(button_frame, text="Register", command=self.on_register_click)
		register_button.pack(side="left", padx=5)

		# Run the main application loop
		self.window.mainloop()

	def center_window(self, win):
		win.update_idletasks()
		width = win.winfo_width()
		frm_width = win.winfo_rootx() - win.winfo_x()
		win_width = width + 2 * frm_width
		height = win.winfo_height()
		titlebar_height = win.winfo_rooty() - win.winfo_y()
		win_height = height + titlebar_height + frm_width
		x = win.winfo_screenwidth() // 2 - win_width // 2
		y = win.winfo_screenheight() // 2 - win_height // 2
		win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
		win.deiconify()

	import tkinter as tk

	def lock(self, win):
		# Prevent interaction with the parent window
		win.grab_set()

		def on_close():
			# Re-enable the main window when child window is closed
			win.grab_release()
			win.destroy()

		# Set the protocol for handling window close (WM_DELETE_WINDOW)
		win.protocol("WM_DELETE_WINDOW", on_close)


	# Function to handle Login button click
	def on_login_click(self):
		login_window = tk.Toplevel(self.window)
		login_window.title("Login")
		login_window.geometry("300x200")
		login_window.resizable(False, False)
		self.center_window(login_window)
		self.lock(login_window)

		tk.Label(login_window, text="Email:").pack(pady=10)
		email_entry = tk.Entry(login_window)
		email_entry.pack(pady=5)

		tk.Label(login_window, text="Password:").pack(pady=10)
		password_entry = tk.Entry(login_window, show="*")
		password_entry.pack(pady=5)

		def login():
			email = email_entry.get()
			password = password_entry.get()
			user = Utils.login(email, password)

			if user.status:
				messagebox.showinfo("Berhasil", f"Login berhasil sebagai {user.role} {user.nama}!")
				login_window.destroy()
			else:
				messagebox.showerror("Gagal", "Login gagal. Email atau password salah.")
				login_window.focus_set()

		login_button = tk.Button(login_window, text="Login", command=login)
		login_button.pack(pady=10)

	# Function to handle Register button click
	def on_register_click(self):
		register_window = tk.Toplevel(self.window)
		register_window.title("Register")
		register_window.geometry("300x300")
		register_window.resizable(False, False)
		self.center_window(register_window)
		self.lock(register_window)

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
			user = Utils.register(email, password, nik, nama)
			
			if user.status_reg:
				messagebox.showinfo("Register", "Akun berhasil dibuat!")
				register_window.destroy()
			else:
				messagebox.showerror("Register", "Gagal membuat akun. Cek input Anda.")

		register_button = tk.Button(register_window, text="Register", command=register)
		register_button.pack(pady=10)
	
   # Fungsi untuk menampilkan tampilan admin
"""	def show_admin_menu():
		admin_window = tk.Toplevel(window)
		admin_window.title("Admin Menu")
		admin_window.geometry("400x300")

		tk.Label(admin_window, text="Admin Menu", font=("Arial", 16)).pack(pady=10)

		def apply_ticket():
			messagebox.showinfo("Apply Ticket", "Fitur apply ticket belum tersedia.")

		def schedule():
			messagebox.showinfo("Penjadwalan", "Fitur penjadwalan belum tersedia.")

		def history():
			messagebox.showinfo("History", "Fitur history belum tersedia.")

		button_frame = tk.Frame(admin_window)
		button_frame.pack(pady=10)

		tk.Button(button_frame, text="Apply Ticket", command=apply_ticket).pack(side="left", padx=5)
		tk.Button(button_frame, text="Penjadwalan", command=schedule).pack(side="left", padx=5)
		tk.Button(button_frame, text="History", command=history).pack(side="left", padx=5)

		tk.Button(admin_window, text="Log Out", command=admin_window.destroy).pack(side="bottom", pady=10)

	# Fungsi untuk menampilkan tampilan user
	def show_user_menu():
		user_window = tk.Toplevel(window)
		user_window.title("User Menu")
		user_window.geometry("400x300")

		tk.Label(user_window, text="User Menu", font=("Arial", 16)).pack(pady=10)

		tk.Label(user_window, text="A").pack(pady=5)
		input1 = tk.Entry(user_window)
		input1.pack(pady=5)

		tk.Label(user_window, text="->").pack(pady=5)

		tk.Label(user_window, text="B").pack(pady=5)
		input2 = tk.Entry(user_window)
		input2.pack(pady=5)

		tk.Label(user_window, text="Tanggal:").pack(pady=5)
		date_entry = tk.Entry(user_window)
		date_entry.pack(pady=5)

		def confirm():
			# Lakukan sesuatu dengan data input
			selected_input1 = input1.get()
			selected_input2 = input2.get()
			selected_date = date_entry.get()
			messagebox.showinfo("Confirm", f"Input 1: {selected_input1}, Input 2: {selected_input2}, Tanggal: {selected_date}")

		tk.Button(user_window, text="Confirm", command=confirm).pack(pady=10)

		def show_history():
			messagebox.showinfo("History", "Fitur history belum tersedia.")

		tk.Button(user_window, text="History", command=show_history).pack(side="top", pady=5)

		tk.Button(user_window, text="Log Out", command=user_window.destroy).pack(side="bottom", pady=10)

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
				if user.role == 'admin':
					show_admin_menu()
				else:
					show_user_menu()
				login_window.destroy()
			else:
				messagebox.showerror("Login", "Login gagal. Email atau password salah.")

		login_button = tk.Button(login_window, text="Login", command=login)
		login_button.pack(pady=10)

		
		def menu_pilihan(self):
			pass

		def menu_pilih_kursi(self):
			pass
	"""