import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
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
				self.window.destroy()
				if user.role == 'admin':
					self.show_admin_menu(user)
				else:
					self.show_user_menu(user)
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
			Utils.get_user = user
			if user.status_reg:
				messagebox.showinfo("Register", "Akun berhasil dibuat!")
				register_window.destroy()
			else:
				messagebox.showerror("Register", "Gagal membuat akun. Cek input Anda.")

		register_button = tk.Button(register_window, text="Register", command=register)
		register_button.pack(pady=10)
	
   # Fungsi untuk menampilkan tampilan admin
	def show_admin_menu(self, user):
		admin_window = tk.Tk()
		admin_window.title("Admin Menu")
		admin_window.geometry("400x300")
		self.center_window(admin_window)
		admin_window.resizable(False, False)

		tk.Label(admin_window, text="Admin Menu", font=("Arial", 16)).pack(pady=10)

		def acc_tiket():
			messagebox.showinfo("Acc Ticket", "Fitur acc ticket belum tersedia.")

		def jadwal():
			messagebox.showinfo("Penjadwalan", "Fitur penjadwalan belum tersedia.")

		def history():
			  	messagebox.showinfo("History", "Fitur history belum tersedia.")
			
			

		button_frame = tk.Frame(admin_window)
		button_frame.pack(pady=10)

		tk.Button(button_frame, text="Apply Ticket", command=acc_tiket).pack(side="left", padx=5)
		tk.Button(button_frame, text="Penjadwalan", command=jadwal).pack(side="left", padx=5)
		tk.Button(button_frame, text="History", command=history).pack(side="left", padx=5)

		tk.Button(admin_window, text="Log Out", command=admin_window.destroy).pack(side="bottom", pady=10)

	# Fungsi untuk menampilkan tampilan user
	def show_user_menu(self,  user):
		user_window = tk.Tk()
		user_window.title("User Menu")
		user_window.geometry("400x450")
		self.center_window(user_window)
		user_window.resizable(False, False)

		tk.Label(user_window, text="User Menu", font=("Arial", 16)).pack(pady=10)

		stasiun_frame = tk.Frame(user_window)
		stasiun_frame.pack(pady=5)

		stasiun = Utils.get_stasiun()

		# Stasiun Awal
		awal_frame = tk.Frame(stasiun_frame)
		awal_frame.pack(side=tk.LEFT, padx=5)
		tk.Label(awal_frame, text="Stasiun Awal").pack()
		stasiun_nama = [f"{s['kode']} - {s['nama']}" for s in stasiun]
		stasiun_awal_var = tk.StringVar(awal_frame)
		input1 = tk.OptionMenu(awal_frame, stasiun_awal_var, *stasiun_nama)
		stasiun_awal_var.set(stasiun_nama[0])  # Set default value
		input1.pack()

		# Arrow
		tk.Label(stasiun_frame, text="->").pack(side=tk.LEFT, padx=5, pady=10)

		# Stasiun Akhir
		akhir_frame = tk.Frame(stasiun_frame)
		akhir_frame.pack(side=tk.LEFT, padx=5)
		tk.Label(akhir_frame, text="Stasiun Akhir").pack()
		stasiun_akhir_var = tk.StringVar(akhir_frame)
		input2 = tk.OptionMenu(akhir_frame, stasiun_akhir_var, *stasiun_nama)
		stasiun_akhir_var.set(stasiun_nama[0])  # Set default value
		input2.pack()

		tk.Label(user_window, text="Tanggal:").pack(pady=5)
		calendar = Calendar(user_window, selectmode='day', year=2024, month=10, day=29)
		calendar.pack(pady=5)

		def confirm():
			# Lakukan sesuatu dengan data input
			selected_stasiun_awal = stasiun_awal_var.get()
			selected_stasiun_akhir = stasiun_akhir_var.get()
			selected_date = calendar.get_date()
			selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")
			if selected_stasiun_awal == selected_stasiun_akhir:
				messagebox.showerror("Error", "Stasiun awal dan stasiun akhir tidak boleh sama.")
				return
			messagebox.showinfo("Confirm", f"Input 1: {selected_stasiun_awal}, Input 2: {selected_stasiun_akhir}, Tanggal: {selected_date}")

		tk.Button(user_window, text="Confirm", command=confirm).pack(pady=15)

		def show_history():
			history_window = tk.Toplevel(user_window)
			history_window.title("History Pemesanan")
			history_window.geometry("500x400")
			
			tk.Label(history_window, text="History Pemesanan", font=("Arial", 16)).pack(pady=10)
			user_search = Utils.get_user()
			history_data = Utils.get_history_user(user_search.id)
			if history_data:
				for booking in history_data:
					booking_frame = tk.Frame(history_window, bd=1, relief="solid")
					booking_frame.pack(fill="x", padx=10, pady=5)
					booking_info = (
						f"Booking ID: {booking['id_pemesanan']}\n"
						f"User: {booking['nama']}, NIK: {booking['nik']}\n"
						f"From: {booking['stasiun_awal']} To: {booking['stasiun_akhir']}\n"
						f"Date: {booking['tanggal']}, Time: {booking['waktu']}\n"
						f"Status: {'Approved' if booking['status'] == 1 else 'Pending'}"
					)
					tk.Label(booking_frame, text=booking_info, justify="left").pack()

				else:
					tk.Label(history_window, text="No booking history found.", font=("Arial", 12)).pack(pady=20)

			 
		tk.Button(user_window, text="History", command=show_history).pack(side="left", padx=10, pady=5)

		tk.Button(user_window, text="Log Out", command=user_window.destroy).pack(side="right", padx=10, pady=5)

"""	# Fungsi untuk menangani klik tombol Login
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