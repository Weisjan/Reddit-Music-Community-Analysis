# Data

Dane nie są załączone w repozytorium ze względu na rozmiar.

## Źródło
Komentarze pobrane z Pushshift Reddit Dataset:
https://the-eye.eu/redarcs/

## Struktura
data/
├── raw/          # pliki .zst pobrane z Pushshift
└── processed/    # CSV-ki wygenerowane przez src/extract_data.py

## Jak odtworzyć
1. Pobierz pliki .zst i umieść w data/raw/
2. Uruchom src/extract_data.py
