admin = {
    'username' : ['admin1', 'admin2'],
    'name' : ['fakhriza', 'arden'],
    'password' : ['123', '321']
}

manager = {
    'username' : ['manager1', 'manager2'],
    'name' : ['raden', 'bondan'],
    'password' : ['123', '321']

}

pembeli = {
    'username' : ['haikal', 'luna'],
    'name' : ['ali', 'aulia'],
    'password' : ['123', '321']
}

database = {
    'penerbangan' : {
        'seat' : {
            'regular' : 1,
            'premium' : 2,
            'firstclass': 3
        }, 
        'rute' : {
            'bandung' : 1000,
            'jakarta' : 2000,
            'surabaya' : 1000, 
            'pekanbaru' : 500
        }
    },
    'armada' : {
        'tv_girl' : {
            'vocal' : 'alex',
            'guitarist' : 'mark',
            'drummer' : 'john',
            'harga' : 5000
        },
        'grrl_gen' : {
            'vocal' : 'maudy',
            'guitarist' : 'djadjat',
            'dummer' : 'sucipto',
            'harga' : 7000
        }
    },
    'tiket' : {
        'stok' : {
            'tv_girl' : {
                150 : 10,
                151 : 10
            },
            'grrl_gen' : {
                140 : 10,
                141 : 10
            }
        }
    },
    'pembeli' : {
        'tv_girl' : {
            'nama' : ['haikal', 'luna'],
            'tanggal' : [150, 151],
            'pesawat' : [3000, 2500],
            'seat' : [3, 3],
            'jumlah' : [5, 5]
        },
        'grrl_gen' : {
            'nama' : ['aulia', 'ali'],
            'tanggal' : [140, 141],
            'pesawat' : [2500, 2000],
            'seat' : [2, 3],
            'jumlah' : [5, 10]
        }
    }
}

class Aplikasi:
    def __init__(self, username, name, password, pengguna):
        self.username = username    # isinya username
        self.name = name            # isinya nama user
        self._password = password   # isinya password username
        self.pengguna = pengguna    # isinya jenis pengguna, admin, manager, pembeli
    
    def main_menu(self):
        print('Login Sebagai: ')
        print('1. Admin')
        print('2. Manager')
        print('3. Pembeli')

    def userlogin(self):
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')
        return username, password
    
    def login(self, pengguna):
        username, password = self.userlogin()
        for username_stored, name_stored, password_stored in zip(pengguna['username'], pengguna['name'], pengguna['password']):
            if username == username_stored and password == password_stored:
                return username_stored, name_stored, password_stored
        else:
            return '', '', ''
    
    def verifikasi(self, username, name, password):
        if username != '' and name != '' and password !='':
            return True
        else:
            return False
        
    def buat_akun(self):
        print('Harap Isi Data Dibawah Ini :')
        pembeli['username'].append(input('Username : '))
        pembeli['name'].append(input('Nama : '))
        pembeli['password'].append(input('Password: '))
        print('Data Behasil Di Tambahkan !')
    
    def ubah_tanggal(self, jenis, tanggal):
        if jenis == 'dd/mm':
            hari, bulan = map(int, tanggal.split('/'))
            tanggal_per_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if bulan < 1 or bulan > 12 or hari < 1 or hari > tanggal_per_bulan[bulan]:
                return 0
            
            hasil = sum(tanggal_per_bulan[:bulan]) + hari
            return hasil
        elif jenis == '365':
            tanggal_per_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if tanggal < 1 or tanggal > 365:
                return 0
            bulan = 1
            while tanggal > tanggal_per_bulan[bulan]:
                tanggal -= tanggal_per_bulan[bulan]
                bulan += 1
            hasil = tanggal
            return f'{hasil:02d}/{bulan:02d}'
        
class Admin(Aplikasi):
    def __init__(self, username, name, password, pengguna):
        super().__init__(username, name, password, pengguna)

    def main_menu(self):
        print('Pilih Opsi Yang Ingin Digunakan: ')
        print('1. Tambah Manager')
        print('2. Edit Manager')
        print('3. Hapus Manger')
        print('4. Keluar')

    def tambah_data(self):
        print('Masukkan Data Manager Yang Mau Ditambah: ')
        manager['username'].append(input('Masukkan Username: '))
        manager['name'].append(input('Masukkan Nama Manager: '))
        manager['password'].append(input('Masukkan Password Manager: '))

    def edit_data(self):
        print('Masukkan Data Manager Yang Mau Diganti: ')
        username, password = self.userlogin()
        for indeks, username_stored, in enumerate(manager['username']):
            if username == username_stored:
                manager['username'][indeks] = input('Masukkan Username Baru: ')
                manager['name'][indeks] = input('Masukkan Nama Manager Baru: ')
                manager['password'][indeks] = input('Masukkan Password Baru: ')
                print('Data Berhasil Diganti !')
        else:
            print('Data Tidak Ditemukan !')

    def hapus_data(self):
        print('Masukkan Data Manager Yang Ingin Dihapus: ')
        username, password = self.userlogin()
        for username_stored, name_stored, password_stored in zip(manager['username'], manager['name'], manager['password']):
            if username == username_stored and password == password_stored:
                manager['username'].remove(username_stored)
                manager['name'].remove(name_stored)
                manager['password'].remove(password_stored)
                print('Data Telah Dihapus!')
        else:
            print('Data Tidak Ditemukan !')

