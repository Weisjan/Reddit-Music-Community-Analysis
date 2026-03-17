# Reddit Music Community Analysis

> Comparative analysis of discussion topics and user interaction patterns across music-focused subreddits using NLP and social network analysis.

## Research Question

Do subreddits dedicated to different music genres differ in the topics they discuss and how their users interact with each other?

## Dataset

| Subreddit     | Genre   | Comments |
| ------------- | ------- | -------- |
| r/hiphopheads | Hip-hop | ~110k    |
| r/indieheads  | Indie   | ~30k     |
| r/Metal       | Metal   | ~10k     |
| r/popheads    | Pop     | ~70k     |

**Time period:** March 2020 – March 2021  
**Source:** [Pushshift Reddit Dataset](https://the-eye.eu/redarcs/)

## Methods

| Step               | Technique                                                    |
| ------------------ | ------------------------------------------------------------ |
| Text Mining        | Word frequency, bigrams, LDA topic modeling                  |
| Sentiment Analysis | VADER compound score                                         |
| Network Analysis   | Degree & betweenness centrality, Louvain community detection |

## Results

### Activity

![Activity per month](outputs/figures/activity_per_month.png)

### Most Discussed Topics (Word Clouds)

![Word Clouds](outputs/figures/wordclouds.png)

### Sentiment

All subreddits show overall positive sentiment. r/popheads and r/indieheads score highest, while r/hiphopheads has the most neutral comments — likely due to VADER's limited handling of hip-hop slang.

![Sentiment distribution](outputs/figures/sentiment_dist.png)

| Subreddit     | Mean  | Median |
| ------------- | ----- | ------ |
| r/popheads    | 0.299 | 0.361  |
| r/indieheads  | 0.285 | 0.341  |
| r/Metal       | 0.175 | 0.153  |
| r/hiphopheads | 0.088 | 0.000  |

## Project Structure

```
├── data/
│   ├── raw/              # .zst files from Pushshift (not included)
│   └── processed/        # extracted CSV files (not included)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_text_mining.ipynb
│   └── 03_network_analysis.ipynb
├── src/
│   ├── scan_dates.py     # check date ranges in .zst files
│   └── extract_data.py   # extract and filter comments to CSV
├── outputs/
│   └── figures/
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**To reproduce the data:**

1. Download `.zst` files from [Pushshift](https://the-eye.eu/redarcs/) and place in `data/raw/`
2. Run `src/scan_dates.py` to verify date ranges
3. Run `src/extract_data.py` to extract comments to `data/processed/`
4. Run notebooks in order (`01` → `02` → `03`)

## Tech Stack

`pandas` · `spacy` · `nltk` · `gensim` · `vaderSentiment` · `networkx` · `python-louvain` · `matplotlib` · `seaborn` · `wordcloud`
