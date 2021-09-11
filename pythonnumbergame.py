import random 

tutulansayi = random.randint(0,1000)
print("Sayý Tahmin Etme Oyunu")
sayigirisi = int(input("Sayý Giriniz : "))

i = 120
while  i > 100:
  if sayigirisi == tutulansayi:
    print("Tebrikler Kazandýnýz")
    break
  elif sayigirisi < tutulansayi:
    print("Daha Büyük Sayý Giriniz")
    sayigirisi = int(input("Sayý Giriniz : "))
  elif sayigirisi > tutulansayi:
    print("Daha küçük sayi giriniz")
    sayigirisi = int(input("Sayý Giriniz : "))
    continue