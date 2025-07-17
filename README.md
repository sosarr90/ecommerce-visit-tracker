# E-commerce Visit Tracker | PySpark + Hive + Azure Blob + Parquet

## Description

Ce projet met en œuvre un pipeline **Big Data** end-to-end qui suit les visites d'utilisateurs sur un site e-commerce. Il simule le traitement des logs bruts à travers :

- 🔹 Azure Blob Storage (stockage cloud)
- 🔹 PySpark pour le traitement ETL
- 🔹 Format **Parquet** pour stockage efficace
- 🔹 Apache Hive pour l’analyse en SQL

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
