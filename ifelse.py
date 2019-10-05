"""
a == b  
a != b
a < b
a > b
a <= b
a >= b
AND
OR
NOT

IS
IN

"""
a = int(input("1. Sayıyı Giriniz"))
b = int(input("2. Sayıyı Giriniz"))
if a==b:
    print("a ve b eşit")
    print("olabilir yani")
else:
    print("a b ye eşit değil")
print("İyi Günler")

Not = int(input("Notu Giriniz"))
if Not >80:
    print("AA")
elif Not > 65:
    print("BB")
elif Not > 55:
    print("CC")
elif Not>45:
    print("DD")
elif Not>0:
    print("EE")
else:
    print("Yanlış Not")

# x = 1
# y = -1
# z = 2
# if x == 0 and y<=0 or z != 0 and z == 2 or not x == 3:
#     print("Doğru")
# else:
#     print("Yanlış")



var1 = ""
var2 = []
var3 = 0

if var1:
    print("var1 Değişken Dolu")
elif var2:
    print("var2 Değişken Dolu")
elif var3:
    print("var3 Değişken Dolu")
else:
    print("Tümü Boş")


liste = [1,2,3,4,5]
liste2 = liste
if 2 in liste:
    print("liste içinde")
if liste is liste2:
    print("eşitler")

metin = "Hava Kapalı Ama Akalım Arabaya Bindim Yürü Bakalım"

if "Hava" in metin:
    print("Fero")