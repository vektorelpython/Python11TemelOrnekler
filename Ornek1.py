# import random
# # for i in range(0,6):
# #     rnd = random.randint(1,50)
# #     print(rnd)


# kolonSay = int(input("Kolon Sayısı:"))
# buyukListe = []
# for i in range(0,kolonSay):
#     kucukListe = []
#     for i in range(0,6):
#         rnd = random.randint(1,50)
#         while rnd in kucukListe:
#             rnd = random.randint(1,50)
#         kucukListe.append(rnd)
#     kucukListe.sort()
#     buyukListe.append(kucukListe)
# print(*buyukListe,sep="\n")



# 1*2*3*4*5

# a = int(input("Sayıyı Giriniz"))
# sonuc = 1
# for i in range(1,a+1):
#     sonuc *=i
# print(sonuc)

# a = int(input("Sayıyı Giriniz"))
# for i in range(2,a):
#     if a % i == 0:
#         print("{} sayısı {} ile kalansız bölündü".format(a,i))
#         break
# else:
#     print("Sayı Asal")

a = int(input("Sayıyı Giriniz"))
liste = []
for i in range(2,a):
    if a % i == 0:
        asal=2
        for j in range(2,i):
            asal = j+1
            if i % j == 0:
                break
        else:
            liste.append(asal)
print(liste)

