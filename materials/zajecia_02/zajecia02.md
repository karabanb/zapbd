# Zajęcia 2: Podstawowe struktury danych i kontrola przepływu w Pythonie

## 1. Sekwencyjne typy danych

### Wprowadzenie do typów sekwencyjnych
Typy sekwencyjne to struktury danych, które przechowują uporządkowane kolekcje elementów. W Pythonie podstawowe typy sekwencyjne to listy, , słowniki, krotki, zakresy.

### Listy (list)
Listy to uporządkowane, zmienialne kolekcje elementów, które mogą być różnych typów.

```python
# Tworzenie listy
owoce = ["jabłko", "banan", "gruszka", "pomarańcza"]
mieszana_lista = [1, "dwa", 3.0, True, None]

# Dostęp do elementów (indeksowanie)
pierwszy_owoc = owoce[0]      # "jabłko"
ostatni_owoc = owoce[-1]      # "pomarańcza"

# Modyfikacja elementów
owoce[1] = "truskawka"        # ["jabłko", "truskawka", "gruszka", "pomarańcza"]

# Dodawanie elementów
owoce.append("malina")        # Dodaje element na końcu
owoce.insert(2, "borówka")    # Wstawia element na pozycji 2

# Usuwanie elementów
usuniety_owoc = owoce.pop(1)  # Usuwa i zwraca element na pozycji 1
owoce.remove("gruszka")       # Usuwa pierwsze wystąpienie "gruszka"

# Długość listy
liczba_owocow = len(owoce)

# Wycinki list (slicing)
pierwsze_dwa = owoce[0:2]     # ["jabłko", "truskawka"]
co_drugi = owoce[::2]         # co drugi element
```
### Zadanie praktyczne: Wprowadzanie danych BMI z wykorzystaniem list

W tym zadaniu przeanalizujemy dane dotyczące BMI (Body Mass Index) kilku osób. Wykonaj poniższe kroki w swoim notebooku Jupyter:

- stwórz listę osoba_1, która zawiera dane pojedyńczej osoby w postaci wartości dla pojedeynczej osoby. Niech wartości te reprezentują imię (str), wiek (int), waga (int), wzrost w m (float)
- na podstawie kalkulatora BMI dopisz jako ostatnią wartość wskaźnik BMI wyliczony na podstawie dostarczonych danych,
- zmodyfkuj imie osoby 

### Krotki (tuple)
Krotki to uporządkowane, niemodyfikowalne kolekcje elementów.

```python
# Tworzenie krotki
wymiary = (10, 20, 30)
osoba = ("Jan", "Kowalski", 30, "Programista")
pojedynczy_element = (42,)    # Krotka jednoelementowa (przecinek jest konieczny)

# Dostęp do elementów
imie = osoba[0]               # "Jan"
zawod = osoba[-1]             # "Programista"

# Próba modyfikacji wywołuje błąd
# osoba[0] = "Adam"  # TypeError: 'tuple' object does not support item assignment

# Rozpakowanie krotki
imie, nazwisko, wiek, zawod = osoba

# Krotki są niezmienne, ale mogą zawierać elementy zmienne
zmienne_dane = ([1, 2, 3], "test")
zmienne_dane[0].append(4)     # Modyfikacja listy w krotce jest dozwolona
```

### Łańcuchy znaków (str)
Łańcuchy znaków to sekwencje znaków, które są niemodyfikowalne.

```python
# Tworzenie łańcuchów znaków
tekst = "Python jest świetny!"
tekst_apostrofy = 'Python to język programowania'
tekst_wieloliniowy = """To jest tekst
na wiele
linii."""

# Dostęp do znaków
pierwsza_litera = tekst[0]    # "P"
ostatnia_litera = tekst[-1]   # "!"

# Wycinki
pierwsze_slowo = tekst[:6]    # "Python"
bez_pierwszego = tekst[7:]    # "jest świetny!"

# Podstawowe metody dla stringów
male_litery = tekst.lower()   # zamienia na małe litery
wielkie_litery = tekst.upper()  # zamienia na wielkie litery
zamiana = tekst.replace("Python", "JavaScript")  # zamienia "Python" na "JavaScript"
lista_slow = tekst.split()    # dzieli string na listę słów

# Łączenie (konkatenacja)
powitanie = "Cześć, " + "świecie!"

# Formatowanie
imie = "Anna"
wiek = 25
tekst_formatowany1 = "Mam na imię %s i mam %d lat." % (imie, wiek)
tekst_formatowany2 = "Mam na imię {} i mam {} lat.".format(imie, wiek)
tekst_formatowany3 = f"Mam na imię {imie} i mam {wiek} lat."  # f-string (od Python 3.6)
```
### Zadanie praktyczne: Wprowadzanie i modyfikaowanie danych tekstowych

