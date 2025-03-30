import pandas as pd
from pathlib import Path

Path("storage/output").mkdir(parents=True, exist_ok=True)
Path("storage/aggregated").mkdir(parents=True, exist_ok=True)

# Fake raw output
raw_data = pd.DataFrame([
    {"text": "Love this company!", "platform": "facebook", "sentiment": 0.9},
    {"text": "Terrible service.", "platform": "twitter", "sentiment": -0.6},
    {"text": "Decent coverage.", "platform": "linkedin", "sentiment": 0.2},
])
raw_data.to_parquet("storage/output/fake_sentiment.parquet", index=False)

# Fake aggregated data
agg_data = pd.DataFrame([
    {"platform": "facebook", "date": "2025-03-28", "avg_sentiment": 0.9},
    {"platform": "twitter", "date": "2025-03-28", "avg_sentiment": -0.6},
    {"platform": "linkedin", "date": "2025-03-28", "avg_sentiment": 0.2},
])
agg_data.to_parquet("storage/aggregated/fsummary.parquet", index=False)

print("✅ Simulated data written to storage.")
