import pygame
import random
import configparser

configpath=("config.cfg")
configSnake = configparser.ConfigParser()
configSnake.read(configpath)

FPS :int = int(configSnake['SETTINGS']['FPS'])
WIELKOSC_KAFLA :int = int (configSnake['SETTINGS']['WIELKOSC_KAFLA'])
SZEROKOSC_EKRANU :int = int (configSnake['SETTINGS']['SZEROKOSC_EKRANU'])
WYSOKOSC_EKRANU :int = int (configSnake['SETTINGS']['WYSOKOSC_EKRANU'])

wiersz = int(SZEROKOSC_EKRANU / WIELKOSC_KAFLA)
kolumna = int(WYSOKOSC_EKRANU / WIELKOSC_KAFLA)

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("./images/apple.png")
        self.rect = pygame.Rect(random.randint(0,wiersz - 1)*WIELKOSC_KAFLA, random.randint(0,kolumna -1)*WIELKOSC_KAFLA, WIELKOSC_KAFLA, WIELKOSC_KAFLA)