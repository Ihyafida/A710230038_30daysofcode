a = int(input("masukan jumlah anak bebek: "))
print("tek kotek kotek kotek")
if a>=2:
    while a>1:
        print("anak bebek turun %d mati satu tinggal %d"%(a,a-1))
        a = a-1
        if a<=1:
            print("anak bebek turun %d mati satu tinggal induknya"%(a))
else:
    print("anak bebek ada %d beli lagi aja yang banyak"%(a))