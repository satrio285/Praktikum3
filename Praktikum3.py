print('NAMA : SATRIO HUTOMO PRABU BUANA')
print('NIM : 312510330')

# Program untuk menentukan bilangan terbesar dari N input

print("Masukkan bilangan satu per satu.")
print("Masukkan angka 0 untuk mengakhiri input.")

maksimum = None  # Menyimpan bilangan terbesar

while True:
    try:
        angka = int(input("Masukkan bilangan: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat.")
        continue

    if angka == 0:
        break

    if maksimum is None or angka > maksimum:
        maksimum = angka

if maksimum is None:
    print("Tidak ada bilangan yang dimasukkan.")
else:
    print("Bilangan terbesar adalah:", maksimum)
