from OOP4 import *
import random
import time

class Gamer():
    def __init__(self,tip):
        self.tip = tip
        self.karakter = None
        self.karakterBelirle()

    
    def karakterSec(self):
        karakterListesi = """
        1-DeadPool
        2-Hulk
        3-IronMan
        4-Agent Romanoff
        """
        print(karakterListesi)
        return int(input("karakter seçimi yapınız"))

    def hareketSec(self,hero):
        hareketListesi = """
        1-Vurus
        2-Savunma
        3-SuperVurus
        """
        if self.tip == 1 :
            print(hareketListesi)
            secim =  int(input("hareket seçimi yapınız"))
        else:
            secim = random.randint(1,4)
        if secim == 1:
            self.karakter.vurus(hero)
        elif secim == 2:
            self.karakter.savunma()
        elif secim == 3:
            self.karakter.supervurus(hero)

    

    def karakterBelirle(self):
        karakterlistesi = [deadPool,Hulk,IronMan,AgentRomanoff]
        if self.tip == 1:
            secim = self.karakterSec() - 1
            self.karakter = karakterlistesi[secim]()
        else:
            secim = random.randint(0,3)
            self.karakter = karakterlistesi[secim]()
        
Oyuncu1 = Gamer(0)
Oyuncu2 = Gamer(0)
while Oyuncu1.karakter.saglik>0 and Oyuncu2.karakter.saglik >0:
    time.sleep(1)
    Oyuncu1.hareketSec(Oyuncu2.karakter)
    time.sleep(1)
    Oyuncu2.hareketSec(Oyuncu1.karakter)







