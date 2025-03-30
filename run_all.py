import subprocess, threading, sys, os

python = sys.executable
project_root = os.path.dirname(os.path.abspath(__file__))

services = [
    "ingestion.facebook_ingest",
    "ingestion.twitter_ingest",
    "ingestion.instagram_ingest",
    "ingestion.linkedin_ingest"
]

def run_script(module):
    print(f"▶ Launching {module}")
    subprocess.call([python, "-m", module], cwd=project_root)

if __name__ == "__main__":
    threads = [threading.Thread(target=run_script, args=(m,)) for m in services]
    [t.start() for t in threads]
    [t.join() for t in threads]
    run_script("processing.spark_stream")