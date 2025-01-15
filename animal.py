from utlis import Config

class Tamagotchi:
    def __init__(self):
        config = Config()
        self.poziom_glodu = float(config.get_float
                                  ('ANIMAL_DEFAULT_SETTINGS', 'GLOD'))
        self.poziom_szczescia = float(config.get_float
                                      ('ANIMAL_DEFAULT_SETTINGS', 'SZCZESCIE'))

    def nakarm(self):
        self.poziom_glodu += 10
        
    def pobaw_sie(self):
        self.poziom_szczescia += 10
        
    def aktualizuj(self):
        self.poziom_glodu -= 0.1
        self.poziom_szczescia -= 0.1
        