krotka = (4,2,11,2,4)

#count
print("ilosc elementow w krotvce")
print(krotka.count(4))

print("chce wziac elemnty od 2 do 4")
print(krotka[2:3])

#index
print("znajdz element 11")
print(krotka.index(11))

zbior = {1,2,3,4,5,6,7,8,9,10}
print("Zbior")
print(zbior)
pusty_zbior = set()
zbior.add(11)
print("Zbior po dodaniu 11")
print(zbior)
zbior.remove(11)
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
# 2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
# 3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
# 4. Teraz wypisz wartości słownika zamiast kluczy
# 5. Wypisz te same elementy w odwrotnej kolejności, czy zawsze 
# jest to możliwe bezpośrednio? 
# W razie problemów skorzystaj z pomocy chataGPT
# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.
# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.
# 8. Sprawdź długość listy.
# 9.Zamień listę na krotkę- krotka2 i sprawdź jej długość.
# 10.Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, 
# z czego wynika różnica?
