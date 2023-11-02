import datetime

class Produs:
    def __init__(self, nume, categorie, data, pret, cantitate):
        self.nume = nume
        self.data = data
        self.data_de_valabilitate = datetime.date(2023, 10, 20)
        self.categorie = categorie
        self.pret = pret
        self.cantitate = cantitate

    def adauga_produs(self, magazin, cumparaturi):
        nume_produs = self.nume.lower()
        if nume_produs in magazin.stoc.keys() and self.cantitate < magazin.stoc[nume_produs]:
            cumparaturi.cos[nume_produs] = self.pret * self.cantitate
            magazin.stoc[nume_produs] -= self.cantitate
            return cumparaturi.cos
        else:
            print(f"Produsul {self.nume} nu este in stocul magazinului")
            return False

    def returneaza_produs(self, magazin, cumparaturi):
        nume_produs = self.nume.lower()
        if nume_produs in cumparaturi.cos.keys():
            del cumparaturi.cos[nume_produs]
            magazin.stoc[nume_produs] += self.cantitate
            return f"Produsul {nume_produs} a fost returnat iar stocul a revenit la valoarea initiala"
        else:
            print(f"Produsul {nume_produs} nu se afla in cosul dumneavoastra")
            return False

    def adauga_stoc(self, magazin, produs, cantitate):
        if produs in magazin.stoc.keys():
            magazin.stoc[produs] += cantitate
            return magazin.stoc

    def adauga_categorie(self, magazin):
        if self.categorie not in magazin.categorie_produse:
            magazin.categorie_produse.append(self.categorie)
            return magazin.categorie_produse

    def verifica_data_de_valabilitate(self, magazin, cumparaturi, produs):
        if self.data < self.data_de_valabilitate:  # and produs in cumparaturi.cos.keys() or produs in magazin.stoc.keys() :
            print(f"Produsele ({produs}) sunt expirate asa ca va fi aruncat din cos si din stocul magazinului")
            # del cumparaturi.cos[produs]
            magazin.stoc[produs] -= self.cantitate
            return True
        else:
            print("Produsul inca este in termenul de valabilitate")
            return False


class Cumparaturi:
    def __init__(self):
        self.cos = {}

    def calcul_cos(self):
        valoare = sum(self.cos.values())
        return valoare


class Person:
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta


class Client(Person):
    def __init__(self, nume, prenume, varsta, salariu, job, departament):
        super().__init__(nume, prenume, varsta)
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.salariu = salariu
        self.job = job
        self.departament = departament
        self.info = {self.nume + " " + self.prenume: [self.varsta, self.salariu, self.job, self.departament]}

    def adauga_client(self, magazin):
        full_name = self.nume + " " + self.prenume
        if full_name not in magazin.clienti.keys():
            magazin.clienti[full_name] = [self.varsta, self.salariu, self.job, self.departament]
            return magazin.clienti
        else:
            return False


class Magazin:
    def __init__(self, nume):
        self.nume = nume
        self.categorie_produse = []
        self.clienti = {}
        self.stoc = {
            "mere": 250,
            "banane": 150,
            "lapte": 100,
            "paine": 150,
            "oua": 200,
            "cereale": 50,
            "branza": 100,
            "yogurt": 200,
            "ciocolata": 100,
            "orez": 170
        }


# Crearea unui magazin
magazin1 = Magazin("LIDL")

# Crearea unui cos de cumparaturi
cos1 = Cumparaturi()

# Introducere
print(
    f"Buna ziua si bine ati venit la magazinul {magazin1.nume} .\nAici puteti cumpara produse alimentare din urmatoarele categorii: \n\nLactate, Fainoase, Fructe, Animala, Cereale\n")
print("La categoria de lactate avem urmatoarele produse: Lapte si Branza ")

input1 = input("Ce doriti sa cumparati dintre acestea?(Lapte, Branza, ambele):")
# AMBELE
if input1.lower() == "ambele":
    print("Ati ales lapte si branza!")
    input2 = int(input("Ce cantitate ati dori pentru lapte?(1-10): "))
    if input2 < magazin1.stoc["lapte"] and magazin1.stoc["lapte"] > 0:

        # Creare obiect de tip lapte
        lapte = Produs("lapte", "lactate", datetime.date(2023, 11, 20), 25, input2)

        # Verificare termen de valabilitate
        if lapte.verifica_data_de_valabilitate(magazin1, cos1, "lapte") == False:
            lapte.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")

        input3 = int(input("Ce cantitate ati dori pentru branza?(1-10): "))
        if input3 < magazin1.stoc["branza"] and magazin1.stoc["branza"] > 0:

            # Creare obiect de tip branza
            branza = Produs("branza", "lactate", datetime.date(2023, 11, 20), 13, input3)

            # Verificare termen de valabilitate
            if branza.verifica_data_de_valabilitate(magazin1, cos1, "branza") == False:
                branza.adauga_produs(magazin1, cos1)
            else:
                print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
        else:
            # Adaugare stoc
            branza.adauga_stoc(magazin1, "branza", 100)
            print("Nu avem atata branza mosule, altadata poate ai noroc")
    else:
        # Adaugare stoc
        lapte.adauga_stoc(magazin1, "lapte", 100)
        print("Nu avem atata lapte domnle in magazin, reveniti maine")
