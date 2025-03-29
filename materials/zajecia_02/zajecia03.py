# Zajęcia 3: Zaawansowane struktury danych i operacje w Pythonie

# %% [markdown]

## Funkcje

### Wprowadzenie do funkcji w Pythonie

Funkcje to jeden z fundamentalnych elementów programowania w Pythonie. Są to bloki kodu, które wykonują określone zadanie i można je wielokrotnie wywołać w różnych miejscach programu.

#### Czym są funkcje?

Funkcje można porównać do małych "maszyn", które:
- Przyjmują dane wejściowe (argumenty)
- Wykonują pewne operacje na tych danych
- Zwracają wynik (wartość)

#### Dlaczego używamy funkcji?

1. **Modularność kodu** - Funkcje pozwalają dzielić program na mniejsze, łatwiejsze do zrozumienia części
2. **Wielokrotne użycie kodu** - Zamiast kopiować i wklejać ten sam kod w wielu miejscach, możemy użyć funkcji
3. **Czytelność** - Dobrze nazwane funkcje sprawiają, że kod jest bardziej zrozumiały
4. **Łatwiejsze testowanie** - Łatwiej jest testować małe, izolowane funkcje niż duże bloki kodu
5. **Abstrakcja** - Użytkownik funkcji nie musi znać szczegółów jej implementacji, wystarczy że wie jak jej używać

#### Podstawowa składnia funkcji w Pythonie

```python
def nazwa_funkcji(parametr1, parametr2, ...):
    """Dokumentacja funkcji (docstring)."""
    # Ciało funkcji - kod wykonywany podczas wywołania
    # ...
    return wynik  # Opcjonalnie - funkcja może zwrócić wartość
```

# %%
# definicja funkcji
def oblicz_srednia(liczby):
    """Oblicza średnią arytmetyczną z listy liczb."""
    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

# przykład użycia funkcji
liczby_testowe = [10, 20, 30, 40, 50]
wynik = oblicz_srednia(liczby_testowe)
print(f"Średnia z listy {liczby_testowe} wynosi {wynik}")

# %%
# Przykłady prostych funkcji

# Funkcja bez parametrów
def powitanie():
    """Wyświetla powitanie."""
    print("Witaj w świecie funkcji!")

# Funkcja z parametrami
def powitaj_osobe(imie):
    """Wyświetla spersonalizowane powitanie."""
    print(f"Witaj, {imie}!")

# Funkcja z wartością domyślną parametru
def powitaj_z_tytułem(imie, tytul="Pan/Pani"):
    """Wyświetla powitanie z tytułem."""
    print(f"Witaj, {tytul} {imie}!")

# Funkcja zwracająca wartość
def kwadrat(liczba):
    """Zwraca kwadrat liczby."""
    return liczba ** 2

# Wywołania funkcji
powitanie()
powitaj_osobe("Anna")
powitaj_z_tytułem("Jan", "Dr")
powitaj_z_tytułem("Maria")
wynik_kwadratu = kwadrat(5)
print(f"5 do kwadratu to {wynik_kwadratu}")

