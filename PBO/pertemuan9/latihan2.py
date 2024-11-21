# implementasi polimorfisme dengan mencari bangun datar
class bangundatar: # abstrak class
    def luas (self): # abstrak method
        raise NotImplementedError("method ini wajib diimplementasikan")
class persegi(bangundatar): # kelas tururnan 1
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        print(f"luas persegi adalah: [self.sisi**2]")
class segitiga(bangundatar): # kelas turunan 2
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        print(f"luas segitiga adalah: {(self.alas*self.tinggi)/2}")
class lingkaran(bangundatar): # kelas turunan 2
    def __init__(self, r, pi=3.14 ):
        self.pi = pi
        self.r = r
    def luas(self):
        print(f"luas lingkaran adalah: {self.pi*(self.r**2)}")

objek1 = persegi(2)
objek2 = segitiga(2,3)
objek3 = lingkaran(5)
objek1.luas()
objek2.luas()
objek3.luas()