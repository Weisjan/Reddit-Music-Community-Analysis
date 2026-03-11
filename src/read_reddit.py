import zstandard as zstd
import json
import io

filename = "data/Music_comments.zst"

with open(filename, "rb") as f:
    dctx = zstd.ZstdDecompressor()

    with dctx.stream_reader(f) as reader:
        text_stream = io.TextIOWrapper(reader, encoding="utf-8")

        for i, line in enumerate(text_stream):

            data = json.loads(line)

            print("subreddit:", data.get("subreddit"))
            print("author:", data.get("author"))
            print("text:", data.get("body") or data.get("title"))
            print("-"*50)

            if i >= 5:
                break