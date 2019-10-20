



def dosyaAc(adres): 
    import os
    if not os.path.exists(adres) :
        dosya = open(adres,"w+",encoding="UTF-8")
    else:
        dosya = open(adres,"r+",encoding="UTF-8")
    return dosya



def dosyaKayitListele(dosya):
    dosya.seek(0)
    liste = dosya.readlines()
    print("-"*55)
    for i in range(0,len(liste)):
        adi = liste[i].split(";")[0]
        soyadi = liste[i].split(";")[1]
        telefon = liste[i].split(";")[2]
        satir = "{} - {} {} {}".format(str(i+1),adi,soyadi,telefon)
        print(satir)
    print("-"*55)


def dosyaYaz(*args,dosya):
    metin = ""
    for item in args:   # Ali,Veli,123456
        metin += item+";" 
    # Ali;Veli;123456;
    metin = metin.rstrip(";")+"\n"
    # Ali;Veli;123456\n
    liste = dosya.readlines()
    dosya.seek(0)
    dosya.truncate()
    liste.append(metin)
    dosya.writelines(liste)
    dosya.close()



def Logtut(MesajTipi,Mesaj,Zaman):
    dosyaismi = "log.csv"
    dosya = dosyaAc(dosyaismi)
    dosyaYaz(MesajTipi,Mesaj,Zaman,dosya=dosya)



