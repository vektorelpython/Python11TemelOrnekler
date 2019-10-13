# units = [1,0.00078125,0.0352739619]
# menu = """
# 1- Gram
# 2- Oka
# 3- Ounce
# """

# weight = int(input("Enter Weight:"))
# print(menu)
# unit1 = int(input("Enter Unit 1:"))
# print(menu)
# unit2 = int(input("Enter Unit 2:"))
# result = weight*units[unit1-1]*units[unit2-1]
# print(result)

# def GramToOka(param,direction=0):
#     if direction == 0:
#         return param*0.00078125
#     else:
#         return param*1280

# def GramToOunce(param,direction=0):
#     if direction == 0:
#         return param*0.0352739619
#     else:
#         return param*28.34952



# def OkaToOunce(param,direction=0):
#     if direction == 0:
#         return param*0.0221480649414062
#     else:
#         return param*45.150671295463



# angle1 = int(input("Enter Angle 1:"))
# angle2 = int(input("Enter Angle 2:"))

# if (angle1 < 178 or  angle2 <178) and  (angle1 + angle2 < 180):
#     angle3 = 180 - (angle1+angle2)
#     if angle1 == angle2 == angle3:
#         result = "Eşkenar"
#     elif angle1 in [angle2,angle3] or angle2 in [angle3,angle1] or angle3 in [angle1,angle2]:
#         result = "ikizkenar"
#     else : 
#         result = "Normal"
#     print(result)



# number = input("Enter Number")
# basamak = len(number)
# sonuc = 0
# for i in range(0,basamak):
#     sonuc += int(number[i])**basamak
# if sonuc == int(number):
#     print("Sayı Armstrong Sayısıdır")
# else:
#     print("Üzgünüm")

import time



# def ArmstrongCheck(number):
#     temp = int(number)
#     basamak = len(number)
#     sonuc = 0
#     while temp > 0:
#         sonuc += (temp%10)**basamak
#         temp //=10
#     return sonuc == int(number)

# zaman = time.time()
# for i in range(10000000,1,-1):
#     if ArmstrongCheck(str(i)):
#         print(i)
# print(time.time()-zaman)


# numList = []
# number = 0
# adim = 0
# while  number != -1 and adim < 20:
#     number = int(input("Enter Number -1 For Quit"))
#     numList.append(number)
# else:
#     numList.sort()
#     numList.reverse()
#     print(numList[0])


