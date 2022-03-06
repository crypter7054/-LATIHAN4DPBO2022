# LATIHAN4DPBO2022
## Identitas
- Nama : Yosafat
- NIM  : 2009929
- Prodi : Ilmu Komputer C2

## Janji
Saya Yosafat (2009929) mengerjakan evaluasi Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Soal
Make a design and the program for this assignment : Formatted as PNG / JPEG / JPG (ex : Link) and put the link of the design in the description on the README on your GitHub project, and add the explanation of the design (Why do you use this design over another?).
Make a program with Python implementing Multiple Inheritance/ Hierarchical Inheritance and using getter, setter, make dummy data (Min : 5 data per class & print the data) and print the content of the class.

The classes are :
Vehicle : fuelType, maxPassengers, Move()
Ship : age, type, countryOfManufacture
Airplane : type, age, wingsLength

Person : NIK, Name, Gender, sleep()
Job : NIP, companyName, position
Driver : lisenceID, activeUntil, vehicleType


### Analisis dan Desain
Berdasarkan soal, maka dapat diidentifikasi hasil analisis dan desain yaitu sebagai berikut:

Membuat program menggunakan paradigma pemrograman berorientasi objek atau OOP dan menerapkan konsep multiple/hierarchical pada bahasa Python. Dikarenakan akan menggunakan paradigma pemrograman berorientasi objek, maka pada program ini akan membutuhkan lebih dari satu kelas untuk menerapkan konsep inheritance. Berdasarkan kondisi nyata maka dapat ditentukan bahwa Vehicle memilik child yaitu kelas Ship dan Airplane, hal ini dikarenakan Ship dan Airplane merupakan jenis kendaraan. Sedangkan untuk kelas Driver merupakan child dari kelas Person dan Job, jika dianalisis dari atribut masing-masing kelas maka dapat ditentukan Person dan Job berada pada level yang sama sehingga menghasilkan turunan atau child yaitu Driver. Pada kelas Driver terdapat beberapa informasi gabungan yang merepresentasikan informasi dari kelas Person dan Job. Contohnya Driver perlu licenseID dimana atribut ini digunakan untuk merepsentasikan informasi bahwa pada Driver juga terdapat informasi tentang Person. Kemudian pada atribut vehicleType digunakan untuk merepresentasikan informasi bahwa Driver juga terdapat informasi tentang Vehicle. Berdasarkan asumsi dan analisis tersebut, maka desain model inheritance dari soal ini dapat digambarkan sebagai berikut:


![Desain LAT4](https://user-images.githubusercontent.com/77567907/156917805-71fa5f9c-60e1-46d4-8f42-23046564ee8e.jpg)



## Screenshot
### Airplane Data
![Airplane Data](https://user-images.githubusercontent.com/77567907/156917271-af91ea2e-2000-4883-828e-66181d42ab6e.jpg)

### Ship Data
![Ship Data](https://user-images.githubusercontent.com/77567907/156917279-2d93e700-a5ee-4fe0-9b9a-1c2dc97d666a.jpg)

### Vehicle Data
![Vehicle Data](https://user-images.githubusercontent.com/77567907/156917280-93f30f13-8a3f-4086-8bfd-353a8c965e38.jpg)

### Person Data
![Person Data](https://user-images.githubusercontent.com/77567907/156917277-4b459b2b-5feb-46a3-bc62-2ea3f054e12b.jpg)

### Job Data
![Job Data](https://user-images.githubusercontent.com/77567907/156917276-fa1c68d2-6885-4307-8d55-1524e3eecd2a.jpg)

### Driver Data
#### Bagian 1
![Driver Data (1)](https://user-images.githubusercontent.com/77567907/156917274-2bb3f573-8d42-433d-aff4-d35cd93422b9.jpg)

#### Bagian 2
![Driver Data (2)](https://user-images.githubusercontent.com/77567907/156917275-2670162c-0dbe-4d7f-b27f-5df81cbb9eb5.jpg)

