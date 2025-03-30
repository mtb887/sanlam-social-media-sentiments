# 🧠 Social Media Sentiment Analysis Platform

This is a real-time data engineering proof-of-concept pipeline that ingests simulated social media posts (Twitter, Facebook, Instagram, LinkedIn), analyzes them for sentiment, and makes the results available for streaming dashboards and analytical tools.

> **Created with love by Motebang Mokoena, your Potential tech Lead** 💛

---

## 📦 Architecture Overview

```
            [Facebook]   [Instagram]   [Twitter]   [LinkedIn]
                 │             │            │             │
                 ▼             ▼            ▼             ▼
      ┌────────────────────────────────────────────────────────┐
      │                 Ingestion Scripts (Python)             │
      └────────────────────────────────────────────────────────┘
                               │
                               ▼
      ┌────────────────────────────────────────────────────────┐
      │               Apache Kafka (Dockerized)                │
      └────────────────────────────────────────────────────────┘
                               │
                               ▼
      ┌────────────────────────────────────────────────────────┐
      │           Spark Structured Streaming + UDF             │
      └────────────────────────────────────────────────────────┘
                               │
                 ┌────────────┴────────────┐
                 ▼                         ▼
     [Parquet Output]         [Sentiment Aggregation (CSV/SQL)]
                               │
                               ▼
         ┌────────────┐   ┌──────────────┐   ┌────────────┐
         │ Power BI   │   │ PostgreSQL   │   │ Streamlit  │
         └────────────┘   └──────────────┘   └────────────┘
```

---

## ⚙️ Features

- Multi-platform sentiment ingestion
- Real-time stream processing with PySpark
- Sentiment scoring using TextBlob
- Storage in Parquet, export to CSV & PostgreSQL
- Retry-enabled CLI orchestration
- Modular directory structure
- Docker-based Kafka + Airflow support
- Exported for Power BI + dashboarding

---

## 🛠 Tech Stack

| Layer            | Tools Used                      |
|------------------|----------------------------------|
| Ingestion        | Python scripts per platform     |
| Messaging Queue  | Kafka (Wurstmeister via Docker) |
| Processing       | PySpark + TextBlob UDF          |
| Storage          | Parquet, CSV, SQLite, PostgreSQL|
| Visualization    | Power BI, Streamlit             |
| Orchestration    | CLI Wrapper + Airflow DAG       |

---

## 🚀 How to Run

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Start Kafka Locally**
```bash
docker-compose up -d
```

3. **Run All Scripts**
```bash
python run_all.py
```

4. **Export to PostgreSQL (Optional)**
```bash
python -m processing.export_to_postgres
```

5. **Power BI Dashboard**
- Open `sentiment_summary.csv` in Power BI Desktop
- Use platform & sentiment columns to chart trends

---

## 🔐 Security & Config

- All secrets are stored in `.env`
- No PII is stored or processed
- Configurable output, database, and Kafka paths

---

## 🧱 Scalability Plan (AWS)

| Component     | Production Equivalent        |
|---------------|------------------------------|
| Kafka         | AWS MSK                      |
| Spark         | AWS Glue or EMR              |
| Storage       | Amazon S3                    |
| Export        | PostgreSQL on RDS            |
| Orchestration | MWAA or Step Functions       |
| Secrets       | AWS Secrets Manager          |

---

## ✅ Submission Requirements Checklist

- [x] Ingests from 4 sources
- [x] Kafka messaging layer
- [x] Stream processing
- [x] Sentiment scoring
- [x] Modular code layout
- [x] Retry logic with CLI
- [x] Logging
- [x] Export to CSV, SQL
- [x] Dashboard support
- [x] Scalable architecture
- [x] Fully orchestrated flow

---

## 🧾 Documentation Included

- ✅ `Final_Architecture_and_Explanation_v2.pdf`
- ✅ `EXPORT_ISSUE_REPORT.txt` (CSV export fallback)
- ✅ Airflow DAG `airflow/dags/sentiment_pipeline.py`

---

## ❤️ Created With Love

This project was handcrafted with love by **Motebang Mokoena** as a complete, scalable, cloud-ready data engineering proof-of-concept.

---