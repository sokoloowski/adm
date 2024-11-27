import pandas as pd

conn = "postgresql://postgres:adm@10.10.10.10:5432/adm"
query = "SELECT * FROM filtered"
df = pd.read_sql(query, conn)
df.to_pickle("filtered.pkl")
