"""
Curs: Variabile, tipuri de date
Obiective curs:
Setup functional
Principii de baza in programare
Primul meu program Python
Print statement
Comentarii
Variabile
Cele mai uzuale tipuri de date
Type casting
Intro in operatori
Input statement
Complexitatea unui string (index, length, metode ajutatoare)
"""

# programul ruleaza de sus in jos, de la stanga la dreapta

print("Hello World, PYTA20!")
# print("Luni")
# print(29)
# comentam o linie de cod

# variabile
masina = "Volvo"             # date de tip string
an_inmatriculare = 2000      # date de tip integer
pret_masina = 15000.50       # date de tip float
inmatriculata = True         # date de tip boolean


# Mihai si-a cumparat o masina Volvo care este inmatriculata in anul 2000.
print("Mihai si-a cumparat o masina Volvo care este inmatriculata in anul 2000.")
print(f"Mihai si-a cumparat o masina {masina} care este inmatriculata in anul {an_inmatriculare}.")
print(f"Pretul masinii a fost de {pret_masina} euro")


pret_masina = 10000.459
print(f"Pretul masinii este de {pret_masina} euro")

masina1 = "Dacia"
masina3 = "BMW"

nota_mate, nota_fizica, nota_sport = 10, 9, 7    # mandatory: declaram 3 variabile, trebuie 3 valori
print("nota mate: ", nota_mate)
print("nota fizica: ", nota_fizica)
print("nota sport: ", nota_sport)
ore_romana = ore_mate = 4

GRUPA = 'PYTA_20'
print(GRUPA)
# GRUPA = "pyta_20"
# print(GRUPA)        # suprascriere

nume = 'Popescu'
prenume = 'Maria'
nume_restaurant = "Mc'Donalds"


# Exercitiile: 1, 2, 3 -  studiu individual


# # concatenarea stringurilor
# nume_complet = nume + prenume
# print (nume_complet)
#
# varsta = 20
# # Maria are 20 de ani
# print(f"{prenume} are {varsta} ani")
# print(prenume + " are " + str(varsta) + " ani")     # concatenam date de tip string si facem un type-casting (convertim datele de tip int in date de tip string)
#
#
# pret = "15"
# print(type(pret))   # afiseaza ce tip de date este salvat in variabila pret
# pret = int(pret)
# print(type(pret))
#
#
# meniu = input("ce meniu doresti?")  # in variabila meniu salvez datele preluate de la tastatura cu ajutorul functiei input
# print (meniu)                       # afisam datele din variabila meniu
# print(type(meniu))                  # afisam tipul de date
#
# pret_meniu = int(input("care este pretul meniului?"))
# print (pret_meniu)
# print(type(pret_meniu))
#
# # Maria a mers la Mc'Donalds si a cumparat un meniu mediu, iar pretul a fost de 15 lei
# print(f"{prenume} a mers la {nume_restaurant} si a cumparat un meniu {meniu}, iar pretul a fost de {pret_meniu} lei")   # folosind print formatting
# print(prenume + " a mers la " + nume_restaurant + " si a cumparat un meniu " + meniu + ", iar pretul a fost de " + str(pret_meniu) + " lei")    # folosind type-casting


# 10 exercitii de facut pana joi



print(3)
print(3.5)

print("rosu", "galben")
print("verde", "albastru", sep=", ")

print("text1", end="*")
print("text2", end="*")

print("text3", "text4", sep=",", end="***")

print()

# nume2 = input('Cum te numesti? ') # default - string
# varsta = int(input('Cati ani ai? ')) # fortam varsta sa fie un int
#
# print(nume2)
# print(varsta)


numar1 = 10
numar2 = '10'

print(type(numar1))
print(type(numar2))

print(type(int(numar2)))

numar2 = '11'
print(type(numar2))

numar2 = 11
print(type(numar2))



"""
BONUS
type casting/conversie date de tip int in date de tip bool
"""

open1 = 0
open1 = 1
# open1 = -1            # pentru orice alta valoare, inafara de 0, va returna True
print(type(open1))
open1 = bool(open1)
print(type(open1))
print(open1)
