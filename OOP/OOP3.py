class Kedi():
    familya = "Felix"
    liste = []
    
    def __init__(self, adi="Tekir"):
        self.adi = adi
        self.tuy = "Kısa"
        Kedi.liste.append(adi)
    
    def beslenme(self):
        print(self.adi," beslendi")


    @classmethod
    def miyavla(cls):
        print(cls.familya," miyavladı")

    @staticmethod
    def pi(aa):
        print(22/7)


behlul = Kedi("Behlül")
melek = Kedi("Melek")
behlul.beslenme()
melek.beslenme()
print(Kedi.liste)
Kedi.pi(5)
melek.pi()