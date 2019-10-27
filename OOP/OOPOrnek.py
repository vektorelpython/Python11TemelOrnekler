import os
import datetime as dt
class FileTools:
    fileFormat = ".csv"
    fileList = []
    def __init__(self,*args,**kwargs):
        self.fileName = "Unnamed"
        self.fileAddress = os.getcwd()
        self.fields = ["a","b","c"]
        for key,value in kwargs.items():
            if key == "fileName":
                if value not in FileTools.fileList:
                    self.fileName = value
                    FileTools.fileList.append(value)
                else:
                    raise print("Aynı Dosyadan Bir Tane Daha Var")
            elif key == "fileAddress":
                self.fileAddress = value
            elif key == "field":
                self.fields = value
        self.dosyaAc()
        self.fileContent = []

    def dosyaAc(self):
        adres = self.fileAddress + os.sep + self.fileName + FileTools.fileFormat
        if not os.path.exists(adres) :
            self.dosya = open(adres,"w+",encoding="UTF-8")
        else:
            self.dosya = open(adres,"r+",encoding="UTF-8")


    def dosyaOku(self,param=1,cursor=0):
        try:
            self.dosyaAc()
            result = ""
            if param == 1:
                if cursor:
                    result = self.dosya.read(cursor)
                else:
                    result = self.dosya.read()
            elif param == 2:
                if cursor:
                    result = self.dosya.readline(cursor)
                else:
                    result = self.dosya.readline()
            else:
                result = self.dosya.readlines()
        except Exception as hata:
            pass
            # Logtut("1",hata,tarih())
        finally:
            self.dosya.close()
        self.fileContent = result

    @staticmethod
    def tarih(tarih=dt.date.today()):
        return str(tarih.year)+"_"+str(tarih.month)+"_"+str(tarih.day)

    def dosyaKayitListele(self):
        self.dosyaAc()
        liste = self.dosya.readlines()
        print("-"*55)
        for i in range(0,len(liste)):
            line = liste[i].split(";")
            satir = "{} -".format(str(i+1))
            for item in line:
                satir += item + " "
            print(satir)
        print("-"*55)

    def kayitDuzenle(self):
        try:
            self.dosyaKayitListele()
            ID = int(input("Kayıt Numarası Giriniz"))
            self.dosya.seek(0)
            liste = self.dosya.readlines()
            kayit = self.GetFieldsEntries()
            liste[ID-1] = kayit
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(liste)
        except Exception as hata:
            pass
            # Logtut("1",str(hata),str(dt.date.today))
        finally:
            self.dosya.close()

    def GetFieldsEntries(self):
        record =""
        for item in self.fields:
            record += input("Enter "+item) + ";"
        record = record.rstrip(";")+"\n"
        return record

    def kayitSil(self):
        try:
            fisim = "KayitSil"
            self.dosyaKayitListele()
            ID = int(input("Kayıt Numarası Giriniz"))
            self.dosya.seek(0)
            liste = self.dosya.readlines()
            liste.pop(ID-1)
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(liste)
        except Exception as hata:
            pass
            # Logtut("1",str(hata)+-+fisim,tarih())
        finally:
            self.dosya.close()

    def dosyaYaz(self):
        self.dosyaAc()
        metin = ""
        metin = self.GetFieldsEntries()
        # Ali;Veli;123456\n
        liste = self.dosya.readlines()
        self.dosya.seek(0)
        self.dosya.truncate()
        liste.append(metin)
        self.dosya.writelines(liste)
        self.dosya.close()

    def AnaMenu(self):
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
            self.dosyaAc()
            if islem == "1":
                self.dosyaYaz()
            elif islem == "2":
                self.dosyaKayitListele()
            elif islem == "3":
                self.kayitDuzenle()
            elif islem == "4":
                self.kayitSil()
            elif islem == "5":
                break

if __name__ == '__main__':
    fileDefault = FileTools()
    fileDefault.AnaMenu()