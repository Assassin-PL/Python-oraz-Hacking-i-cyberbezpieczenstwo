from utlis import Config

def wyswietl(slownik: dict) -> None:
    """Funkcja wyswietlajaca slownik w formie tekstu."""
    for klucz, wartosc  in slownik.items():
        print(f"Naszym kluczem jest {klucz} i przechowuje wartosc : {wartosc}")
        print(f"ale {wartosc} to tez jest slownik wiec mozemy go wyprintowac")
        if(isinstance(wartosc, dict)):
            for klucz2, wartosc2 in wartosc.items():
                print(f"klucz: {klucz2} wartosc: {wartosc2}")

config = Config()

slownik : dict = config.get_dict()

wyswietl(slownik)

