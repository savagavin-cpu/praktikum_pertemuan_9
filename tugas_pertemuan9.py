#LATIHAN

#1. kendaraan = ["motor","mobil","sepeda","bus"]

#a. tambahkan "truk di akhir list"
data = ["motor","mobil","sepeda","bus","truck"]
print (data)

#b. sisipkan becak pada index 1.
data = ["motor","mobil","sepeda","bus","truck"]
data.insert (1, "becak")
print (data)

#c. hapus data yang berada di paling belakang.
data = ["motor","mobil","sepeda","bus","truck"]
data.remove ("truck")
print (data)

#d. ubah elemen "sepeda" menjadi "skuter"
data = ["motor","mobil","sepeda","bus","truck"]
data [2] ="skuter"
print (data)

#e. tampilkan informasi jumlah total data di dalam list tersebut.
data = ["motor","mobil","sepeda","bus","truck"]
panjang_data = len (data)
print(f"panjang data = {panjang_data}")


#2. angka = [75, 80, 90, 75, 85, 100, 65]

#a. cari tahu di indeks ke berapa skor 100 berada.
data = [75,80,90,75,85,100,65]
print(f"angka 100 berada di index = {data.index(100)}")

#b. hitung ada berapa banyak siswa yang mendapat skor 75
jumlah_75 = data.count(75)
print(f"siswa yang mendapat 75 = {jumlah_75}")

#c. urutkan list skor_ujian tersebut dari terkecil hingga terbesar.
print(f"data sebelum sort \n{data}")
data.sort()
print(f"data angka sort \n{data}")

#d. balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.
data.reverse()
print(f"data di reverse \n{data}")


#3. menu utama = nasi goreng, mie ayam
#   menu tambahan = kerupuk, es teh

#gabungkan menu tambahan kedalam menu utama.
menu_utama = ["nasi goreng", "mie ayam"]
menu_tambahan = ["kerupuk", "es teh"]

menu_utama.extend(menu_tambahan)
print(f"menu gabungan \n{menu_utama}")


#4. diberikan data nested list:
data_barang = [["buku", 5000], ["pensil", 2000], ["penggaris", 3000]]

#a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom.
harga_pensil = data_barang[1][1]
print(f"harga pensil = {harga_pensil}")

#b. gunakan perulangan untuk membaca data satu persatu.
barang_0 = ["buku", 5000]
barang_1 = ["pensil", 2000]
barang_2 = ["penggaris", 3000]

list_barang = [barang_0, barang_1, barang_2]
print(f"barang = {list_barang}")

for barang in list_barang:
    print(f"nama\t : {barang[0]}")
    print(f"harga\t : {barang[1]}")