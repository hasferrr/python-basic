# Function

def tampilkan_kontak(daftar_kontak):
    for data in daftar_kontak:
        print(f'Nama : {data["nama"]}')
        print(f'Email : {data["email"]}')
        print(f'Nomor Telepon : {data["nomor telepon"]}')
        print()

def buat_kontak():
    nama_baru = input('Masukkan Nama Anda : ')
    email_baru = input('Masukkan Email Anda : ')
    nomor_telepon_baru = input('Masukkan Nomor Telepon Anda : ')
    
    kontak_baru = {
        'nama' : nama_baru,
        'email' : email_baru,
        'nomor telepon' : nomor_telepon_baru
    }
    return kontak_baru

def cari_kontak(daftar_kontak):
    type_nama = input('Cari nama : ')
    if type_nama.lower() in daftar_kontak[0]['nama'].lower():
        print('yess') # BELUM SELESAI
        # <-----------------------------------------

# Other Function

def pause():
    programPause = input('\n'+"Tekan <ENTER> untuk kembali ke menu...")
