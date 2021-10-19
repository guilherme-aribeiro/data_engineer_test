import database

sql_count = "SELECT count(id) from dados WHERE ( CAST (data ->> 'passenger_count' AS INTEGER) < 3);"
sql_soma =  "SELECT SUM(CAST (data ->> 'trip_distance' AS NUMERIC(30,2))) AS total from dados WHERE ( CAST (data ->> 'passenger_count' AS INTEGER) < 3 );"

count= database.consulta_sql(sql_count)
soma= database.consulta_sql(sql_soma)

print (count[0][0])
print (soma[0][0])

media = soma[0][0] / count[0][0]

print (round(media,3))