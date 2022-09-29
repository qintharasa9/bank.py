# Himpunan bilangan asli kurang dari 10 yang merupakan kelipatan 3 atau 5
# Mencari jumlah seluruh bilangan asli yang merupakan kelipatan 3 atau 5 dan kurang dari 1000

Jumlah_semua_bilangan_asli = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        Jumlah_semua_bilangan_asli = Jumlah_semua_bilangan_asli + i 

print ("Jumlah semua bilangan asli kelipatan 3 atau 5 kurang dari 1000 =", Jumlah_semua_bilangan_asli)