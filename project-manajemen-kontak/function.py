# Function

def tampilkan_kontak(daftar_kontak):
    print('==========Daftar Kontak==========')
    for data in daftar_kontak:
        print()
        print(f'Nama : {data["nama"]}')
        print(f'Email : {data["email"]}')
        print(f'Nomor Telepon : {data["nomor telepon"]}')

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
    cari = input('Cari nama : ')
    x = 0

    for data in daftar_kontak:       
        if data['nama'].lower().find(cari.lower()) != -1:
            print()
            x += 1
            if x == 1:
                print('==========Daftar Kontak==========')
            print(f'Nama : {data["nama"]}')
            print(f'Email : {data["email"]}')
            print(f'Nomor Telepon : {data["nomor telepon"]}')
    if x == 0:
        print('Tidak ada kontak yang ditemukan')

def hapus_kontak(daftar_kontak):
    cari = input('Cari nama : ')        # input nama kontak
    
    kontak_sementara = []               # untuk menampung kontak hasil pencarian yang akan dihapus
    i = 0

    for data in daftar_kontak:          # <------ data menjadi dictionary {'nama':'value',}
        if data['nama'].lower().find(cari.lower()) != -1:
            print()
            i += 1
            if i == 1:
                print('==========Pilih kontak yang akan dihapus==========')
            print(i)
            print(f'Nama : {data["nama"]}')
            print(f'Email : {data["email"]}')
            print(f'Nomor Telepon : {data["nomor telepon"]}')
            kontak_sementara.append(data)    
    
    if kontak_sementara != []:          # kontak DITEMUKAN
        
        try:
            print()
            print('Pilih 0 untuk membatalkan')
            pilih_index = int(input('Hapus kontak ke : '))          # user MEMILIH
            if pilih_index == 0:
                return
        except:
            print("Kontak tidak tersedia")
            return
        
        try:
            kontak_akan_dihapus = kontak_sementara[pilih_index-1]   # {'nama':'value'} yg akan dihapus
        except:
            print("Kontak tidak tersedia")
            return

        if pilih_index > 0:
            print()
            print('==========Apakah kamu yakin akan menghapus kontak?==========')
            print(f'Nama : {kontak_akan_dihapus["nama"]}')
            print(f'Email : {kontak_akan_dihapus["email"]}')
            print(f'Nomor Telepon : {kontak_akan_dihapus["nomor telepon"]}')
            print()

            confirm = input('"y" untuk hapus, "n" untuk batal : ').lower()

            if confirm == 'y':
                daftar_kontak.remove(kontak_akan_dihapus)
                print()
                print('Kontak berhasil dihapus')
            else:
                print('Penghapusan dibatalkan')
        
        else:
            print("Kontak tidak tersedia")

    else:                               # TIDAK ADA kontak yang DITEMUKAN
        print('Tidak ada kontak yang ditemukan')

def edit_kontak(daftar_kontak):
    cari = input('Cari nama : ')        # input nama kontak
    
    kontak_sementara = []               # untuk menampung kontak hasil pencarian yang akan dihapus
    i = 0

    for data in daftar_kontak:          # <------ data menjadi dictionary {'nama':'value',}
        if data['nama'].lower().find(cari.lower()) != -1:
            print()
            i += 1
            if i == 1:
                print('==========Pilih kontak yang akan di-edit==========')
            print(i)
            print(f'Nama : {data["nama"]}')
            print(f'Email : {data["email"]}')
            print(f'Nomor Telepon : {data["nomor telepon"]}')
            kontak_sementara.append(data)    

    # Mencegah error 'cannot unpack non-iterable NoneType object' ketika return
    index_kontak = -1
    kontak_diedit = -1

    if kontak_sementara != []:          # kontak DITEMUKAN

        try:
            print()
            print('Pilih 0 untuk membatalkan')
            pilih_index = int(input('Edit kontak ke : '))          # user MEMILIH
            if pilih_index == 0:
                return index_kontak, kontak_diedit
        except:
            print("Kontak tidak tersedia")
            return index_kontak, kontak_diedit
        
        try:
            kontak_akan_diedit = kontak_sementara[pilih_index-1]   # {'nama':'v', 'email':'v', 'nt':'v'} yg akan DIEDIT
            index_kontak = daftar_kontak.index(kontak_akan_diedit)
        except:
            print("Kontak tidak tersedia")
            return index_kontak, kontak_diedit

        if pilih_index > 0:
            print()
            print('==========Kontak yang akan di-edit==========')
            print(f'Nama : {kontak_akan_diedit["nama"]}')
            print(f'Email : {kontak_akan_diedit["email"]}')
            print(f'Nomor Telepon : {kontak_akan_diedit["nomor telepon"]}')
            print()
            print('==========Edit kontak; kosongkan untuk tidak mengubahnya==========')
            nama_baru = input('Nama : ')
            email_baru = input('Email : ')
            no_telp_baru = input('Nomor Telepon : ')

            # Default value
            if nama_baru == "":
                nama_baru = kontak_akan_diedit['nama']
            if email_baru == "":
                email_baru = kontak_akan_diedit['email']
            if no_telp_baru == "":
                no_telp_baru = kontak_akan_diedit['nomor telepon']

            # Variabel yang menampung kontak editan
            kontak_diedit = {'nama':nama_baru,'email':email_baru,'nomor telepon':no_telp_baru}
            
            # Jika semuanya default
            if nama_baru == kontak_akan_diedit['nama'] and email_baru == kontak_akan_diedit['email'] and no_telp_baru == kontak_akan_diedit['nomor telepon']:
                print('Kontak tidak diedit')

        else:
            print("Kontak tidak tersedia")

    else:                               # TIDAK ADA kontak yang DITEMUKAN
        print('Tidak ada kontak yang ditemukan')

    return index_kontak, kontak_diedit

# Other Function

def pause():
    programPause = input('\n'+"Tekan <ENTER> untuk kembali ke menu...")
