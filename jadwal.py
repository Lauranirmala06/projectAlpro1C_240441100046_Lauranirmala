#Data dokter
datadokter = [
    {"id": 1, "nama": "Laura", "spesialis": "Jantung"},
    {"id": 2, "nama": "Nirmala", "spesialis": "Mata"},
    {"id": 3, "nama": "Zara", "spesialis": "Tulang"},
    {"id": 4, "nama": "Syahra", "spesialis": "Gigi"},
    {"id": 5, "nama": "Gata", "spesialis": "Kulit"}
]

#data admin
admin = (
    ("laura", "lauraa"),
    ("Azhara", "Azhara")
)
#jadwal dokter
jadwaldokter = {}

def login():
    print("""
        SELAMAT DATANG DI
        PENJADWALAN DOKTER DI RUMAH SAKIT
        SILAHKAN LOGIN TERLEBIH DAHULU!!!
        """)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if len(password) != 6:
        print("Password harus berisi 6 karakter")
        login()
        
    a = False
    for dt in admin:
        if username == dt[0] and password == dt[1]:
            a = True
            break
    if a:
        menuutama()
    else:
        print("Username atau password yang anda masukkan tidak tersedia!!!")
        login()
  
        
def lihatdokter():
    print("Daftar Dokter:")
    for dokter in datadokter:
        print(f"ID: {dokter['id']} - Dr. {dokter['nama']} ({dokter['spesialis']})")
    print()
     
        
def tambah(nama, spesialis):
    id = max([dokter['id'] for dokter in datadokter], default=0) + 1
    datadokter.append({"id": id, "nama": nama, "spesialis": spesialis})
    print(f"Dokter {nama} berhasil ditambahkan dengan ID {id}.\n")


def ubah(id, nama=None, spesialis=None):
    dokter = next((d for d in datadokter if d["id"] == id), None)
    if dokter:
        if nama:
            dokter["nama"] = nama
        if spesialis:
            dokter["spesialis"] = spesialis
        print(f"Data Dr. {dokter['nama']} berhasil diperbarui.\n")
    else:
        print(f"Tidak ditemukan dokter dengan ID {id}.\n")


def hapus(id):
    dokter = next((d for d in datadokter if d["id"] == id), None)
    if dokter:
        datadokter.remove(dokter)
        if id in jadwaldokter:
            del jadwaldokter[id]
        print(f"Dokter {dokter['nama']} berhasil dihapus.\n")
    else:
        print(f"Tidak ditemukan dokter dengan ID {id}.\n")


def caridokter(katakunci):
    hasil = [dokter for dokter in datadokter if any(katakunci.lower() in str(value).lower() for value in dokter.values())]
    if hasil:
        print(f"Dokter yang ditemukan '{katakunci}':")
        for dokter in hasil:
            print(f"ID: {dokter['id']} - Dr. {dokter['nama']} ({dokter['spesialis']})")
    else:
        print(f"Tidak ditemukan dokter '{katakunci}'.\n")

def menudokter():
    while True:
        print("""
        Menu:
        1. Tampilkan Daftar Dokter
        2. Tambah Dokter
        3. Ubah Data Dokter
        4. Hapus Dokter
        5. Cari Dokter
        6. Kembali Ke Menu Utama
        """)
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihatdokter()

        elif pilihan == "2":
            nama = input("Nama Dokter: ")
            spesialis = input("Spesialisasi: ")
            tambah(nama, spesialis)

        elif pilihan == "3":
            id = input("Masukkan ID Dokter: ")
            if id.isdigit():
                id_dokter = int(id)
                nama = input("Nama Baru (biarkan kosong jika tidak diubah): ")
                spesialis = input("Spesialisasi Baru (biarkan kosong jika tidak diubah): ")
                ubah(id_dokter, nama if nama else None, spesialis if spesialis else None)
            else:
                print("ID dokter harus berupa angka.\n")

        elif pilihan == "4":
            id = input("Masukkan ID Dokter: ")
            if id.isdigit():
                id_dokter = int(id)
                hapus(id_dokter)
            else:
                print("ID dokter harus berupa angka.\n")

        elif pilihan == "5":
            keyword = input("Masukkan kata kunci untuk pencarian (ID, nama, atau spesialisasi): ")
            caridokter(keyword)
        
        elif pilihan == "6":
            menuutama()
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


