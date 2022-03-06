class Person():

    # deklarasi dan inisialisasi atribut private
    __NIK = 0
    __name = ""
    __gender = ""
    

    # constructor tanpa parameter
    def __init__(self):
        __NIK = 0
        __name = ""
        __gender = ""

    # constructor dengan parameter
    def __init__(self, NIK = 0, name = "", gender = ""):
        self.__NIK = NIK
        self.__name = name
        self.__gender = gender

    
    # deklarasi setter sebagai method (Write)
    def setNIK(self, nik):
        self.__NIK = nik

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender


    # deklarasi getter sebagai method (Read Only)
    def getNIK(self):
        return self.__NIK
    
    def getName(self):
        return self.__name
    
    def getGender(self):
        return self.__gender


    # deklarasi method sleep
    def Sleep(self, name):
        print(str(name) + " is not sleep\n")

    
    # deklarasi method Display untuk menampilkan data menggunakan method Getter
    def displayPerson(self):
        print("NIK          : " + str(self.getNIK()))
        print("Name         : " + str(self.getName()))
        print("Gender       : " + str(self.getGender()))