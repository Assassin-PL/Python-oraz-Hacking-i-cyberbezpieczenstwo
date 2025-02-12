krotka = (4,2,11,2,4)

#count
print("ilosc elementow w krotvce")
print(krotka.count(4))

print("chce wziac elemnty od 2 do 4")
print(krotka[2:3])

#index
print("znajdz element 11")
print(krotka.index(11))

zbior = {1,2,3,4,2,5,6,1,8,7,1,8,9,10}
print("Zbior")
print(zbior)
print("ilosc 1 w zbiorze")
if 1 in zbior: print("Tak")
pusty_zbior = set()
zbior.add(1)
print("Zbior po dodaniu 11")
print(zbior)
zbior.remove(1)
print("Zbior po usunieciu 11")
print(zbior)
zbior.discard(11)
print("Zbior po usunieciu 11")
print(zbior)
print("czy 11 jest w zbiorze")
if 11 in zbior: print("Tak") 
print("Nie")

#usuniecie metoda pop
print("usuniecie metoda pop")
losowy_element = zbior.pop()
print(f"usunieto element {losowy_element} z zbioru {zbior}")

#konwertujemy struktury danych
zbior = {1,2,3,4,5,6,7,8,9,10}
krotka= (4,8,9,4,5,6,7,8,9,10)
lista= [4,8,9,4,5,6,7,8,9,10]
slownik = {"klucz1": 1, "klucz2": 2, "klucz3": 3}
print("konwersja slownika na liste")
print(list(slownik))
print("konwersja slownika na krotke")
print(tuple(slownik))
print("konwersja slownika na zbior")
print(set(slownik))
print("konwersja zbioru na liste")
print(list(zbior))
print("konwersja krotki na liste")
print(list(krotka))
print("konwersja listy na zbior")
print(set(lista))
print("konwersja krotki na zbior")
print(set(krotka))
print("konwersja listy na krotke")
print(tuple(lista))
print("konwersja zbioru na krotke")
print(tuple(zbior))


#Zadania
# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 
# elementy (liczby)
krotka = (2,5,1)
lista = [3,0,1]
slownik = {"klucz1": 1, "klucz2": 2, "klucz3": 3}
zbior = {5,3,9}
# 2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów

print(f"dlugosc krotki wynosi {len(krotka)}")
print(f"dlugosc listy wynosi {len(lista)}")
print(f"dlugosc slownika wynosi {len(slownik)}")
print(f"dlugosc zbioru wynosi {len(zbior)}")
# 3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
for a in krotka:
    print(f"nasza krotka wyglada tak {a}")
for b in lista:
    print(f"nasza lista wyglada tak {b}")
for c in slownik:
    print(f"nasz slownik wyglada tak {c}")
for d in zbior:
    print(f"nasz zbior wyglada tak {d}")
# 4. Teraz wypisz wartości słownika zamiast kluczy
for a in slownik.values():
    print(a)
# 5. Wypisz te same elementy w odwrotnej kolejności, czy zawsze 
# jest to możliwe bezpośrednio?
print(krotka[::-1])
print(lista[::-1])
# print(slownik[::-1])
# nie jest to mozliwe dla slownika i zbioru
# W przypadku słownika i zbioru nie jest to możliwe, ponieważ
# nie posiadają one indeksów, a w przypadku zbioru kolejność
# elementów nie jest zachowywana.
# W razie problemów skorzystaj z pomocy chataGPT
# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.
lista.extend(krotka)
lista.extend(zbior)
lista.extend(slownik.values())
print(lista)
# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.
lista.append(max(lista))
lista.append(min(lista))
print(lista)
# 8. Sprawdź długość listy.
print(len(lista))
# 9.Zamień listę na krotkę- krotka2 i sprawdź jej długość.
krotka2 = tuple(lista)
print(len(krotka2))
# 10.Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, 
# z czego wynika różnica?
zbior2 = set(krotka2)
print(len(zbior2))

nowy_slownik = dict(zip(krotka2, zbior2))
print(nowy_slownik)

slownik_literek = {'a': 1, 'b': 2, 'c': 3}
print(slownik_literek)
slownik_wyrazow = {"jeden": 1, 'dwa': 2, "trzy": 3}
print(slownik_wyrazow)