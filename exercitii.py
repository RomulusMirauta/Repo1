"""
Rezolvari exercitii sesiunea 1
"""



def create_triggered_function():        # definim functia "create_triggered_function"
    call_count = 0                      # defineste variabila locala call_count si o initializeaza cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function" este apelata
        print()                         # printam un rand liber
        print()
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print(f"Output pentru exercitiul cu numarul [ {call_count} ]")
                                        # ⬆️ printeaza text + valoare stocata in variabila "call_count" - loop iteration, printeaza o data per apelare functie
        print()
    return triggered_function           # acerst return este folosit pentru functia "create_triggered_function"

# Create the triggered function         # TBD
triggered_function = create_triggered_function()

# Example usage:
# triggered_function()                  # apelarea functiei



"""
EX1:
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""

triggered_function()

latime = 1                      # integer
descriere = 'culoare albastra'  # string
pret = 7.99                     # float
discount = 5.1                  # float
initializat = True              # bool / boolean

print(latime)
print(descriere)
print(pret)
print(discount)
print(initializat)





"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""

triggered_function()

viteza1 = viteza2 = 10



"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.
"""

triggered_function()

tip_masina, culoare_masina = 'hatchback', 'silver'



"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""

triggered_function()

nume = "Ford"
pret = "5k euro"
print("Marca este: " + nume + ", iar pretul este: " + pret)



"""
EX5:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""

triggered_function()

nume = 'Romulus'
varsta = 27
print(f"Numele meu este {nume} si am {varsta} de ani.")     # string formatting



"""
EX6:
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
"""

triggered_function()

putere = 82
print(putere)
print(type(putere))

pret_combustibil = 7.99
print(pret_combustibil)
print(type(pret_combustibil))

culoare = 'argintiu'
print(culoare)
print(type(culoare))

ITP_valid = True
print(ITP_valid)
print(type(ITP_valid))



"""
EX7: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""

triggered_function()

serie = 12345
print(serie)

print(type(serie))

serie_float = float(serie)

print(type(serie_float))



"""
EX8:
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
"""

triggered_function()

model = 'Fiesta'
print(model)

print(type(model))

# model_int = int(model)

# Observatie: nu putem forta conversia string to int => eroare.



"""
EX9: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""

triggered_function()

# nume_produs = input('Care este numele produsului? ')
# print("Numele produsului este: " + nume_produs)


"""
EX10: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""

triggered_function()

# pret = float(input('Care este pretul dorit? '))
# print(f"Pretul produsului este: {pret}")