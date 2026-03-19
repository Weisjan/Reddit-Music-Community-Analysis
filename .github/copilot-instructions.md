# GitHub Copilot Instructions

## Project Overview

This is a data science university project analyzing Reddit music communities using NLP and social network analysis.

**Repository:** Weisjan/Reddit-Music-Community-Analysis  
**Author:** Jan Weis (student)

## Project Details

- **Subreddits:** r/Metal, r/hiphopheads, r/indieheads, r/popheads
- **Time period:** March 2020 – March 2021 (first year of the COVID-19 pandemic)
- **Data source:** Pushshift Reddit Dataset (.zst files)
- **Methods:** LDA topic modeling, VADER sentiment analysis, NetworkX social network analysis

## Research Question

Do subreddits dedicated to different music genres differ in the topics they discuss and how their users interact with each other during the first year of the COVID-19 pandemic (March 2020 – March 2021)?

## Project Structure

```
├── data/
│   ├── raw/              # .zst files from Pushshift (not in repo)
│   └── processed/        # extracted CSV files (not in repo)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_text_mining.ipynb
│   └── 03_network_analysis.ipynb
├── src/
│   ├── scan_dates.py
│   └── extract_data.py
├── outputs/
│   └── figures/
└── requirements.txt
```

## Tech Stack

- Python 3.12
- pandas, matplotlib, seaborn
- spacy (en_core_web_sm), nltk, gensim (LDA), vaderSentiment, wordcloud
- networkx, python-louvain
- zstandard (reading .zst files)

### Language Rules

- Code comments → Polish
- Plot titles and axis labels → Polish
- Everything else (README, variable names, function names, docstrings, commit messages) → English

### Code Style

- No type hints
- No docstrings unless already present in the file
- snake_case for all variables and functions
- Use print() instead of logging
- Keep code simple and readable — this is a student project, not production code
- Do not add unnecessary abstractions or complexity

### README Rules

- Written entirely in English
- Professional and concise
- Must mention the pandemic context (March 2020 – March 2021)
- Include: research question, dataset, methods, results, setup, project structure
- Do not add sections for work that is not yet complete

## Known Bot Accounts (filtered from data)

- MusicMirrorMan, HHHRobot, NoGoogleAMPBot, ReconEG, AutoModerator, RemindMeBot

## Extra Stopwords Used in Text Mining

like, just, get, got, one, know, think, really, would, also, even, much, still, way, good, make, people, time, music, song, songs, album, artist, https, http, www, com, reddit, amp
