# import file kelas Vehicle untuk menerapkan inheritance
from Vehicle import Vehicle


# deklarasi kelas Ship sebagai Child dari kelas Vehicle
class Ship(Vehicle):

    # deklarasi dan inisialisasi atribut private
    __age = 0
    __type = ""
    __countryOfManufacture = ""


    # constructor tanpa parameter
    def __init__(self):
        __age = 0
        __type = ""
        __countryOfManufacture = ""

    # constructor dengan parameter
    def __init__(self, type = "", age = 0, country = "", fuelType = "", maxPass = 0):
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = country
        self.setFuelType(fuelType)
        self.setMaxPass(maxPass)


    # deklarasi setter sebagai method (Write)
    def setAge(self, age):
        self.__age = age
    
    def setType(self, type):
        self.__type = type
    
    def setCountry(self, country):
        self.__countryOfManufacture = country
    

    # deklarasi getter sebagai method (Read Only)
    def getAge(self):
        return self.__age
    
    def getType(self):
        return self.__type
    
    def getCountry(self):
        return self.__countryOfManufacture

    
    # deklarasi method Display untuk menampilkan data menggunakan method Getter
    def displayShip(self):
        print("Type             : " + str(self.getType()))
        print("Age              : " + str(self.getAge()) + " Years")
        print("Country Producer : " + str(self.getCountry()))
        self.displayVehicle()
        self.Move(self.getType())