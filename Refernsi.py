# Program penyewaan perlengkapan camping — TANPA IMPORT
# Data ada di memori (tidak tersimpan ke file)

# ------------------ Data ------------------
inventory = []   # list item {id, name, stock, price}
customers = []   # {id, name, phone}
rentals = []     # {id, customer_id, item_id, qty, days, status}

# ------------------ Helper ------------------
def next_id(data):
    return len(data) + 1


def pause():
    input("\nTekan ENTER untuk lanjut...")

def find_customer_by_id(cid):
    for c in customers:
        if c["id"] == cid:
            return c
    return None

def find_item_by_id(iid):
    for it in inventory:
        if it["id"] == iid:
            return it
    return None

# ------------------ Inventory ------------------
def show_inventory():
    print("\n=== INVENTARIS CAMPING ===")
    if not inventory:
        print("Belum ada item.")
        return
    else:
        print(f"{'ID':<4} {'Nama':<20} {'Stok':<5} {'Harga/Hari'}")
        for it in inventory:
            print(f"{it['id']:<4} {it['name']:<20} {it['stock']:<5} {it['price']}")


def add_inventory():
    print("\nTambah Item Inventaris")
    name = input("Nama item: ").strip()
    if not name:
        print("Nama tidak boleh kosong.")
        return
    try:
        stock = int(input("Stok: "))
        price = int(input("Harga per hari: "))
    except:
        print("Input harus angka!")
        return

    item = {
        "id": next_id(inventory),
        "name": name,
        "stock": stock,
        "price": price
    }
    inventory.append(item)
    print("Item berhasil ditambahkan.")
    pause()

# ------------------ Customers ------------------
def find_or_create_customer():
    print("\nPilih/Masukkan Pelanggan")
    name = input("Nama: ").strip()
    phone = input("Telepon: ").strip()

    for c in customers:
        if c["name"].lower() == name.lower() and c["phone"] == phone:
            print("Pelanggan ditemukan.")
            return c

    # buat baru
    customer = {
        "id": next_id(customers),
        "name": name,
        "phone": phone
    }
    customers.append(customer)
    print("Pelanggan baru dibuat.")
    return customer

# ------------------ Gabungan: Daftar Pelanggan + Sewa Aktif ------------------
def show_customers_with_active_rentals():
    """
    Menampilkan daftar pelanggan. Di bawah setiap pelanggan,
    tampilkan sewa aktif mereka (status == 'rented'). Jika tidak ada,
    tampilkan tanda bahwa tidak ada sewa aktif.
    """
    print("\n=== DAFTAR PELANGGAN & SEWA AKTIF ===")
    if not customers:
        print("Belum ada pelanggan.")
        pause()
        return

    # bikin index: customer_id -> list of rentals (aktif)
    active_by_customer = {}
    for r in rentals:
        if r.get("status") == "rented":
            active_by_customer.setdefault(r["customer_id"], []).append(r)

    for c in customers:
        print(f"\n{c['id']}. {c['name']} ({c['phone']})")
        rent_list = active_by_customer.get(c["id"], [])
        if not rent_list:
            print("   - Tidak ada sewa aktif")
        else:
            for r in rent_list:
                item = find_item_by_id(r["item_id"])
                item_name = item["name"] if item else f"Item#{r['item_id']}"
                print(f"   - Rental ID {r['id']}: {item_name} x{r['qty']} ({r['days']} hari) | Status: {r['status']}")
    pause()

# ------------------ Rentals ------------------
def show_active_rentals():  # tetap tersedia bila diperlukan
    print("\n=== SEWA AKTIF ===")
    found = False
    for r in rentals:
        if r["status"] == "rented":
            found = True
            cust = find_customer_by_id(r["customer_id"])
            item = find_item_by_id(r["item_id"])
            cust_name = cust["name"] if cust else f"Pelanggan#{r['customer_id']}"
            item_name = item["name"] if item else f"Item#{r['item_id']}"
            print(f"ID {r['id']} - Pelanggan: {cust_name} - Item: {item_name} x{r['qty']} ({r['days']} hari)")
    if not found:
        print("Tidak ada sewa aktif.")
    pause()

def rent_item():
    show_inventory()
    try:
        item_id = int(input("ID item yang disewa: "))
    except:
        print("ID tidak valid.")
        return

    item = find_item_by_id(item_id)

    if not item:
        print("Item tidak ditemukan.")
        return

    if item["stock"] <= 0:
        print("Stok habis.")
        return

    try:
        qty = int(input("Jumlah sewa: "))
        days = int(input("Lama sewa (hari): "))
    except:
        print("Input harus angka!")
        return

    if qty <= 0 or qty > item["stock"]:
        print("Jumlah tidak valid.")
        return

    # Ambil/daftar pelanggan
    cust = find_or_create_customer()

    rental = {
        "id": next_id(rentals),
        "customer_id": cust["id"],
        "item_id": item["id"],
        "qty": qty,
        "days": days,
        "status": "rented"
    }
    rentals.append(rental)

    # kurangi stok
    item["stock"] -= qty

    est_total = qty * item["price"] * days
    print(f"Sewa berhasil! Estimasi biaya: {est_total}")
    pause()

def return_item():
    show_active_rentals()
    try:
        rent_id = int(input("ID rental yang dikembalikan: "))
    except:
        print("ID tidak valid.")
        return

    rental = None
    for r in rentals:
        if r["id"] == rent_id:
            rental = r
            break

    if not rental:
        print("ID rental tidak ditemukan.")
        return

    if rental["status"] != "rented":
        print("Sudah dikembalikan.")
        return

    # kembalikan stok
    for it in inventory:
        if it["id"] == rental["item_id"]:
            it["stock"] += rental["qty"]

    rental["status"] = "returned"

    # hitung biaya (tanpa denda karena tidak ada tanggal)
    item_price = 0
    for it in inventory:
        if it["id"] == rental["item_id"]:
            item_price = it["price"]
            break

    total = rental["qty"] * item_price * rental["days"]
    print(f"Berhasil dikembalikan. Total biaya: {total}")
    pause()

# ------------------ Menu ------------------
def menu():
    while True:
        print("""
=== APLIKASI SEWA PERLENGKAPAN CAMPING ===
1. Lihat inventaris
2. Tambah item inventaris
3. Daftar pelanggan & sewa aktif
4. Sewa item
5. Kembalikan item
6. Lihat sewa aktif
7. Keluar
""")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            show_inventory()
        elif pilihan == "2":
            add_inventory()
        elif pilihan == "3":
            show_customers_with_active_rentals()   # menggunakan fungsi gabungan baru
        elif pilihan == "4":
            rent_item()
        elif pilihan == "5":
            return_item()
        elif pilihan == "6":
            show_active_rentals()
        elif pilihan == "7":
            print("Keluar...")
            break
        else:
            print("Menu tidak dikenal.")

# ------------------ Run ------------------
menu()
