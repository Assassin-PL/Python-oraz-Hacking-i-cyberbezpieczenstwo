import pygame
from utlis import Config
from platforma import Platforma
from Kulka import Kulka

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
# print(f"Nasze mozliwe ustawienia w slowniku {ustawienia} to: {config.get_all_options(ustawienia)}")
print(f"a nasze sciezki w PATHS to {config.get_all_options(sciezki)}")
#wysokość i szerokość ekranu 
#Przykladowy kod dla ladowania do zmiennej szerokosci ekranu
SZEROKOSC_EKRANU = config.get(ustawienia,"SZEROKOSC_EKRANU")
print(f"Szerokosc naszego ekranu wynosi: {SZEROKOSC_EKRANU} pixseli")
WYSOKOSC_EKRANU = config.get(ustawienia, "WYSOKOSC_EKRANU")
print(f"WYSOKOSC_EKRANU naszego ekranu wynosi: {WYSOKOSC_EKRANU} pixseli")
zycie : int = 3

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode([int(SZEROKOSC_EKRANU), int(WYSOKOSC_EKRANU)])
zegar = pygame.time.Clock()
czcionka = pygame.font.SysFont('Comic Sans MS', 24)

#do poziomow: 
#poziomy gry
poziom1 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

obraz_tla = pygame.image.load(config.get(sciezki, "tlo"))
FPS : int = int( config.get(ustawienia, "FPS") )
print(f"FPS naszej gry wynosi: {FPS}")
#glowna petla gry

gra_dziala : bool = True
platforma = Platforma()
kulka = Kulka()
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    #sterowanie platforma
    keys=pygame.key.get_pressed() 
    if keys[pygame.K_a] and not platforma.pozycja.left < 0:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d] and not platforma.pozycja.right > int(SZEROKOSC_EKRANU):
        platforma.ruszaj_platforma(1)
    kulka.aktualizuj(platforma)
    #wyswietlamy tlo
    ekran.blit(obraz_tla, (0, 0))
    #przemieszczanie platformy
    ekran.blit(platforma.obraz, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)
    #zrobienie tekstu
    tekst = czcionka.render(f"Zycie: {zycie}", False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))
    pygame.display.flip()
    zegar.tick(FPS)
    print(platforma.pozycja.left)

pygame.quit()