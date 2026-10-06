# Program Jadwal Kuliah

# Nama : Deka Rizky Fauzan

# Nim  : 2609116052

# Kelas : B

## Deskripsi Program

Program **Jadwal Kuliah** merupakan aplikasi berbasis **Python Command Line Interface (CLI)** yang digunakan untuk mengelola data jadwal perkuliahan.

Program memiliki sistem **login dan role**, yaitu:

* **Admin**: dapat menambah, melihat, mengubah, menghapus, dan mencari jadwal kuliah.
* **User/Mahasiswa**: hanya dapat melihat dan mencari jadwal kuliah.

Program menggunakan struktur data **Dictionary dan Nested Dictionary** untuk menyimpan data akun dan jadwal. Program juga menggunakan beberapa library Python, yaitu os, time, pwinput, dan prettytable.

---

## 1. Import Library

<img width="350" height="91" alt="image" src="https://github.com/user-attachments/assets/9b821a87-140b-4932-b066-c6c12defc9ef" />

### Penjelasan

Bagian ini digunakan untuk mengimpor library yang diperlukan oleh program.

* os digunakan untuk membersihkan tampilan layar terminal.
* time digunakan untuk memberikan jeda waktu pada program.
* pwinput digunakan untuk menerima input password agar karakter password tidak ditampilkan secara langsung.
* PrettyTable digunakan untuk menampilkan data jadwal dalam bentuk tabel yang lebih rapi.

---

# 2. Data Akun

<img width="553" height="101" alt="image" src="https://github.com/user-attachments/assets/0f2752f9-eb37-4178-84e0-f73973c1c4ac" />


### Penjelasan

Variabel `akun` merupakan **nested dictionary** yang digunakan untuk menyimpan informasi akun pengguna.

Setiap akun memiliki:

* username
* password
* role

Terdapat dua akun yang tersedia:

Username = admin, mahasiswa

Password = admin123, mhs123

Role     = admin, user

Role digunakan untuk menentukan menu yang dapat diakses oleh pengguna setelah berhasil login.

---

# 3. Data Jadwal

<img width="952" height="97" alt="image" src="https://github.com/user-attachments/assets/3fff4165-0ec3-48f7-a46d-7a1a814fe68a" />


### Penjelasan

Variabel `jadwal` merupakan **nested dictionary** yang digunakan untuk menyimpan data jadwal kuliah.

Setiap jadwal memiliki beberapa informasi:

* id → identitas jadwal.
* matkul → nama mata kuliah.
* hari → hari perkuliahan.
* jam → waktu perkuliahan.
* ruang → ruangan perkuliahan.

Contoh data awal

Mata kuliah = Konsep sistem informasi

Hari       = senin

Jam        = 07.30

Ruang      = C402

Mata kuliah = Pendidikan agam islam

Hari        = Kamis

Jam         = 09.10

Ruang       = C403

Data jadwal inilah yang nantinya dapat dikelola oleh admin dan dilihat oleh user.

---

# 4. Daftar Hari

<img width="588" height="32" alt="image" src="https://github.com/user-attachments/assets/baddb3f0-6a7a-43d3-930a-2724f3f47993" />

### Penjelasan

Variabel `daftar_hari` berisi daftar hari yang diperbolehkan dalam program.

Data ini digunakan ketika pengguna memasukkan hari pada saat:

* Menambahkan jadwal.
* Mengubah jadwal.
* Mencari jadwal.

Dengan adanya daftar ini, program dapat melakukan validasi agar pengguna tidak memasukkan nama hari yang tidak sesuai.

---

# 5. Fungsi bersihkan_layar()

<img width="513" height="61" alt="image" src="https://github.com/user-attachments/assets/fe135a8b-a49a-43b5-8724-9f0d5da8aebe" />


### Penjelasan

Fungsi ini digunakan untuk membersihkan tampilan terminal.

Program akan mendeteksi sistem operasi menggunakan os.name.

* Jika menggunakan Windows (nt), program menjalankan perintah cls.
* Jika menggunakan Linux/macOS, program menjalankan perintah clear.

### Output

Tidak menghasilkan output teks secara langsung. Fungsi ini hanya membersihkan layar terminal.

---

# 6. Fungsi input_tidak_kosong()

<img width="437" height="200" alt="image" src="https://github.com/user-attachments/assets/0433ecbc-c282-4c2d-93d7-9d2ee5be8398" />


### Penjelasan

Fungsi ini digunakan untuk memastikan pengguna tidak memasukkan data kosong.