W tym zadaniu będziemy modyfikować i formatować napisy przy uzyciu dostępnych metod:
- Wyciągnij z listy `osoba_1` imię i zapisz je do zmiennej 'imie'
- napdisz zmienna 'imie' i zmien w niej imie na pisane małymi literami
- utwórz nową zmienną 'imie_upper' w której imię jest w całości zapisany WIELKIMI LITERAMI
- 
### Zakresy (range)
Zakresy to sekwencje liczb całkowitych, często używane w pętlach.

```python
# Tworzenie zakresów
liczby1 = range(5)          # 0, 1, 2, 3, 4
liczby2 = range(2, 8)       # 2, 3, 4, 5, 6, 7
liczby3 = range(1, 10, 2)   # 1, 3, 5, 7, 9 (co drugi)

# Konwersja zakresu na listę
lista_liczb = list(liczby3)  # [1, 3, 5, 7, 9]

# Zakresy są często używane w pętlach for
for i in range(3):
    print(i)  # Wyświetli: 0, 1, 2
```

### Słowniki (dict)
Słowniki to kolekcje par klucz-wartość, które umożliwiają szybki dostęp do danych poprzez klucz.

```python
# Tworzenie słownika
osoba = {
    "imie": "Jan", 
    "nazwisko": "Kowalski", 
    "wiek": 30,
    "zawod": "Programista"
}

# Pusty słownik
pusty_slownik = {}
inny_pusty = dict()

# Dostęp do wartości przez klucz
imie = osoba["imie"]      # "Jan"

# Modyfikacja wartości
osoba["wiek"] = 31        # Zmiana istniejącej wartości
osoba["hobby"] = "Sport"  # Dodanie nowej pary klucz-wartość

# Bezpieczny dostęp z get()
telefon = osoba.get("telefon")  # None (klucz nie istnieje)
telefon = osoba.get("telefon", "brak")  # "brak" (wartość domyślna)

# Usuwanie elementów
usuniety_wiek = osoba.pop("wiek")  # Usuwa i zwraca wartość
del osoba["zawod"]               # Tylko usuwa

# Sprawdzanie czy klucz istnieje
if "hobby" in osoba:
    print("Osoba ma hobby")

# Iteracja po słowniku
for klucz in osoba:
    print(klucz, osoba[klucz])

# Iteracja po parach klucz-wartość
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")

# Pobieranie kluczy i wartości
klucze = osoba.keys()    # dict_keys(['imie', 'nazwisko', 'hobby'])
wartosci = osoba.values()  # dict_values(['Jan', 'Kowalski', 'Sport'])
pary = osoba.items()     # dict_items([('imie', 'Jan'), ('nazwisko', 'Kowalski'), ('hobby', 'Sport')])
```

Od Python 3.7 słowniki zachowują kolejność wstawiania elementów, co czyni je jeszcze bardziej wszechstronnymi.

### Operacje wspólne dla typów sekwencyjnych
```python
# Długość (len)
len([1, 2, 3])         # 3
len("Python")          # 6
len((1, 2, 3, 4, 5))   # 5

# Operator in (sprawdzanie zawierania)
2 in [1, 2, 3]         # True
"a" in "Python"        # False
"Py" in "Python"       # True

# Minimalna i maksymalna wartość
min([5, 2, 8, 1])      # 1
max("abcxyz")          # "z"

# Indeksowanie i wycinanie (działa dla list, krotek, stringów)
sekwencja = [10, 20, 30, 40, 50]
sekwencja[1]           # 20
sekwencja[-2]          # 40
sekwencja[1:4]         # [20, 30, 40]
sekwencja[:3]          # [10, 20, 30]
sekwencja[2:]          # [30, 40, 50]
sekwencja[::2]         # [10, 30, 50]
```

## 2. Instrukcje warunkowe if, elif, else

### Wprowadzenie do instrukcji warunkowych
Instrukcje warunkowe pozwalają na wykonanie różnych bloków kodu w zależności od spełnienia określonych warunków.

### Struktura instrukcji if, elif, else
```python
# Podstawowa struktura if
if warunek:
    # kod wykonywany, gdy warunek jest prawdziwy
    
# Struktura if-else
if warunek:
    # kod wykonywany, gdy warunek jest prawdziwy
else:
    # kod wykonywany, gdy warunek jest fałszywy
    
# Struktura if-elif-else
if warunek1:
    # kod wykonywany, gdy warunek1 jest prawdziwy
elif warunek2:
    # kod wykonywany, gdy warunek1 jest fałszywy, a warunek2 prawdziwy
elif warunek3:
    # kod wykonywany, gdy warunek1 i warunek2 są fałszywe, a warunek3 prawdziwy
else:
    # kod wykonywany, gdy żaden z warunków nie jest prawdziwy
```

