
try:
    a = int(input("1. Sayıyı Giriniz"))
    adim = "F1A1"
    b = int(input("2. Sayıyı Giriniz"))
    adim = "F1A2"
    if b == 0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Hobaaaaa",adim)
except Exception as hata:
    print(hata)
finally:
    print("Son olarak buradan aileme selam göndermek istiyorum")

