import pymongo
import psycopg2

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['your_mongo_db_name']
mongo_quotes = mongo_db['quotes']

pg_conn = psycopg2.connect(
    dbname='your_postgres_db_name',
    user='your_postgres_user',
    password='your_postgres_password',
    host='localhost'
)
pg_cursor = pg_conn.cursor()

for author in mongo_quotes.distinct('author'):
    pg_cursor.execute(
        "INSERT INTO quotes_author (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;",
        (author,)
    )
    pg_conn.commit()

for quote in mongo_quotes.find():
    pg_cursor.execute(
        "INSERT INTO quotes_quote (text, author_id) VALUES (%s, (SELECT id FROM quotes_author WHERE name=%s));",
        (quote['text'], quote['author'])
    )
    pg_conn.commit()

pg_cursor.close()
pg_conn.close()
mongo_client.close()