class Manager(Aplikasi):
    def __init__(self, username, name, password, pengguna):
        super().__init__(username, name, password, pengguna)
    
    def main_menu(self):
        print('Pilih Opsi:')
        print('1. Tambah/Edit Data Penerbangan')
        print('2. Tambah/Edit Data Armada')
        print('3. Ubah Harga Tiket')
        print('4. Tampilkan Data Penerbangan')
        print('5. Tampikan Data Armada')
        print('6. Tampilkan Tiket Terjual')
        print('7. Tampilkan Daftar Pembeli')
        print('8. Tampilkan Total Penjualan dan Sisa Tiket')
        print('9. Keluar')

    def tampil_data(self, kategori_1, kategori_2):
        for key, value in database[kategori_1][kategori_2].items():
            print(f'{key}\t{value}')

    def ganti_data(self, cari_kategori , kategori_1, kategori_2, key, value):
        if cari_kategori in database[kategori_1] and key not in database[kategori_1][kategori_2]:
            return False
        database[kategori_1][kategori_2][key] = value
        return True
    
    def tambah_data(self, cari_kategori, kategori_1, kategori_2, key, value):
        if cari_kategori in database[kategori_1]:
            database[kategori_1][kategori_2].update({key : value})
            print('Data Telah Ditambahkan !')
        else:
            print('Data Tidak Berhasil Ditambahkan')

    def penerbangan(self):
        print('Pilih Opsi: ')
        print('1. Tambah Data')
        print('2. Edit Data')
        opsi = int(input('Pilihan Kamu: '))

        if opsi == 1:
            self.tambah_data_penerbangan()
        elif opsi == 2:
            self.edit_data_penerbangan()
        else:
            print('Harap Pilih Opsi Yang Ada')

    def tambah_data_penerbangan(self):
        print('Harap Isi Data Berikut')
        print('1. Tambah Data Seat')
        print('2. Tambah Data Rute')
        opsi = int(input('Opsi Kamu: '))

        if opsi == 1:
            print('Tolong Isi Data Dibawah Ini')
            seat_baru = input('Jenis Seat Baru: ')
            harga_baru = int(input('Harga Seat Baru: '))
            self.tambah_data('seat', 'penerbangan', 'seat', seat_baru, harga_baru)
        elif opsi == 2:
            print('Tolong Isi Data Dibawah Ini')
            rute_baru = input('Kota Baru: ')
            harga_baru = int(input('Biaya Penerbangan: '))
            self.tambah_data(rute_baru, 'penerbangan', 'rute', rute_baru, seat_baru)
        else:
            print('Harap Pilih Opsi Yang Ada')

    def edit_data_penerbangan(self):
        print('Harap Isi Data Berikut')
        print('1. Ganti Data Seat')
        print('2. Ganti Data Rute')
        opsi = int(input('Opsi Kamu: '))

        if opsi == 1:
            self.tampil_data('penerbangan', 'seat')
            key = input('Seat Yang Ingin Diganti: ')
            value = int(input('Harga Seat Yang Baru: '))
            self.ganti_data('seat', 'penerbangan', 'seat', key, value)
        elif opsi == 2:
            self.tampil_data('penerbangan', 'rute')
            key = input('Seat Yang Ingin Diganti: ')
            value = int(input('Harga Seat Yang Baru: '))
            self.ganti_data('rute', 'penerbangan', 'rute', key, value)
        else:
            print('Harap Pilih Opsi Yang Ada')

    def armada(self):
        print('Pilih Opsi: ')
        print('1. Tambah Data')
        print('2. Edit Data')
        opsi = int(input('Pilihan Kamu: '))

        if opsi == 1:
            self.tambah_data_armada()
        elif opsi == 2:
            self.edit_data_armada()
        else:
            print('Harap Pilih Opsi Yang Ada')

    def tambah_data_armada(self):
        print('Tolong Isi Data Dibawah Ini: ')
        band_baru = input("Masukkan Nama Band Yang Dipisah Oleh Underscore '_' : ")
        vocalist = input('Masukkan Nama Vokalist : ')
        guitarist = input('Masukkan Nama Guitarist : ')
        drummer = input('Masukkan Nama Drummer : ')
        harga = int(input('Masukkan Harga Panggung : '))

        verif = input('Data Telah Sesuai (y/n) : ')
        if verif == 'y':
            database['armada'][band_baru] = {
                'vocal': vocalist,
                'guitarist': guitarist,
                'drummer': drummer,
                'harga': harga
            }
        else:
            self.tambah_data_armada()

    def edit_data_armada(self):
        print('Tolong Isi Data Dibawah Ini: ')
        band = input("Masukkan Nama Band Yang Dipisah Oleh Underscore '_' : ")
        vocalist = input('Masukkan Nama Vokalist : ')
        guitarist = input('Masukkan Nama Guitarist : ')
        drummer = input('Masukkan Nama Drummer : ')
        harga = int(input('Masukkan Harga Panggung : '))

        verif = input('Data Telah Sesuai (y/n) : ')
        if verif == 'y' and band in database['armada']:
            database['armada'][band] = {
                'vocal': vocalist,
                'guitarist': guitarist,
                'drummer': drummer,
                'harga': harga
            }
        else:
            print('Band Tidak Ditemukan !')

    def ganti_harga(self):
        print('Band\tHarga')
        for band in database['armada']:
            for key, value in database['armada'][band].items():
                if key == 'harga':
                    print(f'{band}\t{value}')
        print('Masukkan Band Yang Ingin Diganti Harganya:')
        band = input('Nama Band: ')
        harga_baru = int(input('Harga Baru: '))
        self.ganti_data('armada', 'armada', band, 'harga', harga_baru)

    def tampil_data_penerbangan(self):
        print('Rute\tHarga')
        self.tampil_data_data('penerbangan', 'rute')
    
    def tampil_data_band(self):
        print('Band\tVocal\tGuitarist\tDrummer\tHarga Panggung')
        for band, personil in database['armada'].items():
            vocal, gitar, drum, harga = personil['vocal'], personil['guitarist'], personil['drummer'], personil['harga']
            print(f'{band}\t{vocal}\t{gitar}\t{drum}\t{harga}')

    def tampil_tiket_terjual(self):
        print('Band\tTanggal\tTiket Terjual')
        for band, days in database['tiket']['stok'].items():
            for day, tickets_sold in days.items():
                print(f'{band}\t{day}\t{tickets_sold}')
        
    def tampil_daftar_pembeli(self):
        print('Nama\tBand\tTanggal\tJumlah')
        for band, detil in database['pembeli'].items():
            for i in range(len(detil['nama'])):
                nama = detil['nama'][i]
                tanggal = detil['tanggal'][i]
                jumlah = detil['jumlah'][i]
                print(f'{nama}\t{band}\t{tanggal}\t{jumlah}')

    def tampil_penjualan_sisa(self):
        print('Band\tKeuntungan')
        for band, detil in database['pembeli'].items():
            for i in range(len(detil['nama'])):
                nama = detil['nama'][i]
                tanggal = detil['tanggal'][i]
                pesawat = detil['pesawat'][i]
                seat = detil['seat'][i]
                jumlah = detil['jumlah'][i]

                total = database['tiket']['stok'][band][tanggal] * database['penerbangan']['rute'][pesawat] * database['penerbangan']['seat'][seat] * jumlah
                print(f'{band}\t{total}')
            
