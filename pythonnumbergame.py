import random 

tutulansayi = random.randint(0,1000)
print("Say� Tahmin Etme Oyunu")
sayigirisi = int(input("Say� Giriniz : "))

i = 120
while  i > 100:
  if sayigirisi == tutulansayi:
    print("Tebrikler Kazand�n�z")
    break
  elif sayigirisi < tutulansayi:
    print("Daha B�y�k Say� Giriniz")
    sayigirisi = int(input("Say� Giriniz : "))
  elif sayigirisi > tutulansayi:
    print("Daha k���k sayi giriniz")
    sayigirisi = int(input("Say� Giriniz : "))
    continue