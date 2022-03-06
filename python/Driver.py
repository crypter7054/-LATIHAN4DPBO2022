
# import file kelas yang dibutuhkan
from Job import Job
from Person import Person

# deklarasi kelas driver yang merupakan multiple inheritance dari kelas Job dan Person
class Driver(Person, Job):

    # deklarasi dan inisialisasi atribut private
    __licenseID = 0
    __activeUntil = 0
    __vehicleType = ""


    # constructor tanpa parameter
    def __init__(self):
        __licenseID = 0
        __activeUntil = 0
        __vehicleType = ""

    # constructor dengan parameter
    def __init__(self, NIK = 0, name = "", gender = "", NIP = 0, company = "", position = "", licenseID = 0, active = 0, vehicle = ""):
        self.__licenseID = licenseID
        self.__activeUntil = active
        self.__vehicleType = vehicle
        self.setNIK(NIK)
        self.setName(name)
        self.setGender(gender)
        self.setNIP(NIP)
        self.setCompany(company)
        self.setPosition(position)


    # deklarasi setter sebagai method (Write)
    def setLicense(self, licenseID):
        self.__licenseID = licenseID

    def setActiveUntil(self, active):
        self.__activeUntil = active
    
    def setVehicleType(self, vehicle):
        self.__vehicleType = vehicle

    
    # deklarasi getter sebagai method (Read Only)
    def getLicense(self):
        return self.__licenseID
        
    def getActiveUntil(self):
        return self.__activeUntil

    def getVehicleType(self):
        return self.__vehicleType


    # deklarasi method Display untuk menampilkan data menggunakan method Getter
    def displayDriver(self):
        self.displayPerson()
        self.displayJob()
        print("License ID   : " + str(self.getLicense()))
        print("Active Until : " + str(self.getActiveUntil()))
        print("Vehicle Type : " + str(self.getVehicleType()))
        self.Sleep(self.getPositon())