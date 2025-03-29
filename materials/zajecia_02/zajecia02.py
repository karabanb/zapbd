# %%[markdown]  

# # Zajęcia 2: Podstawowe struktury danych i kontrola przepływu w Pythonie

# ## Typy danych w Pythonie

# ### Typy atomowe (proste)
# - `int` - liczby całkowite, np. 42, -7, 0
# - `float` - liczby zmiennoprzecinkowe, np. 3.14, -0.001, 2.0
# - `str` - łańcuchy znaków (tekst), np. "Python", 'Hello'
# - `bool` - wartości logiczne: True lub False

# ### Typy złożone (kolekcje)
# - `list` - listy: uporządkowane, modyfikowalne kolekcje, np. [1, 2, 3]
# - `tuple` - krotki: uporządkowane, niemodyfikowalne kolekcje, np. (1, 2, 3)
# - `dict` - słowniki: pary klucz-wartość, np. {"nazwa": "Python", "wersja": 3.10}
# - `set` - zbiory: nieuporządkowane kolekcje unikalnych elementów, np. {1, 2, 3}


# ### Listy (list)
# Listy to uporządkowane, zmienialne kolekcje elementów, które mogą być różnych typów.

# %%
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
co_drugi = owoce[1::2]       # ["truskawka", "pomarańcza"] 



# %%
# Import a library
import numpy as np# %%

# %%
