import pygame
import random
import configparser

WIELKOSC_KAFLA = 32
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

wiersz = int(SZEROKOSC_EKRANU / WIELKOSC_KAFLA)
kolumna = int(WYSOKOSC_EKRANU/WIELKOSC_KAFLA)

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("./images/apple.png")
        self.rect = pygame.Rect(random.randint(0,wiersz - 1)*WIELKOSC_KAFLA, random.randint(0,kolumna -1)*WIELKOSC_KAFLA, WIELKOSC_KAFLA, WIELKOSC_KAFLA)