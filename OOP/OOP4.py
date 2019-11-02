class MarvelHero():
    def __init__(self,adi,saglik,guc):
        self.adi = adi
        self.saglik = saglik
        self.guc = guc

    def durum(self):
        durum = "Adı :{} Saglık :{}"
        print(durum.format(self.adi,self.saglik))

    def vurus(self,hero):
        hero.darbeal(self.guc)
        print(self.adi," vurdu ")
    
    def darbeal(self,guc):
        self.saglik -=guc
        print(self.adi," darbe aldı")
        self.durum()



class deadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool", 1000, 100)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",1500,150)

    def vurus(self,hero):
        hero.darbeal(self.guc*2)
        print(self.adi," vurdu ")
        self.durum()

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",1750,150)

class AgentRomanoff(MarvelHero):
    def __init__(self):
        super().__init__("Agent Romanoff",1750,175)
    
    def darbeal(self,guc):
        self.saglik -=guc/2
        print(self.adi," darbe aldı")
        self.durum()