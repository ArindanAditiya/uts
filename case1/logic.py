class TagihanLaundry :
  def __init__(self, nama_pelanggan, jenis_layanan, berat_cucian ):
    self.nama_pelanggan = nama_pelanggan,
    self.jenis_layanan = jenis_layanan
    self.berat_cucian = berat_cucian

  def print_nota(self):
    print(f"""
=== NOTA PEMBAYARAN LAUNDRY === 
Pelanggan      : {self.nama_pelanggan} 
Layanan        : {self.jenis_layanan} {self.berat_cucian} 
Berat          : {self.berat_cucian} kg 
Subtotal       : Rp78.000 
Diskon         : 10% 
Potongan       : Rp7.800 
Total Bayar    : Rp70.200 
===============================
""")