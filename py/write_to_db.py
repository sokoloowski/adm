# Usage: python ./write_to_db.py YYYY MM

import sys
import json
from datetime import datetime
from psycopg2.extensions import AsIs
import psycopg2

conn = psycopg2.connect(
    dbname="adm",
    user="postgres",
    password="adm",
    host="127.0.0.1",
    port="5432"
)

year = sys.argv[1]
month = sys.argv[2]
file_name = f"RC_{year}-{month}"

def insert_file(fp: str, cur: psycopg2.extensions.cursor):
    ret = 0
    cur.execute('BEGIN TRANSACTION;')
    with open(fp, "r") as f:
        for line in f:
            data = json.loads(line)
            # replace timestapms with datetime
            data['created_utc'] = datetime.fromtimestamp(int(data['created_utc']))
            data['edited'] = None if data['edited'] is False else datetime.fromtimestamp(data['edited'])
            data['retrieved_on'] = datetime.fromtimestamp(data['retrieved_on']) if 'retrieved_on' in data.keys() else None
            cur.execute('INSERT INTO reddit (%s) VALUES %s', (AsIs(','.join(data.keys())), tuple(data.values())))
            ret += 1
            if ret % 5000 == 0:
                print(f"\rProcessed {ret} rows...", end="")
    cur.execute('COMMIT;')
    print(f"\rProcessed {ret} rows from {fp}...")
    return ret

with conn.cursor() as cursor:
    file_path = f"reddit_data/{year}/{file_name}"
    start = datetime.now()
    lines = insert_file(file_path, cursor)
    end = datetime.now()
    with open(f"reddit_data/{year}/log_{file_name}", "w") as f:
        f.write(f"Finished processing {lines} lines at {end} - took {end - start}")
