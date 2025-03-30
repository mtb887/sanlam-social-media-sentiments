import pandas as pd
from pathlib import Path

Path("storage/output").mkdir(parents=True, exist_ok=True)
Path("storage/aggregated").mkdir(parents=True, exist_ok=True)

raw_data = pd.DataFrame([
    {"text": "Excellent service!", "platform": "facebook", "sentiment": 0.8},
    {"text": "Disappointed by the results.", "platform": "twitter", "sentiment": -0.7},
    {"text": "Reliable product.", "platform": "linkedin", "sentiment": 0.3}
])
raw_data.to_parquet("storage/output/fake_sentiment.parquet", index=False)

agg_data = pd.DataFrame([
    {"platform": "facebook", "date": "2025-03-28", "avg_sentiment": 0.8},
    {"platform": "twitter", "date": "2025-03-28", "avg_sentiment": -0.7},
    {"platform": "linkedin", "date": "2025-03-28", "avg_sentiment": 0.3}
])
agg_data.to_parquet("storage/aggregated/fake_summary.parquet", index=False)

print("✅ Simulated data written.")