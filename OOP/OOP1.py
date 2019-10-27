"""
Encapsulation
Polymorphism
Abstraction
Inheritance
"""
# 1.Aşama 

# sesli_harfler = "aeıioöuü"
# sayac = 0
# kelime = input("Bir Kelime Girin")
# for harf in kelime:
#     if harf.lower() in sesli_harfler:
#         sayac += 1
# mesaj = "{} kelimesinde {} sesli harf var."
# print(mesaj.format(kelime,sayac))


# 2.Aşama

# sesli_harfler = "aeıioöuü"
# sayac = 0
# kelime = input("Bir Kelime Girin")

# def seslidir(harf):
#     return harf.lower() in sesli_harfler

# for harf in kelime:
#     if seslidir(harf):
#         sayac += 1
# mesaj = "{} kelimesinde {} sesli harf var."
# print(mesaj.format(kelime,sayac))


#3.Aşama

# sesli_harfler = "aeıioöuü"
# sayac = 0
# kelime = input("Bir Kelime Girin")

# def seslidir(harf):
#     return harf.lower() in sesli_harfler

# def arttir():
#     global sayac
#     for harf in kelime:
#         if seslidir(harf):
#             sayac += 1
#     return sayac

# mesaj = "{} kelimesinde {} sesli harf var."
# print(mesaj.format(kelime,arttir()))

# 4. Aşama

# sesli_harfler = "aeıioöuü"
# sayac = 0
# kelime = input("Bir Kelime Girin")

# def seslidir(harf):
#     return harf.lower() in sesli_harfler

# def arttir(n):
#     for harf in kelime:
#         if seslidir(harf):
#             n += 1
#     return n

# mesaj = "{} kelimesinde {} sesli harf var."
# print(mesaj.format(kelime,arttir(sayac)))


# 5.Aşama


# sesli_harfler = "aeıioöuü"
# sayac = 0

# def kelimesor():
#     return input("Bir Kelime Girin")

# def seslidir(harf):
#     return harf.lower() in sesli_harfler

# def arttir(sayac,kelime):
#     for harf in kelime:
#         if seslidir(harf):
#             sayac += 1
#     return sayac

# def ekrana_bas(kelime):
#     mesaj = "{} kelimesinde {} sesli harf var."
#     print(mesaj.format(kelime,arttir(sayac,kelime)))

# def calistir():
#     kelime = kelimesor()
#     ekrana_bas(kelime)


# if __name__ == "__main__":
#     calistir()

# 6. Aşama

class HarfSayaci:
    def __init__(self):
        self.sesli_harfler = "aeıioöuü"
        self.sayac=  0

    def kelimesor(self):
        return input("Bir Kelime Girin")

    def seslidir(self,harf):
        return harf.lower() in self.sesli_harfler

    def arttir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac += 1
        return self.sayac

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesli_harf_sayisi = self.arttir()
        print(mesaj.format(self.kelime,sesli_harf_sayisi))

    def calistir(self):
        self.kelime = self.kelimesor()
        self.ekrana_bas()

if __name__ == "__main__":
    sayac = HarfSayaci()
    sayac.calistir()