### Warunki i operatory porównania (przypomnienie)
```python
x = 10
y = 20

# Operatory porównania
x == y    # Równość (False)
x != y    # Nierówność (True)
x < y     # Mniejsze niż (True)
x > y     # Większe niż (False)
x <= y    # Mniejsze lub równe (True)
x >= y    # Większe lub równe (False)
```

### Operatory logiczne
```python
a = True
b = False

# Operatory logiczne
a and b   # Koniunkcja - True, gdy oba wyrażenia są prawdziwe (False)
a or b    # Alternatywa - True, gdy co najmniej jedno wyrażenie jest prawdziwe (True)
not a     # Negacja - odwraca wartość logiczną (False)
```

### Przykłady praktyczne
```python
# Przykład 1: Sprawdzanie BMI
waga = 70  # kg
wzrost = 1.75  # m
bmi = waga / (wzrost ** 2)

if bmi < 18.5:
    print("Niedowaga")
elif bmi < 25:
    print("Waga prawidłowa")
elif bmi < 30:
    print("Nadwaga")
else:
    print("Otyłość")

# Przykład 2: Sprawdzanie oceny
ocena = 75

if ocena >= 90:
    print("Bardzo dobry")
elif ocena >= 75:
    print("Dobry")
elif ocena >= 60:
    print("Dostateczny")
elif ocena >= 50:
    print("Dopuszczający")
else:
    print("Niedostateczny")

# Przykład 3: Złożone warunki
temperatura = 25
pada_deszcz = False

if temperatura > 20 and not pada_deszcz:
    print("Idealna pogoda na spacer!")
elif temperatura > 20 and pada_deszcz:
    print("Ciepło, ale weź parasol.")
elif temperatura <= 20 and not pada_deszcz:
    print("Chłodno, ale sucho.")
else:
    print("Zostań w domu - zimno i pada.")
```

### Wyrażenia warunkowe (conditional expressions)
Python oferuje skróconą formę instrukcji warunkowej w postaci wyrażenia, znaną również jako operator trójargumentowy.

```python
# Zwykła instrukcja if-else
if warunek:
    x = wartosc1
else:
    x = wartosc2
    
# Równoważne wyrażenie warunkowe
x = wartosc1 if warunek else wartosc2

# Przykład
wiek = 20
status = "dorosły" if wiek >= 18 else "niepełnoletni"
```

## 3. Pętle for i while

### Wprowadzenie do pętli
Pętle pozwalają na wielokrotne wykonywanie bloków kodu. W Pythonie mamy dwa główne rodzaje pętli: `for` i `while`.

### Pętla for
Pętla `for` jest używana do iteracji po sekwencji (liście, krotce, słowniku, stringu itd.) lub innych obiektach iterowalnych.

```python
# Podstawowa struktura pętli for
for element in sekwencja:
    # kod wykonywany dla każdego elementu sekwencji
    
# Przykład 1: Iteracja po liście
owoce = ["jabłko", "banan", "gruszka"]
for owoc in owoce:
    print(f"Lubię {owoc}")

# Przykład 2: Iteracja po zakresie liczb
for i in range(5):
    print(i)  # Wyświetli liczby 0, 1, 2, 3, 4

# Przykład 3: Iteracja po łańcuchu znaków
for znak in "Python":
    print(znak)  # Wyświetli każdy znak w osobnej linii

# Przykład 4: Iteracja z indeksem
for i, owoc in enumerate(owoce):
    print(f"Indeks {i}: {owoc}")
```

### Pętla while
Pętla `while` wykonuje blok kodu tak długo, jak długo warunek jest prawdziwy.

```python
# Podstawowa struktura pętli while
while warunek:
    # kod wykonywany dopóki warunek jest prawdziwy
    
# Przykład 1: Prosta pętla while
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1  # Inkrementacja licznika

# Przykład 2: Pętla nieskończona z break
while True:
    odpowiedz = input("Napisz 'koniec' aby zakończyć: ")
    if odpowiedz.lower() == "koniec":
        break  # Przerywa pętlę
    print(f"Wpisałeś: {odpowiedz}")
```

### Instrukcje sterujące pętlą
Python oferuje kilka instrukcji do sterowania przebiegiem pętli.

