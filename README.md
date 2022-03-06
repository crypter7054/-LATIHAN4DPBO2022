# LATIHAN4DPBO2022
## Identitas
- Nama : Yosafat
- NIM  : 2009929
- Prodi : Ilmu Komputer C2

## Janji
Saya Yosafat (2009929) mengerjakan evaluasi Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Soal
1. Task
Make a design and the program for this assignment : Formatted as PNG / JPEG / JPG (ex : Link) and put the link of the design in the description on the README on your GitHub project, and add the explanation of the design (Why do you use this design over another?).
Make a program with Python implementing Multiple Inheritance/ Hierarchical Inheritance and using getter, setter, make dummy data (Min : 5 data per class & print the data) and print the content of the class.

The classes are :
Vehicle : fuelType, maxPassengers, Move()
Ship : age, type, countryOfManufacture
Airplane : type, age, wingsLength

Person : NIK, Name, Gender, sleep()
Job : NIP, companyName, position
Driver : lisenceID, activeUntil, vehicleType


### Analisis
Berdasarkan soal, maka dapat diidentifikasi beberapa hal yaitu sebagai berikut:

1. Membuat program menggunakan paradigma pemrograman berorientasi objek atau OOP dan menerapkan konsep composition pada bahasa Java, C++, PHP, dan Python. Dikarenakan akan menggunakan paradigma pemrograman berorientasi objek, maka pada program ini akan membutuhkan lebih dari satu kelas untuk menerapkan konsep composition yaitu pada kelas Pc. Berdasarkan kondisi nyata dan ketentuan soal, maka model composition dari soal ini adalah kelas Pc akan menampung objek dari kelas-kelas lain yaitu kelas Processor, Disk, dan Ram. 
2. Pada program ini terdapat beberapa kelas yaitu Processor, Disk, Ram, dan Pc yang masing-masing kelasnya terdapat atribut. Kelas-kelas tersebut harus memiliki method Setter dan Getter. Kelas Memory terdapat atribut name yang bertipe data string karena akan menampung kumpulan karakter dan price yang akan menampung data integer dikarenakan data yang akan dimasukkan berupa angka. Kemudian untuk kelas Disk, atribut type, capacity dan price akan bertipe data integer dikarenakan pada representasi nyatanya data yang akan dimasukkan berupa angka. Sedangkan untuk kelas Ram, atribut capacity dan price bertipe data integer yang sesuai dengan representasi data nyatanya bahwa kapasitas dan harga dinyatakan sebagai angka. Terkahir pada kelas Pc terdapat 3 atribut objek yang akan digunakan untuk menerapkan konsep composition. Selain itu, terdapat atribut totalPrice yang digunakan untuk menampung jumlah dari harga-harag pada kelas Processor, Disk, dan Ram.
3. Method yang digunakan pada program ini antara lain, Constructor, Setter dan Getter, Display serta Destructor. Terdapat dua jenis Constructor pada program ini yaitu Constructor tanpa parameter dan Constructor dengan parameter. Beberapa bahasa program yang digunakan menerapkan kedua jenis Constructor, tetapi pada bahasa tertentu hanya menggunakan Constructor dengan parameter. Method Setter dan Getter yang akan digunakan pada program bertujuan untuk menerapkan konsep enkapsulasi. Kemudian, method Display adalah method yang dibuat untuk menampilkan data pada kelas tertentu. Kemudian pada kelas PC terdapat setter yang berbeda yaitu setTotalPrice dengan parameter tiga harga yang dibuat untuk menghitung jumlah harga dari ketiga kelas lainnya.

### Desain
1. Program terdiri dari file kelas yaitu, Processor, Disk, Ram, dan Pc serta file driver utama yaitu Main
2. Setiap bahasa program yang digunakan dibuat untuk dapat menerima inputan user, kecuali bahasa PHP data yang dimasukkan secara hardcode.
3. File kelas Processor terdapat deklarasi dan inisialiasi atribut private yaitu name dan price dengan tipe data yang telah ditentukan sebelumnya. Selanjutnya, terdapat deklarasi method Constructor, Setter dan Getter, Display, serta Destructor (pada bahasa tertentu). Sedangkan kelas Disk terdapat deklarasi dan inisialiasi atribut private yaitu type, capacity, dan price dengan tipe data yang telah ditentukan, seperti halnya dengan kelas Processor maka selanjutnya terdapat deklarasi method yang sama. Kemudian pada kelas Ram, algoritma yang dibuat tidak jauh berbeda dengan kelas-kelas lainnya, hanya berbeda pada atribut yang digunakan. Selanjutnya, pada kelas Pc terdapat deklarasi atribut private yaitu tiga objek dan satu atribut totalPrice, yang kemudian terdapat deklarasi method yang sama dengan kelas sebelumnya.
4. File Main menjadi driver utama yang terdapat deklarasi untuk import file kelas yang dibutuhkan. Pada kasus ini, pada bahasa C++, Python, dan PHP terdapat deklarasi awal untuk import file kelas. Selanjutnya, terdapat deklarasi variabel inputan user untuk menerima inputan data pada setiap kelas. Setelah menerima inputan user, maka proses instansi objek menggunakan Constructor dengan parameter dilakukan. Proses instansi pada objek Processor, Disk, dan Ram menggunakan Constructor, tetapi untuk kelas Pc pada beberapa bahasa program menggunakan Setter untuk instansi objeknya. Terakhir, data pada obek akan ditampilkan menggunakan method Display sekaligus menguji konsep composition


## Screenshot
