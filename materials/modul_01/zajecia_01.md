# Zajęcia 1: Wprowadzenie do Pythona

## 1. Podstawowe koncepcje programowania

### Co to jest programowanie?
Programowanie to proces tworzenia instrukcji dla komputera, które mówią mu co ma zrobić. Komputer wykonuje te instrukcje krok po kroku, dokładnie tak jak zostały zapisane.

### Dlaczego Python?
- Prosty i czytelny składnia
- Duża społeczność i wiele bibliotek
- Wszechstronność zastosowań
- Idealny do nauki programowania
- Powszechnie używany w Big Data i Data Science

Oficjalna strona Pythona: [python.org](https://www.python.org/)<br>
Dokumentacja Pythona: [docs.python.org](https://docs.python.org/3/)<br>
Tutorial Pythona: [docs.python.org/tutorial](https://docs.python.org/3/tutorial/)<br>

## 2. Uruchamianie Pythona na zajęciach

Na zajęciach będziemy korzystać z trzech głównych narzędzi:

### Git Bash
Git Bash to emulator terminala dla systemu Windows, który zapewnia:
- Dostęp do poleceń systemu Unix
- Możliwość uruchamiania skryptów Pythona z linii komend
- Narzędzia do kontroli wersji Git
- Środowisko przypominające systemy Unix/Linux, często używane w Data Science

Strona Git: [git-scm.com](https://git-scm.com/)<br>
Dokumentacja Git: [git-scm.com/doc](https://git-scm.com/doc)<br>
Pobieranie Git Bash: [git-scm.com/downloads](https://git-scm.com/downloads)<br>

### Notepad++
Notepad++ to lekki i szybki edytor tekstu, który oferuje:
- Kolorowanie składni dla wielu języków programowania, w tym Pythona
- Możliwość pracy z wieloma plikami jednocześnie
- Zaawansowane funkcje edycji tekstu
- Niskie wymagania systemowe
- Idealne narzędzie do nauki podstaw programowania

Strona Notepad++: [notepad-plus-plus.org](https://notepad-plus-plus.org/)<br>
Dokumentacja: [npp-user-manual.org](https://npp-user-manual.org/)<br>
Pobieranie: [notepad-plus-plus.org/downloads](https://notepad-plus-plus.org/downloads/)<br>

### Jupyter Notebook
Jupyter Notebook to interaktywne środowisko programistyczne, które:
- Pozwala na tworzenie i udostępnianie dokumentów zawierających "żywy" kod
- Umożliwia mieszanie kodu, tekstu, wzorów matematycznych i wizualizacji
- Jest standardem w Data Science i analizie danych
- Pozwala na wykonywanie kodu "po kawałku" i natychmiastowe widzenie wyników
- Świetnie nadaje się do eksperymentowania i nauki

Strona Jupyter: [jupyter.org](https://jupyter.org/)<br>
Dokumentacja: [docs.jupyter.org](https://docs.jupyter.org/)<br>
Try Jupyter: [try.jupyter.org](https://try.jupyter.org/)<br>

### Jak uruchomić terminal i sprawdzić instalajcę Pythona?
1. Kliknij prawym przyciskiem myszy w dowolnym miejscu na pulpicie lub w folderze
2. Z menu kontekstowego wybierz opcję "Git Bash Here"
3. W otwartym terminalu sprawdź wersję Pythona wpisując:
   ```bash
   python --version
   ```
### Jak uruchomić Pythona i go zamknąć?
1. Otwórz terminal (np. Git Bash)
2. Wpisz polecenie, aby uruchomić Pythona:
   ```bash
   python
   ```
3. Powinieneś zobaczyć interaktywną konsolę Pythona, gdzie możesz wpisywać polecenia Pythonowe.
4. Aby zamknąć Pythona, wpisz:
   ```python
   exit()
   ```
### Jak uruchomić Pythona w Jupter Notebook?


1. Otwórz Jupyter Notebook przez Git Bash komendą:
   ```bash
   jupyter notebook
   ```
2. W przeglądarce utwórz nowy notebook lub otwórz istniejący
3. W pierwszej komórce wpisz kod, aby sprawdzić wersję Pythona:
   ```python
   !python --version
   ```
4. Kod wykonuje się w pojedynczych komórkach za pomocą Shift + Enter

## 3. Pierwszy program w Pythonie

### Program "Hello World"
```python
print("Hello World!")
```

### Jak uruchomić program?
1. Zapisz kod w pliku z rozszerzeniem `.py` (np. `hello.py`)
2. Otwórz terminal w folderze z plikiem
3. Uruchom program komendą:
   ```bash
   python hello.py
   ```

## 4. Zmienne i typy danych

### Zmienne
Zmienne to pojemniki na dane w pamięci komputera.

```python
# Przykłady zmiennych
imie = "Jan"
wiek = 25
wzrost = 1.75
jest_studentem = True
```

### Podstawowe typy danych
- `str` - tekst (string)
- `int` - liczby całkowite
- `float` - liczby zmiennoprzecinkowe
- `bool` - wartości logiczne (True/False)

### Konwersja typów
Python umożliwia konwersję (rzutowanie) wartości z jednego typu na inny. Służą do tego wbudowane funkcje:

```python
# Konwersja na string (str)
liczba = 42
tekst = str(liczba)  # "42"

# Konwersja na liczbę całkowitą (int)
tekst_liczby = "123"
liczba_calkowita = int(tekst_liczby)  # 123

# Konwersja na liczbę zmiennoprzecinkową (float)
tekst_float = "3.14"
liczba_float = float(tekst_float)  # 3.14

# Konwersja na wartość logiczną (bool)
zero = bool(0)  # False
jeden = bool(1)  # True
pusty_tekst = bool("")  # False
niepusty_tekst = bool("Python")  # True
```

#### Uwagi dotyczące konwersji
- Nie każdy string można przekonwertować na liczbę (np. `int("abc")` wywoła błąd)
- Przy konwersji `float` na `int` część ułamkowa jest odcinana (nie zaokrąglana)
- Wartości `0`, `""` (pusty string), `None`, `False` oraz puste kolekcje konwertują się na `False`
- Wszystkie inne wartości konwertują się na `True`

### Przykład praktyczny: Praca ze zmiennymi i typami danych
```python
# Obliczanie wieku w przyszłości
aktualny_wiek = 25
lata_do_dodania = 10
przyszly_wiek = aktualny_wiek + lata_do_dodania
print(f"Za {lata_do_dodania} lat będziesz mieć {przyszly_wiek} lat.")

# Konwersja typów w praktyce
cena_tekst = input("Podaj cenę produktu: ")  # np. "23.50"
cena = float(cena_tekst)
ilosc = int(input("Podaj ilość: "))  # np. "3"
wartosc = cena * ilosc
print(f"Wartość zamówienia: {wartosc} zł")
```

### Konwencje nazewnictwa i komentarze
#### Nazewnictwo zmiennych
- Używaj opisowych nazw zmiennych (np. `wiek_studenta` zamiast `w`)
- Stosuj małe litery i podkreślniki do oddzielania słów (tzw. snake_case)
- Unikaj używania słów kluczowych Pythona jako nazw zmiennych
- Nazwy powinny być związane z danymi, które przechowują

```python
# Dobrze
liczba_studentow = 25
imie_uzytkownika = "Anna"
czy_aktywny = True

# Źle
x = 25
a = "Anna"
zmienna1 = True
```

#### Komentarze
Komentarze w Pythonie zaczynają się od znaku `#` i trwają do końca linii:

```python
# To jest komentarz jednoliniowy

wiek = 25  # Komentarz może być też na końcu linii kodu

# Komentarze wieloliniowe tworzymy używając kilku linii z #
# Pierwsza linia komentarza
# Druga linia komentarza
# Trzecia linia komentarza
```

Dobrze napisane komentarze:
- Wyjaśniają "dlaczego", a nie "co" (kod sam pokazuje "co")
- Są aktualne i zgodne z kodem
- Ułatwiają zrozumienie skomplikowanych fragmentów kodu
- Nie są nadmiarowe dla oczywistych operacji

## 5. Operatory i wyrażenia

### Operatory arytmetyczne
```python
a = 10
b = 3

dodawanie = a + b      # 13
odejmowanie = a - b    # 7
mnozenie = a * b       # 30
dzielenie = a / b      # 3.333...
dzielenie_calkowite = a // b  # 3
reszta = a % b         # 1
potega = a ** b        # 1000
```

### Operatory porównania
```python
x = 5
y = 10

rowne = x == y        # False
rozne = x != y        # True
mniejsze = x < y      # True
wieksze = x > y       # False
mniejsze_rowne = x <= y  # True
wieksze_rowne = x >= y   # False
```

### Przykład praktyczny: Wykorzystanie operatorów
```python
# Obliczanie pola i obwodu prostokąta
dlugosc = 5
szerokosc = 3

pole = dlugosc * szerokosc
obwod = 2 * (dlugosc + szerokosc)

print(f"Prostokąt o długości {dlugosc} i szerokości {szerokosc}:")
print(f"- pole: {pole}")
print(f"- obwód: {obwod}")

# Sprawdzanie warunków
wiek = 18
czy_pelnoletni = wiek >= 18
print(f"Czy osoba w wieku {wiek} lat jest pełnoletnia? {czy_pelnoletni}")
```

### Podsumowanie sekcji 5
- Operatory arytmetyczne pozwalają wykonywać podstawowe operacje matematyczne
- Operatory porównania zwracają wartości logiczne (True/False)
- Operatory można łączyć w bardziej złożone wyrażenia
- Wyniki operacji można przypisywać do zmiennych
- Operatory są podstawowym narzędziem do manipulowania danymi w programach

## Zadania do wykonania

### Zadanie 1: Pierwszy program (skrypt)
Napisz program, który wyświetli Twoje imię i wiek. Użyj zmiennych do przechowywania tych informacji.

Pomocne materiały:
- Tutorial Pythona - Print i zmienne: [docs.python.org/tutorial/introduction.html#using-python-as-a-calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)<br>
- DataCamp - Introduction to Python: [datacamp.com/courses/intro-to-python-for-data-science](https://www.datacamp.com/courses/intro-to-python-for-data-science)<br>

### Zadanie 2: Kalkulator (skrypt)
Napisz program, który:
1. Zdefiniuje dwie zmienne z liczbami
2. Wykona podstawowe operacje matematyczne (dodawanie, odejmowanie, mnożenie, dzielenie)
3. Wyświetli wyniki w czytelny sposób

Pomocne materiały:
- Tutorial Pythona - Operacje matematyczne: [docs.python.org/tutorial/introduction.html#numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)<br>

### Zadanie 3: Konwersja typów (notebook)
Napisz program, który:
1. Zdefiniuje zmienną z liczbą całkowitą
2. Przekonwertuje ją na tekst
3. Wyświetli obie wersje (liczbę i tekst)

Pomocne materiały:
- Tutorial Pythona - Konwersja typów: [docs.python.org/tutorial/introduction.html#strings](https://docs.python.org/3/tutorial/introduction.html#strings)<br>

### Zadanie 4: Obliczenia (notebook)
Napisz program, który:
1. Obliczy pole prostokąta o bokach 5 i 3
2. Obliczy obwód tego prostokąta
3. Wyświetli oba wyniki z odpowiednimi opisami

Pomocne materiały:
- Tutorial Pythona - Wyrażenia matematyczne: [docs.python.org/tutorial/introduction.html#using-python-as-a-calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)<br>

## Wskazówki
- Używaj opisowych nazw zmiennych
- Dodawaj komentarze do kodu używając #
- Testuj program po każdej zmianie
- Zwracaj uwagę na formatowanie kodu

Dodatkowe materiały do nauki:
- Python Style Guide (PEP 8): [python.org/dev/peps/pep-0008](https://www.python.org/dev/peps/pep-0008/)<br>
- Real Python Tutorials: [realpython.com](https://realpython.com/)<br>
- Python Documentation: [docs.python.org](https://docs.python.org/3/)<br>
- DataCamp - Python Basics: [datacamp.com/courses/python-basics](https://www.datacamp.com/courses/python-basics)<br>