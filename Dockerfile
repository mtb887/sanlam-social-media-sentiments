# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optional: create logs and storage folders
RUN mkdir -p logs storage/output storage/aggregated

# Default command (can be overridden)
CMD ["python", "run_all.py"]