Program akan terus meminta input selama pengguna belum memasukkan data.

Fungsi .strip() digunakan untuk menghilangkan spasi yang terdapat di awal atau akhir input.

### Contoh Output

Jika pengguna tidak memasukkan data:

```text
Mata kuliah: 
Data tidak boleh kosong
Mata kuliah:
```

Jika pengguna memasukkan data:

```text
Mata kuliah: Pemrograman Dasar
```

Maka data akan diterima oleh program.

---

# 7. Fungsi input_hari()

<img width="536" height="185" alt="image" src="https://github.com/user-attachments/assets/07dd5799-3854-4599-acef-885483480d22" />


### Penjelasan

Fungsi ini digunakan untuk melakukan validasi input hari.

.capitalize() digunakan agar huruf pertama dari input menjadi huruf kapital.

Program kemudian mengecek apakah hari yang dimasukkan terdapat di dalam daftar_hari.

### Contoh Output

Input benar:

```text
Hari: senin
```

Program akan menerima input tersebut sebagai:

```text
Senin
```

Input salah:

```text
Hari: Minggu
Hari tidak valid (Senin - Sabtu)
```

Program akan meminta pengguna memasukkan hari kembali.

---

# 8. Fungsi cek_jam()

<img width="728" height="256" alt="image" src="https://github.com/user-attachments/assets/d25fe683-313c-422e-8403-15983d3a28a2" />

### Penjelasan

Fungsi cek_jam() digunakan untuk memvalidasi format waktu.

Format yang diterima adalah:

```text
HH:MM
```

Contohnya:

```text
07:30
13:45
21:00
```

Program melakukan beberapa pemeriksaan:

1. Panjang input harus 5 karakter.
2. Karakter ketiga harus berupa :.
3. Dua karakter pertama harus berupa jam.
4. Dua karakter terakhir harus berupa menit.
5. Jam harus berada pada rentang 00–23.
6. Menit harus berada pada rentang 00–59.

Fungsi akan menghasilkan:

```text
True
```

jika format benar dan:

```text
False
```

jika format salah.

---

# 9. Fungsi input_jam()

<img width="522" height="183" alt="image" src="https://github.com/user-attachments/assets/ba064990-cdf1-4684-9b96-01f41db47fc4" />


### Penjelasan

Fungsi ini digunakan untuk meminta input jam dari pengguna.

Fungsi input_jam() memanfaatkan fungsi cek_jam() untuk memeriksa apakah format waktu yang dimasukkan sudah benar.

### Contoh Output

Input salah:

```text
Jam (contoh 07:30): 25:70
Format jam salah, gunakan HH:MM
```

Input benar:

```text
Jam (contoh 07:30): 07:30
```

Input kemudian diterima oleh program.

---

# 10. Fungsi buat_id_baru()

<img width="527" height="142" alt="image" src="https://github.com/user-attachments/assets/28a30c95-afb8-4a6a-aaf0-b2c49e1fbece" />


### Penjelasan

Fungsi ini digunakan untuk membuat ID jadwal baru secara otomatis.

Jika belum terdapat data jadwal, ID pertama akan dibuat:

```text
1
```

Jika sudah terdapat ID:

```text
1
2
3
```

maka ID berikutnya akan menjadi:

```text
4
```

Dengan demikian, pengguna tidak perlu memasukkan ID secara manual ketika menambahkan jadwal.

---

# 11. Fungsi tampilkan_jadwal()

<img width="711" height="323" alt="image" src="https://github.com/user-attachments/assets/634bc78c-3d2a-4ef6-abec-1c326fd2daef" />

### Penjelasan

Fungsi ini digunakan untuk menampilkan seluruh data jadwal.

Program menggunakan library `PrettyTable` agar data ditampilkan dalam bentuk tabel.

Program juga melakukan pengecekan apakah data jadwal kosong.

Jika kosong:

```text
Belum ada jadwal
```

Jika terdapat data, maka data akan ditampilkan dalam bentuk tabel.

### Contoh Output

Daftar Jadwal

Mata kuliah = Konsep sistem informasi

Hari       = senin

Jam        = 07.30

Ruang      = C402

Mata kuliah = Pendidikan agam islam

Hari        = Kamis

Jam         = 09.10

Ruang       = C403

---

# 12. Fungsi Menambahkan Jadwal

<img width="712" height="272" alt="image" src="https://github.com/user-attachments/assets/639d6a26-b44a-45a5-9c1e-c50d213becb3" />


### Penjelasan

