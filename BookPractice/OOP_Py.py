#Crearea unei clase
class Dog:
    #Crearea unui constructor cu argumentele name, age, weight
    def __init__(self, name, age, weight):
        """self devine obiectul nostru creat adica self = obj cu argumentele de dupa ele
        Adica obj cu numele Dodan 25 de ani si 25 kg"""
        self._name = name #-> protected
        self.__age = age #-> private
        self.weight = weight#-> public
    """Variabilele private si protected pot fi apelate doar din clasa mama. 
    Ele se pot apela din alte clase mostenitoare folosing getters.
    Pot fi modificate valorile din alte subclase folosint setters
    Conceptul protejarii a variabilelor se numeste Incapsulare"""


    #Getter pentru name care este protected si se noteaza cu un singur '_'
    def get_name(self):
        return self._name
    #Getter pentru age care este private si se noteaza cu doua '__'
    def get_age(self):
        return self.__age

    #Setter pentru _name
    def set_name(self,new_name):
        self._name = new_name
        return self._name

    #Setter pentru __age
    def set_age(self,new_age):
        self.__age = new_age
        return self.__age

    def __metoda_privata(self):
        return "Aceasta este o metoda privata"


    def print_dog(self):
        print(f"Name {self._name} , age {self.__age}, weight {self.weight}")

class ServiceDog(Dog):
    """Inheritance -> Sub clasa ServiceDog mosteneste super clasa Dog
    Folosim cuvantul cheie super() pentru a mostenii constructorul superclasei
    Atunci cand mostenim constructorul cu super nu adaugam 'self', doar argumentele pe care vrem sa le mostenim."""
    def __init__(self, name, age, weight, handler):
        super().__init__(name, age, weight)
        self.handler = handler

    #Aceasta metoda este una overriden din superclasa si conceptul folosit este numit Polimorfism.
    def print_dog(self):
                    #Getter                   #Getter
        print(f"Name {self.get_name()} , age {self.get_age()}, weight {self.weight} , handles {self.handler}")

    #putem adauga alte metode . . . .


obj = Dog("Dodan", 25, 25)
obj1 = ServiceDog("Pike", 20, 16, "Dodan")
obj.print_dog()
obj1.print_dog()





