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
		admin_window.geometry("300x400")
		self.center_window(admin_window)
		admin_window.resizable(False, False)

		tk.Label(admin_window, text="Admin Menu", font=("Arial", 16)).pack(pady=10)

		def acc_tiket():
			acc_window = tk.Toplevel(admin_window)
			acc_window.title("Persetujuan Tiket")
			acc_window.geometry("415x400")
			acc_window.resizable(False, False)
			self.center_window(acc_window)
			acc_window.grab_set()
   
			tk.Label(acc_window, text="Persetujuan Tiket", font=("Arial", 16)).pack(pady=10)
   
			# Create a frame for the canvas and scrollbar
			frame = tk.Frame(acc_window)
			frame.pack(fill='both', expand=True)

			# Add a canvas in that frame
			canvas = tk.Canvas(frame)
			canvas.pack(side="left", fill="both", expand=True)

			# Add a scrollbar to the frame
			scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
			scrollbar.pack(side="right", fill="y")

			# Enable mouse wheel scrolling
			def on_mouse_wheel(event):
				canvas.yview_scroll(int(-1*(event.delta/120)), "units")

			canvas.bind_all("<MouseWheel>", on_mouse_wheel)
	
			# Configure the canvas
			canvas.configure(yscrollcommand=scrollbar.set)
			canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

			# Create another frame inside the canvas
			history_frame = tk.Frame(canvas)
			canvas.create_window((0, 0), window=history_frame, anchor="nw")

			data_acc = Utils.load_acc_pesanan()
			def approve_booking(kode):
				Utils.acc_pesanan(kode)
				acc_window.destroy()
				acc_tiket()
				

			def load_data():
				if data_acc:
					for booking in data_acc:
						booking_frame = tk.Frame(history_frame, bd=1, relief="solid")
						booking_frame.pack(fill="x", padx=10, pady=5, anchor="nw")
						booking_info = (
							f"Kode Tiket\t: {booking.get('kode')}\n"
							f"Nama\t\t: {booking.get('nama')}\n"
							f"NIK\t\t: {booking.get('nik')}\n"
							f"Tujuan\t\t: {(booking.get('stasiun_awal').upper())} ({booking.get('kode_stasiun_awal')})  >>  {booking.get('stasiun_akhir').upper()} ({booking.get('kode_stasiun_akhir')})\n"
							f"Kursi\t\t: {booking.get('gerbong')} ({booking.get('kursi')})\n"
							f"Tarif\t\t: Rp. {booking.get('harga')}\n"
							f"Berangkat\t: {booking.get('waktu')}\n"
						)
						tk.Label(booking_frame, text=booking_info, font=("Arial", 10), justify="left").pack(anchor="w", padx=5, pady=5)
						tk.Button(booking_frame, text="Approve", command=lambda kode=booking.get('kode'): approve_booking(kode)).pack(side="right", padx=10)
				else:
					tk.Label(history_frame, text=f"No booking found.", font=("Arial", 12)).pack(pady=20)

			load_data()


		def jadwal():
			jadwal_window = tk.Toplevel(admin_window)
			jadwal_window.title("Penjadwalan")
			jadwal_window.geometry("415x450")
			self.center_window(jadwal_window)
			jadwal_window.resizable(False, False)
			jadwal_window.grab_set()
			self.lock(jadwal_window)
   			
			
      
			tk.Label(jadwal_window, text="Penjadwalan", font=("Arial", 16)).pack()
			
			stasiun_frame = tk.Frame(jadwal_window)
			stasiun_frame.pack(pady=5)

			stasiun = Utils.get_stasiun()

			# Stasiun Awal
			awal_frame = tk.Frame(stasiun_frame)
			awal_frame.pack(side=tk.LEFT, padx=5)
			tk.Label(awal_frame, text="Stasiun Awal").pack()
			stasiun_nama = [f"{s['kode']} - {s['nama']}" for s in stasiun]
			stasiun_id = [s['id'] for s in stasiun]
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

			tk.Label(jadwal_window, text="Tanggal:").pack(pady=5)
			calendar = Calendar(jadwal_window, selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
			calendar.pack(pady=5)

			tk.Label(jadwal_window, text="Waktu:").pack(pady=5)
			time_frame = tk.Frame(jadwal_window)
			time_frame.pack(pady=5)
			hours = [f"{i:02d}" for i in range(24)]
			minutes = [f"{i:02d}" for i in range(0, 60, 5)]

			hour_var = tk.StringVar(time_frame)
			hour_spinbox = tk.Spinbox(time_frame, from_=0, to=23, textvariable=hour_var, width=8, format="%02.0f")
			hour_spinbox.pack(side=tk.LEFT, padx=5)

			minute_var = tk.StringVar(time_frame)
			minute_spinbox = tk.Spinbox(time_frame, values=minutes, textvariable=minute_var, width=8)
			minute_spinbox.pack(side=tk.LEFT, padx=5)
   
			second_var = tk.StringVar(time_frame)
			second_var.set("00")
   
			
			def confirm_schedule():
				stasiun_awal_id = stasiun_id[stasiun_nama.index(stasiun_awal_var.get())]
				stasiun_akhir_id = stasiun_id[stasiun_nama.index(stasiun_akhir_var.get())]
				selected_date = calendar.get_date()
				selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")
				selected_datetime = f"{selected_date} {hour_var.get()}:{minute_var.get()}:{second_var.get()}"
				if stasiun_awal_id == stasiun_akhir_id:
					messagebox.showerror("Error", "Stasiun awal dan stasiun akhir tidak boleh sama.")
					return
				# Add logic to handle the selected date and stations for scheduling
				
				if Utils.check_jadwal_duplicate(stasiun_awal_id, stasiun_akhir_id, selected_datetime):
					messagebox.showerror("Error", "Jadwal sudah ada.")
					return
				else:
					messagebox.showinfo("Jadwal Terpilih", f"Stasiun Awal: {stasiun_awal_var.get()}\nStasiun Akhir: {stasiun_akhir_var.get()}\nTanggal: {selected_datetime}")
					Utils.add_jadwal(stasiun_awal_id, stasiun_akhir_id, selected_datetime)
			
			tk.Button(jadwal_window, text="Confirm", command=confirm_schedule).pack(pady=10)
		
		def show_all_jadwal():
			jadwal_window = tk.Toplevel(admin_window) 
			jadwal_window.title("Jadwal Kereta")
			jadwal_window.geometry("310x500")
			self.center_window(jadwal_window)
			jadwal_window.resizable(False, False)
			jadwal_window.grab_set()

			tk.Label(jadwal_window, text="Jadwal Kereta", font=("Arial", 16)).pack()

			# Create a frame for the canvas and scrollbar
			frame = tk.Frame(jadwal_window)
			frame.pack(fill="both", expand=True)

			# Add a canvas in that frame
			canvas = tk.Canvas(frame)
			canvas.pack(side="left", fill="both", expand=True)

			# Add a scrollbar to the frame
			scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
			scrollbar.pack(side="right", fill="y")

			# Enable mouse wheel scrolling
			def on_mouse_wheel(event):
				canvas.yview_scroll(int(-1*(event.delta/120)), "units")

			canvas.bind_all("<MouseWheel>", on_mouse_wheel)

			# Configure the canvas
			canvas.configure(yscrollcommand=scrollbar.set)
			canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

			# Create another frame inside the canvas
			history_frame = tk.Frame(canvas)
			canvas.create_window((0, 0), window=history_frame, anchor="nw")

			history_data = Utils.get_list_jadwal()
			print(f"Jadwal data") 
			if history_data:
				for jadwal in history_data:
					jadwal_frame = tk.Frame(history_frame, bd=1, relief="solid")
					jadwal_frame.pack(fill="x", padx=10, pady=5)
					jadwal_info = (
						f"Stasiun Awal\t: {jadwal.get('s_awal').upper()} ({jadwal.get('kode_s_awal')})\n"
						f"Stasiun Akhir\t: {jadwal.get('s_akhir').upper()} ({jadwal.get('kode_s_akhir')})\n"
						f"Harga Ekonomi\t: Rp. {jadwal.get('harga_eko')}\n"
						f"Harga Bisnis\t: Rp. {jadwal.get('harga_bis')}\n"
						f"Harga Eksekutif\t: Rp. {jadwal.get('harga_eks')}\n"
						f"Berangkat\t: {jadwal.get('waktu')}\n"
					)
					tk.Label(jadwal_frame, text=jadwal_info, font=("Arial", 10), justify="left").pack(anchor="w", padx=10, pady=5)	
			else:
				tk.Label(history_frame, text=f"No Jadwal found.", font=("Arial", 12)).pack(pady=20)


   

		def history():
			history_window = tk.Toplevel(admin_window)
			history_window.title("History Pemesanan")
			history_window.geometry("415x450")
			self.center_window(history_window)
			history_window.resizable(False, False)
			history_window.grab_set()

			tk.Label(history_window, text="History Pemesanan", font=("Arial", 16)).pack()

			# Create a frame for the canvas and scrollbar
			frame = tk.Frame(history_window)
			frame.pack(fill="both", expand=True)

			# Add a canvas in that frame
			canvas = tk.Canvas(frame)
			canvas.pack(side="left", fill="both", expand=True)

			# Add a scrollbar to the frame
			scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
			scrollbar.pack(side="right", fill="y")

   			# Enable mouse wheel scrolling
			def on_mouse_wheel(event):
				canvas.yview_scroll(int(-1*(event.delta/120)), "units")

			canvas.bind_all("<MouseWheel>", on_mouse_wheel)
			# Configure the canvas
			canvas.configure(yscrollcommand=scrollbar.set)
			canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

			# Create another frame inside the canvas
			history_frame = tk.Frame(canvas)
			canvas.create_window((0, 0), window=history_frame, anchor="nw")

			history_data = Utils.history_admin()
			print(f"History data") 
			if history_data:
				for booking in history_data:
					booking_frame = tk.Frame(history_frame, bd=1, relief="solid")
					booking_frame.pack(fill="x", padx=10, pady=5)
					booking_info = (
						f"Kode Tiket\t: {booking.get('kode')}\n"
						f"Nama\t\t: {booking.get('nama')}\n"
						f"NIK\t\t: {booking.get('nik')}\n"
						f"Tujuan\t\t: {(booking.get('stasiun_awal').upper())} ({booking.get('kode_stasiun_awal')})  >>  {booking.get('stasiun_akhir').upper()} ({booking.get('kode_stasiun_akhir')})\n"
						f"Kursi\t\t: {booking.get('gerbong')} ({booking.get('kursi')})\n"
						f"Tarif\t\t: Rp. {booking.get('harga')}\n"
						f"Berangkat\t: {booking.get('waktu')}\n"
						f"Status\t\t: {'Approved' if booking.get('status') == 1 else 'Pending'}"
					)
					tk.Label(booking_frame, text=booking_info, font=("Arial", 10), justify="left").pack(anchor="w", padx=10, pady=5)	
			else:
				tk.Label(history_frame, text=f"No booking of user {user.nama} history found.", font=("Arial", 12)).pack(pady=20)

			
			

		button_frame = tk.Frame(admin_window)
		button_frame.pack(pady=10, )
		
		tk.Button(button_frame, text="Konfirmasi Tiket", font=("Arial", 15), command=acc_tiket).pack(side="top", padx=15, pady=10)
		tk.Button(button_frame, text="Tambah jadwal", font=("Arial", 15), command=jadwal).pack(side="top", padx=15, pady=10)
		tk.Button(button_frame, text="Jadwal", font=("Arial", 15), command=show_all_jadwal).pack(side="top", padx=15, pady=10)
		tk.Button(button_frame, text="History", font=("Arial", 15), command=history).pack(side="top", padx=15, pady=10)

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
		stasiun_id = [s['id'] for s in stasiun]
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
		calendar = Calendar(user_window, selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
		calendar.pack(pady=5)

		def confirm():
			# Lakukan sesuatu dengan data input
			stasiun_awal_id = stasiun_id[stasiun_nama.index(stasiun_awal_var.get())]
			stasiun_akhir_id = stasiun_id[stasiun_nama.index(stasiun_akhir_var.get())]
			selected_date = calendar.get_date()
			selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")
			if stasiun_awal_id == stasiun_akhir_id:
				messagebox.showerror("Error", "Stasiun awal dan stasiun akhir tidak boleh sama.")
				return
			jadwal = Utils.get_jadwal(stasiun_awal_id, stasiun_akhir_id, selected_date)
			if jadwal.jadwal_data:
				user_window.destroy()
				self.pilih_kursi(user, jadwal.jadwal_data)
			else:
				messagebox.showinfo("Info", "Tidak ada jadwal tersedia untuk rute dan tanggal yang dipilih.")

		tk.Button(user_window, text="Confirm", command=confirm).pack(pady=15)

		def show_history():
			history_window = tk.Toplevel(user_window)
			history_window.title("History Pemesanan")
			history_window.geometry("450x400")
			self.center_window(history_window)
			history_window.resizable(False, False)
			history_window.grab_set()

			tk.Label(history_window, text="History Pemesanan", font=("Arial", 16)).pack()

			# Create a frame for the canvas and scrollbar
			frame = tk.Frame(history_window)
			frame.pack(fill="both", expand=True)
			
			# Add a canvas in that frame
			canvas = tk.Canvas(frame)
			canvas.pack(side="left", fill="both", expand=True)

			# Add a scrollbar to the frame
			scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
			scrollbar.pack(side="right", fill="y")

			# Enable mouse wheel scrolling
			def on_mouse_wheel(event):
				canvas.yview_scroll(int(-1*(event.delta/120)), "units")

			canvas.bind_all("<MouseWheel>", on_mouse_wheel)

			# Configure the canvas
			canvas.configure(yscrollcommand=scrollbar.set)
			canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

			# Create another frame inside the canvas
			history_frame = tk.Frame(canvas)
			canvas.create_window((0, 0), window=history_frame, anchor="nw")

			history_data = Utils.history_pesanan(user.id)
			print(f"History data for user_id {user.id}")
			if history_data:
				for booking in history_data:
					booking_frame = tk.Frame(history_frame, bd=1, relief="solid")
					booking_frame.pack(fill="x", padx=10, pady=5)
					booking_info = (
						f"Kode Tiket\t: {booking.get('kode')}\n"
						f"Nama\t\t: {booking.get('nama')}\n"
						f"NIK\t\t: {booking.get('nik')}\n"
						f"Tujuan\t\t: {(booking.get('stasiun_awal').upper())} ({booking.get('kode_stasiun_awal')})  >>  {booking.get('stasiun_akhir').upper()} ({booking.get('kode_stasiun_akhir')})\n"
						f"Kursi\t\t: {booking.get('gerbong')} ({booking.get('kursi')})\n"
						f"Tarif\t\t: Rp. {booking.get('harga')}\n"
						f"Berangkat\t: {booking.get('waktu')}\n"
						f"Status\t\t: {'Approved' if booking.get('status') == 1 else 'Pending'}"
					)
					tk.Label(booking_frame, text=booking_info, font=("Arial", 10), justify="left").pack(anchor="w", padx=10, pady=5)	
			else:
				tk.Label(history_frame, text=f"No booking of user {user.nama} history found.", font=("Arial", 12)).pack(pady=20)

			 
		tk.Button(user_window, text="History", command=show_history).pack(side="left", padx=10, pady=5)

		tk.Button(user_window, text="Log Out", command=user_window.destroy).pack(side="right", padx=10, pady=5)

	def pilih_kursi(self, user, jadwal):
		waktu_tempuh_window = tk.Tk()
		waktu_tempuh_window.title("Waktu Tempuh")
		waktu_tempuh_window.geometry("300x200")
		self.center_window(waktu_tempuh_window)
		waktu_tempuh_window.resizable(False, False)

		coach_list = ["EKS-1", "EKS-2", 
					"BIS-1", "BIS-2", "BIS-3", 
					"EKO-1", "EKO-2", "EKO-3", "EKO-4"]

		# Function to display the seat selection window
		def show_seat_selection(selected_time, coach = 0):
			seat_window = tk.Tk()
			seat_window.title("Kursi yang Ditempati")
			seat_window.geometry("350x700")
			self.center_window(seat_window)
			seat_window.resizable(False, False)

			tk.Label(seat_window, text="Pilihan Gerbong:").pack(pady=5)
			selected_coach = tk.StringVar(seat_window)
			selected_coach.set(coach_list[coach])

			def on_coach_change(*args):
				seat_window.destroy()
				show_seat_selection(selected_time, coach_list.index(selected_coach.get()))

			selected_coach.trace_add("write", on_coach_change)

			coach_menu = tk.OptionMenu(seat_window, selected_coach, *coach_list)
			coach_menu.pack(pady=10)

			# Seat layout label
			tk.Label(seat_window, text="Pilih Kursi:").pack(pady=5)

			# Frame for seat buttons
			seat_frame = tk.Frame(seat_window)
			seat_frame.pack(pady=5)

			rows = 16 
			columns = ["A", "B", "C", "D"]
			selected_seat = tk.StringVar()
			id_jadwal = next(item['id'] for item in jadwal if item['waktu'] == selected_time)
			kursi = Utils.cari_kursi(id_jadwal, coach_list[coach])

			def select_seat(row, col):
				selected_seat.set(f"{col}{row}")
				payment_method()

			for row in range(1, rows + 1):
				for col in columns:
					seat_text = f"{col}{row}"
					if seat_text in kursi:
						seat_button = tk.Button(seat_frame, text=seat_text, width=4, state=tk.DISABLED)
					else:
						seat_button = tk.Button(seat_frame, text=seat_text, width=4, command=lambda r=row, c=col: select_seat(r, c))
					col_index = columns.index(col)
					if col == "B":
						seat_button.grid(row=row-1, column=col_index, padx=(2, 40), pady=2)  # Add extra space after column C
					else:
						seat_button.grid(row=row-1, column=col_index, padx=2, pady=2)

			def payment_method():
				payment_window = tk.Toplevel(seat_window)
				payment_window.title(coach_list[coach] + " " + selected_seat.get() + " — Metode Pembayaran")
				payment_window.geometry("300x150")
				self.center_window(payment_window)
				payment_window.resizable(False, False)
				self.lock(payment_window)

				tk.Label(payment_window, text=coach_list[coach] + " " + selected_seat.get() + "\nPilih Metode Pembayaran", font=("Arial", 14)).pack(pady=20)

				button_frame = tk.Frame(payment_window)
				button_frame.pack(pady=10)

				counter_button = tk.Button(button_frame, text="Counter", width=15, height=2, command=confirm_counter)
				counter_button.pack(side="left", padx=10)

				instant_button = tk.Button(button_frame, text="Instant", width=15, height=2, command=confirm_instant)
				instant_button.pack(side="right", padx=10)

			def confirm_counter():
				confirm_selection('counter')
			
			def confirm_instant():
				confirm_selection('instant')

			# Confirm and Cancel buttons
			def confirm_selection(condition):
				selected_coach_value = selected_coach.get()
				selected_seat_value = selected_seat.get()
				messagebox.showinfo("Konfirmasi", f"Gerbong: {selected_coach_value}, Kursi: {selected_seat_value}, Waktu: {selected_time}")
				id_user = user.id
				if condition == "counter":
					kode = Utils.add_pesanan(id_user, id_jadwal, selected_coach_value, selected_seat_value, 0)
					messagebox.showinfo("Pemesanan", f"Pemesanan berhasil dengan kode {kode}!\nSilakan bayar di konter terdekat.")
				else:
					kode = Utils.add_pesanan(id_user, id_jadwal, selected_coach_value, selected_seat_value, 1)
					messagebox.showinfo("Pemesanan", f"Pemesanan dan pembayaran berhasil dengan kode {kode}!")
				seat_window.destroy()
				self.show_user_menu(user)

			def cancel_selection():
				seat_window.destroy()

			tk.Button(seat_window, text="Cancel", command=cancel_selection).pack(side="left", pady=10, padx=10)
			# tk.Button(seat_window, text="Confirm", command=confirm_selection).pack(side="right", pady=10, padx=10)

		# Sample function to show travel time selection menu
		def show_waktu_tempuh_menu():
			tk.Label(waktu_tempuh_window, text="Waktu Perjalanan", font=("Arial", 16)).pack(pady=20)

			# List of available times
			waktu_tempuh_list = [item['waktu'] for item in jadwal]

			selected_waktu = tk.StringVar(waktu_tempuh_window)
			selected_waktu.set(waktu_tempuh_list[0])  # default value

			waktu_tempuh_menu = tk.OptionMenu(waktu_tempuh_window, selected_waktu, *waktu_tempuh_list)
			waktu_tempuh_menu.pack(pady=10)

			def confirm_waktu_tempuh():
				chosen_waktu = selected_waktu.get()
				id_jadwal = next(item['id'] for item in jadwal if item['waktu'] == chosen_waktu)
				if Utils.cek_jadwal(user.id, id_jadwal):
					messagebox.showerror("Error", "Anda sudah memesan pada jadwal ini!")
					waktu_tempuh_window.destroy()
					return self.show_user_menu(user)
				waktu_tempuh_window.destroy()  # Close time selection window
				show_seat_selection(chosen_waktu)  # Open seat selection with chosen time

			tk.Button(waktu_tempuh_window, text="Confirm", command=confirm_waktu_tempuh).pack(pady=10)
		
		show_waktu_tempuh_menu()