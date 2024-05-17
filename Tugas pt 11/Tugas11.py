import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

list_data = []

def show_menu():
    clear_screen()
    print("=== Menu Aplikasi ===")
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Edit Nama Mahasiswa")
    print("[4] Hapus Data")
    print("[0] Exit")
    print("------------------------------------------")
    menu = input("Pilih Menu: ")

    if menu == '1':
        lihat_data()
    elif menu == '2':
        tambah_data()
    elif menu == '3':
        edit_nama()
    elif menu == '4':
        hapus_data()
    elif menu == '0':
        exit()
    else:
        print("Menu tidak valid. Silakan pilih menu yang sesuai.")
        input("Tekan Enter untuk kembali ke menu utama...")
        show_menu()

def data_mahasiswa():
    if list_data:
        for data in list_data:
            nim, nama = data
            print(f"NIM : {nim},     Nama : {nama}")
    else:
        print("Belum ada data Mahasiswa.")

def lihat_data():
    clear_screen()
    print("=== Data Mahasiswa ===")
    data_mahasiswa()
    input("Tekan Enter untuk kembali ke menu utama...")
    show_menu()

def tambah_data():
    clear_screen()
    print("=== Tambah Mahasiswa ===")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    list_data.append((nim, nama))
    print("Data berhasil ditambahkan.")
    input("Tekan Enter untuk kembali ke menu utama...")
    show_menu()

def edit_nama():
    clear_screen()
    print("=== Edit Nama Mahasiswa ===")
    nim = input("Masukkan NIM Mahasiswa yang akan diubah namanya: ")
    for i, data in enumerate(list_data):
        if data[0] == nim:
            nama_baru = input("Masukkan Nama Baru: ")
            list_data[i] = (nim, nama_baru)
            print("Nama berhasil diubah.")
            break
    else:
        print("NIM tidak ditemukan.")
    input("Tekan Enter untuk kembali ke menu utama...")
    show_menu()

def hapus_data():
    clear_screen()
    print("=== Hapus Data ===")
    if not list_data:
        print("Belum ada data.")
    else:
        data_mahasiswa()
        nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
        found = False 
        for i, data in enumerate(list_data):
            if data[0] == nim:
                found = True
                confirm = input(f"Apakah Anda yakin ingin menghapus data dengan NIM {nim}? (y/n): ")
                if confirm.lower() == 'y':
                    del list_data[i]
                    print("Data berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
                break
        if not found:
            print("NIM tidak ditemukan.")
    input("Tekan Enter untuk kembali ke menu utama...")
    show_menu()

show_menu()