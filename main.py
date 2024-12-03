import pygame
from utlis import Config
from platforma import Platforma

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

ekran = pygame.display.set_mode([int(SZEROKOSC_EKRANU), int(WYSOKOSC_EKRANU)])
zegar = pygame.time.Clock()

obraz_tla = pygame.image.load(config.get(sciezki, "tlo"))
FPS : int = int( config.get(ustawienia, "FPS") )
print(f"FPS naszej gry wynosi: {FPS}")
#glowna petla gry

gra_dziala : bool = True
platforma = Platforma()
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    #sterowanie platforma
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)
    #wyswietlamy tlo
    ekran.blit(obraz_tla, (0, 0))
    #przemieszczanie platformy
    ekran.blit(platforma.obraz, platforma.pozycja)
    pygame.display.flip()
    zegar.tick(FPS)
    print(platforma.pozycja.left)

pygame.quit()