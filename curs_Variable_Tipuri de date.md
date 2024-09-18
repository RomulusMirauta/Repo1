# Curs: Variable, tipuri de date
## 📝 OBIECTIVE
1. Setup functional
2. Principii de baza in programare
3. Primul meu program Python
4. Print statement
5. Comentarii
6. Variabile
7. Cele mai uzuale tipuri de date
8. Type casting
9. Intro in operatori
10. Input statement
11. Complexitatea unui string (index, length, metode ajutatoare)

## 📌 Principii de baza in programare
- A compila = a traduce din 'human reading syntax' in 'machine language'
- Codul se interpreteaza secvential, linie cu linie, de sus in jos.
- Machine language = binary code (cod binar) - combinatii diferite de 0 si 1.
- Principiul seamana cu cel din codul morse. Pentru 1 se transmite un impuls electric, pentru 0 o pauza.
- 1 bit = memorie in care incape doar o singura valoare. 1 (true), 0 (false).
- 1 Byte = 8 biti. Numere intre 0 (000000) si 255 (111111).
- 1 Kilobyte = 1.024 bytes
- 1 Megabyte = 1.024 kilobytes (1.048.575 bytes)
- Terminal = zona in care trimitem instructiuni catre program (altele decat cod python).
Exemplu: 'python --version'.
Tot de aici putem instala librarii externe (ex: pip install selenium).
- Consola = zona in care primim output (raspuns vizual) de la programul rulat.
- IDE = Integrated Development Environment - Pycharm. Este un editor de cod.
- Venv = Virtual Environment - zona in care folosim in mod izolat si securizat toate librariile externe.

## 📌 Limbaj compilat vs limbaj interpretat
- limbaj compilat = transformarea codului din sintaxa citibila in cod citibil de procesor
    - codul e transformat (compilat) in limbaj masina iar ulterior rulat
    - limbaj compilat: Java
- limbaj interpretat = codul e citit la momentul executiei linie cu linie si transformat in cod masina "on the go"
    - limbaj interpretat: Python
    - in Python, interpretorul Python citeste codul linie cu linie si il transforma in cod masina in momentul executiei

## 📌 Primul meu program Python
Afisarea in terminal a mesajului "Hello World".

```python
print("Hello World")
```

## 📌 Functia built-in print()

❔ Ce este o functie?
- O functie este o logica de cod predefinita care face ceva.
- Are sintaxa **nume_functie()**
- In paranteza punem datele de intrare/ input (argumente sau parametri)
- Vom discuta pe larg despre functii in capitolele urmatoare.
- functiile built-in sunt furnizate de limbajul de programare, ele reprez parte integrata in limbajul de programare  
  -Exemple de functii: print(), type(), input(), int(), str(), bool(), float(), len(), sum(), etc.
🔸 Functia print() este polimorfica, ea afiseaza in consola ce punem in paranteze.

```pytho
print("Produsul acesta costa 5 lei.")
```

```python
print(3)
print(3.5)

print("rosu", "galben")
print("verde", "albastru", sep=",")

print("text1", end="*")
print("text2", end="*")

print("text3", "text4", sep=",", end="***")
```
### ❗ Rularea codului si consola
- Pentru rularea codului puteM da click dreapta oriunde in fisierul pe care vreti sa il rulati si selectati optiunea Run
- Rezultatele rularii fisierelor Python le gasim in consola
- IMPORTANT!! Codul scris trebuie sa respecte anumite “reguli” pe care sistemul le recunoaste, altfel vom primi ceea ce se numeste eroare de sintaxa. Sintaxa reprezinta totalitatea regulilor care definesc limbajul recunoscut de un sistem.

## 📌 Comentarii
### 🔸 Definitie
- Comentariile sunt linii de cod care sunt ignorate in timpul rularii unui program.

### 🔸 Tipuri de comentarii
In Python, comentariile sunt definite folosind semnul '#' la inceputul liniei de cod.

#### *Single-line comments*
- Exemplu
```python
# Acesta este un comentariu pe o singura linie
```

#### *Multi-line comments*
- Exemplu 1:
```python
# Acesta este un comentariu
# pe mai multe linii
```

- Exemplu 2:
```python
"""
Acesta este alt comentariu
pe mai multe linii
"""
```

### 🔸 De ce avem nevoie de comentarii?
- Documentarea codului
- Cresterea intelegerii codului
- Prevenirea executarii uneia sau mai multor linii de cod.

## 📌 Variabile: definitie, de ce avem nevoie de variabile
### 🔸 Definitie
- O variabila este un container(adresa) din memorie care stocheaza valori.
- Va puteti imagina o casa care se afla la o anumita adresa si contine mobila. 


