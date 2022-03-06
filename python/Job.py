class Job():

    # deklarasi dan inisialisasi atribut private
    __NIP = 0
    __companyName = ""
    __position = ""


    # constructor tanpa parameter
    def __init__(self):
        __NIP = 0
        __companyName = ""
        __position = ""

    # constructor dengan parameter
    def __init__(self, NIP = 0, company = "", position = ""):
        self.__NIP = NIP
        self.__companyName = company
        self.__position = position


    # deklarasi setter sebagai method (Write)
    def setNIP(self, NIP):
        self.__NIP = NIP

    def setCompany(self, company):
        self.__companyName = company
    
    def setPosition(self, position):
        self.__position = position


    # deklarasi getter sebagai method (Read Only)
    def getNIP(self):
        return self.__NIP

    def getCompany(self):
        return self.__companyName

    def getPositon(self):
        return self.__position


    # deklarasi method Display untuk menampilkan data menggunakan method Getter
    def displayJob(self):
        print("NIP          : " + str(self.getNIP()))
        print("Company      : " + str(self.getCompany()))
        print("Position     : " + str(self.getPositon()))

