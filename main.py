mojaLista = []

def zwrocWyrazenie(x):
    return x**2 + x  % 7
    
def sprawdzCzyNieparzysta(x):
    return x % 2 != 0

for i in range(10):
    mojaLista.append(i)
    
print(mojaLista)

kwadraty = tuple(zwrocWyrazenie(i) for i in mojaLista if sprawdzCzyNieparzysta(i))
print(kwadraty)


class Zwierze():
    def __init__(self, nazwa, wiek):
        self.nazwa = nazwa
        self.wiek = wiek
        
    def __str__(self):
        return f"{self.nazwa} ma {self.wiek} lat"
    
    def __del__(self):
        print(f"Usuwam obiekt {self.nazwa}")
        
print("Tu zaczyna sie nasz program")
pies = Zwierze("Burek", 5)
print(pies)
print("Tu konczy sie nasz program")

stolice = ["Warszawa", "Berlin", "Paryż", "Madryt", "Londyn", "Rzym", "Lizbona", "Oslo", "Sztokholm", "Kopenhaga"]
panstwa = ["Polska", "Niemcy", "Francja", "Hiszpania", "Wielka Brytania"]

informacje = dict(zip(stolice, panstwa))
print(informacje)

#Utworz liste zawierajaca tylko slowa bedace palindromami
slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]
print(f"Slowa do sprawdzenia: {slowa} Czy sa palindromami?")
p = [slowo for slowo in slowa if slowo == slowo[::-1]]
print(f"Slowa bedace palindromami: {p}")
# Utworz liste zawierajaca tylko krotki, ktore moglyby zawierac dlugosci bokow trojkata
trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5), (5, 5, 5), (6, 7, 8)]
print(f"Trojkaty do sprawdzenia: {trojkaty} ktore moglyby zawierac dlugosci bokow trojkata?")

def wzorNaTrojkat(a, b, c):
    return a + b > c and a + c > b and b + c > a

def przelicznikStopnie(x):
    return (x - 32) * 5/9   
# [expression for item in iterable if condition]
poprawneTrojkaty = [trojkat for trojkat in trojkaty if wzorNaTrojkat(*trojkat)]
# trojkat[0] , trojkat[1], trojkat[2] == *trojkat
print(f"Trojkaty, ktore moga byc trojkatami: {poprawneTrojkaty}")
#Na podstawie listy temperatur w stopniach Fahrenhaita wygeneruj liste z stopniami Celcjusza
stopnie_fahrenheit = [32, 68, 104, 140]
stopnie_celciusza =[przelicznikStopnie(stopnie) for stopnie in stopnie_fahrenheit]
print(f"Stopnie w Fahrenhaitach: {stopnie_fahrenheit}")

# Z wyrazu usanac wszystko co nie jest literka
wyraz = "nn1122@#a@z3D4a5młąę"
literki = [char for char in wyraz if char.isalpha()]
print(f"Wyraz: {wyraz} po usunieciu znakow nie bedacych literkami: {literki}")
# nasze wyjatki:
try:
    print(1/0)
except ZeroDivisionError as e:
    print(f"Blad: {e}")
finally:
    print("Koniec programu")

mojaLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    print(mojaLista[10])
except IndexError as e:
    print(f"Blad: {e}") 
finally:
    print("Koniec programu")

def dodawanie(a,b):
    try:   
        a+b
    except TypeError as e:
        print(f"Blad: {e}")
    finally:
        print(f"Wynik dodawania: {a} + {b}")
        
print(dodawanie(1, 2))
dodawanie(1, "2")

def parzyste(a,b):
    try:
        if a % 2 == 1 and b % 2 == 1:
            raise ValueError("Oba argumenty sa nieparzyste")
        else:
            return a + b
    except ValueError as e:
        print(f"Blad: {e}")
    finally:
        print(f"Wynik dodawania: {a} + {b}")
        return "Koniec programu"
        
print(parzyste(1, 1))
print(parzyste(2, 2))