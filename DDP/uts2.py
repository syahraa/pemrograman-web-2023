#Syahra
angka1 = float(input("Masukkan angka 1: "))
angka2 = float(input("Masukkan angka 2: "))
operator = input("Pilih operator ((+),(-),(),(/),(*): ")
if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error! Pembagian tidak boleh dengan anhka nol."
elif operator == '**':
    hasil = angka1 ** angka2
else:
    hasil = "Error! Operator tidak valid."
print(f"Hasil: {hasil}")