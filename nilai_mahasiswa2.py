# Program Penghitung Rata-rata Nilai Mahasiswa

print("--- Program Perhitungan Nilai Mahasiswa ---")

# Memasukkan jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Menyiapkan total nilai
total = 0

# Perulangan memasukkan nilai mahasiswa
for i in range(1, jumlah + 1):
    print("Masukkan Nilai Mahasiswa ke-", i)
    nilai = float(input("Masukkan nilai: "))
    total = total + nilai

# Menghitung rata-rata
rata_rata = total / jumlah

# Menampilkan hasil
print("Rata-rata nilai mahasiswa:", rata_rata)