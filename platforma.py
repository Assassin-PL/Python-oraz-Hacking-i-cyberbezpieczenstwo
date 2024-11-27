import pygame
from utlis import Config

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
SZEROKOSC_EKRANU = config.get(ustawienia,"SZEROKOSC_EKRANU")
WYSOKOSC_EKRANU = config.get(ustawienia, "WYSOKOSC_EKRANU")
class Platforma(pygame.sprite.Sprite):
    def __init__(self, x, y, szerokosc, wysokosc):
        super().__init__()
        self.config = Config()
        self.ustawienia : str = "SETTINGS"
        self.sciezki : str = "PATHS"
        self.obraz = pygame.image.load(self.config.get(self.sciezki, "pad")) 
        self.zresetujobraz()
    
    def zresetujobraz(self):
        self.pozycja = pygame.Rect(SZEROKOSC_EKRANU / 2 -70 , WYSOKOSC_EKRANU - 100, 140, 30)

    def ruszaj_platforma(self, wartosc):
        predkosc = int(self.config.get_int(self.ustawienia, "PREDKOSC"))
        self.pozycja.move_ip(wartosc * predkosc, 0)