import pygame
from utlis import Config

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"

class Platforma(pygame.sprite.Sprite):
    def __init__(self, x, y, szerokosc, wysokosc):
        super().__init__()
        self.config = Config()
        self.ustawienia : str = "SETTINGS"
        self.sciezki : str = "PATHS"
        self.obraz = pygame.image.load(self.config.get(self.sciezki, "platforma")) 
