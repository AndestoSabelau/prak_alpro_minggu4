parameter = "IYA" or "TIDAK"
while parameter == "IYA":
    def cek_digit_belakang (aa,bb,cc):
        if aa%10 == bb%10 or aa%10 == cc%10 or bb%10 == cc%10: return True
        else: return False

    no1 = int(input("Masukan Bilangan Pertama :"))
    no2 = int(input("Masukan Bilangan Kedua :"))
    no3 = int(input("Masukan Bilangan Ketiga :"))
    print(cek_digit_belakang(no1,no2,no3))

    parameter = str(input("cek lagi? IYA?TIDAK :"))
    print("")