Fungsi ini digunakan untuk **menambahkan jadwal baru**.

Prosesnya:

1. Meminta nama mata kuliah.
2. Meminta hari.
3. Meminta jam.
4. Meminta ruang.
5. Membuat ID baru secara otomatis.
6. Menyimpan data ke dictionary `jadwal`.
7. Menampilkan pesan keberhasilan.

### Contoh Output

```text
Tambah Jadwal
Mata kuliah: Algoritma dan Pemrograman
Hari: Selasa
Jam (contoh 07:30): 10:00
Ruang: C401
Jadwal berhasil ditambahkan
```

Fungsi ini merupakan bagian dari operasi **Create** pada konsep CRUD.

---

# 13. Fungsi ubah_jadwal()

<img width="251" height="51" alt="image" src="https://github.com/user-attachments/assets/86305619-51b5-4305-91aa-f4a109e33a4e" />


Fungsi ini digunakan untuk **mengubah data jadwal yang sudah tersedia**.

Program terlebih dahulu menampilkan jadwal, kemudian meminta ID jadwal yang ingin diubah.

Jika ID ditemukan, pengguna dapat mengganti:

* Mata kuliah
* Hari
* Jam
* Ruang

Jika ID tidak ditemukan, program akan menampilkan:

```text
ID jadwal tidak tersedia
```

### Contoh Output

```text
Ubah Jadwal

Masukkan ID jadwal: 1
Mata kuliah baru: Sistem Informasi
Hari: Selasa
Jam (contoh 07:30): 09:00
Ruang baru: C401
Jadwal berhasil diubah
```

Fungsi ini merupakan bagian dari operasi **Update** pada konsep CRUD.

---

# 14. Fungsi hapus_jadwal()

<img width="265" height="55" alt="image" src="https://github.com/user-attachments/assets/b811c302-4863-4b6c-84f1-a014b50b0e43" />


### Penjelasan

Fungsi ini digunakan untuk menghapus data jadwal.

Sebelum data dihapus, program meminta konfirmasi kepada pengguna:

```text
Yakin ingin menghapus? (y/n):
```

Jika pengguna memasukkan:

```text
y
```

maka data akan dihapus menggunakan:

```python
data.pop(id_jadwal)
```

Jika pengguna memasukkan selain `y`, penghapusan dibatalkan.

# Contoh Output

```text
Hapus Jadwal

Masukkan ID jadwal: 2
Yakin ingin menghapus? (y/n): y
Jadwal berhasil dihapus
```

Jika dibatalkan:

```text
Yakin ingin menghapus? (y/n): n
Penghapusan dibatalkan
```

Fungsi ini merupakan bagian dari operasi **Delete** pada konsep CRUD.

---

# 15. Fungsi cari_jadwal()

<img width="460" height="205" alt="image" src="https://github.com/user-attachments/assets/fa45f586-bc04-40fc-a5b5-fcb563397cd3" />


### Penjelasan

Fungsi ini digunakan untuk mencari jadwal berdasarkan hari tertentu.

Program meminta pengguna memasukkan hari, kemudian melakukan perulangan terhadap seluruh data jadwal.

Jika hari pada jadwal sama dengan hari yang dicari, data tersebut dimasukkan ke dictionary `hasil`.

Jika tidak ditemukan jadwal, program akan menampilkan:

```text
Tidak ada jadwal pada hari Senin
```

Jika ditemukan, program akan menampilkan jadwal berdasarkan hari yang dipilih.

# Contoh Output

```text
Cari Jadwal Berdasarkan Hari
Hari: Senin

Jadwal Hari Senin
Mata Kuliah = Konsep Sistem Informasi
Hari        = Senin
Jam         = 07.30
Ruang       = C402
```
---


# 16. Fungsi login()

<img width="672" height="87" alt="image" src="https://github.com/user-attachments/assets/f1602a0d-36ad-43f0-a752-280363f5535c" />


### Penjelasan

Fungsi `login()` digunakan untuk melakukan autentikasi pengguna.

Pengguna diberikan **3 kali kesempatan** untuk memasukkan username dan password.

Password dimasukkan menggunakan:

```python
pwinput.pwinput("Password: ")
```

Sehingga password tidak ditampilkan secara langsung di terminal.

Program kemudian mengecek apakah:

1. Username terdapat dalam dictionary akun.
2. Password yang dimasukkan sesuai dengan password akun.

Jika benar:

```text
Login berhasil, selamat datang admin
```

Fungsi kemudian mengembalikan:

