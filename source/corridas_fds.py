import database

sql_parte1 = "SELECT count(id),EXTRACT(EPOCH FROM (sum( (CAST(data ->> 'dropoff_datetime' AS TIMESTAMP) - CAST( data ->> 'pickup_datetime' AS TIMESTAMP) ) ) ) ) FROM dados "
sql_parte2= "WHERE (EXTRACT(DOW FROM CAST(data ->> 'pickup_datetime' AS TIMESTAMP)) = 0 OR EXTRACT(DOW FROM CAST(data ->> 'pickup_datetime' AS TIMESTAMP)) = 6);"
sql= sql_parte1 + sql_parte2

retorno=database.consulta_sql(sql)
total_corridas=retorno[0][0]
total_segundos=retorno[0][1]
tempo_medio_s = total_segundos/total_corridas
tempo_medio_m= int(tempo_medio_s//60)
tempo_medio_s = tempo_medio_s % 60

print("Tempo médio é : " + str(tempo_medio_m)+ " minutos e " + str(tempo_medio_s) + " segundos")