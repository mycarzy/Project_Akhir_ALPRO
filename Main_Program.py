#  denda = 5000 perhari


#  ---------- List untuk menyimpan data 
inventaris = [
    {"id": 1, "nama": "Tenda", "stok": 10, "harga": 150000, "Deskripsi": "Tenda camping kapasitas 4 orang"},
    {"id": 2, "nama": "Sleeping Bag", "stok": 20, "harga": 20000, "Deskripsi": "Sleeping bag nyaman dan hangat"},
    {"id": 3, "nama": "Kompor Portable", "stok": 5, "harga": 30000, "Deskripsi": "Kompor kecil, mudah dibawa"},
    {"id": 4, "nama": "Lampu Senter", "stok": 30, "harga": 10000, "Deskripsi": "Lampu senter baterai"},
    {"id": 5, "nama": "Kursi Lipat", "stok": 15, "harga": 15000, "Deskripsi": "Kursi lipat ringan"}
]
data_penyewaan = []

#  ------------- fungsi pembantu

# membuat id unik di list inventaris dan penyewa
def id_unik(data):
    if not data:
        return 1
    return max(d.get("id", 0) for d in data) + 1

def pencarian_barang(itemid):
    for item in inventaris:
        if item['id'] == itemid:
            return item
    return None

# ------- Data inventaris ------------

#  menampilkan data dala list inventaris
def tampilkan_inventaris():
    if not inventaris:
        print("Belum Ada Item Pada Inventaris")
        return
    print(f"{'ID':<3} | {'Nama':<20} | {'Stok':<5} | {'Harga/Hari':<10} | {'Deskripsi':<35} |")
    print("=" * 90)
    for item in inventaris:
        print(f"{item['id']:<3} | {item['nama']:<20} | {item['stok']:<5} | {item['harga']:<10} | {item['Deskripsi']:<35} |")

#  menambahkan data barang
def tambahkan_inventaris():
    print("Menambahkan Item Inventaris")
    
    namaitem = input("Masukan Nama Item : ").strip().title()
    if not namaitem:
        print("--Nama tidak boleh kosong--")
        return
    
    while True:
        try:
            stok = int(input("Stok: "))
            harga = int(input("Harga per hari: "))
            if stok < 0 or harga < 0:
                print("Harga Atau Stok Tidak Boleh Minus")
                continue
            break
        except:
            print("Input harus angka!")
            continue

    deskripsi = input("Masukan Deksripsi Barang :  ").title()
    item = {
    "id": id_unik(inventaris),
    "nama": namaitem,
    "stok": stok,
    "harga": harga,
    "Deskripsi": deskripsi
    }
    inventaris.append(item)
    print("Item berhasil ditambahkan.")


def hapus_inventaris():
    tampilkan_inventaris()

    if not inventaris:
        print("Belum Ada Item Pada Inventaris")
        return

    try:
        idhapus = int(input("Masukkan ID barang yang ingin dihapus: ").strip())
    except ValueError:
        print("Input hanya boleh angka!")
        return

    # cari item berdasarkan ID
    item = None
    for barang in inventaris:
        if barang["id"] == idhapus:
            item = barang
            break

    if not item:
        print("ID barang tidak ditemukan.")
        return

    # konfirmasi penghapusan
    konfirmasi = input(f"Yakin ingin menghapus '{item['nama']}'? (y/n): ").lower()
    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return

    inventaris.remove(item)
    print(f"Barang '{item['nama']}' berhasil dihapus.")


#  ----------- sistem penyewaan --------

def tampilkan_penyewa():
    if not data_penyewaan:
        print("--Belum ada penyewa--")
        return
    print(f"{'ID':<3} | {'nama':<15} | {'telepon':<13} | {'ID Item':<7} | {'Nama barang':<20} | {'jumlah':<7} | {'hari':<4} | {'status':<15}")
    for data in data_penyewaan:
        print(f"{data['id']:<3} | {data['nama']:<15} | {data['telepon']:<13} | {data['id_item']:<7} | {data['nama barang']:<20} | {data['jumlah']:<7} | {data['hari']:<4} | {data['status']:<15} ")

