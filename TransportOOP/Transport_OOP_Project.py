class Vehicul:
    def __init__(self, marca, an_fabricatie, numar_locuri, combustibil):
        self.marca = marca
        self.an_fabricatie = an_fabricatie
        self.numar_locuri = numar_locuri
        self.combustibil = combustibil

    def afiseaza_info(self):
        return f"Vehicul marca: {self.marca}, an de fabricatie: {self.an_fabricatie}, numar de locuri: {self.numar_locuri}, merge cu {self.combustibil}"


class Autobuz(Vehicul):
    def __init__(self, marca, an_fabricatie, numar_locuri, combustibil, linie, sofer):
        super().__init__(marca, an_fabricatie, numar_locuri, combustibil)
        self.linie = linie
        self.sofer = sofer

    def afiseaza_ruta(self):
        return f"Ruta pe care acest autobuz circlula este {self.linie}"

    def afiseaza_sofer(self):
        return f"Soferul se numeste {self.sofer}"


class Camion(Vehicul):
    def __init__(self, marca, an_fabricatie, numar_locuri, combustibil, tonaj_maxim, marfa_transportata):
        super().__init__(marca, an_fabricatie, numar_locuri, combustibil)
        self.tonaj_maxim = tonaj_maxim
        self.marfa_transportata = marfa_transportata

    def afiseaza_tonaj_maxim(self):
        return f"tonajul maxim pe care il poate transporta acest camion este de {self.tonaj_maxim} tone"

    def incarca_marfa(self, cantitate):
        if cantitate < self.tonaj_maxim:
            self.tonaj_maxim -= cantitate
        else:
            print("Ati depasit tonajul maxim")
        return f"Ati incarcat {cantitate} tone de marfa in camion, ati mai ramas cu {self.tonaj_maxim} tone disponibile "

    def descarca_marfa(self, cantitate):
        self.tonaj_maxim += cantitate
        return f"Ati descarcat {cantitate} tone de marfa, acum aveti {self.tonaj_maxim} tone disponibile"


class CompanieTransport:
    def __init__(self, nume, adresa):
        self.nume = nume
        self.adresa = adresa
        self.vehicule = {}
        self.soferi = []

    def afiseaza_informatii(self):
        return f"Numele companiei: {self.nume}\Adresa companiei: {self.adresa}"

    def adauga_vehicul(self, vehicul):
        if vehicul not in self.vehicule.keys():
            self.vehicule[vehicul] = vehicul.afiseaza_info
            return self.vehicule
        else:
            return False

    def cauta_vehicul(self, vehicul):
        if vehicul in self.vehicule.keys():
            True
        else:
            False

    def sterge_vehicul(self, vehicul):
        if vehicul in self.vehicule.keys():
            del self.vehicule[vehicul]
            True
        else:
            False

    def afiseaza_flota(self):
        return f"Flota este formata din {self.vehicule}"

    def afiseaza_soferi_autobuze(self):
        return f"Lista soferilor de autobuze este: {self.soferi}"


autobuz1 = Autobuz("Ford", "1995", "30", "benzina", "52-2", "Adrian")
print(autobuz1.afiseaza_info())
print(autobuz1.afiseaza_ruta())
print(autobuz1.afiseaza_sofer())

camion1 = Camion("Mercedes", "2006", "6", "motorina", 2000, "moloz")
print(camion1.afiseaza_info())
print(camion1.afiseaza_tonaj_maxim())
print(camion1.incarca_marfa(1500))
print(camion1.descarca_marfa(1000))

companie1 = CompanieTransport("TransportSRL", "Nicolae balcescu 1b")
print(companie1.afiseaza_flota())
print(companie1.adauga_vehicul(camion1))
print(companie1.afiseaza_flota())
print(companie1.afiseaza_informatii())
