```python
# declaram si initializam 2 variabile
marca_masina = 'Volvo'
model_masina = 'XC 60'
```
### ❗ De retinut
- Variabilele au un nume unic, ca sa poata fi identificate si folosite anterior.
- Variabila este creata in momentul in care ii atribuim o valoare.
- NU putem pune spatiu in numele unei variabile.
- Variabilele incep cu litera mica dar pot contine cifre (user1) si simbolul _.
- Variabilele sunt CASE-SENSITIVE (my_var = 5 e diferita de my_Var = 5).
- Variabilele pot sa isi schimbe valoarea pe parcursul executiei programului (suprascriere).
- Variabilele pot sa isi schimbe tipul de date pe parcursul executiei.
- Putem atribui mai multe valori in one line, sau aceeasi valoare mai multor variabile.

```python
x, y, z = "Orange", "Banana", "Cherry"
a = b = c = "Apple"
```
- Procesul de alocare de memorie pentru o variabila se numeste declarare, iar salvarea unei valori la acea adresa de memorie se numeste initializare. In Python declararea nu e posibila fara initializare

## 📌 Constantele: definitie si exemplu
### 🔸 Definitie
- Constantele sunt adrese din memorie care nu isi pot schimba valoarea pe parcursul executiei programului.
- constantele trebuie scrise cu litere mari.
- IMPORTANT!! In Python conceptul de constanta nu exista decat ca si conventie de scriere, daca vom incerca sa actualizam o valoare dintr-o constanta nu va returna eroare. Acest lucru nu se intampla in alte limbaje de programare.
```python
# exemplu de definire a constantelor
SUNT_INSCRIS_LA_CURS = True
```

### ❗ De retinut
- Se numeste constanta deoarece valoarea adresei de memorie NU poate sa varieze pe parcursul executiei programului (este constanta)
- Caracteristica principala a constantei este faptul ca nu isi poate schimba valoarea, drept urmare atunci cand definim o constanta este important sa nu uitam de aceasta, care e de fapt cea care descrie conceptul de constanta
- Cand vorbim despre o constanta vorbim despre o adresa de memorie, nu despre valoarea in acea adresa de memorie. Deci atunci cand definim o constanta nu spunem ca este o valoare, ci o adresa de memorie care stocheaza o valoare

## 📌 Tipuri de date: string, int, float, bool
- Datele/valorile salvate in variabile pot avea mai multe tipuri
- Exista mai multe tipuri de date dar cele mai importante/folosite sunt:
1. int = numar intreg
```python
# initializam o variabila de tip int/numar intreg
cantitate = 10
```
2. float = numar zecimal
```python
# initializam o variabila de tip float/numar zecimal
pret = 10.45
```
3. bool = adevarat/fals
```python
# initializam variabile de tip boolean
este_impar = False
este_par = True
```
4. string = sir de caractere de la tastatura delimitate de '  ' sau "  "
```python
# definim o variabila string folosind ghilimele simple
nume = 'Popa'

# definim o variabila string folosind ghilimele duble
prenume = "Maria"
```

```python
"""
EX1: 
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
```

```python
"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""
```

```python
"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.
"""
```

📌 Concatenarea string-urilor
- Putem concatena string-uri in doua moduri:
    - cu semnul "+"
    - folosind f-strings

```python
nume = 'Popescu'
print(nume)

prenume = 'Carmen'
print(prenume)

nume_complet = nume + prenume
print(nume_complet)
print('Numele meu este ' + nume + prenume)

varsta = 20
# print("Varsta mea este de:" + varsta) # da eroare
print(f"Varsta mea este de: {varsta}") 
print("Varsta mea este de: ", varsta)
```

```python
"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""
```

```python
"""
EX5:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""
```

## 📌 Functia built-in type()
- Functia type ne expune tipul de date al variabilei date ca input.

```python
# definim o variabila string
culoare = 'rosu'
# afisam in consola tipul variabilei culoare
print(type(culoare)) # <class 'str'>
```

- Convertirea tipurilor de variabile - type casting
```python
numar1 = 10
numar2 = '10'

# Sunt numar1 si numar2 de acelasi tip?
```
Functiile int(), str(), bool(), float() schimba tipul de date.

```python
"""
EX6:
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
"""
```

```python
"""
EX7: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""
```

```python
"""
EX8:
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
"""
```


## 📌 Functia built-in input()
- Functia input() ne ajuta sa luam date de la tastatura si sa le salvam intr-o variabila.
- Daca nu facem type casting, default-ul datelor furnizate de utilizator for fi te tip string.
- Ulterior putem accesa valorile salvate in variabile dupa necesitate.

```python
nume = input('Cum te numesti? ') # default - string
varsta = int(input('Cati ani ai? ')) # fortam varsta sa fie un int
```

```python
"""
EX9: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
```

```python
"""
EX10: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
```


