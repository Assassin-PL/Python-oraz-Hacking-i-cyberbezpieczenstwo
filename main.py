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

