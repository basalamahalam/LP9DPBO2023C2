from hunian import Hunian


class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos."

    def get_sewa(self):
        return "Rp.1.000.000,- / Hari"

    def get_dapur(self):
        return "Ya"

    def get_wc(self):
        return "Ya"

    def get_jumlahkamar(self):
        return "12 Kamar"

    def get_jumlahpenghuni(self):
        return "10 Orang"

    def get_detail(self):
        return self.get_summary() + "\nPemilik : " + self.nama_pemilik + "\nHarga Sewa : " + self.get_sewa() + "\nJumlah Penghuni : " + self.get_jumlahpenghuni() + "\nJumlah Kamar : " + self.get_jumlahkamar() + "\nDapur di dalam : " + self.get_dapur() + "\nKamar Mandi di dalam : " + self.get_wc()

    def get_photo(self):
        return "kucing2.png"
