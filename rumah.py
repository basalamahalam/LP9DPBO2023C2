from hunian import Hunian


class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_luas_tanah(self):
        return "120 x 200 meter"

    def get_luas_bangunan(self):
        return "100 x 180 meter"

    def get_jml_kamar(self):
        return "5 Kamar + 3 Kamar Mandi"

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + self.get_jml_kamar() + "\nLuas Tanah : " + self.get_luas_tanah() + "\nLuas Bangunan : " + self.get_luas_bangunan()

    def get_photo(self):
        return "kucing.png"
