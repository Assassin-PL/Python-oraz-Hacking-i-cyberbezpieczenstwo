import pygame
from pygame.sprite import AbstractGroup
from Kierunek import Kierunek
import configparser

#Tutaj stowrzymy klase weza

configpath=("config.cfg")
configSnake = configparser.ConfigParser()
configSnake.read(configpath)

WIELKOSC_KAFLA :int = int (configSnake['SETTINGS']['WIELKOSC_KAFLA'])

class Waz(pygame.sprite.Sprite):
    orginalny_obraz = None
    obraz = None
    rect = None
    
    def __init__(self):
        #orginalny obraz glowy
        self.orginalny_obraz = pygame.image.load("images/head.png")
        #nasz obraz pomocniczy
        self.obraz = pygame.transform.rotate(self.orginalny_obraz , 0)
        #wspolrzedne glowy 
        self.rect = self.obraz.get_rect(center=(12*WIELKOSC_KAFLA+16 , 9*WIELKOSC_KAFLA + 16))
         
