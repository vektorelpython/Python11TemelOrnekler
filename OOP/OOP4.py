class MarvelHero():
    def __init__(self,adi,saglik,guc):
        self.adi = adi
        self.saglik = saglik
        self.guc = guc
        self.comboLimit = 10
        self.combo = self.comboLimit

    def durum(self):
        durum = "Adı :{} Saglık :{}"
        print(durum.format(self.adi,self.saglik))

    def vurus(self,hero):
        hero.darbeal(self.guc)
        print(self.adi," vurdu ",hero.adi,"darbe aldı")
        self.combo +=1
        if self.combo == self.comboLimit:
            self.supervurus(hero)
            self.combo = 0
        hero.durum()
    
    def savunma(self):
        self.saglik += 5
        self.combo += 1
        print(self.adi,"savunma ")
        self.durum()

    def supervurus(self,hero):
        if self.combo == self.comboLimit:
            hero.darbeal(self.guc*5)
            print(self.adi,"süper vuruş ",hero.adi,"darbe aldı")
            hero.durum()
            self.combo = 0
        else:
            print(self.adi,"yeterli gücü yok")
    
    def darbeal(self,guc):
        self.saglik -=guc

       



class deadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool", 1000, 100)
        self.comboLimit = 3

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",1500,150)
        self.comboLimit = 5

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",1750,150)

class AgentRomanoff(MarvelHero):
    def __init__(self):
        super().__init__("Agent Romanoff",1750,175)
    