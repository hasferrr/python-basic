# Program Manajemen Kontak
import function

# Daftar kontak dalam bentuk Dictionary di dalam List

daftar_kontak = []

daftar_kontak.append(
{
        'nama' : 'ayaka',
        'email' : 'ayaka@gmail.com',
        'nomor telepon' : '098877'
    }
)

# Menu
while True:
    print()
    print('Menu')
    print('1. Daftar kontak')
    print('2. Buat kontak')
    print('3. Cari kontak')
    print('4. Hapus kontak')
    print('5. Edit kontak')
    print('0. Keluar')
    
    menu = input('Pilih Menu : ')
    print()
    
    if menu == '0':
        break

    if menu == '1':
        function.tampilkan_kontak(daftar_kontak)
        function.pause()
    
    if menu == '2':
        kontak_baru = function.buat_kontak()
        daftar_kontak.append(kontak_baru)
        function.pause()

    if menu == '3':
        function.cari_kontak(daftar_kontak)
