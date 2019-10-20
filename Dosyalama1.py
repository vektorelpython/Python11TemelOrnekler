
from Log import Logtut
import datetime as dt

def dosyaAc(adres): 
    import os
    if not os.path.exists(adres) :
        dosya = open(adres,"w+",encoding="UTF-8")
    else:
        dosya = open(adres,"r+",encoding="UTF-8")
    return dosya

def dosyaOku(dosya,param=1,cursor=0):
    try:
        dosya.seek(0)
        result = ""
        if param == 1:
            if cursor:
                result = dosya.read(cursor)
            else:
                result = dosya.read()
        elif param == 2:
            if cursor:
                result = dosya.readline(cursor)
            else:
                result = dosya.readline()
        else:
            result = dosya.readlines()
    except Exception as hata:
        Logtut("1",hata,tarih())
    finally:
        dosya.close()
    return result

def tarih(tarih=dt.date.today()):
    return str(tarih.year)+"_"+str(tarih.month)+"_"+str(tarih.day)




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

def kayitDuzenle(dosya):
    try:
        dosyaKayitListele(dosya)
        ID = int(input("Kayıt Numarası Giriniz"))
        dosya.seek(0)
        liste = dosya.readlines()
        adi = input("Adını Giriniz")
        soyadi = input("Soyadini Giriniz")
        telefon = input("Telefon Giriniz")
        kayit = adi + ";" + soyadi + ";" + telefon + "\n"
        liste[ID-1] = kayit
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except Exception as hata:
        Logtut("1",str(hata),str(dt.date.today))
    finally:
        dosya.close()


def kayitSil(dosya):
    try:
        fisim = "KayitSil"
        dosyaKayitListele(dosya)
        ID = int(input("Kayıt Numarası Giriniz"))
        dosya.seek(0)
        liste = dosya.readlines()
        liste.pop(ID-1)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except Exception as hata:
        Logtut("1",str(hata)+-+fisim,tarih())
    finally:
        dosya.close()

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

def AnaMenu(adres = ""):
    print(__name__)
    menu = """
    1-Yazma
    2-Listeleme
    3-Düzenleme
    4-Sil
    5-Çıkış
    """
    while True:
        print(menu)
        islem = input("İşlem Numarası Giriniz")
        dosya = dosyaAc(adres)
        if islem == "1":
            adi = input("Adını Giriniz")
            soyadi = input("soyadi Giriniz")
            telefon = input("telefon Giriniz")
            dosyaYaz(adi,soyadi,telefon,dosya=dosya)
        elif islem == "2":
            dosyaKayitListele(dosya)
        elif islem == "3":
            kayitDuzenle(dosya)
        elif islem == "4":
            kayitSil(dosya)
        elif islem == "5":
            break

if __name__ == '__main__':
    AnaMenu("deneme.csv")



