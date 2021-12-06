import psycopg2
import requests
r=requests.get("https://jsonplaceholder.typicode.com/posts")

hostname='localhost'
database='NewDatabase'
username='postgres'
pwd='test@123'
port_id=5432
conn=None
cur=None
try:
    conn=psycopg2.connect(
         host=hostname,
         dbname=database,
         user=username,
         password=pwd,
         port=port_id)
    cur=conn.cursor()
    create_script='''CREATE TABLE IF NOT EXISTS mohiteA(
                            id      int PRIMARY KEY ,
                            title   varchar,
                            body    varchar
                           ) ;'''
    
    cur.execute(create_script, )
    insert_script = 'INSERT INTO mohiteA (id, title, body) VALUES ( %s, %s, %s)'
    insert_values = r
    cur.execute(insert_script,insert_values)

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
      cur.close()
    if conn is not None:
      conn.close()
    print("PostgreSQL connection is closed")


