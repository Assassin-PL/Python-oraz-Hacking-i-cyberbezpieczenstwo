import pygame
import random
import time
import configparser
from Klasy import Jablko

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
        obrazek = pygame.image.load("./images/background.png")
        maska = (random.randrange(0,20), random.randrange(0,20),
                 random.randrange(0,20))
        obrazek.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obrazek, (i*WIELKOSC_KAFLA,j*WIELKOSC_KAFLA))

#ustawienia
pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU,WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

#jablka
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

czy_gra_dziala : bool = True
while czy_gra_dziala:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                czy_gra_dziala = False
        elif event.type == pygame.QUIT:
            czy_gra_dziala = False
    #rysowanie tla
    ekran.blit(tlo, (0, 0))
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    #czyszczenia ekranu
    pygame.display.flip()
    #ustawiamy nasze zegar na fps
    zegar.tick(FPS)
#wprowadzimy opzonienie przed zamknieciem
time.sleep(3)
#zamkniencie aplikacji
pygame.quit()