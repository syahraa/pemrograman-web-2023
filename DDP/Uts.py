# Program menghitung luas dan keliling trapesium

import math

# Input panjang sisi atas, panjang sisi bawah, dan tinggi dari pengguna
sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

# Hitung luas dan keliling
luas = (sisi_atas + sisi_bawah) * tinggi / 2
sisi_miring = math.sqrt(((sisi_atas - sisi_bawah) / 2) * 2 + tinggi * 2)
keliling = sisi_atas + sisi_bawah + 2 * sisi_miring

# Tampilkan hasil
print("Luas trapesium:", luas)
print("Keliling trapesium:", keliling)