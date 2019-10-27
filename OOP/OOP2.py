"""
class Sınıf:
    # class attribute
    sinif_niteligi = 0
    def __init__(self):
        #instance attributes
        self.ornek_nitelik = 0
        self.ornek_nitelik2 = 0
    
    # instanse methods
    def ornek_metod(self):
        self.ornek_nitelik
    def ornek_metod2(self):
        self.ornek_metod()
    #class methods
    @classmethod
    def sinif_metodu(cls):
        pass

#instanstiation
Sınıf()
instance1 = Sınıf()
instance2 = Sınıf()

"""

# class Person:
#     def __init__(self,name):
#         self.name1 = name
#     def say_hi(self):
#         print("Hello How r u? ",self.name1)
    
# p = Person("Jason")
# p.say_hi()


import time
class Robot:
    """ Bir Robot Temsil Eder isim girilmeli """
    population = 0

    def __init__(self,name):
        self.name = name
        print("Oluşturuluyor {}".format(self.name))
        Robot.population += 1

    def die(self):
        """ Ölüyorum Haberin Yok """
        print("{}   Yok edildi".format(self.name))
        Robot.population -= 1
    def say_hi(self):
        print("Hello How r u? ",self.name)

    @classmethod
    def kac_tane(cls):
        """ Kaç Robot Olduğunu Söyler"""
        print("Toplam {} robot var".format(cls.population))


droid = Robot("Soner")
droid.say_hi()
Robot.kac_tane()

time.sleep(2)

droid2 = Robot("Şevket")
droid2.say_hi()
Robot.kac_tane()

time.sleep(2)

droid.die()
droid2.die()

time.sleep(2)
Robot.kac_tane()
    