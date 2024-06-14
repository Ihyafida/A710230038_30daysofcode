phone_book = {}
for i in range(5):
    nama = input("masukkan nama teman ke-{}: ".format(i+1))
    no_hp = input("masukkan nomor handphone teman ke-{}: ".format(i+1))
    phone_book[nama] = no_hp
print("phone book".center(60))
for i, (nama, no_hp)in enumerate(phone_book.items(), 1):
    print("{}. {} = {}".format(i, nama, no_hp))