```python
# break - przerywa pętlę całkowicie
for i in range(10):
    if i == 5:
        break  # Przerywa pętlę po osiągnięciu 5
    print(i)  # Wyświetli liczby 0, 1, 2, 3, 4

# continue - przeskakuje do następnej iteracji
for i in range(10):
    if i % 2 == 0:
        continue  # Pomija parzyste liczby
    print(i)  # Wyświetli liczby 1, 3, 5, 7, 9

# else w pętlach - wykonuje kod, gdy pętla zakończy się normalnie (bez break)
for i in range(5):
    print(i)
else:
    print("Pętla zakończona normalnie")

# Przykład z break i else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Ten kod nie zostanie wykonany, bo pętla została przerwana")
```

### Zagnieżdżone pętle
Pętle mogą być zagnieżdżane jedna w drugiej, co jest przydatne przy pracy z wielowymiarowymi strukturami danych.

```python
# Przykład: Tablica mnożenia
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Nowa linia po każdym wierszu

# Przykład: Iteracja po macierzy (liście list)
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for wiersz in macierz:
    for element in wiersz:
        print(element, end=" ")
    print()
```

### List comprehension (wyrażenia listowe)
List comprehension to zwięzły sposób tworzenia list na podstawie istniejących sekwencji.

```python
# Tradycyjny sposób tworzenia listy
kwadraty = []
for i in range(1, 6):
    kwadraty.append(i**2)
print(kwadraty)  # [1, 4, 9, 16, 25]

# Równoważne list comprehension
kwadraty = [i**2 for i in range(1, 6)]
print(kwadraty)  # [1, 4, 9, 16, 25]

# List comprehension z warunkiem
parzyste_kwadraty = [i**2 for i in range(1, 11) if i % 2 == 0]
print(parzyste_kwadraty)  # [4, 16, 36, 64, 100]

# Zagnieżdżone list comprehension
macierz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(macierz)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## Zadania do wykonania

### Zadanie 1: Operacje na listach
Napisz program, który:
1. Utworzy listę zawierającą 5 różnych owoców
2. Doda nowy owoc na końcu listy
3. Wstawi inny owoc na pozycji 2
4. Usunie ostatni element listy
5. Wyświetli zawartość listy po każdej operacji

Pomocne materiały:
- Tutorial Pythona - Listy: [docs.python.org/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)<br>

### Zadanie 2: Warunki
Napisz program, który:
1. Poprosi użytkownika o podanie wieku
2. Na podstawie wieku określi kategorię wiekową:
   - 0-12 lat: "Dziecko"
   - 13-17 lat: "Nastolatek"
   - 18-64 lata: "Dorosły"
   - 65+ lat: "Senior"
3. Wyświetli odpowiednią kategorię

Pomocne materiały:
- Tutorial Pythona - Instrukcje warunkowe: [docs.python.org/tutorial/controlflow.html#if-statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)<br>

### Zadanie 3: Pętla for
Napisz program, który:
1. Utworzy listę liczb od 1 do 10
2. Za pomocą pętli for znajdzie sumę wszystkich liczb na liście
3. Za pomocą pętli for znajdzie sumę tylko liczb parzystych
4. Wyświetli obie sumy

Pomocne materiały:
- Tutorial Pythona - Pętla for: [docs.python.org/tutorial/controlflow.html#for-statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)<br>

### Zadanie 4: Pętla while
Napisz program, który:
1. Generuje losową liczbę całkowitą od 1 do 100
2. Prosi użytkownika o zgadnięcie tej liczby
3. Informuje, czy podana liczba jest za duża, za mała lub prawidłowa
4. Kontynuuje, aż użytkownik zgadnie liczbę
5. Na końcu wyświetla liczbę prób, które były potrzebne do zgadnięcia

Pomocne materiały:
- Tutorial Pythona - Pętla while: [docs.python.org/tutorial/introduction.html#first-steps-towards-programming](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)<br>
- Random - Generowanie liczb losowych: [docs.python.org/library/random.html](https://docs.python.org/3/library/random.html)<br>

## Wskazówki
- Używaj wcięć do oznaczania bloków kodu (4 spacje)
- Sprawdzaj poprawność warunków przed uruchomieniem pętli
- Uważaj na pętle nieskończone - zawsze upewnij się, że warunek pętli while w końcu stanie się fałszywy
- Używaj instrukcji sterujących (break, continue) tylko wtedy, gdy są naprawdę potrzebne
- List comprehension może znacznie uprościć kod, ale nie nadużywaj go kosztem czytelności

Dodatkowe materiały do nauki:
- Python Documentation - Data Structures: [docs.python.org/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)<br>
- Real Python - Python for Loop Tutorial: [realpython.com/python-for-loop/](https://realpython.com/python-for-loop/)<br>
- DataCamp - Python Lists: [datacamp.com/community/tutorials/python-lists-tutorial](https://www.datacamp.com/community/tutorials/python-lists-tutorial)<br>

