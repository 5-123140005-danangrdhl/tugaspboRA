tugas = []  # Inisialisasi daftar tugas di luar loop

while True:
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        tugas_add = input("Masukkan tugas yang ingin ditambahkan: ")
        tugas.append(tugas_add)
        print("Tugas berhasil ditambahkan!")
    elif pilihan == '2':
        cari = input("Masukkan nomor tugas yang ingin dihapus: ")
        try:
            cari = int(cari)  # Mengonversi input ke integer
            if cari < 1 or cari > len(tugas):
                raise IndexError(f"Error: Tugas dengan nomor {cari} tidak ditemukan.")
            tugas.pop(cari - 1)  # Menghapus tugas berdasarkan nomor
            print(f"Tugas nomor {cari} berhasil dihapus.")
        except ValueError:
            raise ValueError("Error: Masukkan nomor yang valid.")
    elif pilihan == '3':
        if not tugas:
            print("Daftar Tugas: Tidak ada tugas yang tersedia.")
        else:
            print("Daftar Tugas:")
            for ada in tugas :
                print(f"- {ada}")
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    else:
        raise ValueError("Error: Pilihan tidak valid. Harap pilih 1, 2, 3, atau 4.")