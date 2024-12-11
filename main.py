import pygame
from utlis import Config
from platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek

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
Poziom = 0
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

poziom2 = [
[0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
[0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
poziom3 = [
[2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
[2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
[2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
[3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
[0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
[0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
[0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]

klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    if Poziom == 2:
        wczytany_poziom = poziom3
    
    for i in range (10):
        for j in range (7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32 + i*96, 32 + j*48, wczytany_poziom[j][i])
                klocki.add(klocek)
    
dodaj_klocki()
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
    
    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetujpozycje()
        platforma.zresetujobraz()
        dodaj_klocki()
    
    kulka.aktualizuj(platforma, klocki)
    klocki.update()
    platforma.aktualizuj()
    #wyswietlamy tlo
    ekran.blit(obraz_tla, (0, 0))
    #przemieszczanie platformy
    ekran.blit(platforma.obraz, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)
    for brick in klocki:
        ekran.blit(brick.obraz, brick.pozycja)
    #zrobienie tekstu
    tekst = czcionka.render(f"Zycie: {zycie}", False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))
    pygame.display.flip()
    zegar.tick(FPS)
    print(platforma.pozycja.left)

pygame.quit()