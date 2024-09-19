#membuat class perpustakaan
class buku:
    jumlah_buku = 0
    #membuat construtor
    def __init__(self, judul, penulis, tahunterbit):
        #intance variabel
        self.judulbuku = judul
        self.penulisbuku = penulis
        self.tahunterbitbuku = tahunterbit
        buku.jumlah_buku += 1
    def __str__(self):
        return f"{self.judulbuku}, {self.penulisbuku}, {self.tahunterbitbuku}"
    def boreup(self, bore):
        self.tahunterbitbuku += bore

B1 =buku("ayat ayat cinta", "Habiburrahman El Shirazy", 2004)
print(B1)
print(buku.jumlah_buku)
B1.boreup(500)
print(B1)
B2 =buku("The Architecture of Love", "Ika Natassa", 2016)
print(B2)
print(buku.jumlah_buku)
B2.boreup(500)
print(B2)
B3 =buku("Autumn In Paris", "Illana Tan", 2007)
print(B3)
print(buku.jumlah_buku)
B3.boreup(500)
print(B3)