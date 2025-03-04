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

## 2. Uruchamianie Pythona na zajęciach

Na zajęciach będziemy korzystać z trzech głównych narzędzi:

### Git Bash
Git Bash to emulator terminala dla systemu Windows, który zapewnia:
- Dostęp do poleceń systemu Unix
- Możliwość uruchamiania skryptów Pythona z linii komend
- Narzędzia do kontroli wersji Git
- Środowisko przypominające systemy Unix/Linux, często używane w Data Science

### Notepad++
Notepad++ to lekki i szybki edytor tekstu, który oferuje:
- Kolorowanie składni dla wielu języków programowania, w tym Pythona
- Możliwość pracy z wieloma plikami jednocześnie
- Zaawansowane funkcje edycji tekstu
- Niskie wymagania systemowe
- Idealne narzędzie do nauki podstaw programowania

### Jupyter Notebook
Jupyter Notebook to interaktywne środowisko programistyczne, które:
- Pozwala na tworzenie i udostępnianie dokumentów zawierających "żywy" kod
- Umożliwia mieszanie kodu, tekstu, wzorów matematycznych i wizualizacji
- Jest standardem w Data Science i analizie danych
- Pozwala na wykonywanie kodu "po kawałku" i natychmiastowe widzenie wyników
- Świetnie nadaje się do eksperymentowania i nauki

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

## Zadania do wykonania

### Zadanie 1: Pierwszy program (skrypt)
Napisz program, który wyświetli Twoje imię i wiek. Użyj zmiennych do przechowywania tych informacji.

### Zadanie 2: Kalkulator (skrypt)
Napisz program, który:
1. Zdefiniuje dwie zmienne z liczbami
2. Wykona podstawowe operacje matematyczne (dodawanie, odejmowanie, mnożenie, dzielenie)
3. Wyświetli wyniki w czytelny sposób

### Zadanie 3: Konwersja typów (notebook)
Napisz program, który:
1. Zdefiniuje zmienną z liczbą całkowitą
2. Przekonwertuje ją na tekst
3. Wyświetli obie wersje (liczbę i tekst)

### Zadanie 4: Obliczenia (notebook)
Napisz program, który:
1. Obliczy pole prostokąta o bokach 5 i 3
2. Obliczy obwód tego prostokąta
3. Wyświetli oba wyniki z odpowiednimi opisami

## Wskazówki
- Używaj opisowych nazw zmiennych
- Dodawaj komentarze do kodu używając #
- Testuj program po każdej zmianie
- Zwracaj uwagę na formatowanie kodu 