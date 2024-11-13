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
    kierunek = None 
    nowy_kierunek = None
    
    def __init__(self):
        #orginalny obraz glowy
        self.orginalny_obraz = pygame.image.load("images/head.png")
        #nasz obraz pomocniczy
        self.obraz = pygame.transform.rotate(self.orginalny_obraz , 0)
        #wspolrzedne glowy 
        self.rect = self.obraz.get_rect(
            center=(12*WIELKOSC_KAFLA+16 , 9*WIELKOSC_KAFLA + 16)
            )
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA
    
    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa :bool = True
        if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False
        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek
            
    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.orginalny_obraz, self.kierunek.value*-90)
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -1*WIELKOSC_KAFLA)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 1*WIELKOSC_KAFLA)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(WIELKOSC_KAFLA, 0)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-1*WIELKOSC_KAFLA, 0)
         