class Pembeli(Aplikasi):
    def __init__(self, username, name, password, pengguna):
        super().__init__(username, name, password, pengguna)

    def main_menu(self):
        print('Pilih Opsi')
        print('1. Tampilkan Dan Cari Penerbangan')
        print('2. Tampilkan Dan Cari Tiket')
        print('3. Pesan Tiket')
        print('4. Keluar')  
        
    def tampil_daftar(self, cari):
        tipe = cari
        for tipe_item, keterangan_item in database[cari].items():
            nama = tipe_item
            keterangan = list(keterangan_item.keys())
            harga = list(keterangan_item.values())
            print(f'{nama}')
            for i in range(len(keterangan)):
                print(f'.\t{keterangan[i]}\{harga[i]}')

    def cari_item(self, data, cari, tipe):
        if tipe in database[data][cari]:
            return database[data][cari][tipe]
        else:
            return '0'
        
    def login(self):
        print('Harap Masuk Menggunakan Akun Kamu : ')
        self.verifikasi(self.pengguna)

    def tampil_daftar_dan_cari_penerbangan(self):
        print('Jenis\tJenis\tKeterangan')
        self.tampil_daftar('penerbangan')
        cari = input('Silakan Masukkan Jenis Yang Ingin dicari lebih lanjut: ')  # Isinya Seat Atau Rute
        keterangan = input('Silakan Masukkan Keterangan Yang Ingin Dicari: ')
        if self.cari_item('penerbangan', cari, keterangan) != '0':
            print('Harganya adalah: ' + str(self.cari_item(cari, keterangan)))
        else:
            print('Silakan Cari Dari Pilihan Yang Ada')

    def tampil_daftar_dan_cari_tiket(self):
        print('Band\tTanggal\tHarga')
        self.tampil_daftar('armada')
        cari = input('Silakan Masukkan Band Yang Ingin Anda Cari: ')  # Isinya Tv_Girl Atau Grrl Gen
        keterangan = input('Silakan Masukkan Member Yang Ingin Anda Cari: ')
        if self.cari_item('armada', cari, keterangan) != '0':
            print(f'{keterangan} : {self.cari_item(cari, keterangan)}')
        else:
            print('Silakan Cari Dari Pilihan Yang Ada')     

    def pesan_tiket(self):
        print('Silakan Isi Data Berikut: ')
        nama = input('Masukkan Nama Anda: ')
        band = input('Masukkan Nama Band Yang Ingin Ditonton: ')
        tanggal = input('Masukkan Tanggal Format dd/mm : ')
        asal = input('Masukkan Kota Asal: ')
        tujuan = input('Masukkan Kota Tujuan: ')
        kursi = input('Masukkan Jenis Kursi Pesawat: ')
        jumlah = int(input('Masukkan Tiket Yang Dibeli: '))
        fix = input('Apakah Sudah Sesuai (y/n) ? ') 
    
        if fix == 'y':
            biaya = database['penerbangan']['rute'][asal] + database['penerbangan']['rute'][tujuan]
            if kursi in database['penerbangan']['seat']:
                kelas =  database['penerbangan']['seat'][kursi]
            hari = self.ubah_tanggal('dd/mm', tanggal)
            database['pembeli'][band]['nama'].appned(nama)
            database['pembeli'][band]['tanggal'].apend(hari)
            database['pembeli'][band]['pesawat'].append(biaya)
            database['pembeli'][band]['seat'].append(kelas)
            database['pembeli'][band]['jumlah'].append(jumlah)

