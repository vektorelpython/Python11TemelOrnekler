


def dosyaAc(adres): 
    import os
    if not os.path.exists(adres) :
        dosya = open(adres,"w+",encoding="UTF-8")
    else:
        dosya = open(adres,"r+",encoding="UTF-8")
    return dosya

def dosyaOku(dosya,param=1):
    dosya.seek(0)
    result = ""
    if param == 1:
        result = dosya.read()
    elif param == 2:
        result = dosya.readline()
    else:
        result = dosya.readlines()
    dosya.close()
    return result


def dosyaYaz(*args,dosya):
    metin = ""
    for item in args:
        metin += item+";"
    metin = metin.rstrip(";")+"\n"
    liste = dosya.readlines()
    dosya.seek(0)
    dosya.truncate()
    liste.append(metin)
    dosya.writelines(liste)
    dosya.close()

def AnaMenu():
    menu = """
    1-Yazma
    2-Listeleme
    5-Çıkış
    """
    while True:
        print(menu)
        islem = input("İşlem Numarası Giriniz")
        dosya = dosyaAc("defter.csv")
        if islem == "1":
            adi = input("Adını Giriniz")
            soyadi = input("soyadi Giriniz")
            telefon = input("telefon Giriniz")
            dosyaYaz(adi,soyadi,telefon,dosya=dosya)
        elif islem == "2":
            print(*dosyaOku(dosya,param=3))
        elif islem == "5":
            break

AnaMenu()
    



