mahasiswa = {'nama':'Andika','umur': 21}
mahasiswa ['umur'] = 19
mahasiswa ['Alamat'] = 'sragen' 
mahasiswa ['angkatan'] = 2020
print(mahasiswa)
print(mahasiswa.pop('angkatan'))
print(mahasiswa)
print('nama' in mahasiswa)
print(len(mahasiswa))
print(sorted(mahasiswa))
mahasiswa.clear()
print(mahasiswa)