def lihatjadwal():
    if not jadwaldokter:
        print("Belum ada jadwal yang tersedia.\n")
    else:
        print("Daftar Jadwal Dokter:")
        for id, jadwal in jadwaldokter.items():
            print(f"ID: {id} - Dr. {jadwal['nama']} ({jadwal['spesialis']}) - {jadwal['hari']}")
    print()


def tambahjadwal(id, hari):
    dokter = next((d for d in datadokter if d["id"] == id), None)
    if dokter:
        if id in jadwaldokter:
            print(f"Dr. {dokter['nama']} sudah memiliki jadwal. Gunakan opsi update untuk mengubah.\n")
        else:
            jadwaldokter[id] = {
                "nama": dokter["nama"],
                "spesialis": dokter["spesialis"],
                "hari": hari
            }
            print(f"Jadwal Dr. {dokter['nama']} berhasil ditambahkan.\n")
    else:
        print(f"Tidak ditemukan dokter dengan ID {id}.\n")


def ubahjadwal(id, hari):
    if id in jadwaldokter:
        jadwaldokter[id]["hari"] = hari
        print(f"Jadwal Dr. {jadwaldokter[id]['nama']} berhasil diperbarui.\n")
    else:
        print(f"Tidak ditemukan jadwal untuk dokter dengan ID {id}.\n")


def hapusjadwal(id):
    if id in jadwaldokter:
        dokter = jadwaldokter[id]
        del jadwaldokter[id]
        print(f"Jadwal Dr. {dokter['nama']} berhasil dihapus.\n")
    else:
        print(f"Tidak ditemukan jadwal untuk dokter dengan ID {id}.\n")


def cari(hari):
    hasil = [jadwal for jadwal in jadwaldokter.values() if jadwal["hari"].lower() == hari.lower()]
    if hasil:
        print(f"Dokter dengan jadwal pada hari {hari}:")
        for dokter in hasil:
            print(f"- Dr. {dokter['nama']} ({dokter['spesialis']})")
    else:
        print(f"Tidak ditemukan dokter dengan jadwal pada hari {hari}.\n")
    print()


def validasi(id):
    return any(dokter['id'] == id for dokter in datadokter)

def menuutama():
    while True:
        print("""
        PENJADWALAN DOKTER DI RUMAH SAKIT
        
        Menu:
        1. Daftar Dokter
        2. Tambah Jadwal
        3. Lihat Jadwal
        4. Ubah Jadwal
        5. Hapus Jadwal
        6. Cari Jadwal
        7. Keluar
        """)
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menudokter()

        elif pilihan == "2":
            id = input("Masukkan ID Dokter: ")
            if id.isdigit():
                id_dokter = int(id)
                if validasi(id_dokter):
                    hari = input("Hari Jadwal: ")
                    tambahjadwal(id_dokter, hari)
                else:
                    print("ID dokter tidak valid.\n")
            else:
                print("ID dokter harus berupa angka.\n")

        elif pilihan == "3":
            lihatjadwal()

        elif pilihan == "4":
            id = input("Masukkan ID Dokter: ")
            if id.isdigit():
                id_dokter = int(id)
                if validasi(id_dokter):
                    hari = input("Hari Jadwal Baru: ")
                    ubahjadwal(id_dokter, hari)
                else:
                    print("ID dokter tidak valid.\n")
            else:
                print("ID dokter harus berupa angka.\n")

        elif pilihan == "5":
            id = input("Masukkan ID Dokter: ")
            if id.isdigit():
                id_dokter = int(id)
                if validasi(id_dokter):
                    hapusjadwal(id_dokter)
                else:
                    print("ID dokter tidak valid.\n")
            else:
                print("ID dokter harus berupa angka.\n")

        elif pilihan == "6":
            jadwal = input("Masukkan Hari: ")
            cari(jadwal)

        elif pilihan == "7":
            print("Program keluar. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
login()