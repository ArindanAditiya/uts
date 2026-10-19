from case4.services import cek_kategori_usia

class Pasien :
  def __init__(self, nama, usia):
    self.nama = nama
    self.usia = usia

  def kategori_usia(self):
    return cek_kategori_usia(self.usia)