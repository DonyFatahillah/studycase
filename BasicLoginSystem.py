#basic login system
#contains register, login, change password, delete account, and list user
#made by scioss a.k.a Dony
#might be updated soon <3

data_pengguna = []

while True:
    print("Masuk ke akun")
    print("1.) Register")
    print("2.) Login")
    print("3.) Ganti Password")
    print("4.) Hapus akun")
    print("5.) List User")

    pilihan = input("Masukan pilihan opsi (1/2/3/4/5) : ")

    if pilihan == "1":
        print("\nMendaftarkan pengguna baru\n")
        nama_pengguna = input("Masukan Username : ")
        email_pengguna = input(r"Masukan Email : ")
        password_pengguna = input("Masukan Password : ")
        user = {'nama': nama_pengguna, 'email': email_pengguna, 'password': password_pengguna}
        data_pengguna.append(user)
        print("Berhasil mendaftarkan pengguna {}!".format(nama_pengguna))
        print("Selamat Datang!")

    elif pilihan == "2":
        print("\nLogin ke akun\n")
        nama_pengguna = input("Masukan Username : ")
        password_pengguna = input("Masukan Password : ")
        login_berhasil = False
        for user in data_pengguna:
            if user['nama'] == nama_pengguna and user['password'] == password_pengguna:
                print("Berhasil Login!")
                print("Selamat Datang {}".format(nama_pengguna))
                login_berhasil = True
                break
        
        if not login_berhasil:
            print("Username atau Password tidak valid!")
            keluar = input("Ulangi dari program ini? y/n : ")
            if keluar.lower() != "y":
                break
            else:
                continue

    elif pilihan == "3":
        email_pengguna = input("Masukan Email : ")
        password_ditemukan = False
        for user in data_pengguna:
            if user['email'] == email_pengguna:
                print("Email ditemukan!")
                passwordBaru = input("Masukan password baru : ")
                user['password'] = passwordBaru
                print("Password pengguna {} dengan email {} telah diganti!".format(user['nama'], email_pengguna))
                password_ditemukan = True
                break
        
        if not password_ditemukan:
            print("User yang memiliki Email tersebut tidak ditemukan!")
            keluar = input("Keluar dari program ini? y/n : ")
            if keluar.lower() == "y":
                break
    elif pilihan == "4":
            print("\nMenghapus akun\n")
            nama_pengguna = input("Masukan Nama : ")
            email_pengguna = input("Masukan Email : ")
            password_pengguna = input("Masukan Password : ")
            akunDitemukan = False
            for user in data_pengguna:
                if user['nama'] == nama_pengguna and user['email'] == email_pengguna and user['password'] == password_pengguna:
                    print("Akun ditemukan")
                    akunDitemukan = True
                    hapusAkun = input("Apakah Anda yakin ingin menghapus akun ini? (y/n) : ")
                    if hapusAkun.lower() == "y":
                        data_pengguna.remove(user)
                        print("Akun Telah dihapus")
                    else:
                        print("Akun tidak jadi dihapus")
                    break
            
            if not akunDitemukan:
                print("Akun tidak ditemukan")
                keluar = input("Keluar dari program ini? y/n : ")
                if keluar.lower() == "y":
                    break
    elif pilihan == "5":
            
            if len(data_pengguna) == 0:
                print("User tidak ditemukan")
            else:
                print("Daftar User : ")
                for idx, user in enumerate(data_pengguna, start=1):
                    print("{}.Nama : {} = aktif".format(idx, user['nama']))

    ulangi = input("Ulangi Proses? (y/n) : ")
    if ulangi.lower() != "y":
        break
