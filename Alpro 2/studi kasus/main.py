import data_array as ar
import stok_gudang as gd
import os
import time

lagi = True
menus = """1. Mengurutkan NIM;
2. Cari NIM;
3. Gudang;
4. Exit."""

#Data NIM // ada 50 NIM random
nim = [2200016101, 2200016139, 2200016120, 2200016115, 2200016123, 2200016119, 2200016126, 2200016114, 
       2200016111, 2200016104, 2200016134, 2200016128, 2200016102, 2200016105, 2200016142, 2200016110, 
       2200016149, 2200016108, 2200016147, 2200016103, 2200016144, 2200016129, 2200016140, 2200016117, 
       2200016131, 2200016132, 2200016112, 2200016130, 2200016137, 2200016107, 2200016145, 2200016118, 
       2200016124, 2200016121, 2200016143, 2200016106, 2200016138, 2200016148, 2200016135, 2200016146, 
       2200016136, 2200016141, 2200016127, 2200016116, 2200016147, 2200016113, 2200016125, 2200016149, 
       2200016109, 2200016148, 2200016150, 2200016142]

#Gudang
warehouse_capacity = 100 #kapasistas gudang
gudang = gd.Gudang(warehouse_capacity)

def gudang_menu() :
    while True :
        menus = """1. Jumlah Barang;
2. Kapasitas;
3. Restock barang;
4. Kembali;
5. Exit."""
        print(menus)
        ask_user = int(input("Pilih Menu : "))
        if ask_user == 1 :
            gudang.tampilkan_jumlah_barang()
        elif ask_user == 2 :
            gudang.tampilkan_sisa_kapasitas()
        elif ask_user == 3 :
            restock_amount = int(input("Jumlah Restock : "))
            gudang.restok_barang(restock_amount)
        elif ask_user == 4 :
            return
        elif ask_user == 5 :
            global lagi
            lagi = False
            return
        else :
            print("Error, Coba Lagi")
        time.sleep(3)
        os.system('cls')

def main_menu(ask_user) :
    global nim
    if ask_user == 1 :
        print("Setelah diurutkan : ", ar.selectionSort(nim))
        time.sleep(10)
    elif ask_user == 2 :
        cari_nim = int(input("Masukkan NIM yang dicari : "))
        posisi = ar.search(nim, cari_nim)
        if posisi is not None :
            print("Data Ditemukan di Posisi : ", posisi)
        else :
            print("Data Tidak Ditemukan")
    elif ask_user == 3 :
        os.system('cls')
        gudang_menu()
    elif ask_user == 4 :
        global lagi
        lagi = False
    else :
        print("Error, Coba Lagi")
        user_input = int(input("Pilih menu : "))
        main_menu(user_input)

while lagi:
    print(menus)
    user_input = int(input("Pilih menu : "))
    main_menu(user_input)
    time.sleep(3)
    os.system('cls')

print("Program Ended")