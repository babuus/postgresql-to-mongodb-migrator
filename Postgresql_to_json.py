import psycopg2
import json
import datetime

conn = psycopg2.connect(
    host="strapi-database.ch1ndhwkqrdf.eu-west-2.rds.amazonaws.com",
    database="postgres",
    user="postreadonly",
    password="readonly123$")

cur = conn.cursor()
cur.execute("SELECT * FROM public.brand_content_data")
# cur.execute("ORDER BY id ASC LIMIT 100")
columns = ('id','Brand','created_at','updated_at','entity_content_datum')
results = []
for row in cur.fetchall():
    results.append(dict(zip(columns, row)))
print ("Table viewed successfully")
# print(results)
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

with open('data.json', 'w') as outfile:
    json.dump(results, outfile,sort_keys=True, default = myconverter)


conn.commit()
conn.close()