class Vehicle():
    
    # deklarasi dan inisialisasi atribut private
    __fuelType = ""
    __maxPassengers = 0


    # constructor tanpa parameter
    def __init__(self):
        __fuelType = ""
        __maxPassengers = 0
    
    # constructor dengan parameter
    def __init__(self, type = "", maxPass = 0):
        self.__fuelType = type
        self.__maxPassengers = maxPass


    # deklarasi setter sebagai method (Write)
    def setFuelType(self, type):
        self.__fuelType = type

    def setMaxPass(self, maxPass):
        self.__maxPassengers = maxPass


    # deklarasi getter sebagai method (Read Only)
    def getFuelType(self):
        return self.__fuelType

    def getMaxPass(self):
        return self.__maxPassengers
    

    # deklarasi method Move
    def Move(self, vType):
        print(str(vType) + " just move\n")

    
    # deklarasi method Display untuk menampilkan data menggunakan method Getter
    def displayVehicle(self):
        print("Fuel Type        : " + str(self.getFuelType()))  
        print("Max Passenger    : " + str(self.getMaxPass()))

    
