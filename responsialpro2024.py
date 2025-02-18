def menu() :
    menu = """Menu : 
0. Exit
1. Baju
2. Celana
3. Topi"""
    print(menu)

def hitung(jumlah, harga) :
    total = jumlah*harga
    if jumlah < 10 :
        diskon = 0.10*total
    elif jumlah <= 20 :
        diskon = 0.20*total
    elif jumlah > 20 :
        diskon = 0.30*total
    else :
        print("Jumlah yang anda masukkan tidak valid, coba lagi")
        return hitung(jumlah, harga)
    print("="*45)
    print(f"Harga sebelum diskon : {total}")
    print(f"Diskon : {int(diskon)}")
    total -= diskon
    print(f"Total Akhir : {int(total)}")
    print("="*45)
    

def belanja() :
    pilihMenu = int(input("Pilih Menu : "))
    if pilihMenu == 0 :
        return 0
    elif pilihMenu == 1 :
        jumlah = int(input("Jumlah Baju : "))
        harga = 30000
    elif pilihMenu == 2 :
        jumlah = int(input("Jumlah Celana : "))
        harga = 45000
    elif pilihMenu == 3 :
        jumlah = int(input("Jumlah Topi : "))
        harga = 15000
    else :
        return belanja()
    return hitung(jumlah, harga)

def main() :
    menu()
    belanja()

main()