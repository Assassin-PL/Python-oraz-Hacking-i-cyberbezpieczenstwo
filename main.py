import pygame
import random
import time
import configparser
from Klasy import Jablko
from Waz import Waz
from Kierunek import Kierunek


configpath=("config.cfg")
configSnake = configparser.ConfigParser()
configSnake.read(configpath)

FPS :int = int(configSnake['SETTINGS']['FPS'])
WIELKOSC_KAFLA :int = int (configSnake['SETTINGS']['WIELKOSC_KAFLA'])
SZEROKOSC_EKRANU :int = int (configSnake['SETTINGS']['SZEROKOSC_EKRANU'])
WYSOKOSC_EKRANU :int = int (configSnake['SETTINGS']['WYSOKOSC_EKRANU'])

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

#waz
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

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