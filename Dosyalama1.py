


def dosyaAc(adres): 
    import os 
    import sys
    sys.path.append(os.getcwd())
    if not os.path.exists(adres) :
        dosya = open(adres,"w+",encoding="UTF-8")
    else:
        dosya = open(adres,"r+",encoding="UTF-8")
    return dosya

def dosyaOku(dosya,param=1):
    dosya.seek(0)
    if param == 1:
        return dosya.read()
    elif param == 2:
        return dosya.readline()
    else:
        return dosya.readlines()


def dosyaYaz(*args,dosya):
    metin = ""
    for item in args:
        metin += item+";"
    metin = metin.rstrip(";")+"\n"
    liste = dosyaOku(dosya,param=3)
    dosya.seek(0)
    dosya.truncate()
    liste.append(metin)
    dosya.writelines(liste)
    dosya.close()

dosya = dosyaAc("defter.csv")
dosyaYaz("Ali","Veli","123456",dosya=dosya)

dosya = dosyaAc("defter.csv")
print(dosyaOku(dosya,param=3))


