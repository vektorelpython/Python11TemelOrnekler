def Fonk(a=1):
    pass

def Fonk2(*args):
    pass

def Fonk3(**kwargs):
    pass


# a = 2
# def Fonk(b):
#     a=3
#     return a*2

# print(Fonk(3))
# print(a)


a = 2
# def Fonk(b):
#     global a
#     a=3
#     return a*2
# Fonk(3)
# print(Fonk(3))
# print(a)

# def OuterFunction(a = 3):
#     print(a*3)
#     def innerFunction(a):
#         print(a*2)
#     innerFunction(a)

# OuterFunction()  


# metin = "BEŞİKTAŞ"

# def RecFunk(metin):
#     print(metin)
#     if len(metin)>1:
#         RecFunk(metin[1:])
#     print(metin)
# RecFunk(metin)
# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(6000))
# print(sys.getrecursionlimit())

fonk = lambda x : x**2
print(fonk(2))


alfabe = "abcçdefgğhıijklmnoöpqrsştuvwxyz"
dizilim = { i :alfabe.index(i) for i in alfabe}
print(liste)
liste = ["ahmet","ışınsu","ışıl","ilayda","hülagü","hakkı","çiğdem","şerife","soner"]
liste = sorted(liste,key=lambda x : dizilim.get(x[0]))
print(liste)


