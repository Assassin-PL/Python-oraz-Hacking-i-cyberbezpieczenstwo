import pygame
import random
import configparser

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Inicjalizacja configparser
        config = configparser.ConfigParser()
        config.read('config.cfg')

        # Wczytywanie wartości jako stałe
        self.FPS = int(config['SETTINGS']['FPS'])
        self.WIELKOSC_KAFLA = int(config['SETTINGS']['WIELKOSC_KAFLA'])
        self.SZEROKOSC_EKRANU = int(config['SETTINGS']['SZEROKOSC_EKRANU'])
        self.WYSOKOSC_EKRANU = int(config['SETTINGS']['WYSOKOSC_EKRANU'])

        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("images/apple.png")
        self.rect = pygame.Rect(random.randint(0, 24) * self.WIELKOSC_KAFLA, random.randint(0, 18) * self.WIELKOSC_KAFLA, self.WIELKOSC_KAFLA, self.WIELKOSC_KAFLA)