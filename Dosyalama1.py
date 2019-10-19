


def dosyaAc(adres): 
    import os 
    import sys
    sys.path.append(os.getcwd())
    if not os.path.exists(adres) :
        dosya = open(adres,"w+",encoding="UTF-8")
    else:
        dosya = open(adres,"r+",encoding="UTF-8")
    return dosya



dosya = dosyaAc("defter.csv")
metin = dosya.read()
print(metin)
dosya.seek(0)
metin = dosya.readlines()
print(dosya.tell())
print(metin)