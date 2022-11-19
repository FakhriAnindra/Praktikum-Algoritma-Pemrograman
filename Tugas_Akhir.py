# Tugas Akhir Praktikum Algoritma Pemrograman
# Create by Muhammad Fakhri Anindra

"""
Kasir RM Padang Elok Basamo

Program ini berfungsi untuk melakukan pencetakan bon total harga makanan RM Padang. Program akan 
meminta memasukan identitas customer, kemudian menghitung biaya dari total harga makanan tersebut dan
mencetak bon hasil transaksi.
"""
import datetime

identitas = ["Nama Pelanggan", "Alamat", "No Telepon", "Porsi", "Menu"]
data = []
biayaLayanan = 0
tanggal = datetime.datetime.now()

print(30*"="+"""
Nama\t: Muhammad Fakhri Anindra
NIM\t: 2270231067
Program\t: RM Padang
""" + 30*"=" + "\n")

for x in range(len(identitas)):
    val = input("Masukkan " + identitas[x] + ": ")
    data.append(val)

serviceCheck = str(data[4]).upper()

if(serviceCheck == "nasi rendang"):
    biayaLayanan = 15000* int(data[3])
elif(serviceCheck == "nasi dendeng balado"):
    biayaLayanan = 20000 * int(data[3])
else:
    print("Harap masukkan menu")

print("\n"+15*"=" + "Transaksi RM Padang" + 15*"="+"\n") 

print("Tanggal : " + tanggal.strftime("%d - %m - %Y %X"))

for x in range(4):
    print(identitas[x] + " : " + data[x])

if(biayaLayanan % 15000 == 0):
    print("Menu : 15000/Porsi")
else:
    print("Menu : 20000/Porsi")
print("Total biaya: " + str(biayaLayanan))