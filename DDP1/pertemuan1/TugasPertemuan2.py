# Input untuk persegi
sisi = float(input("Masukkan panjang sisi persegi: "))
luas_persegi = sisi * sisi
print(f"\nLuas Persegi = {luas_persegi}")

# Input untuk persegi panjang
panjang = float(input("\nMasukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
luas_persegi_panjang = panjang * lebar
print(f"Luas Persegi Panjang = {luas_persegi_panjang}")

# Input untuk segitiga
alas = float(input("\nMasukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
luas_segitiga = 0.5 * alas * tinggi
print(f"Luas Segitiga = {luas_segitiga}")

# Input untuk lingkaran
jari_jari = float(input("\nMasukkan jari-jari lingkaran: "))
luas_lingkaran = 3.14 * jari_jari * jari_jari
print(f"Luas Lingkaran = {luas_lingkaran}")

# Perbandingan luas persegi dan persegi panjang
print("\nPerbandingan Persegi dan Persegi Panjang:")
if luas_persegi > luas_persegi_panjang:
    print("Luas Persegi lebih besar dari Luas Persegi Panjang")
elif luas_persegi < luas_persegi_panjang:
    print("Luas Persegi lebih kecil dari Luas Persegi Panjang")
else:
    print("Luas Persegi sama dengan Luas Persegi Panjang")

# Perbandingan luas segitiga dan lingkaran
print("\nPerbandingan Segitiga dan Lingkaran:")
if luas_segitiga > luas_lingkaran:
    print("Luas Segitiga lebih besar dari Luas Lingkaran")
elif luas_segitiga < luas_lingkaran:
    print("Luas Segitiga lebih kecil dari Luas Lingkaran")
else:
    print("Luas Segitiga sama dengan Luas Lingkaran")