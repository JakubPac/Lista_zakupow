# Lista zakupów z GUI w Pythonie

Prosta aplikacja desktopowa z graficznym interfejsem użytkownika (GUI) zbudowanym w Tkinter, obsługująca listę zakupów z trwałym zapisem danych w bazie SQLite.

## Opis projektu

Projekt umożliwia:

- Dodawanie nowych produktów na listę zakupów przez interaktywne okno.
- Usuwanie pojedynczych produktów lub wielu zaznaczonych jednocześnie.
- Przechowywanie i odczytywanie listy zakupów z bazy danych SQLite, dzięki czemu dane są trwałe między uruchomieniami.
- Łatwe i intuicyjne GUI oparte na Tkinter.

## Wymagania

- Python 3.x
- Moduły standardowe: `tkinter`, `sqlite3`

Nie wymaga instalacji zewnętrznych bibliotek.

## Jak uruchomić?

1. Sklonuj lub pobierz repozytorium.
2. Uruchom skrypt:

python aplikacja_lista_zakupow.py

3. Pojawi się okno listy zakupów z opcjami dodawania i usuwania produktów.

## Struktura projektu

- `aplikacja_lista_zakupow.py` – główny plik z kodem aplikacji, zawiera klasę GUI i klasę obsługi bazy danych.
- `lista_db` – plik bazy danych SQLite tworzony automatycznie przy pierwszym uruchomieniu programu.

## Funkcjonalności

- Dodawanie produktów do listy zakupów z wpisywaniem nazwy w oknie dialogowym.
- Usuwanie pojedynczych produktów przez przycisk „-” obok nazwy.
- Usuwanie wielu produktów zaznaczonych checkboxem i kliknięcie „Remove selected”.
- Lista jest ładowana automatycznie z bazy danych przy starcie aplikacji.
- Baza zapewnia unikane wartości produktów (brak duplikatów).

## Możliwe rozszerzenia

- Dodanie obsługi ilości produktów.
- Dodanie możliwości edycji produktów.
- Sortowanie i filtrowanie listy.
- Zapisywanie listy do pliku CSV lub JSON.
- Udoskonalenie GUI (np. lepszy design, ikony, menu).

## Autor

Jakub
