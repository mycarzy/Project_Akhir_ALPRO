#  ---------- List untuk menyimpan data 
inventaris = []
data_penyewaan = []

#  ------------- fungsi pembantu

# membuat id unik di list inventaris dan penyewa
def id_unik(data):
    return len(data) + 1

# def pencaripelanggan(penyewaid): # pid = penyewwa id
#     for pid in penyewa:
#         if pid['id'] == penyewaid:
#             return pid
#     return None

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


# -------------------- data penyewa ----------------------------
# menambahkan penyewa
def tambah_penyewa():
    pass
#     while True:
#         nama = input("Nama penyewa : ").strip().capitalize()
#         if not nama:
#             print("Nama tidak boleh kosong")
#             continue
#         if not nama.isalpha():
#             print("Terdapat angka didalam input nama")
#             continue
#         break
    
#     while True:
#         telepon = input("Nomor Telepon penyewa : ")
#         if not telepon:
#             print("Nomor telepon hanya boleh berisi angka")
#             continue
#         if not telepon.isdigit():
#             print("Terdapat angka didalam input nama")
#             continue
#         break
    
#     namapenyewa = {
#     "id": id_unik(penyewa),
#     "nama":nama,
#     "telepon":telepon
#     }
#     penyewa.append(namapenyewa)
#     print("Penyewa telah berhasil ditambahkan.")


# def list_penyewa():
#     if not penyewa:
#         print("Tidak ada data penyewa")
#         return
#     print(f"{'ID':<3} | {'Nama':<15} | {'Telepon':<15}")
#     for np in penyewa:
#         print(f"{np['id']:<3} - {np['nama']:<15} | {np['telepon']:<15}")

#  ----------- sistem penyewaan --------

def tampilkan_penyewa():
    if not data_penyewaan:
        print("--Belum ada penyewa--")
        return
    print(f"{'ID':<3} | {'nama':<15} | {'telepon':<13} | {'ID Item':<7} | {'jumlah':<5} | {'hari':<4} | {'status':<15}")
    for data in data_penyewaan:
        print(f"{data['id']:<3} | {data['nama']:<15} | {data['telepon']:<13} | {data['id_item']:<7} | {data['jumlah']:<5} | {data['hari']:<4} | {data['status']:<15} ")

def penyewaan_item():
    tampilkan_inventaris()
    if not inventaris:
        print("Belum ada inventaris, tidak dapat melakukan penyewaan.")
        return
    
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

    try:
        jumlah = int(input("Jumlah item/barang : "))
        hari = int(input("Lama sewa (hari) : "))
    except ValueError:
        print("inout tidak valid,tolong hanya masukan angka (integer)")
        return
    if jumlah <= 0 or hari <= 0:
        print("Jumlah barang dan Lama sewa Tidak Boleh Minus")
        return
    
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
        telepon = input("Nomor Telepon penyewa : ")
        if not telepon:
            print("Nomor telepon hanya boleh berisi angka")
            continue
        if not telepon.isdigit():
            print("Terdapat angka didalam input nama")
            continue
        break
    
    sewa = {
        "id": id_unik(data_penyewaan),
        "nama": nama,
        "telepon": telepon,
        "id_item": item['id'],
        "jumlah": jumlah,
        "hari": hari,
        "status": "Sedang Di Sewa"
    }
    data_penyewaan.append(sewa)
    
    item["stok"] -= jumlah
    
    totalbiayasewa = jumlah * item['harga'] * hari
    print(f"""Sewa berhasil
Total harga : {totalbiayasewa}
""") 



#  belum jadi
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
    
    for item in inventaris:
        if item["id"] == data_penyewaan["id_item"]:
            item['stok'] += data_penyewaan["jumlah"]
    
    print(f"Berhasil dikembalikan.")
    
#  ------------------------ Perubahan data

def update_stok_barang():
    if not inventaris:
        print("Belum ada inventaris barang, tidak dapat melakukan update stok.")
        return
    
    try:
        id_item = int(input("Masukan ID barang yang ingin diupdate stoknya: "))
    except ValueError:
        print("Input tidak valid, masukan harus angka.")
        return

    item = pencarian_barang(id_item)
    if not item:
        print("Barang dengan ID tersebut tidak ditemukan.")
        return
    
    try:
        stok_baru = int(input(f"Masukan stok baru untuk {item['nama']}: "))
        if stok_baru < 0:
            print("Stok baru tidak boleh kurang dari 0.")
            return
    except ValueError:
        print("Input stok harus berupa angka.")
        return
    
    item['stok'] = stok_baru
    print(f"Stok barang '{item['nama']}' berhasil diperbarui menjadi {stok_baru}.")

def menu():
    while True:
        print("""
==== PENYEWAAN PERLENGKAPAN CAMPING ====
|1. |Lihat inventaris                  | 
|2. |Tambah item inventaris            |
|3. |Daftar penyewa                    |
|4. |Menyewa Item                      |
|5. |Pengembalian Item Sewa            |
|6. |Lihat sewa aktif                  |
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
            tampilkan_penyewa()
        elif pilihan == "4":
            penyewaan_item()
        elif pilihan == "5":
            pass
            # pengembalian_item()
        elif pilihan == "6":
            update_stok_barang()
        elif pilihan == "0":
            print("Keluar Program")
            break
        else:
            print("Menu tidak dikenal")

# ------------------ menjlankan program ------------------
menu()