# LAPTE
elif input1 == "Lapte".lower():
    print("Ati ales lapte!")
    input2 = int(input("Ce cantitate ati dori pentru lapte?(1-10): "))
    if input2 < magazin1.stoc["lapte"] and magazin1.stoc["lapte"] > 0:

        # Creare obiect de tip lapte
        lapte = Produs("lapte", "lactate", datetime.date(2023, 11, 20), 25, input2)

        # Verificare termen de valabilitate
        if lapte.verifica_data_de_valabilitate(magazin1, cos1, "lapte") == False:
            lapte.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
    else:
        # Adaugare stoc
        lapte.adauga_stoc(magazin1, "lapte", 100)
        print("Nu avem atata lapte domnle in magazin, reveniti maine")
    # BRANZA
elif input1 == "Branza".lower():
    print("Ati ales branza!")
    input2 = int(input("Ce cantitate ati dori pentru branza?(1-10): "))
    if input2 < magazin1.stoc["branza"] and magazin1.stoc["branza"] > 0:

        # Creare obiect de tip branza
        branza = Produs("branza", "lactate", datetime.date(2023, 11, 20), 13, input2)

        # Verificare termen de valabilitate
        if branza.verifica_data_de_valabilitate(magazin1, cos1, "branza") == False:
            branza.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
    else:
        # Adaugare stoc
        branza.adauga_stoc(magazin1, "branza", 100)
        print("Nu avem atata branza mosule, altadata poate ai noroc")
else:
    print("Ce ati ales nu face parte din categoria de lactate")

# PAINE
print("La categoria de fainoase avem urmatoarele produse: Paine ")
input1 = input("Doriti sa cumparati paine?(da/nu)")
if input1.lower() == "da":
    print("Ati ales sa cumparati paine")
    input2 = int(input("Ce cantitate ati dori pentru paine?(1-10): "))
    if input2 < magazin1.stoc["paine"] and magazin1.stoc["paine"] > 0:

        # Creare obiect de tip paine
        paine = Produs("paine", "fainoase", datetime.date(2023, 9, 20), 10, input2)

        # Verificare termen de valabilitate
        if paine.verifica_data_de_valabilitate(magazin1, cos1, "paine") == False:
            paine.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
    else:
        # Adaugare stoc
        paine.adauga_stoc(magazin1, "paine", 100)
        print("Nu avem paine ca la balamuc, sorry")

elif input1.lower() == "nu":
    print("Ati ales sa nu cumparati paine, verificati si celelalte produse pe care le avem!")
else:
    print("Ce ati ales nu face parte din categoria de fainoase")

# MERE
print("La categoria de fructe avem urmatoarele produse: Mere ")
input1 = input("Doriti sa cumparati Mere?(da/nu)")
if input1.lower() == "da":
    print("Ati ales sa cumparati mere")
    input2 = int(input("Ce cantitate ati dori pentru mere?(1-20): "))
    if input2 < magazin1.stoc["mere"] and magazin1.stoc["mere"] > 0:

        # Creare obiect de tip mar
        mar = Produs("mere", "fructe", datetime.date(2023, 7, 20), 3, input2)

        # Verificare termen de valabilitate
        if mar.verifica_data_de_valabilitate(magazin1, cos1, "mere") == False:
            mar.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
    else:
        # Adaugare stoc
        mar.adauga_stoc(magazin1, "mere", 100)
        print("Nu avem atatea mere in magazin")
elif input1.lower() == "nu":
    print("Ati ales sa nu cumparati mere, verificati si celelalte produse pe care le avem!")
else:
    print("Ce ati ales nu face parte din categoria de fructe")

# OUA
print("La categoria de animala avem urmatoarele produse: Oua ")
input1 = input("Doriti sa cumparati oua?(da/nu)")
if input1.lower() == "da":
    print("Ati ales sa cumparati oua")
    input2 = int(input("Ce cantitate ati dori pentru oua?(10-20): "))
    if input2 < magazin1.stoc["oua"] and magazin1.stoc["oua"] > 0:

        # Creare obiect de tip ou
        ou = Produs("oua", "animala", datetime.date(2023, 11, 20), 3, input2)

        # Verificare termen de valabilitate
        if ou.verifica_data_de_valabilitate(magazin1, cos1, "oua") == False:
            ou.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
    else:
        # Adaugare stoc
        ou.adauga_stoc(magazin1, "oua", 100)
        print("Nu avem atatea oua in magazin sorry")
elif input1.lower() == "nu":
    print("Ati ales sa nu cumparati oua, verificati si celelalte produse pe care le avem!")
else:
    print("Ce ati ales nu face parte din categoria de animala")

