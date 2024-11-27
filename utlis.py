import configparser


class Config:
    __config_file = "config.cfg"  # Prywatny i niezmienny atrybut
    
    def __init__(self) -> None:
        self.__config = configparser.ConfigParser()
        self.__load_config()

    def __load_config(self) -> None:
        """Wczytuje konfigurację z pliku."""
        try:
            with open(self.__config_file, 'r') as file:
                self.__config.read_file(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Plik konfiguracyjny '{self.__config_file}' nie został znaleziony.")
        except Exception as e:
            raise Exception(f"Wystąpił problem podczas wczytywania pliku konfiguracyjnego: {e}")

    def get(self, section: str, option: str) -> str:
        """Zwraca wartość z określonej sekcji i opcji."""
        try:
            return self.__config.get(section, option)
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
        except configparser.NoOptionError:
            raise ValueError(f"Opcja '{option}' nie istnieje w sekcji '{section}'.")

    def get_all_options(self, section: str) -> dict:
        """Zwraca wszystkie opcje w danej sekcji jako słownik."""
        try:
            return dict(self.__config.items(section))
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")

    def get_int(self, section: str, option: str) -> int:
        """Zwraca wartość z określonej sekcji i opcji."""
        try:
            return self.__config.get(section, option)
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
        except configparser.NoOptionError:
            raise ValueError(f"Opcja '{option}' nie istnieje w sekcji '{section}'.")