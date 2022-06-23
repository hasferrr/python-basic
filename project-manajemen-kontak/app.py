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
daftar_kontak.append({
        'nama' : 'Ayato',
        'email' : 'ayato@gmail.com',
        'nomor telepon' : '099954'
    })
daftar_kontak.append(
    {
        'nama' : 'lumine',
        'email' : 'lumine@gmail.com',
        'nomor telepon' : '07765'
    })

# Menu
while True:
    print()
    print('==========Menu Utama==========')
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

    elif menu == '1':
        function.tampilkan_kontak(daftar_kontak)
        function.pause()
    
    elif menu == '2':
        kontak_baru = function.buat_kontak()
        daftar_kontak.append(kontak_baru)
        function.pause()

    elif menu == '3':
        function.cari_kontak(daftar_kontak)
        function.pause()

    elif menu == '4':
        function.hapus_kontak(daftar_kontak)
        function.pause()

    elif menu == '5':
        function.edit_kontak(daftar_kontak)
        function.pause()

    else:
        print('Menu tidak tersedia')