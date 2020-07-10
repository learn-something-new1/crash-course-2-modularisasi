"""
Program menghitung luas segitiga
luas-segitiga = alas * tinggi /2
"""
print('\nMenghitung Segitiga 1')
alas = 10
tinggi =6
luas_segitiga = alas * tinggi /2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMenghitung Segitiga 2 dengan copy paste')
alas = 20
tinggi =2
luas_segitiga = alas * tinggi /2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMembuat Fungsi Hitung Luas Segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')