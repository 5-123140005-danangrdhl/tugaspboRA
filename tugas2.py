import random

class Robot:
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack
        self.defense = 5  # Nilai pertahanan default

    def attack_enemy(self, lawan):
        lawan.hp -= max(0, self.attack - lawan.defense) # Serangan dikurangi pertahanan
        print(f"{self.nama} menyerang {lawan.nama}!")

    def defend(self):
        self.defense += 5
        print(f"{self.nama} bertahan!")

    def surrender(self):
        self.hp = 0
        print(f"{self.nama} menyerah!")

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = 1

    def mulai_permainan(self):
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"\n--- Ronde {self.ronde} ---")
            self.tampilkan_status()
            self.pilih_aksi(self.robot1, self.robot2)
            if self.robot2.hp > 0: # Pastikan robot2 masih hidup sebelum gilirannya
                self.pilih_aksi(self.robot2, self.robot1)
            self.ronde += 1
            self.reset_defense() # Reset nilai pertahanan setiap ronde

        print("\n--- Permainan Berakhir ---")
        if self.robot1.hp > 0:
            print(f"{self.robot1.nama} menang!")
        else:
            print(f"{self.robot2.nama} menang!")

    def tampilkan_status(self):
        print(f"{self.robot1.nama}: HP = {self.robot1.hp}")
        print(f"{self.robot2.nama}: HP = {self.robot2.hp}")

    def pilih_aksi(self, robot, lawan):
        print(f"\nGiliran {robot.nama}:")
        print("1. Serang")
        print("2. Bertahan")
        print("3. Menyerah")
        pilihan = input("Pilih aksi: ")

        if pilihan == "1":
            robot.attack_enemy(lawan)
        elif pilihan == "2":
            robot.defend()
        elif pilihan == "3":
            robot.surrender()

    def reset_defense(self):
        self.robot1.defense = 5
        self.robot2.defense = 5

# Contoh penggunaan
robot1 = Robot("Atreus", 500, 10)
robot2 = Robot("Daedalus", 758, 7)
game = Game(robot1, robot2)
game.mulai_permainan()