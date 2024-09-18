"""
EXERCITII WORKSHOP (Sesiunea 1)
"""

# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------

def create_triggered_function():        # definim functia "create_triggered_function"
    call_count = 0                      # defineste variabila locala call_count si o initializeaza cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function" este apelata
        # print()                         # printam un rand liber
        # print()
        print("-" * 150 + "\n" * 2)
        print(f"Output pentru exercitiul cu numarul [ {call_count} ]")
                                        # ⬆️ printeaza text + valoare stocata in variabila "call_count" - loop iteration, printeaza o data per apelare functie
        print()
    return triggered_function           # acerst return este folosit pentru functia "create_triggered_function"

# Create the triggered function         # TBD
triggered_function = create_triggered_function()

# Example usage:
# triggered_function()                  # apelarea functiei

# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------


"""
1. In cadrul unui comentariu, explica in cuvintele tale ce este o variabila.
"""

triggered_function()

# variabila = un loc din memoria de lucru in care stocam o anumita valoare (data), care poate fi apoi accesata (folosing numele variabilei); variabila => valoare poate varia, putem incarca o noua valoare in aceeasi variabila


"""
2. Declara si initializeaza cate o variabila din fiecare din urmatoarele tipuri de date:
- string
- int 
- float
- bool

OBSERVATIE: Valorile vor fi alese de tine, dupa preferinte.
"""

triggered_function()

string = 'Sir de caractere'
int = 29
float = 2.9
bool = True


"""
3. Utilizeaza functia type pentru a verifica daca variabilele definite la exercitiul 2 au tipul de date asteptat.
"""

triggered_function()

# print(type(string))     # str
# print(type(int))
# print(type(float))
# print(type(bool))


"""
4. 
a. Rotunjeste variabila de tip float definita la exercitiul 2, folosind functia round(),
si salveaza aceasta modificare in aceeasi variabila (SUPRASCRIERE).
b. Verifica si afiseaza tipul acesteia.
"""

triggered_function()

# float = round(float)
# # print(float)
# print(type(float))


"""
5. Foloseste functia print() si afiseaza in consola 4 propozitii,
folosind cele 4 variabile declarate la exercitiul 2. 
Rezolva nepotrivirile de tip prin ce modalitate doresti.
"""

triggered_function()

# print(f'Aceasta este o variabila de tip string: {string}')
# print(f'Aceasta este o variabila de tip int: {int}')
# print(f'Aceasta este o variabila de tip float: {float}')
# print(f'Aceasta este o variabila de tip bool: {bool}')


"""
6. Citeste de la tastatura:
- numele utilizatorului
- prenumele utilizatorului

Afiseaza propozitia 'Numele complet are x caractere',
unde x reprezinta numarul total de caractere din numele complet
al utilizatorului.
"""

triggered_function()

nume = input("Introduceti numele utilizatorului: ")
prenume = input("Introduceti prenumele utilizatorului: ")

print(f'Numele complet are {len(nume + prenume)} caractere')
