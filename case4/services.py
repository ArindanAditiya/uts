# ======= services for Pasien =======
def cek_kategori_usia(usia):
  if usia < 17 :
    return "Anak"
  elif usia < 59 :
    return "Dewasa"
  else :
    return "Lansia"

# ======= services for klinik =======
def cek_rata_rata_usia(data_pasien):
  usia = 0 
  for x in data_pasien :
    usia += x["usia"]
  return usia / len(data_pasien)

def cek_jumlah_pasien_per_kategori(daftar_pasien):
  anak = 0
  dewasa = 0
  lansia = 0

  # cek dulu satu"
  for x in daftar_pasien :
    if x["usia"] < 17 :
      anak += 1
    elif x["usia"] < 59 :
      dewasa += 1
    else :
      lansia += 1

  return {
    "anak": anak,
    "dewasa": dewasa,
    "lansia" : lansia
  }

def cek_daftar_kunjungan(data_pasien):
  history = []
  for x in data_pasien:
    history.append({
      "nama" : x["nama"],
      "usia" : x["usia"],
      "kategori" : cek_kategori_usia(x["usia"])
    })

  return history
  
# ======= services for main klinik =======
def validation(inp):

  # cek kalau buka angka
  try :
    input = int(inp) 
    if input == 0:
      return "error: Must be not 0"
    elif input > 120:
      return "error: max in range 120"
  
    return input
  except :
    return "error: Not Number"