aplikasi = Aplikasi('', '', '', '')

start = True
while start == True:
    aplikasi.main_menu()
    opsi = int(input('Masukkan Pilihan Anda: '))

    if opsi == 1:
        username_admin, nama_admin, password_admin = aplikasi.login(admin)
        if aplikasi.verifikasi(username_admin, nama_admin, password_admin):
            while True:
                admin = Admin(username_admin, nama_admin, password_admin, admin)
                admin.main_menu()
                pilihan = int(input('Masukkan Pilihan Kamu: '))

                if pilihan == 1:
                    admin.tambah_data()
                elif pilihan == 2:
                    admin.edit_data()
                elif pilihan == 3:
                    admin.hapus_data()
                elif pilihan == 4:
                    break
                else:
                    print('Pilih Silakan Pilih Pilihan Yang Ada')
        else:
            print('Akun Tidak Ditemukan !')

    elif opsi == 2:
        username_manager, nama_manager, password_manager = aplikasi.login(manager)
        if aplikasi.verifikasi(username_manager, nama_manager, password_manager):
            while True:
                manager = Manager(username_manager, nama_manager, password_manager, manager)
                manager.main_menu() 
                pilihan = int(input('Masukkan Pilihan Kamu: '))

                if pilihan == 1:
                    manager.penerbangan()
                elif pilihan == 2:
                    manager.armada()
                elif pilihan == 3:
                    manager.ganti_harga()
                elif pilihan == 4:
                    manager.tampil_data_penerbangan()
                elif pilihan == 5:
                    manager.tampil_data_band()
                elif pilihan == 6:
                    manager.tampil_tiket_terjual()
                elif pilihan == 7:
                    manager.tampil_daftar_pembeli()
                elif pilihan == 8:
                    manager.tampil_penjualan_sisa()
                elif pilihan == 9:
                    break
                else:
                    print('Harap Pilih Pilihan Yang Ada')
        else:
            print('Akun Tidak Ditemukan !')

    elif opsi == 3:
        username_buyer, nama_buyer, password_buyer = aplikasi.login(pembeli)
        if aplikasi.verifikasi(username_buyer, nama_buyer, password_buyer):
            while True:
                buyer = Pembeli(username_buyer, nama_buyer, password_buyer, pembeli)
                buyer.main_menu()
                pilihan = int(input('Masukkan Pilihan Kamu: '))

                if pilihan == 1:
                    buyer.tampil_daftar_dan_cari_penerbangan()
                elif pilihan == 2:
                    buyer.tampil_daftar_dan_cari_tiket()
                elif pilihan == 3:
                    buyer.pesan_tiket()
                elif pilihan == 4:
                    break
                else:
                    print('Harap Pilih Pilihan Yang Ada')
        else:
            print('Akun Tidak Ditemukan !')

            masuk = input('Buat Akun (y/n) ?')

            if masuk == 'y' :
                aplikasi.buat_akun()
            