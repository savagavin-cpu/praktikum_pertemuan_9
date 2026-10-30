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