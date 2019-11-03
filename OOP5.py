class DB:
    def __init__(self):
        self.__ip = "12.25.30.85"

    @property
    def ip(self):
        return self.__ip
    
    @ip.setter
    def ip(self,ip):
        liste = ip.split(".")
        for item in liste:
            if item in ("0","255"):
                print("Olmadı Yar")
                break
        else:
            self.__ip = ip
    @ip.deleter
    def ip(self):
        self.__ip = "12.25.30.85"


veritabani =  DB()
print("1",veritabani.ip)
veritabani.ip = "254.85.74.12"
print("2",veritabani.ip)
del veritabani.ip
print("3",veritabani.ip)
veritabani.__ip