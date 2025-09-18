import random
sayi=random.randint(1,5)
tahmin=int(input("1 ile 5 arasında bir sayı giriniz: "))
if tahmin==sayi:
    print("Tebrikler bildiniz.")
else:
    print("Bilemediniz. Doğru sayı:",sayi)
    