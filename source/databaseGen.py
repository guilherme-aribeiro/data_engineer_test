import json
import database

def carrega_json(path):
    data = []
    i= 0 
    sql= "INSERT INTO dados (data) VALUES ('"
    with open(path) as f:
        for line in f:
            i+=1
            sql = sql + line + "');"
            database.manipula_sql(sql)
            sql= "INSERT INTO dados (data) VALUES ('"
          
      
     
carrega_json('data\data-sample_data-nyctaxi-trips-2009-json_corrigido.json')
carrega_json('data\data-sample_data-nyctaxi-trips-2010-json_corrigido.json')
carrega_json('data\data-sample_data-nyctaxi-trips-2011-json_corrigido.json')
carrega_json('data\data-sample_data-nyctaxi-trips-2012-json_corrigido.json')



