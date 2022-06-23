from db_connect import cnx, cursor

query = "SELECT * FROM paper_references"
cursor.execute(query)

myresult = cursor.fetchall()
for x in myresult:
  print(x)

cursor.close()
cnx.close()