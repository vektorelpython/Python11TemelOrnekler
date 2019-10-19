def Fonk(*args):
    sonuc = 0
    for item in args:
        sonuc += item
    return sonuc,args

print(Fonk(1,2,3,4,5)[1][1])