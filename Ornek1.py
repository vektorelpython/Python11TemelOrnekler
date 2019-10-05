import random
# for i in range(0,6):
#     rnd = random.randint(1,50)
#     print(rnd)


kolonSay = int(input("Kolon Sayısı:"))
buyukListe = []
for i in range(0,kolonSay):
    kucukListe = []
    for i in range(0,6):
        rnd = random.randint(1,50)
        while rnd in kucukListe:
            rnd = random.randint(1,50)
        kucukListe.append(rnd)
    kucukListe.sort()
    buyukListe.append(kucukListe)
print(*buyukListe,sep="\n")
