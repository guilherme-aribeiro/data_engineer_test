import database


#Cria tabela 

sql_cria = 'CREATE TABLE DADOS (id serial primary key, data jsonb) ;'

database.manipula_sql(sql_cria)
