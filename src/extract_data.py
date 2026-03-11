import zstandard as zstd
import json
import io
import pandas as pd

filename = "../data/raw/Music_comments.zst"

rows = []
limit = 5000

with open(filename, "rb") as f:

    dctx = zstd.ZstdDecompressor()

    with dctx.stream_reader(f) as reader:

        text_stream = io.TextIOWrapper(reader, encoding="utf-8")

        for line in text_stream:

            data = json.loads(line)

            rows.append({
                "author": data.get("author"),
                "body": data.get("body"),
                "score": data.get("score"),
                "parent_id": data.get("parent_id"),
                "link_id": data.get("link_id"),
                "created_utc": data.get("created_utc"),
                "subreddit": data.get("subreddit")
            })

            if len(rows) >= limit:
                break

df = pd.DataFrame(rows)

df.to_csv("../data/processed/music_comments_sample.csv", index=False)

print(df.head())
print("Saved dataset.")