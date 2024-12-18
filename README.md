# Zaawansowwane Struktury Dancyh
Repozytorium do zajęć z Python oraz Hacking i cyberbezpieczeństwo Lekcja 14. Nauka struktur danych i jak komputer przechowuje obiekty w pamieci

## Jak pobrać kod z GitHuba
Jeśli chcesz pobrać kod z konkretnego brancha, wykonaj następujące kroki:

### 1. Klonowanie repozytorium
Aby sklonować repozytorium, użyj poniższego polecenia w terminalu:

```bash
git clone https://github.com/Assassin-PL/Snake.v1
```

Powyższe polecenie utworzy lokalną kopię repozytorium na Twoim komputerze.

### 2. Przełączanie się na określony branch
Po sklonowaniu repozytorium, przejdź do folderu z repozytorium i przełącz się na odpowiedni branch:

```bash
cd Snake.v1
git checkout <nazwa-brancha>
```

Na przykład, jeśli branch ma nazwę `feature-branch`, możesz użyć:

```bash
git checkout feature-branch
```

### 3. Aktualizacja repozytorium
Aby pobrać najnowsze zmiany z repozytorium (bez wysyłania niczego), możesz użyć:

```bash
git pull origin <nazwa-brancha>
```

To polecenie pobiera najnowsze zmiany z określonego brancha na GitHubie.

## Jak działają commity
W kontekście pobierania kodu z repozytorium, ważne jest, aby zrozumieć, że commity to zmiany w kodzie, które są przechowywane w repozytorium. Aby pobierać aktualne wersje kodu bez wysyłania niczego na GitHuba, wystarczy korzystać z poniższych poleceń:

- **git fetch**: Pobiera wszystkie zmiany (commity) z GitHuba do Twojego lokalnego repozytorium, ale nie wprowadza ich automatycznie do bieżącego brancha. Pozwala na podgląd, jakie zmiany zostały dokonane.

    ```bash
    git fetch
    ```

- **git pull**: Pobiera i automatycznie łączy zmiany zdalnego repozytorium z Twoim lokalnym branchem. To najprostszy sposób, aby mieć najnowszą wersję kodu.

    ```bash
    git pull
    ```

Pamiętaj, że powyższe polecenia umożliwiają jedynie pobieranie zmian z repozytorium, nie wysyłają żadnych lokalnych zmian na GitHuba.

