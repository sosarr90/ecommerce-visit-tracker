# E-commerce Visit Tracker | PySpark + Hive + Azure Blob + Parquet

## Description

This project implements an end-to-end Big Data pipeline that tracks user visits on an e-commerce website. It simulates the processing of raw logs through:

🔹 Azure Blob Storage (cloud storage)

🔹 PySpark for ETL processing

🔹 Parquet format for efficient storage

🔹 Apache Hive for SQL-based analysis

---

## Architecture du pipeline

```plaintext
Raw Logs (CSV) → Azure Blob Storage
      ↓
PySpark ETL: Read + Clean + Aggregate
      ↓
Write to Parquet (Azure Blob)
      ↓
Save as Hive Table (ecommerce.visits_summary)
      ↓
Notebook or HiveQL for analytics
