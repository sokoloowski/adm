# %%
import psycopg2

db = psycopg2.connect(
    dbname="adm",
    user="postgres",
    password="adm",
    host="10.10.10.10",
    port="5432"
)
db.autocommit = True

# %%
query = """
SELECT
    DATE_TRUNC('month', created_utc) AS year_month,
    COUNT(created_utc) AS row_count
FROM
    reddit
GROUP BY
    DATE_TRUNC('month', created_utc)
ORDER BY
    year_month;
"""

# %%
with db.cursor() as cursor:
    cursor.execute(query)
    data = cursor.fetchall()

# %%
import pandas as pd

df = pd.DataFrame(data, columns=['year_month', 'count'])
df['year'] = df['year_month'].dt.year
df['month'] = df['year_month'].dt.month
df = df.drop(columns=['year_month'])
df.head()

# %%
import matplotlib.pyplot as plt

df = df[df['year'] < 2015]
df['date'] = df['month'].map(str) + '-' + df['year'].map(str)
df['date'] = pd.to_datetime(df['date'], format='%m-%Y')
plt.figure(figsize=(16, 9))
plt.ticklabel_format(useOffset=False, style='plain')
plt.plot(df['date'], df['count'])
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Number of comments')
plt.savefig('comments_count.png')
plt.show()

# %%
df.groupby('year').sum('count')['count']

# %%
plt.figure(figsize=(16, 9))
plt.ticklabel_format(useOffset=False, style='plain')
plt.bar(df.groupby('year').sum('count').index, df.groupby('year').sum('count')['count'])
plt.xlabel('Date')
plt.ylabel('Number of comments')
plt.savefig('comments_count_agg.png')
plt.show()

# %%
df[['count']].sum()

# %%
db.close()
