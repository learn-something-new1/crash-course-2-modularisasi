#from geometri.segitiga import hitung_luas_segitiga
# import geometri.segitiga as gs
from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegi_panjang
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
print(f'Hitung luas segitiga {hitung_luas_segitiga(10, 6)}')

print(info_persegi_panjang())
print(f'Hitung luas persegi panjang {hitung_luas_persegi_panjang(10, 6)}')