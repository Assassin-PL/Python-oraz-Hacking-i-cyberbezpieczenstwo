import pygame
from utlis import Config

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
SZEROKOSC_EKRANU = int(config.get(ustawienia,"SZEROKOSC_EKRANU"))
WYSOKOSC_EKRANU = int(config.get(ustawienia, "WYSOKOSC_EKRANU"))

vec = pygame.math.Vector2
class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        self.config = Config()
        self.ustawienia : str = "SETTINGS"
        self.sciezki : str = "PATHS"
        self.obraz = pygame.image.load(self.config.get(self.sciezki, "ball")) 
        self.zresetujobraz()

    
