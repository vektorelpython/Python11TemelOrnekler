from OOP4 import *
import random
import time
menu = """
1-İnsan - İnsan
2-Bilgisayar - İnsan
3-Bilgisayar - Bilgisayar
"""
print(menu)
tercih = input("Oyun tipini seçiniz")
karakterlistesi = [deadPool,IronMan,Hulk,AgentRomanoff]
if tercih == "1":
    for item in karakterlistesi:
        print(karakterlistesi.index(item)+1)
    oyuncu1 = input("Oyuncu 1 için seçim")
    oyuncu2 = input("Oyuncu 2 için seçim")
    oyuncu1 = karakterlistesi[int(oyuncu1)-1]()
    oyuncu2 = karakterlistesi[int(oyuncu2)-1]()
    while oyuncu1.saglik >= 0 or oyuncu2.saglik >= 0:
        liste = [oyuncu1,oyuncu2]
        liste[random.randint(0,1)].vurus(liste[random.randint(0,1)])
        time.sleep(2)
# elif tercih == "2":
#     pass
#     #karakter seçimi ve bilgisayar rastgele
# if tercih == "3":
