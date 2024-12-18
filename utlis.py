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
#nowe klasy
class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        buffor = None
        if not self.is_empty():
            # return self.stack.pop()
            buffor = self.stack[-1]
            self.stack.remove(self.stack[-1])
            return buffor            
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def pokaz_elemnty(self):
        return print(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item):
         self.queue.append(item)   
    def dequeue(self):
        buffor = None
        if not self.is_empty():
            buffor = self.queue[0]
            self.queue.remove(self.queue[0])
            return buffor   
    def peek(self):
        if not self.is_empty():
            return self.queue[0]   
    def pokaz_elemnty(self):
        return print(self.queue)
    def size(self):
        return len(self.queue)