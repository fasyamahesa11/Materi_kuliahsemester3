# membuat sebuah super class
class Animal:
    # membuat kontruktor untuk menampung attribut
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras
    # membuat method bersuara
def Speaks(self):
    print(f"{self.name} bisa bersuara")
# membuat kelas 1 turunan dari super kelas
class Cat(Animal):
    def speakCat(self):
        print(f"Nama {self.name} dengan ras {self.ras} bersuara Meowwww")
# membuat kelas 2 turunan dari super kelas
class Dog(Animal):
    def speakDog(self):
        print(f"Nama {self.name} dari ras {self.ras} bersuara GUK GUK GUK")
# membuat objek
Cat = Cat("kitty", "anggora")
Cat.speakCat()
Dog = Dog("Puppy", "Pitbull")
Dog.speakDog()