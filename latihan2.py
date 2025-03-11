class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")

    def bergerak(self):
        print("Kendaraan sedang bergerak.")


class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        super().info_kendaraan()
        print(f"Merk: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

    def bunyikan_klakson(self):
        print("Tin tin!")


class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda  # Enkapsulasi: private attribute
        self.__harga = harga  # Enkapsulasi: private attribute

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga = value

    def info_mobil_sport(self):
        super().info_mobil()
        print(f"Tenaga Kuda: {self.__tenaga_kuda} HP")
        print(f"Harga: {self.__harga} juta rupiah")

    def mode_balap(self):
        print("Mobil sport memasuki mode balap!")


# Contoh penggunaan
mobil_sport = MobilSport("Darat", 300, "Ferrari", 2, 700, 500)

mobil_sport.info_mobil_sport()
mobil_sport.bergerak()
mobil_sport.bunyikan_klakson()
mobil_sport.mode_balap()

# Menggunakan getter dan setter
print(f"Tenaga kuda sebelum diubah: {mobil_sport.get_tenaga_kuda()} HP")
mobil_sport.set_tenaga_kuda(750)
print(f"Tenaga kuda setelah diubah: {mobil_sport.get_tenaga_kuda()} HP")