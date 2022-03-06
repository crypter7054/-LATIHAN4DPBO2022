# import file kelas Vehicle untuk menerapkan inheritance
from Vehicle import Vehicle


# deklarasi kelas Airplane sebagai Child dari kelas Vehicle
class Airplane(Vehicle):

    # deklarasi dan inisialisasi atribut private
    __type = ""
    __age = 0
    __wingsLength = 0


    # constructor tanpa parameter
    def __init__(self):
        __type = ""
        __age = 0
        __wingsLength = 0

    # constructor dengan parameter
    def __init__(self, type = "", age = 0, wingLen = 0, fuelType = "", maxPass = 0):
        self.__type = type
        self.__age = age
        self.__wingsLength = wingLen
        self.setFuelType(fuelType)
        self.setMaxPass(maxPass)


    # deklarasi setter sebagai method (Write)
    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age
    
    def setWingLen(self, wingLen):
        self.__wingsLength = wingLen


    # deklarasi getter sebagai method (Read Only)
    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age
    
    def getWingLen(self):
        return self.__wingsLength


    # deklarasi method Display untuk menampilkan data menggunakan method Getter
    def displayAirplane(self):
        print("Type             : " + str(self.getType()))
        print("Age              : " + str(self.getAge()) + " Years")
        self.displayVehicle()
        self.Move(self.getType())

