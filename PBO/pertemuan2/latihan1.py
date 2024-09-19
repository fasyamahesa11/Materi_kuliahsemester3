#membuat class
class mobil:
  #membuat class variabel
    jumlah_mobil =0
    #membuat construtor
    def __init__(self, ban, merk, cc):
        #intance variabel
        self.merkban = ban
        self.merkmobil = merk
        self.kapasitas = cc
        mobil.jumlah_mobil += 1
    #membuat method string
    def __str__(self):
        return f"{self.merkban}, {self.merkmobil}, {self.kapasitas}"
    #membuat method baru bore up
    def boreup(self, bore):
        self.kapasitas += bore

#membuat objek baru m1
m1 = mobil("Brigestone", "Toyota -Kijang", 1500)
print(m1)
print(mobil.jumlah_mobil)
m1.boreup(500)
print(m1)
#membuat objek baru m2
m2 = mobil("pirelll", "subaru", "2000")
print(m2)
print("jumlah mobil: ", mobil.jumlah_mobil)
 