no1 = input("Masukan Bilangan pertama :")
no2 = input("Masukan Bilangan kedua :")
no3 = input("Masukan Bilangan ketiga :")

def cek_angka(no1,no2,no3):
    if no1 != no2 != no3:
        return True
        if no1 + no2 == no3 or no1 + no3 == no2 or no2 + no3 == no1:
                return True
        else:
            return False

print(cek_angka(no1,no2,no3)) 
print(cek_angka(no1,no1,no3)) 
print(cek_angka(no3,no2,no1)) 
print(cek_angka(no1,no3,no3)) 