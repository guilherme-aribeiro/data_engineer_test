import database
import matplotlib.pyplot as plot

sql = "SELECT sum ( CAST ( data ->> 'tip_amount' AS DECIMAL (6,2))), EXTRACT(MONTH FROM (CAST(data ->> 'pickup_datetime' AS TIMESTAMP))),EXTRACT(DAY FROM (CAST(data ->> 'pickup_datetime' AS TIMESTAMP))) FROM dados WHERE EXTRACT(MONTH FROM CAST ( data ->> 'pickup_datetime' AS TIMESTAMP)) > 9 AND EXTRACT(YEAR FROM CAST ( data ->> 'pickup_datetime' AS TIMESTAMP)) = 2012 GROUP BY EXTRACT(MONTH FROM (CAST(data ->> 'pickup_datetime' AS TIMESTAMP))) , EXTRACT(DAY FROM (CAST(data ->> 'pickup_datetime' AS TIMESTAMP)));"

saida=database.consulta_sql(sql)
dic={}


for data in saida:
    mes= int(data[1])
    dia= int(data[2])
    dic[str(dia)+'/'+str(mes)]= float(data[0])


for mes in range (10,13):
    for dia in range(1,32):
        if(not(mes==11 and dia ==31)):
            try:
                a = dic[str(dia)+'/'+str(mes)]
            except:
                dic[str(dia)+'/'+str(mes)] = 0.0

lista_chaves = list(dic.keys())
lista_valores = list(dic.values())


plot.plot_date(lista_chaves,lista_valores, linestyle='solid')
plot.xticks(rotation=90)
plot.xlabel("Dia do mês")
plot.ylabel("Soma dos valores da gorgeta")
plot.show()