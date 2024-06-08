nama_depan = input('Nama depan : ')
nama_belakang = input('Nama belakang : ')
NIM = input('NIM : ')
nama_lengkap = nama_depan + (" ")+ nama_belakang
print(" ")

kata_prodi = 'Pendidikan Teknik Informatika'
kata_fakultas = 'Fakultas Keguruan Dan Ilmu Pendidikan'
kata_universitas = 'Universitas Muhammadiyah Surakarta'

print (kata_prodi.center(60))
kapital = kata_universitas.upper()
print(" ")
print('Nama : {}'.format(nama_lengkap))
print('NIM : {}'.format(NIM))
print('{}'.format(kata_fakultas))
print(" ")
print(kapital.center(60))