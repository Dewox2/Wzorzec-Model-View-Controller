# Zarządzanie Płytami CD - Model View Controller (MVC)

## Opis projektu
Ten projekt jest prostą aplikacją zarządzającą kolekcją płyt CD z muzyką. Został zaprojektowany w oparciu o wzorzec projektowy Model View Controller (MVC), który rozdziela logikę aplikacji, interfejs użytkownika i zarządzanie danymi.

## Funkcjonalności
### Aplikacja umożliwia:
- Dodawanie albumów do bazy danych.
- Wyświetlanie listy albumów z kluczowymi informacjami (tytuł, wykonawca, rok, wydawca).
- Usuwanie albumu z bazy.
- Modyfikowanie wybranego albumu (np. zmiana tytułu lub innych danych).

## Struktura danych
### Każdy album zawiera następujące dane:
- Tytuł albumu (np. "Thriller")
- Wykonawca (np. "Michael Jackson")
- Rok wydania (np. 1982)
- Wydawca (np. "Epic Records")

## Architektura MVC
- Model: Zarządza logiką danych i obsługuje operacje na bazie danych (dodawanie, usuwanie, edytowanie).
- View: Odpowiada za interfejs użytkownika, wyświetlanie danych i interakcję z użytkownikiem.
- Controller: Koordynuje interakcję między Modelem a Widokiem.