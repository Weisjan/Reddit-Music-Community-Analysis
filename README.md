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
│   ├── 01_eda.ipynb
│   └── 02_text_mining.ipynb
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

## Results

### Exploratory Data Analysis

![Activity per month](outputs/figures/activity_per_month.png)

### Text Mining

![Word Clouds](outputs/figures/wordclouds.png)

Topic modeling (LDA, 5 topics per subreddit) and sentiment analysis (VADER) across 4 subreddits.

**Key findings:**

- r/Metal discussions focus on subgenres and sound ("black", "death", "genre")
- r/hiphopheads in 2015 was dominated by the Drake vs Meek Mill beef
- r/indieheads shows more emotional language around music ("feel", "life", "love")
- r/popheads centers on specific artists (Taylor Swift, Justin Bieber) and charts

**Sentiment (VADER compound score):**

| Subreddit     | Mean  | Median |
| ------------- | ----- | ------ |
| r/popheads    | 0.299 | 0.361  |
| r/indieheads  | 0.285 | 0.341  |
| r/Metal       | 0.175 | 0.153  |
| r/hiphopheads | 0.088 | 0.000  |

![Sentiment distribution](outputs/figures/sentiment_dist.png)

All subreddits show positive sentiment overall. r/popheads and r/indieheads are the most positive, while r/hiphopheads has the most neutral comments — likely due to VADER's limited handling of hip-hop slang.

## Status

- [x] Data extraction and filtering
- [x] Exploratory data analysis (EDA)
- [x] Text mining (word frequency, bigrams, LDA, sentiment)
- [ ] Social network analysis
