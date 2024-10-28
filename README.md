![](https://raw.githubusercontent.com/asyary/github-stats/master/generated/overview.svg#gh-dark-mode-only)
![](https://raw.githubusercontent.com/asyary/github-stats/master/generated/languages.svg#gh-dark-mode-only)

# I have (no) idea what to do =

## Register
* username 
* password 
* (optional) no telp for forgor password auth
* (optional) email?
* NIK?

## Log in
* username (/email?)
* password

## Pesan tiket :
* destinasi A 
* destinas ke B (opsi pulang pergi)
* tanggal berangkat
* tanggal pulang (jika pulang pergi)
  * tampilan kereta yg tersedia
    * pilihan kelas
    * kursi?

## Pembayaran 2 opsi :
* kode pembayaran va
* pembayaran di loket

## Cetak/info tiket 
identitas, jadwal kereta (, no. kursi?)

## ADMIN 
* Acc pembayaran
* add/del kereta
* add/del User

## DATA MANAGE :
* User and Admin
* Train (jadwal, kapasitas?)

## Optional : 
* Log pesanan?
* Reset password
* Edit profile

# Seberapa jauh fungsionalitasnya 🗿?
### File handling kereta

Ini seberapa kompleks? apkh harus ada sampai opsi kursi dan ada validasi ketika kursi sudah dipesan maka tidak bisa diorder oleh orang lain? (artinya ada counter kapasitas juga) 
kalo bisa ya opsi pilihan kursi dan kalo kursi dah ada yang milih ya nggaj bisa di order

seberapa banyak destinasinya? kalo ini semakin banyak jadi data yang harus input dan simpan jadi banyak juga.
sejatim? atau ambil aja beberapa kota jatim sama beberapa stasiunnya


# flow program yg kuperkirakan

### (Asumsi: User sudah login)

1. **Tiket Pemesanan**
   - Pilih stasiun **berangkat**
   - Pilih stasiun **tujuan**
   - Cari stasiun berangkat dan tujuan. Jika ditemukan, lanjutkan ke langkah berikutnya.
   
2. **Pilih Hari Keberangkatan**
   - Pilih hari keberangkatan
   - Cari seluruh kereta yang memiliki stasiun berangkat dan tujuan yang sama. Jika ditemukan, lanjutkan ke langkah berikutnya.

3. **Tampilkan Jadwal dan Kode Kereta**
   - Tampilkan jadwal kereta yang tersedia beserta kode keretanya
   - User memasukkan kode kereta yang ingin dipilih.

4. **Pilih Kelas**
   - Tampilkan kelas yang tersedia (misalnya: Ekonomi, Bisnis, Eksekutif) beserta harga tiketnya
   - User memilih kelas yang diinginkan.

5. **Pilih Kursi**
   - Tampilkan kursi yang tersedia untuk kelas yang dipilih
   - Kursi yang telah dibooking oleh user lain tidak dapat dipilih.
   - Simpan data kursi yang dipilih.

6. **Kode Pembayaran**
   - Tampilkan kode pembayaran yang harus digunakan oleh user untuk menyelesaikan pembayaran.

7. **Konfirmasi Pembayaran oleh Admin**
   - Admin mengonfirmasi pembayaran user.

8. **Tiket Diterbitkan**
   - Setelah pembayaran dikonfirmasi, tiket dicetak dan disimpan dalam sistem.

---

### Tips dan Catatan Tambahan:
- Kursi yang telah dibooking harus disimpan di database sehingga tidak dapat dibooking oleh user lain.
- Pastikan setiap langkah memiliki validasi data, seperti validasi stasiun, jadwal, kelas, dan pembayaran.
- Pertimbangkan juga sistem penyimpanan database untuk setiap entitas (stasiun, kereta, kursi, tiket) untuk mempermudah manajemen data.

? database pake apa? file handling? ada sqlite3 sih di python cuma kurang tau cara kerjanya