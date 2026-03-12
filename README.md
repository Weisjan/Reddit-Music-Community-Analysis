# Reddit Music Community Analysis

Comparative analysis of discussion topics and user interaction patterns across music-focused subreddits.

## Research Question

Do subreddits dedicated to different music genres differ in the topics they discuss and how their users interact with each other?

## Subreddits

| Subreddit     | Genre   |
| ------------- | ------- |
| r/hiphopheads | Hip-hop |
| r/indieheads  | Indie   |
| r/Metal       | Metal   |
| r/popheads    | Pop     |

**Time period:** August 2015 – December 2022  
**Data source:** [Pushshift Reddit Dataset](https://the-eye.eu/redarcs/)

## Project Structure

```
├── data/
│   ├── raw/            # .zst files from Pushshift (not included)
│   └── processed/      # extracted CSV files (not included)
├── notebooks/
│   └── 01_eda.ipynb
├── src/
│   ├── scan_dates.py   # diagnostic script — check date ranges in .zst files
│   └── extract_data.py # extract and filter comments from .zst to CSV
├── outputs/
│   └── figures/        # generated plots
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

To reproduce the data:

1. Download `.zst` files from Pushshift and place them in `data/raw/`
2. Run `src/scan_dates.py` to verify date ranges
3. Run `src/extract_data.py` to extract comments to `data/processed/`
4. Run notebooks in order

## Status

- [x] Data extraction and filtering
- [x] Exploratory data analysis (EDA)
- [ ] Text mining
- [ ] Social network analysis
