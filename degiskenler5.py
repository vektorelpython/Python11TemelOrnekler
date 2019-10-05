# liste1 = [1,2,3,4]
# liste2 = liste1 
# liste2[3] = 2584
# print(liste1)


# liste1 = [1,2,3,4]
# liste2  = liste1.copy()
# liste2[3] = 2584
# print(liste1)


# liste1 =[1,2,3,4]
# liste2 = [5,6,7,8]
# liste1.extend(liste2)
# # liste1 += liste2
# print(liste1)



liste = [[1,2,3],[4,5,6],[7,8,9]]
print(liste[0][1])


# a = 1
# b = 1
# for i in range(0,10):
#     c = a+b
#     print(c)
#     print(a/b)
#     a,b = b,c

liste =  (1,2,3,[1,"2"])
liste[1] = 3  #++++++++++++++++++++
demet = (1,2,3,[1,"2"])
demet[1] = 3  #----------------


sozluk = {"book":"kitap","pencil":"kalem"}
print(sozluk["book"])
sozluk.update({"table":"masa"})
print(sozluk)
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())
# print(sozluk["deneme"])
print(sozluk.get("deneme"))
liste = ["Ali","Veli","Mahmut","Hakkı"]
sozluk = dict.fromkeys(liste,0)


sozluk = {x:str(x*2) for x in range(0,10) }
print(sozluk)
sozluk.popitem()
print(sozluk)


sozluk = {"Aday 1":{"Adı":"Sinan"},
    "Aday 2":{"Adı":"Soner"}
}