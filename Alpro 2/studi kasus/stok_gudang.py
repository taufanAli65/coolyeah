class Gudang:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.stok_barang = 0

    def tambah_stok(self, jumlah):
        if self.stok_barang + jumlah <= self.kapasitas:
            self.stok_barang += jumlah
            return True
        else:
            return False

    def kurangi_stok(self, jumlah):
        if self.stok_barang - jumlah >= 0:
            self.stok_barang -= jumlah
            return True
        else:
            return False

    def tampilkan_jumlah_barang(self):
        print(f"Jumlah barang di gudang: {self.stok_barang}")

    def tampilkan_kapasitas(self):
        print(f"Kapasitas gudang: {self.kapasitas}")

    def restok_barang(self, jumlah):
        if self.tambah_stok(jumlah):
            print(f"Berhasil melakukan restok sebanyak {jumlah} barang.")
        else:
            print(f"Gagal melakukan restok. Kapasitas gudang tidak mencukupi.")

    def tampilkan_sisa_kapasitas(self):
        sisa_kapasitas = self.kapasitas - self.stok_barang
        print(f"Sisa kapasitas gudang: {sisa_kapasitas}")

