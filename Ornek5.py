import os
import datetime

zaman = datetime.date.today()
klasoryol = str(zaman.year)+os.sep+str(zaman.month)+os.sep+str(zaman.day))
# isim = input("Klasör Adı Giriniz")
os.makedirs(klasoryol)