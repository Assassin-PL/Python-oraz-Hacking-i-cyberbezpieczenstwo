from utlis import Config, DataManager
import pygame

config = Config()
sekcje = []
dane = DataManager()

for keys, values in config.get_dict().items():
    sekcje.append(keys)

print(sekcje)

# Pobieranie koloru tła jako krotki
try:
    kolor_tla = config.get_tuple('UI', 'KOLOR_TLA', as_tuple=True)
    print(f"Kolor Tła: {kolor_tla} (typ: {type(kolor_tla)})")
except (ValueError, TypeError) as e:
    print(e)
    
# Start naszej gry i jej inicjalizacja
pygame.display.init()
pygame.font.init()
SZEROKOSC = int(config.get_int('SETTINGS', 'SZEROKOSC'))
WYSOKOSC  = int(config.get_int('SETTINGS', 'WYSOKOSC'))
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
zegar = pygame.time.Clock()
pygame.display.set_caption(config.get_str('SETTINGS', 'NAZWA_GRY'))

# print(DataManager().data['wiek']) do przeczytania danej z pliku

# Glowna petla naszej gry
koniec_gry : bool = False
while not koniec_gry:
    #glowna petla gry
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN: #przy wscisnieciu klawisza escape
            if zdarzenie.key == pygame.K_ESCAPE:
                koniec_gry = True
        elif zdarzenie.type == pygame.QUIT:
            koniec_gry = True
    ekran.fill(kolor_tla)
    
    pygame.display.flip()
    zegar.tick(30)
    
pygame.quit()