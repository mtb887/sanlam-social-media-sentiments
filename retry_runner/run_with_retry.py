import subprocess
import time
import sys
import logging
from pathlib import Path

log_file = Path("logs/retry_runner.log")
log_file.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def run_with_retry(module, max_retries=3, delay=5):
    attempt = 1
    while attempt <= max_retries:
        logging.info(f"Attempt {attempt} to run {module}")
        result = subprocess.run([sys.executable, "-m", module])
        if result.returncode == 0:
            logging.info(f"{module} completed successfully.")
            return
        else:
            logging.warning(f"{module} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
            attempt += 1
    logging.error(f"{module} failed after {max_retries} attempts.")
    sys.exit(1)

if __name__ == "__main__":
    services = [
        "ingestion.facebook_ingest",
        "ingestion.twitter_ingest",
        "ingestion.instagram_ingest",
        "ingestion.linkedin_ingest",
        "processing.spark_stream"
    ]
    for svc in services:
        run_with_retry(svc)