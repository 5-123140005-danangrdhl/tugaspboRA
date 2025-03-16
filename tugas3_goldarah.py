import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        father_allele = random.choice(self.father.blood_types)
        mother_allele = random.choice(self.mother.blood_types)
        alleles = father_allele + mother_allele
        alleles = "".join(sorted(alleles)) #mengurutkan kombinasi alel
        if alleles in ["OO"]:
            return "O"
        elif alleles in ["AO", "AA"]:
            return "A"
        elif alleles in ["BO", "BB"]:
            return "B"
        else:
            return "AB"

# Contoh penggunaan
ayah = Father("AO")
ibu = Mother("BO")
anak = Child(ayah, ibu)
print(f"Golongan darah ayah: {ayah.blood_types}")
print(f"Golongan darah ibu: {ibu.blood_types}")
print(f"Golongan darah anak: {anak.blood_type}")
