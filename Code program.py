import os
import time
import pwinput
from prettytable import PrettyTable

# Data (Dictionary) 

#  Nested dictionary akun: username -> password dan role
akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "mahasiswa": {"password": "mhs123", "role": "user"}
}

# nested dictionary jadwal: id -> data jadwal
jadwal = {
    "1": {"matkul": "Konsep Sistem Informasi", "hari": "Senin", "jam": "07:30", "ruang": "C402"},
    "2": {"matkul": "Pendidikan Agama Islam", "hari": "Kamis", "jam": "09:10", "ruang": "C403"}
}

daftar_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]


# Function Bantu

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def input_tidak_kosong(pesan):
    # mengembalikan teks yang tidak kosong
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Data tidak boleh kosong")
        else:
            return teks


def input_hari():
    while True:
        hari = input("Hari: ").strip().capitalize()
        if hari in daftar_hari:
            return hari
        else:
            print("Hari tidak valid (Senin - Jumat)")


def cek_jam(jam):
    # True jika format jam benar (HH:MM), False jika salah
    if len(jam) != 5 or jam[2] != ":":
        return False
    try:
        jam_int = int(jam[0:2])
        menit_int = int(jam[3:5])
    except ValueError:
        return False
    return jam_int >= 0 and jam_int <= 23 and menit_int >= 0 and menit_int <= 59


def input_jam():
    while True:
        jam = input("Jam (contoh 07:30): ").strip()
        if cek_jam(jam):
            return jam
        else:
            print("Format jam salah, gunakan HH:MM")


def buat_id_baru(data):
    # id baru = id terbesar + 1
    if len(data) == 0:
        return "1"
    return str(max(int(kunci) for kunci in data) + 1)


# Function Crud

def tampilkan_jadwal(data, judul="Daftar Jadwal"):
    print(judul)

    if len(data) == 0:
        print("Belum ada jadwal")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Mata Kuliah", "Hari", "Jam", "Ruang"]
    for id_jadwal in data:
        isi = data[id_jadwal]
        tabel.add_row([id_jadwal, isi["matkul"], isi["hari"], isi["jam"], isi["ruang"]])
    print(tabel)


def tambah_jadwal(data):
    print("Tambah Jadwal")

    matkul = input_tidak_kosong("Mata kuliah: ")
    hari = input_hari()
    jam = input_jam()
    ruang = input_tidak_kosong("Ruang: ")

    id_baru = buat_id_baru(data)
    data[id_baru] = {"matkul": matkul, "hari": hari, "jam": jam, "ruang": ruang}
    print("Jadwal berhasil ditambahkan")


def ubah_jadwal(data):
    print("Ubah Jadwal")

    if len(data) == 0:
        print("Belum ada jadwal")
        return

    tampilkan_jadwal(data)
    id_jadwal = input("Masukkan ID jadwal: ")

    if id_jadwal in data:
        data[id_jadwal]["matkul"] = input_tidak_kosong("Mata kuliah baru: ")
        data[id_jadwal]["hari"] = input_hari()
        data[id_jadwal]["jam"] = input_jam()
        data[id_jadwal]["ruang"] = input_tidak_kosong("Ruang baru: ")
        print("Jadwal berhasil diubah")
    else:
        print("ID jadwal tidak tersedia")


def hapus_jadwal(data):
    print("Hapus Jadwal")

    if len(data) == 0:
        print("Belum ada jadwal")
        return

    tampilkan_jadwal(data)
    id_jadwal = input("Masukkan ID jadwal: ")

    if id_jadwal in data:
        yakin = input("Yakin ingin menghapus? (y/n): ").lower()
        if yakin == "y":
            data.pop(id_jadwal)
            print("Jadwal berhasil dihapus")
        else:
            print("Penghapusan dibatalkan")
    else:
        print("ID jadwal tidak tersedia")


def cari_jadwal(data):
    print("Cari Jadwal Berdasarkan Hari")
    hari = input_hari()

    hasil = {}
    for id_jadwal in data:
        if data[id_jadwal]["hari"] == hari:
            hasil[id_jadwal] = data[id_jadwal]

    if len(hasil) == 0:
        print("Tidak ada jadwal pada hari", hari)
    else:
        tampilkan_jadwal(hasil, "Jadwal Hari " + hari)


# Login

def login(data_akun):
    # mengembalikan username dan role jika berhasil, None jika gagal
    kesempatan = 3

    while kesempatan > 0:
        print("LOGIN")
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password: ")

        if username in data_akun and data_akun[username]["password"] == password:
            print("Login berhasil, selamat datang", username)
            time.sleep(1)
            return username, data_akun[username]["role"]
        else:
            kesempatan -= 1
            print("Username atau password salah, sisa kesempatan:", kesempatan)

    return None, None


# Menu

def menu_admin(username):
    while True:
        bersihkan_layar()
        print("PROGRAM JADWAL KULIAH - ADMIN (" + username + ")")
        print("1. Tambah Jadwal")
        print("2. Tampilkan Jadwal")
        print("3. Ubah Jadwal")
        print("4. Hapus Jadwal")
        print("5. Cari Jadwal per Hari")
        print("6. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_jadwal(jadwal)
        elif pilihan == "2":
            tampilkan_jadwal(jadwal)
        elif pilihan == "3":
            ubah_jadwal(jadwal)
        elif pilihan == "4":
            hapus_jadwal(jadwal)
        elif pilihan == "5":
            cari_jadwal(jadwal)
        elif pilihan == "6":
            print("Logout berhasil")
            time.sleep(1)
            break
        else:
            print("Pilihan menu tidak tersedia")

        input("\nTekan Enter untuk lanjut...")


def menu_user(username):
    while True:
        bersihkan_layar()
        print("PROGRAM JADWAL KULIAH - USER (" + username + ")")
        print("1. Tampilkan Jadwal")
        print("2. Cari Jadwal per Hari")
        print("3. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_jadwal(jadwal)
        elif pilihan == "2":
            cari_jadwal(jadwal)
        elif pilihan == "3":
            print("Logout berhasil")
            time.sleep(1)
            break
        else:
            print("Pilihan menu tidak tersedia")

        input("\nTekan Enter untuk lanjut...")


# Program Utama

while True:
    bersihkan_layar()
    print("PROGRAM JADWAL KULIAH")
    print("1. Login")
    print("2. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        username, role = login(akun)

        if username is None:
            print("Kesempatan login habis")
            input("\nTekan Enter untuk lanjut...")
        elif role == "admin":
            menu_admin(username)
        else:
            menu_user(username)
    elif pilihan == "2":
        print("Program selesai")
        break
    else:
        print("Pilihan menu tidak tersedia")
        input("\nTekan Enter untuk lanjut...")
