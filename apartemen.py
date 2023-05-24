from hunian import Hunian


class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_harga(self):
        return "Rp.150.000.000 / Kamar"

    def get_photo(self):
        return "kucing3.png"

    def get_jumlahpenghuni(self):
        return "75 Orang"

    def get_jumlahkamar(self):
        return "120 Kamar"

    def get_detail(self):
        return "Pemilik : " + self.get_nama_pemilik() + "\nHarga Jual : " + self.get_harga() + "\nJumlah Penghuni : " + self.get_jumlahpenghuni() + "\nJumlah Kamar : " + self.get_jumlahkamar()
