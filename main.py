import sqlite3
import os
import platform
from datetime import datetime

kosongkanCmd = lambda: os.system('cls')
login = []

class Database:
	def __init__(self):
		self.mydb = sqlite3.connect("sewaMotor.db")
		self.mycursor = self.mydb.cursor()

class KumpulanQuery(Database):
	def __init__(self, query=None, isi=None):
		Database.__init__(self)
		self.query = query
		self.isi = isi

	def masukkanData(self):
		self.mycursor.executemany(self.query, self.isi)
		self.mydb.commit()

	def ambilSemuaData(self):
		self.mycursor.execute(self.query)
		return self.mycursor.fetchall()

	def ambilSemuaDataSpesifik(self):
		self.mycursor.execute(self.query, self.isi)
		return self.mycursor.fetchall()

	def ambilSatuData(self):
		self.mycursor.execute(self.query, self.isi)
		return self.mycursor.fetchone()

	def ubahData(self):
		self.mycursor.execute(self.query, self.isi)
		self.mydb.commit()

	def hapusData(self):
		self.mycursor.execute(self.query, self.isi)
		self.mydb.commit()

class Akun(KumpulanQuery):
	def __init__(self, query=None, isi=None):
		KumpulanQuery.__init__(self, query, isi)

	def prosesLogin(self, username, password):
		self.query = "SELECT id_akun, username, nama_user, hak_akses FROM tb_akun WHERE username = ? AND password = ?"
		self.isi = (username, password)

		hasil = self.ambilSatuData()

		kosongkanCmd()

		if(hasil):
			login.append(hasil)
		else:
			print("Username atau password salah")

		return hasil

	def registrasi(self, data):
		self.query = "INSERT INTO tb_akun (username, password, nama_user, no_ktp, alamat, hak_akses) VALUES (?, ?, ?, ?, ?, ?)"
		self.isi = data

		self.masukkanData()
		print("Berhasil mendaftar. Silahkan login kembali")

class Merk(KumpulanQuery):
	def __init__(self, query=None, isi=None):
		KumpulanQuery.__init__(self, query, isi)

	def inputMerk(self, data):
		self.query = "INSERT INTO tb_merk (nama_merk) VALUES (?)"
		self.isi = data

		self.masukkanData()
		print("Data berhasil diinput")

	def ambilMerk(self):
		self.query = "SELECT * FROM tb_merk"
		hasil = self.ambilSemuaData()

		if(hasil):
			print("=== List Merk ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]})")
		else:
			print("=== List Merk ===")
			print("Tidak ada data di database")

		return hasil

	def ambilSatuMerk(self, inputan):
		self.query = "SELECT * FROM tb_merk where id_merk = ?"
		self.isi = (inputan,)

		return self.ambilSatuData()

	def ubahMerk(self, inputan):
		self.query = "UPDATE tb_merk SET nama_merk = ? WHERE id_merk = ?"
		self.isi = inputan

		self.ubahData()
		print("Berhasil mengubah data")

	def hapusMerk(self, inputan):
		self.query = "DELETE FROM tb_merk WHERE id_merk = ?"
		self.isi = (inputan,)

		self.hapusData()
		print("Berhasil menghapus data")

class Jenis(KumpulanQuery):
	def __init__(self, query=None, isi=None):
		KumpulanQuery.__init__(self, query, isi)

	def inputJenis(self, data):
		self.query = "INSERT INTO tb_jenismotor (nama_jenis) VALUES (?)"
		self.isi = data

		self.masukkanData()
		print("Data berhasil diinput")

	def ambilJenis(self):
		self.query = "SELECT * FROM tb_jenismotor"
		hasil = self.ambilSemuaData()

		if(hasil):
			print("=== List Jenis ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]})")
		else:
			print("=== List Merk ===")
			print("Tidak ada data di database")

		return hasil

	def ambilSatuJenis(self, inputan):
		self.query = "SELECT * FROM tb_jenismotor where id_jenis = ?"
		self.isi = (inputan,)

		return self.ambilSatuData()

	def ubahJenis(self, inputan):
		self.query = "UPDATE tb_jenismotor SET nama_jenis = ? WHERE id_jenis = ?"
		self.isi = inputan

		self.ubahData()
		print("Berhasil mengubah data")

	def hapusJenis(self, inputan):
		self.query = "DELETE FROM tb_jenismotor WHERE id_jenis = ?"
		self.isi = (inputan,)

		self.hapusData()
		print("Berhasil menghapus data")

