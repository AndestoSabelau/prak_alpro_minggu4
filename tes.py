'''
def tambah (ais1, ais2):
    hasil = ais1 + ais2
    return hasil 

def print_twice(pesan):
    print(pesan)
    print(pesan)
print_twice ("hi,kawan")

def tambah (a,b,c):
    hasil = a + b + c
    return hasil
print(tambah(1,2,3))

def cek (no1,no2,no3 = 0):
    Max = max(no1,no2,no3)
    return Max

print(cek(1,4))
print(cek(8,7,9))
print(cek(4,3,8))

def gorengan (tahu,tempe,bakwan):
    print("jumlah gorengan tahu :", tahu)
    print("jumlah gorengan tempe :",tempe)
    print("jumlah gorengan bakwan :",bakwan)

gorengan (tahu = 3, tempe = 2, bakwan = 5)

def genap(angka):
    if angka % 2 == 0 :
        return True
    else:
        return False
print(genap(2))
print(genap(3))
print(genap(4))
print(genap(7))
'''