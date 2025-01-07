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

    def get_dict(self) -> dict:
        """Zwraca wszystkie sekcje i ich opcje jako słownik."""
        try:
            config_dict = {section: dict(self.__config[section]) for section in self.__config.sections()}
            return config_dict
        except configparser.Error as e:
            raise ValueError(f"Wystąpił błąd podczas konwersji konfiguracji na słownik: {e}")

    
    def get(self, section: str, option: str):
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
        
    def get_str(self, section: str, option: str) -> str:
        """Zwraca wartość z określonej sekcji i opcji."""
        try:
            return self.__config.get(section, option)
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
        except configparser.NoOptionError:
            raise ValueError(f"Opcja '{option}' nie istnieje w sekcji '{section}'.")

    def get_int(self, section: str, option: str) -> int:
        """Zwraca wartość z określonej sekcji i opcji."""
        try:
            return self.__config.get(section, option)
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
        except configparser.NoOptionError:
            raise ValueError(f"Opcja '{option}' nie istnieje w sekcji '{section}'.")
        
    def get_float(self, section: str, option: str) -> float:
        """Zwraca wartość z określonej sekcji i opcji."""
        try:
            return self.__config.get(section, option)
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
        except configparser.NoOptionError:
            raise ValueError(f"Opcja '{option}' nie istnieje w sekcji '{section}'.")
        
    def get_bool(self, section: str, option: str) -> bool:
        """Zwraca wartość z określonej sekcji i opcji."""
        try:
            return self.__config.get(section, option)
        except configparser.NoSectionError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
        except configparser.NoOptionError:
            raise ValueError(f"Opcja '{option}' nie istnieje w sekcji '{section}'.")
    
    def add_section(self, section: str, options: dict = None) -> None:
        """
        Dodaje nową sekcję do pliku konfiguracyjnego.

        :param section: Nazwa nowej sekcji.
        :param options: Opcjonalny słownik z kluczami i wartościami do dodania w sekcji.
        :raises ValueError: Jeśli sekcja już istnieje.
        """
        if self.__config.has_section(section):
            raise ValueError(f"Sekcja '{section}' już istnieje.")
        self.__config.add_section(section)
        if options:
            for key, value in options.items():
                self.__config.set(section, key, str(value))
        self.__save_config()

    def update_section(self, section: str, options: dict) -> None:
        """
        Aktualizuje istniejącą sekcję z nowymi opcjami. Nadpisuje istniejące klucze.

        :param section: Nazwa sekcji do aktualizacji.
        :param options: Słownik z kluczami i wartościami do aktualizacji.
        :raises ValueError: Jeśli sekcja nie istnieje.
        """
        if not self.__config.has_section(section):
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        for key, value in options.items():
            self.__config.set(section, key, str(value))
        self.__save_config()

    def add_or_update_key(self, section: str, key: str, value: str) -> None:
        """
        Dodaje nowy klucz do sekcji lub aktualizuje wartość istniejącego klucza.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza do dodania lub aktualizacji.
        :param value: Nowa wartość klucza.
        :raises ValueError: Jeśli sekcja nie istnieje.
        """
        if not self.__config.has_section(section):
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        self.__config.set(section, key, str(value))
        self.__save_config()

    def remove_section(self, section: str) -> None:
        """
        Usuwa sekcję z pliku konfiguracyjnego.

        :param section: Nazwa sekcji do usunięcia.
        :raises ValueError: Jeśli sekcja nie istnieje.
        """
        if not self.__config.has_section(section):
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        self.__config.remove_section(section)
        self.__save_config()

    def remove_key(self, section: str, key: str) -> None:
        """
        Usuwa klucz z sekcji.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza do usunięcia.
        :raises ValueError: Jeśli sekcja lub klucz nie istnieje.
        """
        if not self.__config.has_section(section):
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        if not self.__config.has_option(section, key):
            raise ValueError(f"Klucz '{key}' nie istnieje w sekcji '{section}'.")
        self.__config.remove_option(section, key)
        self.__save_config()

    def __save_config(self) -> None:
        """Zapisuje aktualny stan konfiguracji do pliku."""
        try:
            with open(self.__config_file, 'w') as file:
                self.__config.write(file)
        except Exception as e:
            raise Exception(f"Wystąpił problem podczas zapisywania pliku konfiguracyjnego: {e}")