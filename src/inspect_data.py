import zstandard as zstd
import json
import io

filename = "data\\raw\\Music_submissions.zst"   # wpisz nazwę swojego pliku

with open(filename, "rb") as f:
    dctx = zstd.ZstdDecompressor()

    with dctx.stream_reader(f) as reader:
        text_stream = io.TextIOWrapper(reader, encoding="utf-8")

        for i, line in enumerate(text_stream):

            data = json.loads(line)

            print("=== RECORD ===")
            print(data)

            if i >= 2:
                break