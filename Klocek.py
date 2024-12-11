import pygame
import copy
from utlis import Config

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
SZEROKOSC_EKRANU = int(config.get(ustawienia,"SZEROKOSC_EKRANU"))
WYSOKOSC_EKRANU = int(config.get(ustawienia, "WYSOKOSC_EKRANU"))

class Klocek(pygame.sprite.Sprite):
    def __init__(self, x ,y ,zdrowie):
        super().__init__()
        self.config = Config()
        self.ustawienia : str = "SETTINGS"
        self.sciezki : str = "PATHS"
        self.obraz_org = pygame.image.load(self.config.get(self.sciezki, "cegla"))
        self.pozycja = pygame.Rect(x, y, 96, 48)
        self.zdrowie = zdrowie
    
    def aktualizuj(self):
        maska_koloru = 0
        if self.zdrowie == 3:
            maska_koloru = (128,0,0)
        if self.zdrowie == 2:
            maska_koloru = (0,0,128)
        if self.zdrowie == 1:
            maska_koloru = (0,128,0)
        self.obraz = copy.copy(self.obraz_org)
        self.obraz.fill(maska_koloru, special_flags=pygame.BLEND_ADD)