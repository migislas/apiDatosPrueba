import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='alfa1uno', host='0.0.0.0', port= '15432'
)
print(conn)
cursor = conn.cursor()
print(dir(cursor))
#cursor.execute("INSERT INTO product  (product_id, name) VALUES(%s, %s)", (1, "MIguel"))
#conn.commit()
cursor.execute("SELECT * FROM product")
data = cursor.fetchall()
print("Connection established to: ",data)