class Motor(KumpulanQuery):
	def __init__(self, query=None, isi=None):
		KumpulanQuery.__init__(self, query, isi)

	def inputMotor(self, data):
		self.query = "INSERT INTO tb_motor (id_merk, id_jenis, nama_motor) VALUES (?, ?, ?)"
		self.isi = data

		self.masukkanData()
		print("Data berhasil diinput")

	def ambilMotor(self):
		self.query = "SELECT a.id_motor, b.nama_merk, c.nama_jenis, a.nama_motor FROM tb_motor a INNER JOIN tb_merk b using(id_merk) INNER JOIN tb_jenismotor c using(id_jenis)"
		hasil = self.ambilSemuaData()

		if(hasil):
			print("=== List Motor ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][3]} (ID: {hasil[x][0]} | Merk: {hasil[x][1]} | Jenis: {hasil[x][2]})")
		else:
			print("=== List Motor ===")
			print("Tidak ada data di database")

		return hasil

	def ambilSatuMotor(self, inputan):
		self.query = "SELECT * FROM tb_motor WHERE id_motor = ?"
		self.isi = (inputan,)

		return self.ambilSatuData()

	def ubahMotor(self, inputan):
		self.query = "UPDATE tb_motor SET id_merk = ?, id_jenis = ?, nama_motor = ? WHERE id_motor = ?"
		self.isi = inputan

		self.ubahData()
		print("Berhasil mengubah data")

	def hapusMotor(self, inputan):
		self.query = "DELETE FROM tb_motor WHERE id_jenis = ?"
		self.isi = (inputan,)

		self.hapusData()
		print("Berhasil menghapus data")

class Transaksi(KumpulanQuery):
	def __init__(self, query=None, isi=None):
		KumpulanQuery.__init__(self, query, isi)

	def inputTransaksi(self, data):
		self.query = "INSERT INTO tb_transaksi (id_motor, id_akun, tanggal_sewa) VALUES (?, ?, ?)"
		self.isi = data

		self.masukkanData()
		print("Kamu telah menyewa motor. Silahkan cek transaksi saya untuk melihat riwayat")

	def ambilTransaksiUser(self, inputan):
		self.query = "SELECT a.id_transaksi, b.nama_motor, a.tanggal_sewa FROM tb_transaksi a INNER JOIN tb_motor b using(id_motor) WHERE a.id_akun = ?"
		self.isi = (inputan,)
		hasil = self.ambilSemuaDataSpesifik()

		if(hasil):
			print("=== List Transaksi ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]} | tanggal Sewa: {hasil[x][2]})")
		else:
			print("=== List Transaksi ===")
			print("Tidak ada data di database")

		return hasil

	def ambilTransaksi(self):
		self.query = "SELECT a.id_transaksi, b.nama_motor, c.nama_user, a.tanggal_sewa FROM tb_transaksi a INNER JOIN tb_motor b using(id_motor) INNER JOIN tb_akun c using(id_akun)"
		hasil = self.ambilSemuaData()

		if(hasil):
			print("=== List Transaksi ===")

			for x in range(0, len(hasil)):
				print(f"{x+1}. {hasil[x][1]} (ID: {hasil[x][0]} | Nama Penyewa: {hasil[x][2]} | tanggal Sewa: {hasil[x][3]})")
		else:
			print("=== List Transaksi ===")
			print("Tidak ada data di database")

		return hasil

