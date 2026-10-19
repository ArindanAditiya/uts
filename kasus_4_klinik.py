from case4.data_pasien import pasien
from case4.services import validation
from case4.klinik import Klinik

print("=== DATA PASIEN KLINIK PRATAMA === ")

# validasi
inp = validation(input("Inputkan Jumlah kunjungan pasien : "))
if inp == "error: Not Number":
   print("Validasi gagal, ini bukan angka")

# perulangan menyesuaikan dengan jumlah yang diinputakan oleh user di awal tadi
if inp != "error: Not Number":
  jumlah_kunjungan = inp
  for i, kunjungan in enumerate(range(jumlah_kunjungan), start=1):
    print(f"Pasien ke-{i}")

    inp_nama = input("nama :")

    # pakai validasi dari services
    inp_usia = validation(input("usia :"))
    if inp_usia == "error: Not Number":
      print("Validasi gagal, ini bukan angka. PROGRAM DIHENTIKAN")
      break
    elif inp_usia == "error: Must be not 0":
      print("Validasi gagal, kamu usia tidak boleh 0. PROGRAM DIHENTIKAN")
      break
    elif inp_usia == "error: max in range 120":
      print("Validasi gagal, maksimal usia adalah 120. PROGRAM DIHENTIKAN")
      break

    pasien.append({
      "nama": inp_nama,
      "usia": inp_usia
    })
    print()

print("=== DAFTAR PASIEN HARI INI === ")
if(pasien) :
  Klinik_Object = Klinik(pasien)
  Klinik_Object.print_daftar_kunjungan()
  Klinik_Object.print_rekapitulasi()
else:
  print("tidak ada pasien")


  