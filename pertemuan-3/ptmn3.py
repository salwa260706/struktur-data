# Membuat List
myList = ["Mahardika", 1, True, 4.6]
# List Bersifat mutable / indexing
# untuk menampilkan isi list index ke 0
print(myList[0])
print(myList[-4])

# sifat Slicing
# menampilkan index ke 1 sampai 3
print(f"menampilkan index ke 0-2 {myList[0:3]}")
print(f"dari index awa sampapi ke index 2 {myList[0:3]}")
dataMhs =[{"nama": "Budi", "NIM": "12345", "Prodi" : "Informatika"}, 
          {"nama": "Andi", "NIM": "12346", "Prodi" : "Informatika"}]
# menampilkan list berdasarkan index

# menambahkan nomor urut pada List
no=1
for i in dataMhs:
    no+=1
    print(f"[no=1], nama = {i["nama"]}, NIM = {i["NIM"]}, Prodi ={i["Prodi"]}")
#  Sifat merubah isi List
myList[0] = "informatika"
print(type(dataMhs))
# menghitung jumlah data pada list
print(f"jumlah elemen data List dataMhs = {len(dataMhs)}")
print(f"jumlah elemen data List myList = {len(myList)}")
# menambahkan elemen list 
print(myList)
myList. insert(0,"Mahardika")
print(f"List setelah ditambah didepan{myList}")
# menambahkan elemen di belakang
myList. append("ITEKES")
print(myList)
# menghapus list dengan remove
myList. remove(4.6)
print(myList)
myList.pop(4)
print(myList)
# mengurutkan List
Listwarna = ["merah", "kuning", "hijau", "biru"]
Listwarna.sort()
print(Listwarna)
# membalik List
Listwarna. reverse() 
print(myList)
# menjumlahkan isi list
ListAngka = [1,2,3,4,5]
print(sum(ListAngka))
# membuat saliinan dengan copy
b = Listwarna.copy()
print(b)