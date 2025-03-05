# Zajęcia 1a: Porównanie składni różnych języków programowania

## Czym jest składnia w programowaniu?

Składnia w programowaniu jest jak gramatyka w języku naturalnym. Tak jak w języku polskim musimy przestrzegać zasad gramatycznych, aby nasze zdania miały sens i były zrozumiałe, tak w programowaniu musimy przestrzegać zasad składni, aby komputer mógł poprawnie zinterpretować i wykonać nasze instrukcje.

### Przykład z języka naturalnego:
- Poprawne zdanie: "Ala ma kota."
- Niepoprawne składniowo: "Kota Ala ma."
- Niepoprawne składniowo: "ma Ala kota"

### Analogia do programowania:
- Każdy język programowania ma swoją "gramatykę"
- Instrukcje muszą być zapisane w określony sposób
- Nawet drobna pomyłka składniowa może spowodować, że program nie zadziała lub będzie działał nieprawidłowo

## Porównanie tego samego zadania w różnych językach

### Przykład 1: Wyświetlenie tekstu "Hello, World!"

```python
# Python - prosto i czytelnie
print("Hello, World!")
```

```java
// Java - wymaga więcej kodu "ceremonialnego"
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

```c++
// C++ - również wymaga więcej kodu
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Przykład 2: Obliczenie średniej z listy liczb

```python
# Python - zwięźle i intuicyjnie
liczby = [1, 2, 3, 4, 5]
srednia = sum(liczby) / len(liczby)
print(f"Średnia: {srednia}")
```

```java
// Java - więcej kodu, mniej intuicyjne
import java.util.Arrays;

public class Average {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        double average = Arrays.stream(numbers)
                              .average()
                              .getAsDouble();
        System.out.printf("Średnia: %.2f%n", average);
    }
}
```

```c++
// C++ - wymaga więcej uwagi i kodu
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    double average = std::accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
    std::cout << "Średnia: " << average << std::endl;
    return 0;
}
```

### Przykład 3: Odczytanie danych od użytkownika i wykonanie prostych obliczeń

```python
# Python - naturalne i zrozumiałe
wiek = int(input("Podaj swój wiek: "))
lata_do_emerytury = 65 - wiek
print(f"Do emerytury zostało Ci {lata_do_emerytury} lat")
```

```java
// Java - więcej kodu i złożoności
import java.util.Scanner;

public class RetirementCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Podaj swój wiek: ");
        int age = scanner.nextInt();
        int yearsToRetirement = 65 - age;
        System.out.println("Do emerytury zostało Ci " + yearsToRetirement + " lat");
        scanner.close();
    }
}
```

```c++
// C++ - mniej intuicyjne i bardziej złożone
#include <iostream>

int main() {
    int age;
    std::cout << "Podaj swój wiek: ";
    std::cin >> age;
    int yearsToRetirement = 65 - age;
    std::cout << "Do emerytury zostało Ci " << yearsToRetirement << " lat" << std::endl;
    return 0;
}
```

## Dlaczego Python jest przyjazny dla początkujących?

1. **Czytelna składnia:**
   - Nie wymaga średników na końcu linii
   - Używa wcięć zamiast nawiasów klamrowych do oznaczania bloków kodu
   - Minimalna ilość "kodu szablonowego" (boilerplate code)

2. **Prostota:**
   - Mniej linii kodu do osiągnięcia tego samego celu
   - Wbudowane funkcje wysokiego poziomu
   - Automatyczne zarządzanie pamięcią

3. **Intuicyjność:**
   - Składnia przypomina pseudokod
   - Nazwy funkcji są opisowe
   - Spójne konwencje nazewnictwa (PEP 8)

4. **Bogata biblioteka standardowa:**
   - Wiele przydatnych funkcji dostępnych od razu
   - Nie trzeba "wymyślać koła na nowo"
   - Łatwe importowanie dodatkowych funkcjonalności

5. **Wszechstronność:**
   - Można tworzyć aplikacje webowe, desktopowe, skrypty, analizy danych
   - Doskonały do prototypowania
   - Świetny zarówno dla małych skryptów, jak i dużych projektów

## Podsumowanie

Python został zaprojektowany z myślą o czytelności i prostocie użycia. Jego twórca, Guido van Rossum, położył nacisk na elegancję kodu i łatwość nauki. Podczas gdy inne języki często wymagają więcej kodu i znajomości szczegółów technicznych, Python pozwala skupić się na rozwiązywaniu problemów, a nie na szczegółach składni. 

Ta filozofia projektowa jest wyrażona w "Zen of Python" (dostępnym po wpisaniu `import this` w interpreterze Pythona), który zawiera takie zasady jak "Czytelność się liczy" oraz "Proste jest lepsze niż złożone". Dzięki temu Python jest idealnym językiem zarówno dla początkujących programistów, jak i dla doświadczonych specjalistów, którzy cenią sobie wydajność i czytelność kodu.