print("***Beden Kitle Endeksi Hesaplama.***")
boy = float(input("boyunuzu giriniz:"))
kilo = int(input("kilonuzu giriniz:"))
islem = int(kilo / (boy**2))
if (islem>30):
    print("Obez")
elif(islem<=30 and islem>25):
    print("Fazla Kilolu")
elif(islem<=25 and islem>18.5):
    print("Normal")
elif(islem<=18.5 and islem>16):
    print("Zayıf")
else:
    print("Acından Ölmüş:)")
