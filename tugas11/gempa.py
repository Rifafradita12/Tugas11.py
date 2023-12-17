class Gempa:
    def _init_(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print(f"Gempa di {self.lokasi} tidak terasa.")
        elif 2 <= self.skala < 4:
            print(f"Gempa di {self.lokasi} menyebabkan bangunan retak-retak.")
        elif 4 <= self.skala < 6:
            print(f"Gempa di {self.lokasi} menyebabkan bangunan roboh.")
        elif self.skala >= 6:
            print(f"Gempa di {self.lokasi} menyebabkan bangunan roboh dan berpotensi tsunami.")

# Contoh penggunaan:
lokasi_gempa = "Pulau Jawa"
skala_gempa = 5.8

gempa_hari_ini = Gempa(lokasi_gempa, skala_gempa)
gempa_hari_ini.dampak()