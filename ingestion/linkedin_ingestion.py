import os, json, time, sys, hashlib
from datetime import datetime
from pathlib import Path
from kafka.errors import KafkaError
from ingestion.common.producer import send_to_kafka

platform = "linkedin"
topic = "linkedin-stream"
data_file = "data/linkedin_posts.json"
log_file = f"logs/{platform}_ingest.log"
send_interval = 1
sent_hashes = set()

Path("logs").mkdir(exist_ok=True)

def log(msg, level="INFO"):
    line = f"[{level}] {datetime.now().isoformat()} | {msg}"
    print(line)
    with open(log_file, "a") as f: f.write(line + "\n")

def load_posts(file):
    if not Path(file).exists(): raise FileNotFoundError(f"Missing: {file}")
    with open(file, "r") as f:
        posts = json.load(f)
        if not isinstance(posts, list): raise ValueError("Must be a list.")
        return posts

def is_duplicate(text):
    h = hashlib.sha256(text.strip().lower().encode()).hexdigest()
    if h in sent_hashes: return True
    sent_hashes.add(h)
    return False

def main():
    try:
        posts = load_posts(data_file)
        for post in posts:
            if not isinstance(post, str): continue
            if is_duplicate(post): continue
            send_to_kafka(topic, {"text": post.strip()})
            log(f"Sent: {post.strip()}")
            time.sleep(send_interval)
        sys.exit(0)
    except Exception as e:
        log(f"Error: {e}", "FATAL")
        sys.exit(99)

if __name__ == "__main__":
    main()
