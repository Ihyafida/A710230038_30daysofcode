counter = 0
total = 0

jumlah_barang = int(input('masukan jumlah barang : '))
while counter < jumlah_barang:
    harga = int(input('masukkan jumlah barang ke-{}: '.format(counter+1)))
    jumlah = int(input('masukkan jumlah barang ke-{}: '.format(counter+1)))
    total = total + (harga*jumlah)
    counter = counter+1

print('Total harga barang :',total)