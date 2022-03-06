# import file kelas yang dibutuhkan
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane



# VEHICLE DATA
print("=============")
print("Vehicle Data:")
print("=============")


# instansi objek kelas Vehicle dengan memanggil constructor parameter 
v1 = Vehicle("Coal", 100)
v2 = Vehicle("Solar", 50)
v3 = Vehicle("Solar", 100)
v4 = Vehicle("Diesel", 20)
v5 = Vehicle("Avtur", 150)

# panggil method display dengan menerapkan konsep inheritance (yang dapat mengakses method yang ada pada kelas parent) untuk menampilkan data
v1.displayVehicle()
v2.displayVehicle()
v3.displayVehicle()
v4.displayVehicle()
v5.displayVehicle()


# SHIP DATA
print("\n==========")
print("Ship Data:")
print("==========")


# instansi objek kelas Ship dengan memanggil constructor parameter 
s1 = Ship("War Ship", 10, "Japan", "Biofuel", 80) 
s2 = Ship("War Ship", 20, "Germany", "Biofuel", 200) 
s3 = Ship("Fishing Ship", 15, "Indonesia", "Biofuel", 150) 
s4 = Ship("Cruise Ship", 10, "Singapore", "Biofuel", 500) 
s5 = Ship("Fishing Ship", 20, "China", "Biofuel", 50) 

# panggil method display dengan menerapkan konsep inheritance (yang dapat mengakses method yang ada pada kelas parent) untuk menampilkan data
s1.displayShip()
s2.displayShip()
s3.displayShip()
s4.displayShip()
s5.displayShip()

# AIRPLANE DATA
print("\n==============")
print("Airplane Data:")
print("==============")

# instansi objek kelas Airplane dengan memanggil constructor parameter 
air1 = Airplane("Boeing 001", 20, 30, "Avtur", 150)
air2 = Airplane("Airbus 002", 15, 20, "Avtur", 200)
air3 = Airplane("Boeing 003", 5, 20, "Avtur", 100)
air4 = Airplane("Boeing 004", 5, 20, "Avtur", 150)
air5 = Airplane("Airbus 005", 10, 30, "Avtur", 200)

# panggil method display dengan menerapkan konsep inheritance (yang dapat mengakses method yang ada pada kelas parent) untuk menampilkan data
air1.displayAirplane()
air2.displayAirplane()
air3.displayAirplane()
air4.displayAirplane()
air5.displayAirplane()
