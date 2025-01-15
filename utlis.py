import configparser
import json
import os
from typing import Any, Dict, Optional, List, Tuple

def dict_marger(dict_list: List[Dict[str, Dict[str, Any]]]) -> Dict[str, Dict[str, Any]]:
    """
    Łączy listę słowników w jeden duży słownik.

    :param dict_list: Lista słowników, gdzie każdy słownik ma jedną sekcję.
                      Przykład: [{"Database": {...}}, {"API": {...}}]
    :return: Jeden słownik łączący wszystkie sekcje.
             Przykład: {"Database": {...}, "API": {...}}
    :raises ValueError: Jeśli w liście znajdują się duplikaty sekcji.
    """
    merged_dict = {}
    for d in dict_list:
        if not isinstance(d, dict):
            raise TypeError(f"Oczekiwano słownika, a otrzymano {type(d)}.")
        for key, value in d.items():
            if key in merged_dict:
                raise ValueError(f"Duplikat sekcji '{key}' znaleziony.")
            merged_dict[key] = value
    return merged_dict

def dict_splitter(merged_dict: Dict[str, Dict[str, Any]]) -> List[Dict[str, Dict[str, Any]]]:
    """
    Rozdziela duży słownik na listę mniejszych słowników, każdy z jedną sekcją.

    :param merged_dict: Duży słownik z wieloma sekcjami.
                        Przykład: {"Database": {...}, "API": {...}}
    :return: Lista mniejszych słowników, każdy zawiera jedną sekcję.
             Przykład: [{"Database": {...}}, {"API": {...}}]
    :raises TypeError: Jeśli `merged_dict` nie jest słownikiem.
    """
    if not isinstance(merged_dict, dict):
        raise TypeError(f"Oczekiwano słownika, a otrzymano {type(merged_dict)}.")

    split_list = []
    for key, value in merged_dict.items():
        split_list.append({key: value})
    return split_list


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
    
    def get_tuple(self, section: str, option: str, as_tuple: bool = False) -> tuple:
        """Zwraca wartość z określonej sekcji i opcji.
        
        Jeśli `as_tuple` jest True, próbuje przekonwertować wartość na krotkę.
        
        :param section: Nazwa sekcji.
        :param option: Nazwa opcji.
        :param as_tuple: Czy zwrócić wartość jako krotkę.
        :return: Wartość jako string lub krotka.
        :raises ValueError: Jeśli sekcja lub opcja nie istnieje.
        :raises TypeError: Jeśli konwersja na krotkę się nie powiodła.
        """
        try:
            value = self.__config.get(section, option)
            if as_tuple:
                # Zakładamy, że krotki są zapisane jako "200,200,200"
                try:
                    return tuple(int(x.strip()) for x in value.split(','))
                except ValueError:
                    raise TypeError(f"Wartość opcji '{option}' w sekcji '{section}' nie może zostać przekonwertowana na krotkę.")
            return value
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
class DataManager:
    """
    Klasa DataManager zarządza plikami JSON, umożliwiając odczyt, zapis,
    dodawanie, aktualizację oraz usuwanie sekcji i kluczy w pliku konfiguracyjnym.
    """

    def __init__(self, file_path: Optional[str] = None, template: Optional[Dict[str, Any]] = None) -> None:
        """
        Inicjalizuje DataManager z określonym plikiem JSON lub tworzy nowy plik na podstawie szablonu.

        :param file_path: (Opcjonalnie) Ścieżka do pliku JSON. Jeśli nie podano, plik zostanie utworzony na podstawie szablonu.
        :param template: (Opcjonalnie) Słownik zawierający dane do utworzenia nowego pliku JSON.
        :raises ValueError: Jeśli plik nie istnieje, nie podano szablonu podczas tworzenia nowego pliku.
        """
        self.file_path = file_path or "save.json"
        self.data = {}
        self.template = template

        if os.path.exists(self.file_path):
            self._load()
        else:
            if self.template:
                self.data = self.template
                self._save()
            else:
                # Tworzenie pustego pliku JSON, jeśli nie dostarczono szablonu
                with open(self.file_path, 'w') as file:
                    json.dump({}, file, indent=4)

    def _load(self) -> None:
        """
        Wczytuje dane z pliku JSON.
        """
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Plik '{self.file_path}' zawiera nieprawidłowy JSON: {e}")
        except Exception as e:
            raise Exception(f"Wystąpił problem podczas wczytywania pliku '{self.file_path}': {e}")

    def _save(self) -> None:
        """
        Zapisuje aktualny stan danych do pliku JSON.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            raise Exception(f"Wystąpił problem podczas zapisywania pliku '{self.file_path}': {e}")

    def get_dict(self) -> Dict[str, Any]:
        """
        Zwraca cały plik konfiguracyjny jako słownik.

        :return: Słownik z danymi z pliku JSON.
        """
        return self.data.copy()

    def get(self, section: str, key: str) -> Any:
        """
        Zwraca wartość z określonej sekcji i klucza.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza.
        :return: Wartość przypisana do klucza.
        :raises ValueError: Jeśli sekcja lub klucz nie istnieje.
        """
        try:
            return self.data[section][key]
        except KeyError as e:
            missing = e.args[0]
            if missing == section:
                raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")
            else:
                raise ValueError(f"Klucz '{key}' nie istnieje w sekcji '{section}'.")

    def get_all_options(self, section: str) -> Dict[str, Any]:
        """
        Zwraca wszystkie opcje w danej sekcji jako słownik.

        :param section: Nazwa sekcji.
        :return: Słownik z kluczami i wartościami w sekcji.
        :raises ValueError: Jeśli sekcja nie istnieje.
        """
        try:
            return self.data[section].copy()
        except KeyError:
            raise ValueError(f"Sekcja '{section}' nie istnieje w pliku konfiguracyjnym.")

    def get_str(self, section: str, key: str) -> str:
        """
        Zwraca wartość jako string z określonej sekcji i klucza.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza.
        :return: Wartość jako string.
        :raises ValueError, TypeError: Jeśli sekcja lub klucz nie istnieje lub wartość nie jest stringiem.
        """
        value = self.get(section, key)
        if not isinstance(value, str):
            raise TypeError(f"Klucz '{key}' w sekcji '{section}' nie jest typu string.")
        return value

    def get_int(self, section: str, key: str) -> int:
        """
        Zwraca wartość jako integer z określonej sekcji i klucza.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza.
        :return: Wartość jako integer.
        :raises ValueError, TypeError: Jeśli sekcja lub klucz nie istnieje lub wartość nie jest integerem.
        """
        value = self.get(section, key)
        if isinstance(value, int):
            return value
        try:
            return int(value)
        except (ValueError, TypeError):
            raise TypeError(f"Klucz '{key}' w sekcji '{section}' nie jest typu integer.")

    def get_float(self, section: str, key: str) -> float:
        """
        Zwraca wartość jako float z określonej sekcji i klucza.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza.
        :return: Wartość jako float.
        :raises ValueError, TypeError: Jeśli sekcja lub klucz nie istnieje lub wartość nie jest floatem.
        """
        value = self.get(section, key)
        if isinstance(value, float):
            return value
        try:
            return float(value)
        except (ValueError, TypeError):
            raise TypeError(f"Klucz '{key}' w sekcji '{section}' nie jest typu float.")

    def get_bool(self, section: str, key: str) -> bool:
        """
        Zwraca wartość jako boolean z określonej sekcji i klucza.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza.
        :return: Wartość jako boolean.
        :raises ValueError, TypeError: Jeśli sekcja lub klucz nie istnieje lub wartość nie jest booleanem.
        """
        value = self.get(section, key)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            if value.lower() in ('true', 'yes', '1'):
                return True
            elif value.lower() in ('false', 'no', '0'):
                return False
        raise TypeError(f"Klucz '{key}' w sekcji '{section}' nie jest typu boolean.")

    def add_section(self, section: str, options: Dict[str, Any] = None) -> None:
        """
        Dodaje nową sekcję do pliku konfiguracyjnego.

        :param section: Nazwa nowej sekcji.
        :param options: Opcjonalny słownik z kluczami i wartościami do dodania w sekcji.
        :raises ValueError: Jeśli sekcja już istnieje.
        """
        if section in self.data:
            raise ValueError(f"Sekcja '{section}' już istnieje.")
        self.data[section] = {}
        if options:
            for key, value in options.items():
                self.data[section][key] = value
        self._save()

    def update_section(self, section: str, options: Dict[str, Any]) -> None:
        """
        Aktualizuje istniejącą sekcję z nowymi opcjami. Nadpisuje istniejące klucze.

        :param section: Nazwa sekcji do aktualizacji.
        :param options: Słownik z kluczami i wartościami do aktualizacji.
        :raises ValueError: Jeśli sekcja nie istnieje.
        """
        if section not in self.data:
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        for key, value in options.items():
            self.data[section][key] = value
        self._save()

    def add_or_update_key(self, section: str, key: str, value: Any) -> None:
        """
        Dodaje nowy klucz do sekcji lub aktualizuje wartość istniejącego klucza.
        Jeśli sekcja nie istnieje, jest tworzona.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza do dodania lub aktualizacji.
        :param value: Nowa wartość klucza.
        """
        if section not in self.data:
            self.data[section] = {}
        self.data[section][key] = value
        self._save()
        
    def add_data(self, data: Dict[str, Any]) -> None:
        if not isinstance(data, dict):
            raise TypeError("Expected a dictionary")
        if self.data:
            self.data.update(data)
        else:
            self.data = data
        self._save()
        
    def remove_section(self, section: str) -> None:
        """
        Usuwa sekcję z pliku konfiguracyjnego.

        :param section: Nazwa sekcji do usunięcia.
        :raises ValueError: Jeśli sekcja nie istnieje.
        """
        if section not in self.data:
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        del self.data[section]
        self._save()

    def remove_key(self, section: str, key: str) -> None:
        """
        Usuwa klucz z sekcji.

        :param section: Nazwa sekcji.
        :param key: Nazwa klucza do usunięcia.
        :raises ValueError: Jeśli sekcja lub klucz nie istnieje.
        """
        if section not in self.data:
            raise ValueError(f"Sekcja '{section}' nie istnieje.")
        if key not in self.data[section]:
            raise ValueError(f"Klucz '{key}' nie istnieje w sekcji '{section}'.")
        del self.data[section][key]
        self._save()
