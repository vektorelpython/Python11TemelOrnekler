basamak = { 0:"",1:" Bin ",2:" Milyon ",3:" Milyar ",4:" Trilyon "}
birler = {
    0:" ",
    1:" Bir ",
    2:" İki ",
    3:" Üç ",
    4:" Dört ",
    5:" Beş ",
    6:" Altı ",
    7:" Yedi ",
    8:" Sekiz ",
    9:" Dokuz ",
}
onlar = {
    0:" ",
    1:" On ",
    2:" Yirmi ",
    3:" Otuz ",
    4:" Kırk ",
    5:" Elli ",
    6:" Altmış ",
    7:" Yetmiş ",
    8:" Seksen ",
    9:" Doksan ",
}
metin = input("Sayıyı Giriniz")
# metin = "7,968,852,741"
metin = metin.replace(",","").replace(".","")

while len(metin)%3 != 0:
    metin = "0" + metin
# # 007968852741
# 741     852    968     007
liste = []
for i in range(0,len(metin)//3):
    parca = metin[i*3:(i*3)+3]
    liste.insert(0,parca)
print(liste)
# ['741', '852', '968', '007']
buyukSonuc = ""
adim = 0
for item in liste:
    ifade = item
    sonuc = ""
    if int(ifade[0]) != 0: # yüzler basamağı 7
        if int(ifade[0]) != 1: # yüzler basamağı 7
            sonuc = birler[int(ifade[0])]+" Yüz "
        else:
            sonuc = " Yüz "
    sonuc += onlar[int(ifade[1])]  # onlar basamağı 4
    sonuc += birler[int(ifade[2])] # birler basamağı 1
    sonuc += basamak.get(adim)
    buyukSonuc = sonuc + buyukSonuc
    adim += 1
print(buyukSonuc)