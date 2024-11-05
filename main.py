import pygame
import random
import time
import configparser
from Klasy import Jablko

# Inicjalizacja configparser
config = configparser.ConfigParser()
config.read('config.cfg')

# Wczytywanie wartości jako stałe
FPS = int(config['SETTINGS']['FPS'])
WIELKOSC_KAFLA = int(config['SETTINGS']['WIELKOSC_KAFLA'])
SZEROKOSC_EKRANU = int(config['SETTINGS']['SZEROKOSC_EKRANU'])
WYSOKOSC_EKRANU = int(config['SETTINGS']['WYSOKOSC_EKRANU'])

tlo = pygame.Surface((SZEROKOSC_EKRANU,WYSOKOSC_EKRANU))

wiersz : int= int(SZEROKOSC_EKRANU / WIELKOSC_KAFLA)
kolumna : int = int(WYSOKOSC_EKRANU / WIELKOSC_KAFLA)

for i in range(wiersz):
    for j in range(kolumna):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0,20))
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i * WIELKOSC_KAFLA, j * WIELKOSC_KAFLA))

#ustawienia
pygame.init()
#obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

#jabłka
jablko = Jablko()
if isinstance(jablko, pygame.sprite.Sprite):
    jablka = pygame.sprite.Group()
    jablka.add(jablko)

gra_dziala :bool=True
while gra_dziala :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif event.type == pygame.QUIT:
            gra_dziala = False
        #rysowanie tla
        ekran.blit(tlo, (0, 0))
        # rysowanie jablek
        for jablko in jablka:
            ekran.blit(jablko.obraz, jablko.rect)
        #czyszczenie ekranu
        pygame.display.flip()
        #wygaszanie ekranu
        zegar.tick(FPS)

time.sleep(3)
pygame.quit()

