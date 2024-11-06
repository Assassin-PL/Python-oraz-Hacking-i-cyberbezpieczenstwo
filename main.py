import pygame
import random
import time
import configparser
# from Klasy import Jablko

FPS = 60
WIELKOSC_KAFLA = 32
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

wiersz = int(SZEROKOSC_EKRANU / WIELKOSC_KAFLA)
kolumna = int(WYSOKOSC_EKRANU/WIELKOSC_KAFLA)

#stworznie tlo
tlo = pygame.Surface((SZEROKOSC_EKRANU,WYSOKOSC_EKRANU))

for i in range(wiersz):
    for j in range(kolumna):
        obrazek = pygame.image.load("images/background.png")
        maska = (random.randrange(0,20), random.randrange(0,20),
                 random.randrange(0,20))
        obrazek.fill(maska, special_flags=pygame.BLEND_ADD)

#ustawienia
pygame.init()
