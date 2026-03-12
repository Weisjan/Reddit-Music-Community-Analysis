import io
import json
from pathlib import Path
from datetime import datetime, timezone

import pandas as pd
import zstandard as zstd

input_files = [
    "data/raw/hiphopheads_comments.zst",
    "data/raw/indieheads_comments.zst",
    "data/raw/Metal_comments.zst",
    "data/raw/popheads_comments.zst",
]

output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

# zmień żeby pobrać więcej danych (None = wszystko)
LIMIT = 10_000

# wspólny okres dla wszystkich subredditów (wyznaczony przez scan_dates.py)
date_start = datetime(2015, 8, 1, tzinfo=timezone.utc)
date_end   = datetime(2022, 12, 31, tzinfo=timezone.utc)

ts_start = int(date_start.timestamp())
ts_end   = int(date_end.timestamp())

bot_accounts = {
    "AutoModerator", "RemindMeBot", "RepostSleuthBot",
    "BotTerminator", "B0tRank", "Wikipedia_GPT2_Bot",
}


def is_valid(data):
    body   = data.get("body", "")
    author = data.get("author", "")

    if not body or not author:
        return False
    if body in ("[deleted]", "[removed]"):
        return False
    if author in ("[deleted]",) or author in bot_accounts:
        return False
    if len(body.strip()) < 10:
        return False

    ts = data.get("created_utc")
    try:
        ts = int(ts)
    except (TypeError, ValueError):
        return False

    return ts_start <= ts <= ts_end


def read_comments(file_path, limit=None):
    rows = []
    skipped = 0

    with open(file_path, "rb") as f:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(f) as reader:
            stream = io.TextIOWrapper(reader, encoding="utf-8")

            for line in stream:
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    skipped += 1
                    continue

                if not is_valid(data):
                    skipped += 1
                    continue

                rows.append({
                    "comment_id":       data.get("id"),
                    "author":           data.get("author"),
                    "body":             data.get("body"),
                    "subreddit":        data.get("subreddit"),
                    "score":            data.get("score"),
                    "created_utc":      data.get("created_utc"),
                    "parent_id":        data.get("parent_id"),
                    "link_id":          data.get("link_id"),
                    "controversiality": data.get("controversiality"),
                    "gilded":           data.get("gilded"),
                })

                if limit is not None and len(rows) >= limit:
                    break

    print(f"  zachowano: {len(rows)}, odfiltrowano: {skipped}")
    return rows


all_dfs = []

for file_path in input_files:
    print(f"Przetwarzam: {file_path}")

    rows = read_comments(file_path, limit=LIMIT)
    df = pd.DataFrame(rows)

    name = Path(file_path).stem.replace("_comments", "")
    out_path = output_dir / f"{name}_sample.csv"
    df.to_csv(out_path, index=False, encoding="utf-8-sig")
    all_dfs.append(df)

combined_df = pd.concat(all_dfs, ignore_index=True)
combined_df.to_csv(output_dir / "all_subreddits_sample.csv", index=False, encoding="utf-8-sig")

# szybki podgląd
combined_df["date"] = pd.to_datetime(
    pd.to_numeric(combined_df["created_utc"], errors="coerce"), unit="s"
)

print("\nPodsumowanie:")
for sub, g in combined_df.groupby("subreddit"):
    print(f"  {sub}: {len(g)} komentarzy | {g['date'].min().strftime('%Y-%m')} → {g['date'].max().strftime('%Y-%m')}")