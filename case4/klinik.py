from case4.services import cek_rata_rata_usia
from case4.services import cek_daftar_kunjungan
from case4.services import cek_jumlah_pasien_per_kategori

class Klinik :
  def __init__(self, daftar_pasien):
    self.daftar_pasien = daftar_pasien
    self.total_pasien = len(daftar_pasien)

  # ntuk cek rata-rata usia
  def rata_rata_usia(self):
    return int(cek_rata_rata_usia(self.daftar_pasien))

  def print_daftar_kunjungan(self):
    for i, x in enumerate(cek_daftar_kunjungan(self.daftar_pasien), start=1) :
      print(f"""
      {i}. Radit 
          Usia     : {x["usia"]} tahun 
          Kategori : {x["kategori"]} 
      """)
  
  def print_rekapitulasi(self):
      categori = cek_jumlah_pasien_per_kategori(self.daftar_pasien)
      print( f"""
          === REKAPITULASI KLINIK === 
          Total Pasien      : {self.total_pasien} orang 
          Rata-rata Usia    : {self.rata_rata_usia()} tahun 
          Kategori Anak     : {categori["anak"]} orang 
          Kategori Dewasa   : {categori["dewasa"]} orang 
          Kategori Lansia   : {categori["lansia"]} orang 
          ===========================
      """)

# Orang1 = Klinik(pasien)
# Orang1.print_daftar_kunjungan()
# Orang1.print_rekapitulasi()