def penyewaan_item():
    tampilkan_inventaris()
    if not inventaris:
        print("Belum ada inventaris, tidak dapat melakukan penyewaan.")
        return
    
    print()
    print("!!! JIKA BARANG DIKEMBALIKAN MELEBIHI BATAS SEWA, MAKA AKAN DIKENAKAN DENDA 5000 PER HARI !!!")
    print()
    
    try: 
        id_item = int(input("ID barang yang ingin disewa : "))
        if not id_item:
            print("Input kosong")
    except ValueError:
        print("inout tidak valid,tolong hanya masukan angka (integer)")
        return
    
    item = pencarian_barang(id_item)   
    if not item:
        print("Item tidak ditemukan.")
        return
    if item["stok"] <= 0:
        print("Stok habis")
        return

    while True:
        try:
            jumlah = int(input("Jumlah item/barang : "))
            if jumlah > item["stok"]:
                print(f"Stok tidak mencukupi. Stok tersedia: {item['stok']}")
                continue
            hari = int(input("Lama sewa (hari) : "))
            if jumlah <= 0 or hari <= 0:
                print("Jumlah barang dan Lama sewa Tidak Boleh Minus")
                continue
        except ValueError:
            print("inout tidak valid,tolong hanya masukan angka (integer)")
            continue
        break

    while True:
        nama = input("Nama penyewa : ").strip().capitalize()
        if not nama:
            print("Nama tidak boleh kosong")
            continue
        if not nama.isalpha():
            print("Terdapat angka didalam input nama")
            continue
        break
    
    while True:
        telepon = input("Nomor Telepon penyewa (contoh: 081234567810) : ")
        if not telepon:
            print("Nomor telepon hanya boleh berisi angka")
            continue
        if not telepon.isdigit():
            print("Terdapat angka didalam input nama")
            continue
        if not telepon.startswith("08") or not (11 <= len(telepon) <= 13):
            print("Nomor telepon harus diawali '08' dan mengandun 11-13 digit angka")
            continue
        break
    
    sewa = {
        "id": id_unik(data_penyewaan),
        "nama": nama,
        "telepon": telepon,
        "id_item": item['id'],
        "nama barang": item['nama'],
        "jumlah": jumlah,
        "hari": hari,
        "status": "Sedang Di Sewa"
    }
    data_penyewaan.append(sewa)
    
    item["stok"] -= jumlah
    
    print(f"Data penyewa atas nama {nama} berhasil ditambahkan ke database")



def pengembalian_item ():
    tampilkan_penyewa()
    while True:
        try: 
            idsewa = int(input("Masukan ID penyewaan yang mau di kembalikan : "))
            break
        except ValueError:
            print("--Input Id hanya menerima angka--")
            continue
    
    penyewa = None
    for penyewa in data_penyewaan:
        if penyewa["id"] == idsewa:
            break
    if not penyewa:
        print("Penyewq tidak ditemukan")
        return
    
    try:
        hari_pengembalian = int(input("Masukkan hari pengembalian (berapa hari sejak mulai sewa): "))
    except ValueError:
        print("Input hari harus angka.")
        return

    item = pencarian_barang(penyewa["id_item"])
    if item:
        item['stok'] += penyewa["jumlah"]
    
    denda = 0
    if hari_pengembalian > penyewa["hari"]:
        denda_hari = 5000 
        denda = (hari_pengembalian - penyewa["hari"]) * denda_hari
        # print(f"Denda keterlambatan: Rp{denda}")

    total_bayar = penyewa["jumlah"] * item["harga"] * penyewa["hari"] + denda
    # print(f"Total pembayaran termasuk denda: Rp{total_bayar}")
    
    
    print("\n----------- STRUK PENGEMBALIAN -----------")
    print(f"Nama Penyewa     : {penyewa['nama']}")
    print(f"No. Telepon      : {penyewa['telepon']}")
    print(f"Barang           : {item['nama']}")
    print(f"Jumlah           : {penyewa['jumlah']}")
    print(f"Harga per Hari   : Rp{item['harga']}")
    print(f"Lama Sewa        : {penyewa['hari']} hari")
    print(f"Hari Kembali     : {hari_pengembalian} hari")
    print(f"Denda            : Rp{denda}")
    print(f"Total Pembayaran : Rp{total_bayar}")
    print("-----------------------------------------\n")

    penyewa["status"] = "Sudah Dikembalikan"
    print("Barang telah berhasil dikembalikan.")   # ---> tambahkan output seperti struk kasir
    