def merkMotor():
	print("==========")
	print("Merk Motor")
	print("==========")
	print("1. Tambah Merk\n2. Tampilkan Merk\n3. Ubah Merk\n4. Hapus Merk")
	menu = int(input("Pilih Menu: "))

	kosongkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak merk: "))

		for x in range(0, banyak_data):
			print(f"===== Merk {x+1} =====")
			nama_jenis = input("Input nama merk: ")

			data.append((nama_jenis,))

		kosongkanCmd()
		Merk().inputMerk(data)
	elif(menu == 2):
		Merk().ambilMerk()
	elif(menu == 3):
		cek_data = Merk().ambilMerk()

		if(cek_data):
			inputan = int(input("Masukkan id merk yang diedit: "))
			data_ada = Merk().ambilSatuMerk(inputan)

			if(data_ada):
				nama_jenis = input("Input nama merk: ")

				data = (nama_jenis, inputan)

				kosongkanCmd()
				Merk().ubahMerk(data)
			else:
				kosongkanCmd()
				print(f"Merk dengan ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Merk().ambilMerk()

		if(cek_data):
			inputan = int(input("Masukkan id merk: "))
			data_ada = Merk().ambilSatuMerk(inputan)

			if(data_ada):
				kosongkanCmd()
				Merk().hapusMerk(inputan)
			else:
				kosongkanCmd()
				print(f"Merk dengan ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def jenisMotor():
	print("==========")
	print("Jenis Motor")
	print("==========")
	print("1. Tambah Jenis\n2. Tampilkan Jenis\n3. Ubah Jenis\n4. Hapus Jenis")
	menu = int(input("Pilih Menu: "))

	kosongkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak jenis: "))

		for x in range(0, banyak_data):
			print(f"===== Merk {x+1} =====")
			nama_merk = input("Input nama jenis motor: ")

			data.append((nama_merk,))

		kosongkanCmd()
		Jenis().inputJenis(data)
	elif(menu == 2):
		Jenis().ambilJenis()
	elif(menu == 3):
		cek_data = Jenis().ambilJenis()

		if(cek_data):
			inputan = int(input("Masukkan id jenis yang diedit: "))
			data_ada = Jenis().ambilSatuJenis(inputan)

			if(data_ada):
				nama_merk = input("Input nama jenis: ")

				data = (nama_merk, inputan)

				kosongkanCmd()
				Jenis().ubahJenis(data)
			else:
				kosongkanCmd()
				print(f"Jenis dengan ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Jenis().ambilJenis()

		if(cek_data):
			inputan = int(input("Masukkan id jenis: "))
			data_ada = Jenis().ambilSatuJenis(inputan)

			if(data_ada):
				kosongkanCmd()
				Jenis().hapusJenis(inputan)
			else:
				kosongkanCmd()
				print(f"Jenis dengan ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def motor():
	print("==========")
	print("Nama Motor")
	print("==========")
	print("1. Tambah Motor\n2. Tampilkan Motor\n3. Ubah Motor\n4. Hapus Motor")
	menu = int(input("Pilih Menu: "))

	kosongkanCmd()

	if(menu == 1):
		data = []
		banyak_data = int(input("Masukkan banyak motor: "))

		Merk().ambilMerk()
		Jenis().ambilJenis()
		Motor().ambilMotor()

		for x in range(0, banyak_data):
			print(f"===== Merk {x+1} =====")
			id_merk = input("Input id merk: ")
			id_jenis = input("Input id jenis: ")
			nama_motor = input("Input nama motor: ")

			data.append((id_merk, id_jenis, nama_motor))

		kosongkanCmd()
		Motor().inputMotor(data)
	elif(menu == 2):
		Motor().ambilMotor()
	elif(menu == 3):
		cek_data = Motor().ambilMotor()

		if(cek_data):
			inputan = int(input("Masukkan id motor yang diedit: "))
			data_ada = Motor().ambilSatuMotor(inputan)
			
			Merk().ambilMerk()
			Jenis().ambilJenis()

			if(data_ada):
				id_merk = input("Input id merk: ")
				id_jenis = input("Input id jenis: ")
				nama_motor = input("Input nama motor: ")

				data = (id_merk, id_jenis, nama_motor, inputan)

				kosongkanCmd()
				Motor().ubahMotor(data)
			else:
				kosongkanCmd()
				print(f"Motor dengan ID {inputan} tidak ada.")
		else:
			pass
	elif(menu == 4):
		cek_data = Motor().ambilMotor()

		if(cek_data):
			inputan = int(input("Masukkan id motor: "))
			data_ada = Motor().ambilSatuMotor(inputan)

			if(data_ada):
				kosongkanCmd()
				Motor().hapusMotor(inputan)
			else:
				kosongkanCmd()
				print(f"Motor dengan ID {inputan} tidak ada.")
		else:
			pass
	else:
		pass

def sewaMotor():
	hasil = Motor().ambilMotor()
	
	if(hasil):
		data = []

		id_motor = int(input("Pilih id motor yang ingin disewa: "))
		id_akun = login[0][0]
		tanggal_sewa = datetime.today().strftime('%Y-%m-%d')

		data.append((id_motor, id_akun, tanggal_sewa))

		kosongkanCmd()
		Transaksi().inputTransaksi(data)
	else:
		kosongkanCmd()
		print("Tidak ada motor yang tersedia")

while True:
	if(len(login) == 0):
		print("===========================")
		print("Selamat Datang di Sewa Aja")
		print("===========================")
		print("1. Login")
		print("2. Register Akun")
		menu = int(input("Pilih menu: "))

		kosongkanCmd()

		if(menu == 1):
			username = input("Input username: ")
			password = input("Input password: ")

			kosongkanCmd()
			Akun().prosesLogin(username, password)
		elif(menu == 2):
			username = input("Input username: ")
			password = input("Input password: ")
			nama_user = input("Input nama user: ")
			no_ktp = input("Input No KTP: ")
			alamat = input("Input alamat: ")
			hak_akses = "0"

			data = [(username, password, nama_user, no_ktp, alamat, hak_akses)]

			kosongkanCmd()
			Akun().registrasi(data)
		else:
			print("Kamu disini dulu")
			exit()
	else:
		if(login[0][3] == "1"):
			print("==========")
			print("Menu Admin")
			print("==========")
			print("1. Manajemen Merk Motor")
			print("2. Manajemen Jenis Motor")
			print("3. Manajemen Motor")
			print("4. Riwayat Transaksi (Keseluruhan)")
			print("5. Logout")
			menu = int(input("Pilih menu: "))

			kosongkanCmd()

			if(menu == 1):
				merkMotor()
			elif(menu == 2):
				jenisMotor()
			elif(menu == 3):
				motor()
			elif(menu == 4):
				Transaksi().ambilTransaksi()
			elif(menu == 5):
				login = []

				kosongkanCmd()
				print("Berhasil logout")
			else:
				print("Kamu disini dulu")
				exit()
		else:
			print("=========")
			print("Menu User")
			print("=========")
			print("1. Sewa Motor")
			print("2. Transaksi Saya")
			print("3. Logout")
			menu = int(input("Pilih menu: "))

			kosongkanCmd()

			if(menu == 1):
				sewaMotor()
			elif(menu == 2):
				Transaksi().ambilTransaksiUser(login[0][0])
			elif(menu == 3):
				login = []

				kosongkanCmd()
				print("Berhasil logout")
			else:
				print("Kamu disini dulu")
				exit()