```python
username, role
```

Jika salah, kesempatan login dikurangi.

### Contoh Login Berhasil

```text
LOGIN
Username: admin
Password:
Login berhasil, selamat datang admin
```

### Contoh Login Gagal

```text
LOGIN
Username: admin
Password:
Username atau password salah, sisa kesempatan: 2
```

Jika tiga kali gagal:

```text
Kesempatan login habis
```

---

# 17. Menu Admin

```python
def menu_admin(username):
```

### Penjelasan

Menu admin merupakan menu khusus pengguna yang memiliki role `admin`.

Admin memiliki akses terhadap seluruh fitur pengelolaan jadwal.

### Tampilan Menu

<img width="350" height="173" alt="image" src="https://github.com/user-attachments/assets/358c602e-a31e-44c5-bb84-4ecb9a6b09e3" />

Admin memiliki akses **CRUD lengkap** terhadap data jadwal.

---

# 18. Menu User

```python
def menu_user(username):
```

### Penjelasan

Menu user digunakan oleh pengguna dengan role `user`.

Berbeda dengan admin, user tidak dapat menambahkan, mengubah, atau menghapus jadwal.

User hanya memiliki akses untuk:

1. Menampilkan jadwal.
2. Mencari jadwal berdasarkan hari.
3. Logout.

### Tampilan Menu

<img width="363" height="118" alt="image" src="https://github.com/user-attachments/assets/385f6d46-4a0d-4882-9bd1-01b88fe0eb87" />


Pembatasan tersebut digunakan untuk membedakan hak akses antara admin dan user.

---

# 18. Program Utama

Bagian utama program menggunakan:

```python
while True:
```

Program akan terus berjalan sampai pengguna memilih menu **Keluar**.

### Tampilan Awal

<img width="212" height="88" alt="Cuplikan layar 2026-10-06 100646" src="https://github.com/user-attachments/assets/ae44470a-da4f-4a26-948e-eb47ff8ee24b" />


Jika pengguna memilih:

```text
1
```

program akan menjalankan proses login.

Setelah login berhasil, program memeriksa role pengguna.

Jika role adalah:

```text
admin
```

maka program menjalankan:

```python
menu_admin(username)
```

Jika role bukan admin, program menjalankan:

```python
menu_user(username)
```

Jika pengguna memilih:

```text
2
```

program akan menampilkan:

```text
Program selesai
```

kemudian program berhenti.

---


# 19. Konsep CRUD

Program ini menerapkan konsep **CRUD (Create, Read, Update, Delete)**.

### Create

Digunakan untuk menambahkan jadwal baru.

```python
tambah_jadwal()
```

### Read

Digunakan untuk menampilkan data jadwal.

```python
tampilkan_jadwal()
```

### Update

Digunakan untuk mengubah jadwal.

```python
ubah_jadwal()
```

### Delete

Digunakan untuk menghapus jadwal.

```python
hapus_jadwal()
```

Selain CRUD, terdapat fitur pencarian:

```python
cari_jadwal()
```

yang digunakan untuk mencari jadwal berdasarkan hari.

---

# 20. Contoh Penggunaan Program

## Tampilan Awal

<img width="212" height="88" alt="Cuplikan layar 2026-10-06 100646" src="https://github.com/user-attachments/assets/318a3da3-deac-4520-b10b-4808f5d58750" />


## Login dan menu Admin

<img width="346" height="160" alt="image" src="https://github.com/user-attachments/assets/c7272f72-b8f5-4d94-baa7-3e0d0d3a569c" />


## Output Jadwal

<img width="515" height="177" alt="image" src="https://github.com/user-attachments/assets/233b28f1-9614-476c-9091-4a70645e9a78" />

---

# 21. Kesimpulan

Program **Jadwal Kuliah** merupakan program Python berbasis CLI yang menerapkan beberapa konsep dasar pemrograman, yaitu:

* Variabel dan tipe data.
* Dictionary.
* Nested Dictionary.
* List.
* Function.
* Percabangan if-elif-else.
* Perulangan while dan for.
* Validasi input.
* Sistem login.
* Role/hak akses pengguna.
* CRUD.
* Pencarian data.
* Penggunaan library eksternal.
* Pemformatan data menggunakan PrettyTable.

Program ini dibuat untuk membantu pengelolaan data jadwal kuliah secara sederhana melalui terminal. Admin memiliki hak untuk mengelola data jadwal, sedangkan user/mahasiswa hanya memiliki akses untuk melihat dan mencari jadwal.
