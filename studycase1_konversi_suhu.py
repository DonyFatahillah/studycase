    # konversi suhu
while True:
    suhu = (input("masukan jenis suhu celcius (C), fahrenheit (F), reamur (R), kelvin (K)= "))

    if suhu in ("C", "c", "Celcius", "celcius"):
        angkaSuhu = (input("masukan suhu celcius : "))

        if angkaSuhu.isalpha():
            print("masukan angka yang valid!")
            continue

        celcius = int(angkaSuhu)

        print("""
konversi suhu
a.) fahrenheit
b.) reamur
c.) kelvin
        """)

        opsi = input("masukan opsi : ")

        if opsi == "a":
            fahrenheit = (9/5) * celcius + 32
            print(f"celcius '{celcius}' ke fahrenheit adalah {fahrenheit}")
        elif opsi == "b":
            reamur = (4/5) * celcius
            print(f"celcius '{celcius}' ke reamur adalah {reamur}")
        elif opsi == "c":
            kelvin = celcius + 273
            print(f"celcius '{celcius}' ke kelvin adalah {kelvin}")
        else:
            print("opsi tidak valid!")

    elif suhu in ("F", "f", "Fahrenheit", "fahrenheit"):
        angkaSuhu = (input("masukan suhu fahrenheit : "))
        if angkaSuhu.isalpha():
            print("masukan angka yang valid!")
            continue

        fahrenheit = int(angkaSuhu)

        print("""
konversi suhu
a.) celcius
b.) reamur
c.) kelvin
        """)

        opsi = input("masukan opsi : ")

        if opsi == "a":
            celcius = 5/9 * (fahrenheit - 32)
            print(f"fahrenheit '{fahrenheit}' ke celcius adalah {celcius}")
        elif opsi == "b":
            reamur = 4/9 * (fahrenheit - 32)
            print(f"fahrenheit '{fahrenheit}' ke reamur adalah {reamur}")
        elif opsi == "c":
            kelvin = 5/9 * (fahrenheit - 32) + 273
            print(f"fahrenheit '{fahrenheit}' ke kelvin adalah {kelvin}")
        else:
            print("opsi tidak valid!")

    elif suhu in ("R", "r", "Reamur", "reamur"):
        angkaSuhu = (input("masukan suhu reamur : "))

        if angkaSuhu.isalpha():
            print("masukan angka yang valid!")
            continue

        reamur = int(angkaSuhu)

        print("""
konversi suhu
a.) celcius
b.) fahrenheit
c.) kelvin
        """)
        
        opsi = input("masukan opsi : ")

        if opsi == "a":
            celcius = (5/4) * reamur
            print(f"reamur '{reamur}' ke celcius adalah {celcius}")
        elif opsi == "b":
            fahrenheit = (9/4) * reamur + 32
            print(f"reamur '{reamur}' ke fahrenheit adalah {fahrenheit}")
        elif opsi == "c":
            kelvin = (5/4) * reamur + 273
            print(f"reamur '{reamur}' ke kelvin adalah {kelvin}")
        else:
            print("opsi tidak valid!")

    elif suhu in ("K", "k", "Kelvin", "kelvin"):
        angkaSuhu = (input("masukan suhu kelvin : "))

        if angkaSuhu.isalpha():
            print("masukan angka yang valid!")
            continue

        kelvin = int(angkaSuhu)

        print("""
konversi suhu
a.) celcius
b.) fahrenheit
c.) reamur
        """)

        opsi = input("masukan opsi : ")

        if opsi == "a":
            celcius = kelvin - 273
            print(f"kelvin '{kelvin}' ke celcius adalah {celcius}")
        elif opsi == "b":
            fahrenheit = 9/5 * (kelvin - 273) + 32
            print(f"kelvin '{kelvin}' ke fahrenheit adalah {fahrenheit}")
        elif opsi == "c":
            reamur = 4/5 * (kelvin - 273)
            print(f"kelvin '{kelvin}' ke reamur adalah {reamur}")
        else:
            print("opsi tidak valid!")
    else:
        print("opsi tidak valid!")
        continue

    ulangi = input("ulangi program? (y/n) : ")
    if ulangi.lower() != "y":
        break
