# Membuat Kelas Hero
class Hero:
    # Membuat Konstruktor untuk menampung atribut
    def __init__(self, name, role, health_point, attack_damage, skill):
        # lakukan inisiasi untuk masing masing variabel
        self.nm = name
        self.rl = role
        self.hp = health_point
        self.ad = attack_damage
        self.sk = skill
    # membuat Method Attack
    def attack(self, target):
        target.hp -= self.ad
        print(f"{self.nm} menyerang {target.nm}")
        print(f"{target.nm} kehilangan {self.ad} HP.")
    # membuat method Use skill
    def useskill(self, target):
        target.hp -= self.ad * 2.5
        print(f"{self.nm} menggunakan skill: {self.sk}! \n{target.nm} kehilangan {int(self.ad * 2.5)} HP")
    # membuat method show stats
    def showstats(self):
        print(f"Status: {self.nm}")
        print(f"Role: {self.rl}")
        print(f"HP: {int(self.hp)}")
        print(f"AD: {self.ad}")
        print(f"Skill: {self.sk}")
        print("----------------------")
asa = Hero("asa","Marksman",350,50,"Destruction Rush")
# asa.showstats()
tigreal = Hero("Tigreal", "Tank", 500, 40, "Sacred Hammer")
# tigreal.showstats()
asa.attack(tigreal)
tigreal.useskill(asa)
asa.showstats()
tigreal.showstats()