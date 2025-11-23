
mobil = {}

def listkendaraan():
    if not mobil:
        print("Belum ada data")
        return
    for key,data in mobil.items():
        print(f"Plat Nomor : {key} | Jenis : {data[0]} | Tipe Kendaraan : {data[1]} | Tahun Produksi {data[2]}")

def tambahkendaraan():
    # validasi plat nomor
    while True:
        plat = input("Masukan Plat Kendaraan(Cnt : S0001AB): ").strip().upper()
        if not plat:
            print("Plat yang anda masukan kosong")
            continue
        Nplat = len(plat)
        if Nplat != 7:
            print("Plat harus memiliki 7 karakter")
            continue
        break
    
    # jenis kendaraan
    while True:
        jeniskendaraan = input("Jenis kendaraan (Mobil/Motor) : ").capitalize()
        if jeniskendaraan not in ["Motor","Mobil"]:
            print("Jenis kendaraan invalid")
            continue
        break
    
    # tipe kendaraan
    while True:
        tipe = input(f"Masukan Tipe {jeniskendaraan} : ").title()
        if not tipe:
            print("Tipe tidak boleh kosong")
            continue
        break
    
    # Tahun produksi
    while True:
        tahun = input("Masukan tahun produksi : ").strip()
        if not tahun.isdigit():
            print("Wajib berisi angka")
            continue
        tahun = len(tahun)
        if tahun != 4:
            print("Input tahun harus 4 digit angka")
            continue
        break
    mobil[plat] = [jeniskendaraan,tipe,tahun]
    print(f"Data {tipe} berhasil di tambhakan")



# def tampilan_menu():
#     print("""
# ==== Penyewaan Kendaraan ===
# 1.  Lihat Kendaraan
# 2.  Tambah Kendaraan
# 3.  
# 4.
# """)
while True:
    i = input("masukan : ")
    if i == "1":
        listkendaraan()
    elif i == "2":
        tambahkendaraan()
    elif i == "0":
        break