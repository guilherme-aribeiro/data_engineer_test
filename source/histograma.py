import database
import json
#"SELECT count(id) from dados WHERE EXTRACT(MONTH FROM CAST ( data ->> 'pickup_datetime' AS TIMESTAMP)) =1 AND EXTRACT(YEAR FROM CAST ( data ->> 'pickup_datetime' AS TIMESTAMP)) =2009 AND data ->> 'payment_type = \'CASH\'' ;" 

def consulta_banco(mes, ano):
    sql = "SELECT count(id) from dados WHERE EXTRACT(MONTH FROM CAST ( data ->> 'pickup_datetime' AS TIMESTAMP)) =" + str(mes) 
    sql = sql + " AND EXTRACT(YEAR FROM CAST ( data ->> 'pickup_datetime' AS TIMESTAMP)) =" +str(ano)
    sql = sql +  " AND data ->> 'payment_type' = 'CASH' ;"
    return database.consulta_sql(sql)[0][0]
    

#consulta_banco(1,2009)
dic_dados= {}
for ano in range(2009,2013):
    lista=[]
    print(ano)
    for mes in range(12):
        print (mes)
        lista.append(((mes+1),consulta_banco((mes+1),ano)))
    dic_dados[ano] = dict(lista)

#dic_dados[2009]= dict([(1,12123123),(2,23123)])
with open('data\data_histograma.json', 'w') as fp:
    json.dump(dic_dados, fp)