# CEREALE
print("La categoria de cereale avem urmatoarele produse: Cereale ")
input1 = input("Doriti sa cumparati cereale?(da/nu)")
if input1.lower() == "da":
    print("Ati ales sa cumparati cereale")
    input2 = int(input("Ce cantitate ati dori pentru cereale?(1-10): "))
    if input2 < magazin1.stoc["cereale"] and magazin1.stoc["cereale"] > 0:

        # Creare obiect de tip cereale
        cereale = Produs("cereale", "cereale", datetime.date(2023, 9, 20), 17, input2)

        # Verificare termen de valabilitate
        if cereale.verifica_data_de_valabilitate(magazin1, cos1, "cereale") == False:
            cereale.adauga_produs(magazin1, cos1)
        else:
            print("Produsul este expirat, il vom arunca noi pentru dumneavoastra. Ne pare rau!")
    else:
        # Adaugare stoc
        cereale.adauga_stoc(magazin1, "cereale", 100)
        print("Nu avem atatea cutii de cereale in magazin, sorry")
elif input1.lower() == "nu":
    print("Ati ales sa nu cumparati cereale, verificati si celelalte produse pe care le avem!")
else:
    print("Ce ati ales nu face parte din categoria de cereale")

# PRINTARE COS DE CUMPARATURI
print(f"Cosul dumneavoastra arata asa: {cos1.cos}")
print("Puteti merge la casa sa platiti alimentele")

# CASA DE MARCAT
input_verificare = input("Inainte de a incepe scanarea doriti sa returnati ceva din cosul dumneavoastra?(da/nu): ")
if input_verificare == "da":
    input1 = input(f"Ce doriti sa eliminati din cosul dumneavoastra?\n{cos1.cos}: ")
    if input1 in cos1.cos.keys():
        del cos1.cos[input1]
        print(f"Produsul ales ({input1} a fost eliminat din cos)")
        print(f"Asa arata cosul dumneavoastra {cos1.cos}")
else:
    print("Ok vom continua atunci")

input1 = input("Doriti sa incepe scanarea produselor? y/n: ")

if input1 == "y":
    print(f"Cosul dumneavoastra: {cos1.cos}")
    print(f"Valoarea totala a produselor dumneavoastra este de {cos1.calcul_cos()}")
    modalitate_plata = input("Cum doriti sa platit? cash/card:")

    # CASH
    if modalitate_plata == "cash":
        suma_plata = int(input("Ce suma doriti sa platiti(bacnote de 5, 10, 50, 100, 200): "))
        if suma_plata == cos1.calcul_cos():
            print("Ati achitat alimentele cu suma fixa, rest 0")
        elif suma_plata > cos1.calcul_cos():
            rest = suma_plata - cos1.calcul_cos()
            print(f"Ati achitat alimentele cu o suma mai mare, rest {rest}")
        else:
            adaugare_suma = int(
                input("Nu aveti bani suficienti, mai adaugati bani(bacnote de 5, 10, 50 ,100 si 200): "))
            suma_plata += adaugare_suma
            if suma_plata == cos1.calcul_cos():
                print("Ati achitat alimentele cu suma fixa, rest 0")
            elif suma_plata > cos1.calcul_cos():
                rest = suma_plata - cos1.calcul_cos()
                print(f"Ati achitat alimentele cu o suma mai mare, rest {rest}")
            else:
                print("Returnati cateva produse apoi intorceti-va la casa de marcat")
    # CARD
    elif modalitate_plata == "card":
        card = int(input("Cati bani aveti pe card?: "))
        if card >= cos1.calcul_cos():
            print("Ati achitat cu suma fixa, rest 0 ")
        else:
            print("sold insuficient, va trebuii sa platiti cu cash sau sa returnati produsele")
    else:
        print("Ne pare rau nu acceptam aceasta modalitate de plata")

input_user = input(
    "Indiferent de ce s-a intamplat, va multumim pentru sansa acordata de a cumpara de la magazinul nostru. \nPutem sa va retinem maxim 2 minutele pentru a face un sondaj de opinie?(da/nu): ")
if input_user == "da":
    input1 = input("Cum va numiti?(N familie): ").capitalize()
    input2 = input("Si prenumele?: ").capitalize()
    input3 = int(input("Cati ani aveti?: "))
    input4 = int(input("Cat castigati pe luna?: "))
    input5 = input("Cu ce va ocupati?: ").capitalize()
    input6 = input("In ce domeniu activati?: ").capitalize()

    client = Client(input1, input2, input3, input4, input5, input6)
    client.adauga_client(magazin1)
    print(
        "Ati fost adaugat in baza de date a magazinului si de azi inainte sunteti eligibil pentru ofertele noastre speciale!")
    print(magazin1.clienti)
elif input_user == "nu":
    print(
        "Nu-i nici o problema, va intelegem. \nMultumim pentru prezenta dumneavoastra in magazinul nostru. \nO zi frumoasa sa aveti!")
else:
    print("Nu ati raspuns cum trebuie, mai incercati")



