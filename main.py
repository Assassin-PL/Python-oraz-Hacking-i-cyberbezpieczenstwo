import json
import random

nasza_lista = [1, 2, 3, 4, 5]

# chce dodac true na koniec listy

nasza_lista.append(True)

# print(nasza_lista)

# print(nasza_lista[-4])

for i in range(len(nasza_lista)):
    if i % 2 == 0:
        print(nasza_lista[i])
# poszerzanie listy o dodatkowe elementy        
dodatkowa_lista = [0, False , " pise ", "kot", "sztefan"]
nasza_lista.extend(dodatkowa_lista)

print(nasza_lista)

print(nasza_lista[9])

print(nasza_lista[8]+ " " + nasza_lista[10]) # konkatenacja stringow

nasza_lista.insert(2, "nowy element") # dodanie elementu pod danym indeksem
print("nasza lista po dodaniu pod moiejsce pod danym indeksem :", nasza_lista)

# usuwanie elementu z listy
nasza_lista.remove("nowy element")
print("nasza lista po usunieciu elementu :", nasza_lista)

#wezmy naszego popa
a = nasza_lista.pop()
print ( "usunelismy element z listy: ", a) 
print("nasza lista po usunieciu elementu z konca: ", nasza_lista)
# znajdywanie indkesu w liscie
id  = nasza_lista.index(False)
print("Indeks elementu False w naszej liscie to: ", id)
id  = nasza_lista.index(False, 7)
print("Indeks elementu False w naszej liscie to, ale szukamu od indeksu 7: ", id)
id  = nasza_lista.index(False,6, 7)
print("Indeks elementu False w naszej liscie to, ale szukamu od indeksu 6 a na 7 koncze: ", id)
#liczba wystapien elementu w liscie
liczba = nasza_lista.count(False)
print("Liczba wystapien elementu False w naszej liscie to: ", liczba)
# sortowanie listy
nowa_lista = []
for i in range(10):
    nowa_lista.append(random.randint(0, 100))
print("Nasza lista przed sortowaniem: ", nowa_lista)
nowa_lista.sort()
print("Posortowana lista: ", nowa_lista)

for element in nasza_lista:
    if not isinstance(element, int):
        nasza_lista.remove(element)
for element in nasza_lista:
    if not isinstance(element, int):
        nasza_lista.remove(element)
print("Nasza lista po usunieciu elementow nie bedacych liczbami: ", nasza_lista)
nasza_lista.sort()
print("Nasza lista po posortowaniu: ", nasza_lista)
print("Odwracamy nasz liste:", nasza_lista[::-1])
print("Odwracamy nasz liste w alternatywny sposób:", nasza_lista.reverse())
kopialisty = nasza_lista.copy()
print("Kopia naszej listy: ", kopialisty)
nasza_lista.clear()
print("Nasza lista po wyczyszczeniu: ", nasza_lista)
print("Kopia naszej listy po wyczyszczeniu oryginalnej: ", kopialisty)
#czysczenie
""
def wygeneruj_liste(dlugosc_listy = 0):
    lista = []
    for i in range(dlugosc_listy):
        lista.append(random.randint(0, 100))
    return lista
# Zadania
# 1 Stwórz 2 listy składające się z 3 liczb każda
lista1 = wygeneruj_liste(3)
list2 = wygeneruj_liste(3)
print("Lista 1: ", lista1)
print("Lista 2: ", list2)
# 2 Połącz stworzone wcześniej listy
lista1.extend(list2)
print("Połączone listy: ", lista1)
# 3 Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?'
lista1.pop(5)
lista1.pop(2)
print("Lista po usunięciu elementów: ", lista1)
# 4 Usuń największą i najmniejszą liczbę z listy
lista1.remove(max(lista1))
lista1.remove(min(lista1))
print("Lista po usunięciu największej i najmniejszej liczby: ", lista1)
# 5 Dodaj liczbę do listy
lista1.append(100)
print("Lista po dodaniu liczby: ", lista1)
# 6 Posortuj listę
lista1.sort()
print("Lista po posortowaniu: ", lista1)
# 7 Utwórz kopię listy
kopialisty = lista1.copy()
print("Kopia listy: ", kopialisty)
# 8 Odwróć kolejność elementów w kopii
lista1.reverse()
print("Lista po odwróceniu: ", lista1)
# 9 Dodaj do każdej wartości w pierwszej listy 1, a w drugiej odejmij 1
for i in range(len(lista1)):
    lista1[i] += 1
    list2[i] -= 1
# 10 Wyświetl obie listy
print("Lista 1 po dodaniu 1: ", lista1)
print("Lista 2 po odjęciu 1: ", list2)

print(lista1.count(lista1[0]))