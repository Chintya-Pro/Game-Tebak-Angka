import random

angka = random.randint(1,20)  
maksimum = 3
nomor = 0
benar = False

print('Komputer telah memilih angka secara acak dari 1 s.d 20')
print('anda memiliki {} kali kesempatan untuk menebak'.format(maksimum))

petunjuk = 'Ini adalah tebakan ke-{} anda. Masukkan angka kemudian tekan ENTER '
while not benar and not nomor >= maksimum:
    nomor = nomor + 1
    tebakan = input(petunjuk.format(nomor))
    tebakan = int(tebakan)
    if tebakan == angka:
        benar = True
    elif tebakan > angka:
        print('Angka terlalu besar')
    else:
        print('Angka terlalu kecil')

if benar:
    print('Selamat anda berhasil menebak')
else:
    print('Game Over')