#  ------------------------ Perubahan Stok

def update_stok():
    tampilkan_inventaris()
    if not inventaris:
        print("Belum ada inventaris barang, tidak dapat melakukan update stok.")
        return

    # Input ID barang
    while True:
        try:
            id_item = int(input("Masukan ID barang yang ingin diupdate stoknya: "))
            break
        except ValueError:
            print("Input hanya dapat menerima angka")

    item = pencarian_barang(id_item)
    if not item:
        print("Barang dengan ID tersebut tidak ditemukan.")
        return

    # Pilihan update stok
    while True:
        print("""----- Opsi Perubahan Stok ----
1. Menambahkan Stok
2. Mengurangi Stok
""")
        opsi = input("Pilih : ").strip()

        if opsi not in ("1", "2"):
            print("!!! Silahkan Pilih di antara [1, 2] !!!")
            continue

        # === Opsi 1: Tambah stok ===
        if opsi == "1":
            try:
                jumlah = int(input(f"Masukan jumlah STOK yang akan ditambahkan ke '{item['nama']}': "))
                if jumlah < 0:
                    print("Jumlah tidak boleh negatif.")
                    continue
            except ValueError:
                print("Input stok harus berupa angka.")
                continue

            item["stok"] += jumlah
            print(f"Stok barang '{item['nama']}' berhasil ditambahkan. Stok sekarang: {item['stok']}.")
            return

        # === Opsi 2: Kurangi stok ===
        elif opsi == "2":
            try:
                jumlah = int(input(f"Masukan jumlah STOK yang akan dikurangi dari '{item['nama']}': "))
                if jumlah < 0:
                    print("Jumlah tidak boleh negatif.")
                    continue
            except ValueError:
                print("Input stok harus berupa angka.")
                continue

            if jumlah > item["stok"]:
                print("Jumlah pengurangan melebihi stok yang tersedia.")
                continue

            item["stok"] -= jumlah
            print(f"Stok barang '{item['nama']}' berhasil dikurangi. Stok sekarang: {item['stok']}.")
            return


def menu():
    while True:
        print("""
============> ULO GONDRONG <============
==== PENYEWAAN PERLENGKAPAN CAMPING ====
|1. |Lihat inventaris                  | 
|2. |Tambah item inventaris            |
|3. |Hapus Item Inventaris             |
|4. |Update Stok                       |
|5. |Daftar penyewa                    |
|6. |Menyewa Item                      |
|7. |Pengembalian Item Sewa            |                                  
|   |                                  |
|0. |Keluar                            |
========================================
""")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_inventaris()
        elif pilihan == "2":
            tambahkan_inventaris()
        elif pilihan == "3":
            hapus_inventaris()
        elif pilihan == "4":
            update_stok()
        elif pilihan == "5":
            tampilkan_penyewa()
        elif pilihan == "6":
            penyewaan_item()
        elif pilihan == "7":
            pengembalian_item()
        elif pilihan == "0":
            print("Keluar Program")
            break
        else:
            print("Input yang anda masukan tidak ada dimenu")

# ------------------ menjlankan program ------------------
menu()
