# import file kelas yang dibutuhkan
from Person import Person
from Job import Job
from Driver import Driver


# PERSON DATA
print("============")
print("Person Data:")
print("============")


# instansi objek kelas Person dengan memanggil constructor parameter 
p1 = Person(5111, "Yos", "Male")
p2 = Person(5112, "Yoss", "Males")
p3 = Person(5113, "Yosss", "Maless")
p4 = Person(5114, "Yossss", "Malessz")
p5 = Person(5115, "Yosssss", "Malesssz")


# panggil method display dengan menerapkan konsep inheritance (yang dapat mengakses method yang ada pada kelas parent) untuk menampilkan data
p1.displayPerson()
p2.displayPerson()
p3.displayPerson()
p4.displayPerson()
p5.displayPerson()



# JOB DATA
print("\n\n=========")
print("Job Data:")
print("=========")

# instansi objek kelas Job dengan memanggil constructor parameter 
j1 = Job(201, "Sopi", "CEO")
j2 = Job(202, "AEMDE", "CTO")
j3 = Job(203, "Fantech", "Designer")
j4 = Job(204, "GBL", "Beban")
j5 = Job(205, "Utub", "CMO")

# panggil method display dengan menerapkan konsep inheritance (yang dapat mengakses method yang ada pada kelas parent) untuk menampilkan data
j1.displayJob()
j2.displayJob()
j3.displayJob()
j4.displayJob()
j5.displayJob()



# DRIVER DATA
print("\n============")
print("Driver Data:")
print("============")


# instansi objek kelas Driver dengan memanggil constructor parameter 
d1 = Driver(5111, "Yos", "Male", 201, "Sopi", "CEO", 32123, 2025, "X0120")
d2 = Driver(5112, "Yoss", "Males", 202, "AEMDE", "CTO", 43234, 2020, "X0121")
d3 = Driver(5113, "Yosss", "Maless", 203, "Fantech", "Designer", 54345, "X0122")
d4 = Driver(5114, "Yossss", "Malessz", 204, "GBL", "Beban", 65456, 2045, "X0124")
d5 = Driver(5115, "Yosssss", "Malesssz", 205, "Utub", "CMO", 76567, 2020, "X0125")

# panggil method display dengan menerapkan konsep inheritance (yang dapat mengakses method yang ada pada kelas parent) untuk menampilkan data
d1.displayDriver()
d2.displayDriver()
d3.displayDriver()
d4.displayDriver()
d5.displayDriver()