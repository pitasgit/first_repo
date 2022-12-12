class Automobil:
    # la inceput, definim atributele
    numar_roti = 4
    forma = None
    culoare = None
    numar_usi = 2
# mai jos, definim metode.
    def printeaza_numar_roti(self):
        if self.numar_roti == 2:
            print(f"Numarul de roti este {self.numar_roti}")
            print("Automobilul nostru este motocicleta")

    def printeaza_forma(self, tablaria):
        self.forma = tablaria
        if self.forma == "SUV":
            print(f"Forma este {self.forma}")


    def printeaza_culoare(self):
        if self.numar_roti == 1:
            print(f"Numarul de roti este {self.numar_roti}")
            print("Automobilul nostru este motocicleta")

    def printeaza_numar_usi(self):
        if self.numar_usi == 2:
            print(f"Numarul de usi este {self.numar_usi}")
            print("Automobilul nostru este masina sport")
        elif self.numar_usi == 0:
            print(f"Numarul de usi este {self.numar_usi}")
            print("Automobilul nostru este o motocicleta")
        elif self.numar_usi == 4:
            print(f"Numarul de usi este {self.numar_usi}")
            print("Automobilul nostru este o masina de familie")

# mai jos, am facut o initializare. Am initializat clasa automobil in obiectul caruta
caruta = Automobil()


# acum, folosim proprietatile obiectului caruta.
# 1: apelarea de atribute
print(caruta.numar_usi)
# 2: apelarea de metode
caruta.printeaza_numar_usi()
# 3: apelarea de metode cu argumente
caruta.printeaza_forma("SUV")