import pygame
from utlis import Config

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
print(f"Nasze mozliwe ustawienia w slowniku {ustawienia} to: {config.get_all_options(ustawienia)}")
print(f"a nasze sciezki w PATHS to {config.get_all_options(sciezki)}")
#wysokość i szerokość ekranu 
#Przykladowy kod dla ladowania do zmiennej szerokosci ekranu
SZEROKOSC_EKRANU = config.get(ustawienia,"SZEROKOSC_EKRANU")
print(f"Szerokosc naszego ekranu wynosi: {SZEROKOSC_EKRANU} pixseli")