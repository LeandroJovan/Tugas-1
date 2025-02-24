buku_list = []
buku_dipinjam = []

def tambah_buku(judul, penulis):
    buku = {'judul': judul, 'penulis': penulis, 'dipinjam': False}
    buku_list.append(buku)
    print(f"Buku '{judul}' oleh {penulis} ditambahkan.")

def lihat_buku():
    if not buku_list:
        print("Belum ada buku yang ditambahkan.")
    else:
        print("Daftar buku di perpustakaan:")
        for buku in buku_list:
            status = "Dipinjam" if buku['dipinjam'] else "Tersedia"
            print(f"'{buku['judul']}' oleh {buku['penulis']} - {status}")

def pinjam_buku(judul):
    for buku in buku_list:
        if buku['judul'].lower() == judul.lower():
            if buku['dipinjam']:
                print(f"Buku '{judul}' sedang dipinjam.")
            else:
                buku['dipinjam'] = True
                buku_dipinjam.append(buku)
                print(f"Buku '{judul}' telah dipinjam.")
            return
    print(f"Buku '{judul}' tidak ditemukan.")

def kembalikan_buku(judul):
    for buku in buku_dipinjam:
        if buku['judul'].lower() == judul.lower():
            buku['dipinjam'] = False
            buku_dipinjam.remove(buku)
            print(f"Buku '{judul}' telah dikembalikan.")
            return
    print(f"Buku '{judul}' tidak ditemukan.")

# Contoh penggunaan

# Menambahkan beberapa buku
tambah_buku("Python untuk Pemula", "John Doe")
tambah_buku("Data Science dengan Python", "Jane Smith")

# Melihat daftar buku
lihat_buku()

# Meminjam buku
pinjam_buku("Python untuk Pemula")
lihat_buku()

# Mengembalikan buku
kembalikan_buku("Python untuk Pemula")
lihat_buku()