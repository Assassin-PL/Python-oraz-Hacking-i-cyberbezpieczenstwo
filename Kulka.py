import pygame
from utlis import Config

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
SZEROKOSC_EKRANU = int(config.get(ustawienia,"SZEROKOSC_EKRANU"))
WYSOKOSC_EKRANU = int(config.get(ustawienia, "WYSOKOSC_EKRANU"))
