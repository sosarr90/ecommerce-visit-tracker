##E-commerce Visit Tracker | PySpark + Hive + Azure Blob + Parquet

##Description

Ce projet met en �uvre un pipeline **Big Data** end-to-end qui suit les visites d'utilisateurs sur un site e-commerce. Il simule le traitement des logs bruts � travers :

- Azure Blob Storage (stockage cloud)
- PySpark pour le traitement ETL
- Format **Parquet** pour stockage efficace
- Apache Hive pour l�analyse en SQL

---

##Flux de donn�es r�sum�
Visites brutes ==> Azure Blob ==> PySpark ==> Parquet (Blob) + Hive Table ==> Requ�tes / Visualisation



##Architecture du pipeline

```plaintext
Raw Logs (CSV) : Azure Blob Storage
			--> PySpark ETL: Read + Clean + Aggregate
					--> Write to Parquet (Azure Blob)
										--> Save as Hive Table (ecommerce.visits_summary)
																				--> Notebook or HiveQL for analytics
       

      

      

