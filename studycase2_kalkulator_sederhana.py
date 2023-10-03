# kalkulator sederhana made by scioss a.k.a Dony
angka1 = input("Angka Pertama : ")
angka2 = input("Angka Kedua : ")

while True:
    
    print("""
opsi operasi
a.) perkalian
b.) pembagian
c.) pertambahan
d.) pengurangan
    """)

    opsi = input("masukan opsi operasi (a/b/c/d) : ")

    if opsi == "a":
        angka1 = int(angka1)
        angka2 = int(angka2)
        jumlahKali = angka1 * angka2
        print(f"jumlah dari {angka1} x {angka2} = {jumlahKali}")
    elif opsi == "b":
        angka1 = float(angka1)
        angka2 = float(angka2)
        jumlahBagi = angka1 / angka2
        print(f"jumlah dari {angka1} : {angka2} = {jumlahBagi}")
    elif opsi == "c":
        angka1 = int(angka1)
        angka2 = int(angka2)
        jumlahTambah = angka1 + angka2
        print(f"jumlah dari {angka1} + {angka2} = {jumlahTambah}")
    elif opsi == "d":
        angka1 = int(angka1)
        angka2 = int(angka2)
        jumlahKurang = angka1 - angka2
        print(f"jumlah dari {angka1} - {angka2} = {jumlahKurang}")
    else:
        print("opsi tidak valid!")

    ulangi = input("ulangi proses (y/n) : ")
    if ulangi.lower() != "y":
        break
