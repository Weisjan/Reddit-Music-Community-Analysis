# Reddit Music Community Analysis

Projekt analizuje komentarze z czterech muzycznych subredditow Reddita:
`r/hiphopheads`, `r/popheads`, `r/indieheads` i `r/Metal`.

Celem jest porownanie aktywnosci, jezyka, sentymentu, tematow dyskusji oraz prostych sieci interakcji uzytkownikow w okresie pierwszego roku pandemii COVID-19.

## Struktura projektu

```text
data/
  raw/              surowe pliki .zst z komentarzami
  processed/        przygotowane pliki CSV uzywane w notebookach
  checkpoints/      checkpointy .pkl do szybszego wznawiania analiz

notebooks/
  01_eda_uporzadkowany.ipynb
  02_text_mining_uporzadkowany.ipynb
  03_network_analysis_uporzadkowany.ipynb

outputs/
  figures/          zapisane wykresy .png
  reports/          tabele wynikowe .csv

src/
  scan_dates.py     sprawdzenie zakresu dat w plikach .zst
  extract_data.py   ekstrakcja i filtrowanie komentarzy do CSV
```

Notebooki z dopiskiem `_uporzadkowany` sa glownymi wersjami do pracy i odtwarzania wynikow.

## Notebooki

`01_eda_uporzadkowany.ipynb`:
podstawowa eksploracja danych, czyszczenie, aktywnosc w czasie, dlugosc komentarzy, score i najaktywniejsi autorzy.

`02_text_mining_uporzadkowany.ipynb`:
preprocessing tekstu, najczestsze slowa i bigramy, TF-IDF, wordcloudy, sentyment VADER i tematy LDA.

`03_network_analysis_uporzadkowany.ipynb`:
budowa sieci odpowiedzi, podstawowe metryki grafow, centralnosci, spolecznosci Louvain, nakladanie sie uzytkownikow miedzy subredditami.

## Dane i wyniki

Notebooki zakladaja uruchamianie z katalogu `notebooks/` i korzystaja ze wspolnego ukladu sciezek:

```python
BASE_DIR = Path("..")

DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

FIGURES_DIR = OUTPUTS_DIR / "figures"
REPORTS_DIR = OUTPUTS_DIR / "reports"
CHECKPOINT_DIR = DATA_DIR / "checkpoints"
```

Najwazniejsze dane wejsciowe znajduja sie w `data/processed/`.
Wykresy trafiaja do `outputs/figures/`, a tabele pomocnicze i raportowe do `outputs/reports/`.

## Jak uruchomic

1. Zainstaluj biblioteki:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. Jesli zaczynasz od surowych danych, umiesc pliki `.zst` w `data/raw/`.

3. Opcjonalnie uruchom skrypty:

```bash
python src/scan_dates.py
python src/extract_data.py
```

4. Uruchamiaj notebooki po kolei:

```text
01_eda_uporzadkowany.ipynb
02_text_mining_uporzadkowany.ipynb
03_network_analysis_uporzadkowany.ipynb
```

Checkpointy w `data/checkpoints/` pozwalaja ominac czesc dluzszych obliczen przy ponownym uruchamianiu.
