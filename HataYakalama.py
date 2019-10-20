# try:
#     a = int(input("1. Sayıyı Giriniz"))
#     b = int(input("2. Sayıyı Giriniz"))
# except ValueError:
#     print("Değer Hatası Sayı ile kelime bölme")
# else:
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("Sıfıra Bölüm Yapmak Nedir?")

# try:
#     a = int(input("1. Sayıyı Giriniz"))
#     b = int(input("2. Sayıyı Giriniz"))
#     print(a/b)
# except (ValueError,ZeroDivisionError) :
#     print("Aferin Sana")



try:
    a = int(input("1. Sayıyı Giriniz"))
    b = int(input("2. Sayıyı Giriniz"))
    if b == 0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Hobaaaaa")
except Exception as hata:
    print(hata)
finally:
    print("Son olarak buradan aileme selam göndermek istiyorum")


