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