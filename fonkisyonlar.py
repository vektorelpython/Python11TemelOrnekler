# #Tanımlama-Definition
# def Formul(x):
#     return ((5*x**3)-14*x+8)/(3*x**2+5)

# #Çağırma - Calling
# print(Formul(1))
# print(type(Formul(1)))

# def Topla(a,b):
#     return a+b

# def Cikar(a,b):
#     return a-b

# def Carp(a,b):
#     return a*b

# def Bol(a,b):
#     return a/b

# def Cagir(fonk,a,b):
#     return fonk(a,b)

# print(Cagir(Topla,2,4))



# def Fonk(c,a=2,b=2):
#     print(c,b,a," İyi Gelir",sep="-")

# Fonk(c=3,b=2,a=1)



# liste = ["Ahmet","Mehmet","Ali","Soner"]

def Topluma(liste):
    sonuc = 0
    for item in liste:
        sonuc += int(item)
    return sonuc

adim = int(input("Kaç Sayı Gireceksin"))
sayac = 0
liste = []
while sayac < adim:
    liste.append(int(input("Sayı Gir")))
    sayac += 1
print(Topluma(liste))


