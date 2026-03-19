# skrypt do sprawdzenia zakresów dat w plikach .zst

import io
import json
from pathlib import Path
from datetime import datetime, timezone

import zstandard as zstd

input_files = [
    "data/raw/hiphopheads_comments.zst",
    "data/raw/indieheads_comments.zst",
    "data/raw/Metal_comments.zst",
    "data/raw/popheads_comments.zst",
]


def scan_dates(file_path):
    min_ts = float("inf")
    max_ts = float("-inf")
    total = 0

    with open(file_path, "rb") as f:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(f) as reader:
            stream = io.TextIOWrapper(reader, encoding="utf-8")

            for line in stream:
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    continue

                ts = data.get("created_utc")
                try:
                    ts = int(ts)
                    min_ts = min(min_ts, ts)
                    max_ts = max(max_ts, ts)
                except (TypeError, ValueError):
                    pass

                total += 1
                if total % 500_000 == 0:
                    print(f"  {total:,} linii...")

    date_min = datetime.fromtimestamp(min_ts).strftime("%Y-%m")
    date_max = datetime.fromtimestamp(max_ts).strftime("%Y-%m")

    return {
        "name": Path(file_path).stem,
        "total": total,
        "min_ts": min_ts,
        "max_ts": max_ts,
        "date_min": date_min,
        "date_max": date_max,
    }


results = []

for file_path in input_files:
    print(f"Skanuję: {file_path}")
    result = scan_dates(file_path)
    results.append(result)
    print(f"  {result['name']}: {result['date_min']} → {result['date_max']} ({result['total']:,} komentarzy)")

# wspólny okres = najpóźniejszy start i najwcześniejszy koniec
common_start = datetime.fromtimestamp(max(r["min_ts"] for r in results), tz=timezone.utc).strftime("%Y-%m")
common_end   = datetime.fromtimestamp(min(r["max_ts"] for r in results), tz=timezone.utc).strftime("%Y-%m")

print(f"\nWspólny okres: {common_start} → {common_end}")