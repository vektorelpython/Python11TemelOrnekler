#fibanocci

# a = 1
# b = 1
# for i in range(0,11):       
#     c = a+b
#     print("fibannocci {}. sıradaki terim : {}".format(i+2,c))
#     a,b = b,c




# a = int(input("Sayıyı Giriniz :"))
# sonuc = 1
# for i in range(a,0,-1):
#     sonuc = sonuc * i
# print(sonuc)

# liste = ["Ali","Veli","Mahmut","Hakkı"]

# for i in liste:
#     print(i)

# for i in range(0,len(liste)):
#     print(liste[i])

# metin = "KATLANARAK"
# for item in metin:
#     print(item)


# a = int(input("Sayıyı Giriniz :"))

# # for i in range(2,a):
# #     if a % i == 0:
# #         break
# # else:
# #     print("Sayı Asal",a)
    

# for j in range(2,a):
#     for i in range(2,j):
#         if j % i == 0:
#             break
#     else:
#         print("Sayı Asal",j)
a = 1
# while a>0:
#     a = int(input("Sayıyı Giriniz :"))

    # for i in range(2,a):
    #     if a % i == 0:
    #         break
    # else:
    #     print("Sayı Asal",a)
        

#     for j in range(2,a):
#         for i in range(2,j):
#             if j % i == 0:
#                 break
#         else:
#             print("Sayı Asal",j)
# else:
#     print("iyi günler dileriz") 


ad = input("Adınızı giriniz")
if ad == "Soner":
    pass
else:
    print("merhaba",ad)


liste = ["Ahmet","Hakkı","Soner","Hülagü"]
for item in liste:
    if item == "Soner":
        continue
    print("Merhaba",item)