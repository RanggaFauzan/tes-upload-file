#mesin kasir penjualan risol mayo isi
print(" ")
print("        SELAMAT DATANG DI KING RISOL MAYO       ")
print("                 DAFTAR MENU                     ")
print("|""============================================|")
print("|              RISOL MAYO ISI                |")
print("|""==========|==================|==============|")
print("|   Kode   |        Isi       |    Harga     |")
print("|""==========|==================|==============|")
print("|    B     |       Beef       |   Rp.9000    |")
print("|    A     |       Ayam       |   Rp.8000    |")
print("|    S     |      Sayuran     |   Rp.7000    |")
print("|""==========|==================|==============|")
print(" ")

#input nama pelanggan, no hp, alamat serta tanggal pesanan
nama_pelanggan = str(input("Masukan Nama:"))
no_hp = input("Masukan Nomer HP:")
alamat = str(input("Masukan Alamat:"))
tanggal_pesanan = input("Tanggal pesanan:")
print( )

#menginput banyak jenis pesanan membuat variabel jumlah bayar dan juga list items
banyak_jenis = int(input("Masukan Banyak Jenis Pesanan:"))
jumlah_bayar = 0
items = []

#melakukan perulangan banyak jenis serta menginput kode dan juga banyak pesanan
i = 0
while i < banyak_jenis :
    i += 1
    print("Jenis ke:" , i)
    kode = str(input("Masukan Kode[B/A/S]:"))
    banyak_pesanan = int(input("Masukan Banyak Pesanan:"))
    keterangan = input("Pedas atau tidak [P/T]:")

#menyusun kondisi yang sesuai dengan apa yang kita inginkan
    if kode == "B" :
        jenis = " Beef  "
        harga = int (9000)
        if keterangan == "P":
            ket = " Pedas"
        elif keterangan == "T":
            ket = " Tidak"
    elif kode == "A" :
        jenis = " Ayam  "
        harga = int (8000)
        if keterangan == "P":
            ket = " Pedas"
        elif keterangan == "T":
            ket = " Tidak"
    elif kode == "S" :
        jenis = "Sayuran"
        harga = int (7000)
        if keterangan == "P":
            ket = " Pedas"
        elif keterangan == "T":
            ket = " Tidak"
    else:
        print("Kode Tidak Valid!")
           
#menghitung harga
    jumlah_harga = harga * banyak_pesanan
    jumlah_bayar += jumlah_harga
    items.append((jenis, harga,banyak_pesanan, ket, jumlah_harga))


#menampilkan output
print( )
print("Nama   :", nama_pelanggan)
print("No.Hp  :", no_hp)
print("Alamat :", alamat)
print("Tanggal:", tanggal_pesanan)
print(" ")
print("="*66)
print("                      RISOL MAYO ISI                              ")
print("==================================================================")
print("   Jenis       Harga       Banyak        Pedas/         Jumlah    ")
print("   Isian       Satuan      Beli          Tidak          Harga     ")
print("==================================================================")

#looping serta pemanggilan data dalam literal daftar
for item in items:
    print("  %s       %i         %i          %s          %i "  % item)
print("===================================================================")
print(f"                                     Jumlah Bayar   :Rp.{jumlah_bayar:,.2f}")

#menginput uang bayar serta menghitung uang kembalian
uang_bayar = int(input("Masukan Uang Bayar:Rp"))
kembalian = uang_bayar - jumlah_bayar
print(f"                                     Uang Kembalian :Rp.{kembalian:,.2f}")
print(" ")
print("                TERIMAKASIH TELAH BERBELANJA                        ")
print("               SEMOGA HARI ANDA SELALU BAHAGIA                      ")
print(" ")

print("Rangga ganteng")
