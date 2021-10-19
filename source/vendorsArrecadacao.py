import database 

sql_distinct = "SELECT DISTINCT data ->> 'vendor_id' from dados ;"

vendor_list = database.consulta_sql(sql_distinct)

lista_amounts = []
for vendor in vendor_list :
    sql_vendas = "SELECT SUM(CAST (data ->> 'total_amount' AS DECIMAL(15,2))) AS total from dados WHERE ( data ->> 'vendor_id' = "
    sql_vendas  = sql_vendas +"'" +vendor[0]+"'" + ");"
    lista_amounts.append((vendor[0],database.consulta_sql(sql_vendas)[0][0]))
    
print(max(lista_amounts,key=lambda item:item[1]))
    
    