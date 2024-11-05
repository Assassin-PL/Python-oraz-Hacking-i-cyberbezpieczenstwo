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
